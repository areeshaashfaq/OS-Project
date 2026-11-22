#!/usr/bin/env python3
import argparse
import gzip
import json
import random
import sys
import csv
import urllib.request

BASE = "https://data.gharchive.org/"


def parseHours(s):
    s = s.strip()
    if "-" in s and "," not in s:
        a, b = s.split("-", 1)
        return list(range(int(a), int(b) + 1))
    return [int(x) for x in s.split(",") if x.strip() != ""]


def hourUrls(date, hours):
    return [BASE + date + "-" + str(h) + ".json.gz" for h in hours]


def openSource(src):
    if src.startswith("http://") or src.startswith("https://"):
        resp = urllib.request.urlopen(src, timeout=300)
        return gzip.GzipFile(fileobj=resp)
    return gzip.open(src, "rb")


def collectRepos(lines, eventType, repos):
    for line in lines:
        try:
            ev = json.loads(line)
        except Exception:
            continue
        if eventType and ev.get("type") != eventType:
            continue
        repo = ev.get("repo") or {}
        name = repo.get("name")
        if not name:
            continue
        if name not in repos:
            repos[name] = ev.get("created_at", "")
    return repos


def main():
    ap = argparse.ArgumentParser(description="sample public repo urls from GH Archive")
    ap.add_argument("--date", help="YYYY-MM-DD in UTC, e.g. 2026-11-20")
    ap.add_argument("--hours", default="12", help="comma list or a-b range, e.g. 0,6,12 or 9-11")
    ap.add_argument("--from-file", action="append", default=[], help="local .json.gz instead of downloading")
    ap.add_argument("--sample", type=int, default=50, help="how many repos to keep")
    ap.add_argument("--event-type", default="PushEvent", help="event type filter, '' for all")
    ap.add_argument("--seed", type=int, default=0, help="random seed, record it for reproducibility")
    ap.add_argument("--out", default="repos.txt", help="output repo-url file")
    ap.add_argument("--meta", default="sample_meta.csv", help="csv of repo,created_at for longevity t0")
    args = ap.parse_args()

    sources = list(args.from_file)
    if not sources:
        if not args.date:
            print("need --date (and optionally --hours) or --from-file", file=sys.stderr)
            sys.exit(1)
        sources = hourUrls(args.date, parseHours(args.hours))

    repos = {}
    for src in sources:
        print("reading " + src, file=sys.stderr)
        try:
            collectRepos(openSource(src), args.event_type or "", repos)
        except Exception as e:
            print("  skipped (" + str(e) + ")", file=sys.stderr)
    print("unique repos seen: " + str(len(repos)), file=sys.stderr)
    if not repos:
        print("no repos collected, nothing written", file=sys.stderr)
        sys.exit(1)

    names = sorted(repos.keys())
    rng = random.Random(args.seed)
    if len(names) > args.sample:
        names = rng.sample(names, args.sample)
    names.sort()

    with open(args.out, "w", encoding="utf-8") as f:
        f.write("# sampled from GH Archive seed=" + str(args.seed) + " sources=" + str(len(sources)) + "\n")
        for n in names:
            f.write("https://github.com/" + n + "\n")

    with open(args.meta, "w", encoding="utf-8", newline="") as f:
        w = csv.writer(f)
        w.writerow(["repo_url", "event_created_at"])
        for n in names:
            w.writerow(["https://github.com/" + n, repos[n]])

    print("wrote " + str(len(names)) + " repo urls to " + args.out, file=sys.stderr)
    print("wrote t0 timestamps to " + args.meta, file=sys.stderr)


if __name__ == "__main__":
    main()
