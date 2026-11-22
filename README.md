# secret-scanner

Scans public repositories for accidentally committed secrets and drafts a
disclosure notice for each repo owner. It never tests, stores, or uses any
credential value: trufflehog runs with `--no-verification`, and findings are
redacted to a location plus a masked preview.

## Install trufflehog

macOS/Linux:
```
brew install trufflehog
```
or grab a binary from https://github.com/trufflesecurity/trufflehog/releases
and put it on your PATH. Check it: `trufflehog --version`.

## Run

Against a list of repos (with the custom email/password detectors):
```
python3 scan.py --repos-file repos.txt --config detectors.yaml --workers 4
```

Against every public repo in a GitHub org/user (needs the `gh` CLI, authed):
```
python3 scan.py --org someorg --org-limit 1000 --workers 4
```

## Output

- `findings.json` - redacted findings (file, line, detector, masked preview,
  12-char fingerprint). No full secret values.
- `reports/<repo>.md` - a ready-to-send disclosure draft per repo.

## What it deliberately does not do

- It does not verify credentials against any live service (no login attempts).
- It does not store the actual secret, only a mask and a fingerprint.
- Validity is for the repo owner to confirm on their own systems.

## Custom detectors

`detectors.yaml` adds two generic patterns on top of trufflehog's built-ins:
`EmailPasswordPair` (an email and a `password=value` style assignment near each
other) and `BasicAuthUrl` (`scheme://user:pass@host`). These are deliberately
generic and will produce false positives at scale (example configs, placeholder
values like `password=changeme`, test fixtures), so plan to hand-sample a subset
to estimate your false-positive rate for the paper.

Validate detector behavior without trufflehog installed:
```
python3 detector_check.py detectors.yaml testdata/vuln-repo
```

## Notes

- trufflehog detects known credential formats (API keys, tokens, and some
  generic key/password patterns). It will not catch every arbitrary
  email/password pair, only what its detectors recognize.
- Be polite at scale: keep `--workers` modest and expect disk/network use,
  since each repo is cloned into a temp dir by trufflehog.
