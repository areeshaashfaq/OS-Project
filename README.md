# 🕵️ Secret Scanner & Credential Triage Pipeline

An automated pipeline for scanning public GitHub repositories to discover accidentally committed secrets, extract credential pairs (`username:password`), and filter out false positives for responsible disclosure.

This project uses **TruffleHog** for the heavy lifting (cloning and scanning git history) and a custom Python pipeline to extract, classify, and triage the results.

---

🛠️ Prerequisites
Python 3.8+

TruffleHog installed and available on your system PATH.

macOS: brew install trufflehog

Linux: Download the binary from the TruffleHog Releases page and add it to your PATH.

Python Libraries: Install the required packages (it is recommended to use a virtual environment).

bash
python3 -m venv venv
source venv/bin/activate
pip install pandas openpyxl
🚀 How to Run the Pipeline
To scan a new batch of repositories, follow these 5 steps in order.

Step 1: Discover Repositories
Generate a random sample of public GitHub repositories. You can change the --seed to get a different batch, and --sample to choose how many repos to grab.

bash
python3 sample_github_api.py --sample 200 --seed 5 --out repos_seed5.txt
Step 2: Scan with TruffleHog
Run the scanner. This clones the repos, checks their full git history, and saves the raw findings.

bash
python3 scan.py --repos-file repos_seed5.txt --workers 4 --progress scan_progress_seed5.jsonl
(Note: This step can take 1–3 hours. If it times out or crashes, simply run the exact same command again to resume where it left off).

Step 3: Extract Credentials
Parse the raw TruffleHog output to pull out user_id and password pairs.

Open check_secrets.py and update the filenames at the bottom of the script:

python
# Inside check_secrets.py
clean_secrets("scan_progress_seed5.jsonl", "credentials_seed5.jsonl")
Run the extraction:

bash
python3 check_secrets.py
Step 4: Filter Out Noise
The extracted file will contain many false positives (e.g., postgres:postgres, user:password, placeholders).

Open filter_credentials.py and update the filenames at the top:

python
# Inside filter_credentials.py
IN_PATH  = "credentials_seed5.jsonl"
OUT_PATH = "worth_investigating_seed5.jsonl"
Run the filter:

bash
python3 filter_credentials.py
Step 5: Review & Generate Excel
You now have a clean list of high-signal credentials in worth_investigating_seed5.jsonl.
To combine all your scans into a single, readable Excel spreadsheet:

bash
python3 make_excel.py
(This will generate all_investigating_credentials.xlsx).

🛑 Responsible Disclosure Rules
When your pipeline flags a credential, you must treat it ethically and legally.

Do NOT log in. Attempting to use found credentials against third-party services is unauthorized access (and illegal in most jurisdictions).

Report it. Go to the GitHub repository, click the Security tab, and select Report a vulnerability (or open a standard issue if security advisories are disabled).

Provide the facts. Tell the owner the file path, line number, commit hash, and the type of credential exposed (e.g., "MongoDB URI"). Ask them to rotate the password and purge the file from git history.

🔍 What This Pipeline Deliberately Does NOT Do
No Verification: It does not test credentials against live services (no login attempts). Validity is for the repo owner to confirm.

No Auto-Reporting: It does not automatically email or message maintainers. It only surfaces the data so you can review it manually.

⚙️ How It Works Under the Hood
sample_github_api.py: Uses the GitHub API to grab a random sample of public repos.

scan.py: Calls trufflehog git <url> --json via subprocess, parses the JSON output, and saves it to a progress file.

check_secrets.py: Reads the TruffleHog output and uses regex to extract the user:password parts from connection strings.

filter_credentials.py: Classifies the extracted credentials. It throws out known defaults (e.g., db1:db1), placeholders (e.g., __DB_USER__), and test fixtures, keeping only high-signal hits.

make_excel.py: Uses pandas to merge all worth_investigating files into a neat .xlsx file.
