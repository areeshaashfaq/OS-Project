#!/usr/bin/env python3
"""
Extract user_id/password credentials from scan_progress.jsonl.
- Reads `raw_secret` only (maskedPreview entries are unrecoverable, skipped).
- Rejects API tokens (SnykKey, GoogleGeminiAPIKey, Figma, Infura, Circle, Box,
  GoogleOauth2, TravisCI) — user does not want these.
- Rejects PrivateKey / URI / Polygon / CustomRegex-in-node_modules noise.
- Keeps JDBC / MongoDB / Postgres / Gitlab and pulls user:pass out of them.
"""
import json
import re
from collections import Counter

IN_PATH  = "scan_progress_seed5.jsonl"
OUT_PATH = "credentials_extracted_3.jsonl"

# ---- What we WANT -------------------------------------------------
KEEP_DETECTORS = {"JDBC", "MongoDB", "Postgres", "Gitlab", "MySQL", "Redis"}

# ---- What we DON'T want (tokens / noise) --------------------------
TOKEN_DETECTORS = {
    "SnykKey", "GoogleGeminiAPIKey", "FigmaPersonalAccessToken",
    "Infura", "Circle", "Box", "GoogleOauth2", "TravisCI",
    "AWS", "Slack", "Stripe", "GitHub", "Heroku", "SendGrid",
}
NOISE_DETECTORS = {"PrivateKey", "URI", "Polygon", "CustomRegex"}

# ---- Extraction patterns ------------------------------------------
# user:password@host   (the real prize)
USERPASS_IN_URL = re.compile(r'://([^:/@\s]+):([^@/\s]+)@')
# password = "..."  /  "password": "..."  /  password=xyz
PASSWORD_ASSIGN = re.compile(
    r'password\s*[:=]\s*["\']?([^"\'\s,;}&]+)', re.IGNORECASE)
# username / user field as fallback user_id
USERNAME_ASSIGN = re.compile(
    r'(?:username|user)\s*[:=]\s*["\']?([^"\'\s,;}&]+)', re.IGNORECASE)

# ---- Noise filters -------------------------------------------------
PLACEHOLDER_RE = re.compile(
    r'<user>|<pass>|<password>|<db-host>|<db-port>|'
    r'example\.com|yourselfhosted|notifications@|'
    r'\$\{[^}]+\}|\{\{[^}]+\}\}',          # ${ENV_VAR} / {{template}}
    re.IGNORECASE)

def is_noise_path(p: str) -> bool:
    return any(n in (p or "") for n in
               ("node_modules/", "/vendor/", "/dist/", "/build/",
                ".min.js", ".min.css", "README.md", "CHANGELOG",
                "map/json/", "map/js/"))

def looks_like_binary_blob(s: str) -> bool:
    if len(s) > 400:
        return True
    return s.count('\x00') + s.count('\ufffd') > 5

def extract_from_raw(raw: str):
    """Return list of (user_id, password) found in a raw_secret string."""
    out = []
    # 1) user:pass@host
    for m in USERPASS_IN_URL.finditer(raw):
        u, p = m.group(1), m.group(2)
        # reject obvious placeholders / env expansions
        if not PLACEHOLDER_RE.search(u) and not PLACEHOLDER_RE.search(p):
            out.append((u, p))
    # 2) explicit password = ...
    for m in PASSWORD_ASSIGN.finditer(raw):
        pw = m.group(1).strip('"\'')
        if PLACEHOLDER_RE.search(pw):
            continue
        # try to find a username nearby (before "password" in same string)
        user = ""
        um = USERNAME_ASSIGN.search(raw[:m.start()])
        if um:
            user = um.group(1).strip('"\'')
        out.append((user, pw))
    return out

def main():
    stats = Counter()
    kept = []

    with open(IN_PATH, "r", encoding="utf-8") as f:
        for lineno, line in enumerate(f, 1):
            line = line.strip()
            if not line:
                continue
            try:
                rec = json.loads(line)
            except json.JSONDecodeError:
                stats["bad_json"] += 1
                continue

            findings = rec.get("findings") or []
            if not findings:
                stats["empty_findings"] += 1
                continue

            for fd in findings:
                det  = fd.get("detector", "") or ""
                path = fd.get("file", "") or ""
                raw  = fd.get("raw_secret")
                masked = fd.get("maskedPreview")

                # ---- Skip masked (unrecoverable) ----
                if raw is None:
                    stats["skipped_masked"] += 1
                    continue
                stats["has_raw_secret"] += 1

                # ---- Reject token detectors ----
                if det in TOKEN_DETECTORS:
                    stats[f"rejected_token_{det}"] += 1
                    continue
                # ---- Reject noise detectors ----
                if det in NOISE_DETECTORS:
                    stats[f"rejected_noise_{det}"] += 1
                    continue
                # ---- Reject noise paths ----
                if is_noise_path(path):
                    stats["rejected_noise_path"] += 1
                    continue
                # ---- Reject binary blobs ----
                if looks_like_binary_blob(raw):
                    stats["rejected_binary"] += 1
                    continue
                # ---- Only consider the detectors we want ----
                if det not in KEEP_DETECTORS:
                    stats[f"skipped_other_{det}"] += 1
                    continue

                creds = extract_from_raw(raw)
                if not creds:
                    stats[f"no_cred_in_{det}"] += 1
                    continue

                for user_id, password in creds:
                    kept.append({
                        "user_id": user_id,
                        "password": password,
                        "repo": fd.get("repo", ""),
                        "file": path,
                        "line": fd.get("line"),
                        "commit": fd.get("commit"),
                        "detector": det,
                        "source_secret": raw,   # keep for verification
                    })
                    stats["kept"] += 1

    with open(OUT_PATH, "w", encoding="utf-8") as out:
        for r in kept:
            out.write(json.dumps(r, ensure_ascii=False) + "\n")

    print(f"✨ Wrote {len(kept)} credential records to {OUT_PATH}\n")
    print("Stats:")
    for k in sorted(stats):
        print(f"  {k}: {stats[k]}")

if __name__ == "__main__":
    main()