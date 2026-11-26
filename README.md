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
| 6. Live Verification | Actively test credentials against live services to identify valid exposures. |
| 7. Data Exploration | Explore live databases to catalog data scope and sensitive fields. |

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

## 🚀 Full Pipeline Execution Flow
**1. Set GitHub token (to avoid API rate limits)**
export GITHUB_TOKEN=ghp_your_token_here

**2. Run the automated pipeline**
**Pass the random seed and the number of repositories you want to scan**
**Change the seed (2, 3, 4...) to get completely new batches**
python3 run_pipeline.py 2 

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

### Step 5: Data Preparation & Normalization
**Script:** `prepare_findings.py`

This stage converts the raw consolidated findings from the initial scanning phase into a standardized CSV format suitable for active verification. The script ensures a consistent schema across different scanning batches and handles data cleaning tasks such as whitespace stripping and default value injection.

**Input:** `all_investigating_credentials.xlsx`
**Output:** `findings_annotated.csv`

The standardized schema includes the following columns:
- `source_file`: Origin of the finding.
- `repo`: GitHub repository URL.
- `user_id`: Extracted username or identifier.
- `password`: Extracted password or secret.
- `detector`: TruffleHog detector type (e.g., MongoDB, Postgres).
- `file`: File path within the repository.
- `line`: Line number of the finding.
- `commit`: Commit hash where the secret was introduced.
- `source_secret`: The full connection string or secret value.
- `noise`: Boolean flag indicating if the finding is likely a placeholder.
- `preview`: A redacted preview of the secret for safe display.

### Step 6: Live Credential Verification
**Script:** `db_tester.py`

This stage performs active verification of the filtered credential candidates against their intended services. The goal is to distinguish between historical artifacts (dead credentials) and active exposures (live credentials).

The verifier supports multiple protocols, including MongoDB, PostgreSQL, MySQL, Redis, and HTTP Basic Auth. It employs a multi-stage validation strategy:
1. **Syntactic Parsing:** Extracts host, port, user, and password from connection strings.
2. **Network Reachability:** Performs DNS resolution and TCP socket checks to identify unreachable or firewalled endpoints.
3. **Authentication Handshake:** Initiates a secure connection using the extracted credentials.
4. **Status Classification:** Categorizes the outcome into standardized statuses:
   - `SUCCESS`: Valid credentials with active access.
   - `INVALID_CREDENTIALS`: Service reachable, but authentication failed.
   - `UNREACHABLE`: Network timeout or DNS failure.
   - `INTERNAL_HOST`: Credential points to a private/Docker service name (e.g., `localhost`, `mongo`).
   - `CLUSTER_DELETED`: Specific to MongoDB Atlas, indicating the cluster no longer exists.

**Parameters:**

| Parameter | Description |
| :--- | :--- |
| `--input` | Input CSV file containing filtered credentials (default: `findings_annotated.csv`). |
| `--output` | Output CSV file for verification results (default: `verified_credentials.csv`). |
| `--workers` | Number of concurrent network workers (default: 10). |

**Note:** Verification should be conducted in a controlled environment to avoid unintended side effects on production systems. Read-only operations (`ping`, `version()`) are preferred to minimize impact.

### Step 7: Data Exploration & Extraction
**Script:** `db_read_only_explore.py`

For credentials classified as `SUCCESS`, this stage performs a read-only exploration of the target database. The objective is to catalog the data exposure scope, identifying sensitive collections, user records, and potential PII (Personally Identifiable Information).

The exploration module includes:
- **Database Enumeration:** Lists all accessible databases and collections.
- **Document Sampling:** Retrieves a limited sample (e.g., first 3 documents) from each collection to assess data structure.
- **Flattening:** Converts nested JSON documents into flat, tabular structures for easier analysis.
- **Sensitive Field Detection:** Automatically flags fields containing keywords such as `password`, `email`, `token`, `api_key`, and `secret`.
- **Deduplication & Resumability:** Implements logic to skip connections already explored in previous runs, allowing for incremental pipeline execution.

**Output:**
The results are consolidated into a multi-sheet Excel workbook (`db_exploration_results.xlsx`):
1. **Summary:** High-level overview of explored connections, including status and accessible databases.
2. **Samples:** Flattened sample documents from each collection.
3. **Sensitive_Findings:** A dedicated sheet listing all fields that matched sensitive data patterns, including a preview of the value and its length.

This stage provides the raw evidence required for impact assessment and disclosure drafting.

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
| `prepare_findings.py` | Converts consolidated Excel findings into a standardized CSV format for verification. |
| `db_tester.py` | Performs active live-verification of credentials against target services. |
| `db_read_only_explore.py` | Explores live databases to extract sensitive data and generate structured reports. |

### Input and Output Files

| File | Purpose |
|---|---|
| `repos_seed5.txt` | Repository sample generated using seed 5. |
| `scan_progress_seed5.jsonl` | Scan progress and intermediate findings. |
| `credentials_seed5.jsonl` | Intermediate credential-analysis records. |
| `worth_investigating_seed5.jsonl` | Filtered findings requiring further review. |
| `all_investigating_credentials.xlsx` | Consolidated research spreadsheet. |
| `findings_annotated.csv` | Standardized CSV output from `prepare_findings.py`. |
| `verified_credentials.csv` | Active verification results (status, latency, errors). |
| `db_exploration_results.xlsx` | Final exploration report containing sampled data and sensitive field inventory. |

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

### `prepare_findings.py`**

Normalizes the consolidated Excel data into a CSV format. It handles column mapping, whitespace stripping, and ensures the schema matches the requirements of the verification engine.

### `db_tester.py`

Implements a concurrent verification engine using `concurrent.futures`. It parses connection strings to extract host, port, and credentials, then performs DNS lookups and TCP socket checks to filter unreachable hosts. For reachable hosts, it initiates protocol-specific authentication handshakes (MongoDB, PostgreSQL, etc.) to classify credentials as `SUCCESS`, `INVALID_CREDENTIALS`, or `UNREACHABLE`.

### `db_read_only_explore.py`

For verified `SUCCESS` credentials, this script performs a read-only exploration of the target database. It enumerates collections, samples documents, and flattens nested JSON structures into tabular formats. It includes a sensitive field detector that flags values matching patterns for passwords, emails, and API keys, appending the results to a multi-sheet Excel workbook.

---

## 🛑 Responsible Disclosure Rules

All findings must be handled ethically, securely, and legally.

---


## 🎯 Research Objective

The objective of this project is to study accidental credential exposure in GitHub repositories, understand the limitations of automated secret detection, reduce false positive.

The pipeline provides a structured approach to repository sampling, secret detection, credential classification, noise reduction, and research reporting.

---

**For educational, authorized security research, and responsible disclosure purposes only.**
