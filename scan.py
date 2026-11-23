#!/usr/bin/env python3
import argparse
import json
import subprocess
import sys
import os
import hashlib
from concurrent.futures import ThreadPoolExecutor, as_completed


def maskSecret(raw):
    if not raw:
        return ""
    raw = raw.strip()
    if len(raw) <= 4:
        return "*" * len(raw)
    return raw[:2] + "*" * (len(raw) - 3) + raw[-1:]


def fingerprint(raw):
    if not raw:
        return ""
    return hashlib.sha256(raw.encode("utf-8", "ignore")).hexdigest()[:12]


def parseLine(line):
    try:
        obj = json.loads(line)
    except json.JSONDecodeError:
        return None
    if "SourceMetadata" not in obj:
        return None
    git = ((obj.get("SourceMetadata") or {}).get("Data") or {}).get("Git") or {}
    raw = obj.get("Raw") or ""
    return {
        "repo": git.get("repository", ""),
        "file": git.get("file", ""),
        "line": git.get("line", 0),
        "commit": git.get("commit", ""),
        "detector": obj.get("DetectorName", "unknown"),
        "verified": bool(obj.get("Verified", False)),
        "maskedPreview": maskSecret(raw),
        "fingerprint": fingerprint(raw),
    }


def scanRepo(url, extraArgs):
    cmd = ["trufflehog", "git", url, "--json", "--no-verification", "--no-update"] + extraArgs
    env = dict(os.environ)
    env["GIT_TERMINAL_PROMPT"] = "0"
    env["GCM_INTERACTIVE"] = "never"
    env["GIT_ASKPASS"] = "echo"
    try:
        proc = subprocess.run(cmd, capture_output=True, text=True, timeout=1800, env=env)
    except FileNotFoundError:
        raise RuntimeError("trufflehog not found on PATH, install it first (see README.md)")
    except subprocess.TimeoutExpired:
        return url, [], "timeout after 1800s"
    findings = []
    for ln in proc.stdout.splitlines():
        ln = ln.strip()
        if not ln:
            continue
        rec = parseLine(ln)
        if rec:
            if not rec["repo"]:
                rec["repo"] = url
            findings.append(rec)
    err = ""
    if proc.returncode != 0 and not findings:
        err = (proc.stderr or "").strip().splitlines()[-1:] or ""
        err = err[0] if err else "nonzero exit"
    return url, findings, err


def readRepoList(path):
    repos = []
    with open(path, "r", encoding="utf-8") as f:
        for ln in f:
            ln = ln.strip()
            if not ln or ln.startswith("#"):
                continue
            repos.append(ln)
    return repos


def reposFromOrg(org, limit):
    cmd = ["gh", "repo", "list", org, "--no-archived", "--limit", str(limit),
           "--json", "url", "--source", "--visibility", "public"]
    proc = subprocess.run(cmd, capture_output=True, text=True)
    if proc.returncode != 0:
        raise RuntimeError("gh repo list failed: " + (proc.stderr or "").strip())
    data = json.loads(proc.stdout or "[]")
    return [r["url"] for r in data if r.get("url")]


def writeReports(grouped, outDir):
    os.makedirs(outDir, exist_ok=True)
    written = []
    for repo, items in grouped.items():
        slug = repo.rstrip("/").split("/")[-1].replace(".git", "") or "repo"
        safe = "".join(c if c.isalnum() or c in "-_." else "_" for c in slug)
        path = os.path.join(outDir, safe + ".md")
        lines = []
        lines.append("Subject: Possible exposed secret in your public repository")
        lines.append("")
        lines.append("Hi,")
        lines.append("")
        lines.append("While scanning public repositories for accidentally committed")
        lines.append("secrets, an automated check flagged what looks like credential")
        lines.append("material in this repository:")
        lines.append("")
        lines.append("  " + repo)
        lines.append("")
        lines.append("Flagged locations (secret values are not included):")
        lines.append("")
        for it in items:
            loc = it["file"] or "(unknown file)"
            if it["line"]:
                loc += ":" + str(it["line"])
            lines.append("  - " + loc)
            lines.append("    type: " + it["detector"] + "   preview: " + it["maskedPreview"])
            if it["commit"]:
                lines.append("    first seen in commit: " + it["commit"][:12])
        lines.append("")
        lines.append("If these are real credentials, treat them as compromised:")
        lines.append("  1. Rotate / revoke them now (a committed secret is public forever).")
        lines.append("  2. Remove them from the repo and from git history")
        lines.append("     (git filter-repo or BFG), then force-push.")
        lines.append("  3. Move secrets into environment variables or a secrets manager.")
        lines.append("")
        lines.append("This is an automated courtesy notice. No credentials were tested,")
        lines.append("stored, or used.")
        lines.append("")
        with open(path, "w", encoding="utf-8") as f:
            f.write("\n".join(lines) + "\n")
        written.append(path)
    return written


def loadProgress(path):
    done = set()
    findings = []
    if not os.path.exists(path):
        return done, findings
    with open(path, "r", encoding="utf-8") as f:
        for ln in f:
            ln = ln.strip()
            if not ln:
                continue
            try:
                obj = json.loads(ln)
            except json.JSONDecodeError:
                continue
            repo = obj.get("repo")
            if repo is None:
                continue
            done.add(repo)
            findings.extend(obj.get("findings", []))
    return done, findings


def main():
    ap = argparse.ArgumentParser(description="scan public repos for exposed secrets and draft owner disclosures")
    src = ap.add_mutually_exclusive_group(required=True)
    src.add_argument("--repos-file", help="text file, one public repo URL per line")
    src.add_argument("--org", help="github org/user to enumerate public repos from (needs gh cli)")
    ap.add_argument("--org-limit", type=int, default=1000, help="max repos to pull when using --org")
    ap.add_argument("--workers", type=int, default=4, help="concurrent repo scans")
    ap.add_argument("--out", default="findings.json", help="redacted findings output")
    ap.add_argument("--reports-dir", default="reports", help="per-repo disclosure drafts")
    ap.add_argument("--config", help="trufflehog custom detectors yaml (e.g. detectors.yaml)")
    ap.add_argument("--trufflehog-arg", action="append", default=[], help="extra arg passed to trufflehog")
    ap.add_argument("--progress", default="scan_progress.jsonl",
                    help="resume file written as it goes; delete it to start a scan fresh")
    args = ap.parse_args()

    if args.config:
        args.trufflehog_arg = ["--config", os.path.abspath(args.config)] + args.trufflehog_arg

    if args.org:
        repos = reposFromOrg(args.org, args.org_limit)
    else:
        repos = readRepoList(args.repos_file)
    if not repos:
        print("no repos to scan", file=sys.stderr)
        sys.exit(1)

    alreadyDone, allFindings = loadProgress(args.progress)
    todo = [r for r in repos if r not in alreadyDone]
    total = len(repos)
    if alreadyDone:
        print("resuming: " + str(len(alreadyDone)) + " already scanned, " + str(len(todo)) +
              " left (delete " + args.progress + " to start fresh)", file=sys.stderr)
    else:
        print("scanning " + str(total) + " repo(s) with " + str(args.workers) + " worker(s)", file=sys.stderr)

    progF = open(args.progress, "a", encoding="utf-8")
    try:
        with ThreadPoolExecutor(max_workers=args.workers) as pool:
            futs = {pool.submit(scanRepo, url, args.trufflehog_arg): url for url in todo}
            done = len(alreadyDone)
            for fut in as_completed(futs):
                url = futs[fut]
                done += 1
                try:
                    _, findings, err = fut.result()
                except RuntimeError as e:
                    print(str(e), file=sys.stderr)
                    progF.close()
                    sys.exit(2)
                tag = str(len(findings)) + " finding(s)"
                if err:
                    tag += " [" + err + "]"
                print("[" + str(done) + "/" + str(total) + "] " + url + " -> " + tag, file=sys.stderr)
                progF.write(json.dumps({"repo": url, "findings": findings}) + "\n")
                progF.flush()
                allFindings.extend(findings)
    finally:
        progF.close()

    grouped = {}
    for it in allFindings:
        grouped.setdefault(it["repo"], []).append(it)

    with open(args.out, "w", encoding="utf-8") as f:
        json.dump({"repos": len(grouped), "findings": allFindings}, f, indent=2)

    reports = writeReports(grouped, args.reports_dir)
    print("", file=sys.stderr)
    print("repos with findings: " + str(len(grouped)), file=sys.stderr)
    print("total findings: " + str(len(allFindings)), file=sys.stderr)
    print("redacted findings: " + args.out, file=sys.stderr)
    print("disclosure drafts: " + str(len(reports)) + " in " + args.reports_dir + "/", file=sys.stderr)


if __name__ == "__main__":
    main()