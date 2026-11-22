#!/usr/bin/env python3
# validates detectors.yaml regexes against files the way trufflehog will:
# a detector fires on a chunk only if at least one keyword is present AND
# every named regex matches. re2-safe patterns, so python re matches identically.
import re
import sys
import os
import yaml


def loadDetectors(path):
    with open(path) as f:
        doc = yaml.safe_load(f)
    out = []
    for d in doc["detectors"]:
        out.append({
            "name": d["name"],
            "keywords": [k.lower() for k in d.get("keywords", [])],
            "regex": {k: re.compile(v) for k, v in d["regex"].items()},
        })
    return out


def scanText(text, detectors):
    low = text.lower()
    hits = []
    for det in detectors:
        if det["keywords"] and not any(k in low for k in det["keywords"]):
            continue
        matched = {}
        ok = True
        for name, rx in det["regex"].items():
            m = rx.search(text)
            if not m:
                ok = False
                break
            matched[name] = m.group(0)
        if ok:
            hits.append((det["name"], matched))
    return hits


def main():
    detectors = loadDetectors(sys.argv[1])
    root = sys.argv[2]
    for dirpath, _, files in os.walk(root):
        for fn in sorted(files):
            p = os.path.join(dirpath, fn)
            try:
                text = open(p, encoding="utf-8", errors="ignore").read()
            except Exception:
                continue
            hits = scanText(text, detectors)
            rel = os.path.relpath(p, root)
            if hits:
                for name, matched in hits:
                    preview = {k: (v[:3] + "***") for k, v in matched.items()}
                    print("HIT  " + rel + "  [" + name + "]  " + str(preview))
            else:
                print("ok   " + rel + "  (no secret)")


if __name__ == "__main__":
    main()
