#!/usr/bin/env python3
import argparse
import json
import random
import sys
import os
import time
import urllib.request

API = "https://api.github.com/repositories"


def fetchPage(since, token):
    url = API + "?since=" + str(since)
    headers = {"User-Agent": "secret-scanner-study/1.0", "Accept": "application/vnd.github+json"}
    if token:
        headers["Authorization"] = "Bearer " + token
    req = urllib.request.Request(url, headers=headers)
    resp = urllib.request.urlopen(req, timeout=60)
    return json.loads(resp.read())


def extractNames(page, perPage, names, want):
    taken = 0
    for r in page:
        if taken >= perPage or len(names) >= want:
            break
        fn = r.get("full_name")
        if fn and not r.get("private", False):
            if fn not in names:
                names[fn] = ""
                taken += 1
    return names


def main():
    ap = argparse.ArgumentParser(description="sample public repo urls from the GitHub API")
    ap.add_argument("--sample", type=int, default=50, help="how many repos to collect")
    ap.add_argument("--per-page", type=int, default=10, help="repos to take from each random page")
    ap.add_argument("--max-id", type=int, default=900000000, help="upper bound for random repo id")
    ap.add_argument("--seed", type=int, default=0, help="random seed, record it for reproducibility")
    ap.add_argument("--out", default="repos.txt")
    ap.add_argument("--token", default=os.environ.get("GITHUB_TOKEN", ""),
                    help="optional github token (env GITHUB_TOKEN) for a higher rate limit")
    args = ap.parse_args()

    rng = random.Random(args.seed)
    names = {}
    calls = 0
    budget = (args.sample // max(args.per_page, 1)) + 20
    while len(names) < args.sample and calls < budget:
        calls += 1
        since = rng.randint(0, args.max_id)
        try:
            page = fetchPage(since, args.token)
        except Exception as e:
            print("  page error at since=" + str(since) + " (" + str(e) + ")", file=sys.stderr)
            time.sleep(2)
            continue
        extractNames(page, args.per_page, names, args.sample)
        print("collected " + str(len(names)) + "/" + str(args.sample), file=sys.stderr)

    picked = sorted(names.keys())
    if not picked:
        print("no repos collected (is api.github.com reachable?)", file=sys.stderr)
        sys.exit(1)

    with open(args.out, "w", encoding="utf-8") as f:
        f.write("# sampled from GitHub API seed=" + str(args.seed) + "\n")
        for n in picked:
            f.write("https://github.com/" + n + "\n")
    print("wrote " + str(len(picked)) + " repo urls to " + args.out, file=sys.stderr)


if __name__ == "__main__":
    main()
