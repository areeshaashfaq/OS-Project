#!/usr/bin/env python3
"""
Filter extracted credentials into buckets.
NO network access. NO login attempts. Pure local classification.

Input : credentials_extracted.jsonl   (one JSON object per line)
Output: worth_investigating.jsonl     (only the high-signal rows)
"""
import json
import re
from collections import Counter

IN_PATH  = "credentials_extracted_3.jsonl"
OUT_PATH = "worth_investigating_3.jsonl"

# ---------- Bucket 1: known default dev credentials ----------
DEFAULT_CREDS = {
    ("postgres", "postgres"), ("postgresl", "postgres"),
    ("airflow", "airflow"), ("db1", "db1"), ("webgoat", "webgoat"),
    ("mariadb", "mariadb"), ("scott", "tiger"),
    ("root", "root"), ("root", "changeme"),
    ("admin", "admin"), ("admin", "password"),
    ("user", "user"), ("user", "password"), ("user", "pass"),
    ("test", "test"), ("guest", "guest"),
    ("mongoose_check", "mongoose_check524"),
}

# ---------- Bucket 2: placeholder tokens ----------
PLACEHOLDER_RE = re.compile(
    r'^(__.*__|<.*>|\$\{.*\}|\{\{.*\}\}|\\|'
    r'username|password|user|pass|passwd|secret|'
    r'USERNAME|PASSWORD|USER|PASS|'
    r'adminUser|securePassword|userpasswd|'
    r'PostgresChangeMe|changeme)$',
    re.IGNORECASE,
)

# ---------- Bucket 3: docs / example hosts ----------
DOCS_HOST_RE = re.compile(
    r'(example\.com|hostname|localhost|127\.0\.0\.1|'
    r'\.example\.|your[-_]?host|your[-_]?domain)',
    re.IGNORECASE,
)
DOCS_PATH_RE = re.compile(
    r'(README|CHANGELOG|\.md$|\.adoc$|docs?/|\.example$|\.sample$)',
    re.IGNORECASE,
)

# ---------- Bucket 4: specific, real-looking hosts ----------
SPECIFIC_HOST_RE = re.compile(
    r'@[A-Za-z0-9.\-]+\.'
    r'(cloudapp\.net|mongodb\.net|rds\.amazonaws\.com|'
    r'azure\.com|herokuapp\.com|render\.com|fly\.dev|'
    r'digitaloceanspaces\.com|supabase\.co)',
    re.IGNORECASE,
)

# ---------- Bucket 5: obviously test fixture repos ----------
TEST_REPO_RE = re.compile(
    r'(BearerPipelineTest|/test[s]?/|/spec[s]?/|demo|sample|'
    r'playground|Sandbox)',
    re.IGNORECASE,
)


def classify(rec: dict) -> str:
    """Return one of: bad_record, default, placeholder, docs_example,
    test_fixture, worth_investigating, low_signal."""
    user = (rec.get("user_id") or "").strip()
    pw   = (rec.get("password") or "").strip()
    raw  = rec.get("source_secret") or ""
    path = rec.get("file") or ""
    repo = rec.get("repo") or ""

    if not user or not pw:
        return "bad_record"

    # 1) known default pairs
    if (user.lower(), pw.lower()) in DEFAULT_CREDS:
        return "default"

    # 2) placeholder-shaped tokens
    if PLACEHOLDER_RE.match(user) or PLACEHOLDER_RE.match(pw):
        return "placeholder"

    # 3) common junk passwords regardless of user
    if pw.lower() in {"password", "pass", "passwd", "changeme",
                      "secret", "userpasswd", "postgreschangeme"}:
        return "placeholder"

    # 4) docs / example hosts or doc files
    if DOCS_HOST_RE.search(raw) or DOCS_PATH_RE.search(path):
        return "docs_example"

    # 5) known test repos
    if TEST_REPO_RE.search(repo):
        return "test_fixture"

    # 6) specific non-default host — highest signal
    if SPECIFIC_HOST_RE.search(raw):
        return "worth_investigating"

    # 7) non-default password that isn't pure digits — worth a look
    if len(pw) >= 6 and not pw.isdigit() and pw.lower() not in {"123456", "12345678"}:
        return "worth_investigating"

    # 8) anything else (short passwords, digit-only, etc.)
    return "low_signal"


def main():
    stats = Counter()
    kept  = []
    seen  = set()   # dedupe identical (repo, user, pw)

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

            cat = classify(rec)
            stats[cat] += 1

            if cat != "worth_investigating":
                continue

            key = (rec.get("repo"), rec.get("user_id"), rec.get("password"))
            if key in seen:
                stats["duplicate_worth_investigating"] += 1
                continue
            seen.add(key)
            kept.append(rec)

    with open(OUT_PATH, "w", encoding="utf-8") as out:
        for r in kept:
            out.write(json.dumps(r, ensure_ascii=False) + "\n")

    total = sum(v for k, v in stats.items()
                if k not in ("bad_json", "duplicate_worth_investigating"))
    print(f"Scanned {total} records")
    print(f"Wrote {len(kept)} high-signal rows → {OUT_PATH}\n")
    print("Bucket breakdown:")
    for k in sorted(stats, key=lambda x: -stats[x]):
        print(f"  {k:32s} {stats[k]}")


if __name__ == "__main__":
    main()