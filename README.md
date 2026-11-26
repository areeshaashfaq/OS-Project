# 🕵️ Secret Scanner & Credential Triage Pipeline

An automated security research pipeline designed to identify accidentally committed secrets in GitHub repositories, classify potential credential exposures, reduce false positives, and support responsible disclosure.

The project uses **TruffleHog** for repository scanning and Git history analysis, combined with a custom Python pipeline for data processing, classification, filtering, and reporting.

---

## 📌 Project Overview

The pipeline consists of five main stages:

| Stage | Description |
|---|---|
| 1. Repository Discovery | Generate reproducible samples of GitHub repositories. |
| 2. Secret Detection | Scan authorized repositories and their Git history using TruffleHog. |
| 3. Credential Analysis | Identify potential username-password exposures and other credential types. |
| 4. Noise Filtering | Remove known placeholders, test fixtures, and irrelevant findings. |
| 5. Reporting | Consolidate research findings into a structured Excel report. |

### Pipeline Workflow

**Repository Discovery → Secret Scanning → Credential Analysis → Noise Filtering → Excel Reporting**

---

## 🛠️ Prerequisites

Ensure the following dependencies are installed before running the pipeline.

### 1. Python

- Python 3.8 or above
- pip package manager

### 2. TruffleHog

TruffleHog must be installed and available on your system PATH.

**macOS**

```bash
brew install trufflehog
```

**Linux / WSL**

Download the appropriate binary from the [official TruffleHog Releases page](https://github.com/trufflesecurity/trufflehog/releases) and add it to your system PATH.

### 3. Python Libraries

Using a virtual environment is recommended to avoid dependency conflicts.

```bash
python3 -m venv venv
source venv/bin/activate
pip install pandas openpyxl
```

| Library | Purpose |
|---|---|
| pandas | Data processing, analysis, and consolidation |
| openpyxl | Excel spreadsheet generation |

---

## 🚀 Pipeline Execution

The pipeline is divided into five sequential steps.

### Step 1: Discover Repositories

**Script:** `sample_github_api.py`

The repository discovery script uses the GitHub API to generate reproducible samples of public repositories for research.

| Parameter | Description |
|---|---|
| `--sample` | Number of repositories to sample |
| `--seed` | Random seed used for reproducibility |
| `--out` | Output filename |

Different seeds allow researchers to obtain different repository samples while maintaining reproducibility.

Repository samples should be reviewed for authorization before scanning.

### Step 2: Scan with TruffleHog

**Script:** `scan.py`

The scanner uses TruffleHog to examine authorized repositories and their Git history for potential secret exposures.

The scanning process includes:

- Repository cloning.
- Git history analysis.
- Secret detection.
- Progress tracking.
- Findings collection.
- Resume support.

| Parameter | Description |
|---|---|
| `--repos-file` | Input repository list |
| `--workers` | Number of concurrent scanning workers |
| `--progress` | Progress tracking filename |

Scanning may take approximately 1–3 hours, depending on repository size, network speed, available hardware, and the number of repositories.

The progress tracking mechanism is designed to allow interrupted scans to resume rather than restart entirely.

### Step 3: Credential Analysis

**Script:** `check_secrets.py`

This stage processes the scanner output and identifies potential credential-related findings.

It focuses on distinguishing relevant credential patterns from unrelated secrets and organizing the results for subsequent analysis.

The research scope includes potential username-password pairs and authentication-related connection strings.

Full-value extraction should only be demonstrated with synthetic credentials in controlled test repositories. Third-party findings should remain redacted.

### Step 4: Filter Out Noise

**Script:** `filter_credentials.py`

Initial scanner results may contain false positives, example credentials, placeholders, and test data.

This stage reduces noise by identifying common patterns that are unlikely to represent genuine exposures.

Examples of noise include:

| Category | Example |
|---|---|
| Default credentials | `postgres:postgres` |
| Generic placeholders | `user:password` |
| Environment placeholders | `__DB_USER__` |
| Repeated default values | `db1:db1` |
| Test fixtures | Synthetic authentication data |

The filtered output contains findings that require further investigation.

A retained finding does not necessarily represent a valid or active credential.

### Step 5: Review and Generate Excel

**Script:** `make_excel.py`

The final stage consolidates research findings from multiple scanning batches into a structured Excel spreadsheet.

The script uses pandas and openpyxl to organize redacted research records into a readable format for manual review and statistical analysis.

**Output filename:**

`all_investigating_credentials.xlsx`

Research spreadsheets should not contain plaintext third-party credentials.

---

## 📂 Project Files

### Core Scripts

| File | Description |
|---|---|
| `sample_github_api.py` | Generates reproducible repository samples using the GitHub API. |
| `scan.py` | Performs repository scanning using TruffleHog. |
| `check_secrets.py` | Processes scanner results and identifies credential-related findings. |
| `filter_credentials.py` | Filters placeholders, default credentials, test fixtures, and other noise. |
| `make_excel.py` | Consolidates research findings into an Excel spreadsheet. |

### Input and Output Files

| File | Purpose |
|---|---|
| `repos_seed5.txt` | Repository sample generated using seed 5. |
| `scan_progress_seed5.jsonl` | Scan progress and intermediate findings. |
| `credentials_seed5.jsonl` | Intermediate credential-analysis records. |
| `worth_investigating_seed5.jsonl` | Filtered findings requiring further review. |
| `all_investigating_credentials.xlsx` | Consolidated research spreadsheet. |

Generated files containing sensitive information should be excluded from version control.

---

## ⚙️ How It Works Under the Hood

### `sample_github_api.py`

Uses the GitHub API to collect repository samples. Random seeds support reproducible experiments and comparisons between different scanning batches.

### `scan.py`

Uses Python's subprocess module to execute TruffleHog, process its JSON output, and maintain scan progress.

The scanner examines Git history, allowing the research to identify potential exposures that may no longer be present in the latest version of a repository.

### `check_secrets.py`

Processes TruffleHog findings and examines credential-related patterns, including authentication information within connection strings.

### `filter_credentials.py`

Classifies findings and reduces false positives by identifying known defaults, placeholders, and test fixtures.

The objective is to retain higher-signal findings for responsible manual review.

### `make_excel.py`

Uses pandas and openpyxl to consolidate research records from multiple `worth_investigating` files into a structured Excel spreadsheet.

---

## 🛑 Responsible Disclosure Rules

All findings must be handled ethically, securely, and legally.

### 1. Do Not Log In

Never attempt to authenticate against third-party services using discovered credentials.

Potential credential validity must be confirmed by the repository owner or an explicitly authorized security team.

### 2. Report the Exposure

Navigate to the repository's **Security** tab and use its private vulnerability reporting mechanism where available.

If private vulnerability reporting is unavailable, contact the maintainer through an approved security contact channel.

Do not disclose credential values in public GitHub issues.

### 3. Provide Relevant Information

Responsible disclosure should include:

- Affected repository.
- File path.
- Line number.
- Commit hash.
- Credential type.
- Recommended remediation steps.

Repository owners should be advised to rotate or revoke affected credentials and remove sensitive information from Git history.

### 4. Protect Research Data

- Do not publish plaintext credentials.
- Do not commit sensitive scan outputs to GitHub.
- Restrict access to research datasets.
- Use redacted records in reports and presentations.

---

## 🔍 What This Pipeline Deliberately Does NOT Do

| Limitation | Description |
|---|---|
| No Credential Verification | Does not test credentials against live services or attempt authentication. |
| No Automated Reporting | Does not automatically email or message repository maintainers. |
| No Unauthorized Access | Does not use discovered credentials to access third-party accounts or systems. |
| No Guarantee of Validity | A detected credential may be expired, synthetic, or a false positive. |

All findings require appropriate review before responsible disclosure.

---

## 🎯 Research Objective

The objective of this project is to study accidental credential exposure in GitHub repositories, understand the limitations of automated secret detection, reduce false positives, and support responsible vulnerability disclosure.

The pipeline provides a structured approach to repository sampling, secret detection, credential classification, noise reduction, and research reporting.

---

**For educational, authorized security research, and responsible disclosure purposes only.**
