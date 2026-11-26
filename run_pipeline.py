#!/usr/bin/env python3
import subprocess
import sys
import os

def run_command(cmd):
    print(f"\n[{'+'}] Running: {' '.join(cmd)}")
    result = subprocess.run(cmd)
    if result.returncode != 0:
        print(f"❌ Error occurred during: {' '.join(cmd)}")
        sys.exit(1)

def main():
    if len(sys.argv) != 2:
        print("Usage: python3 run_pipeline.py <seed_number>")
        print("Example: python3 run_pipeline.py 7")
        sys.exit(1)

    seed = sys.argv[1]
    repos_file = f"repos_seed{seed}.txt"
    clean_repos_file = f"repos_seed{seed}_new.txt"
    progress_file = f"scan_progress_seed{seed}.jsonl"
    creds_file = f"credentials_seed{seed}.jsonl"
    worth_file = f"worth_investigating_seed{seed}.jsonl"

    print(f"==================================================")
    print(f" 🚀 STARTING AUTOMATED PIPELINE FOR SEED {seed}")
    print(f"==================================================")

    # 1. Generate Repos
    run_command(["python3", "sample_github_api.py", "--sample", "50", "--seed", seed, "--out", repos_file])

    # 2. Deduplicate Repos against already_scanned.txt
    print(f"\n[{'+'}] Deduplicating {repos_file}...")
    if os.path.exists("already_scanned.txt"):
        # Linux bash command to filter out existing repos
        cmd = f"grep -v '^#' {repos_file} | grep -vxFf already_scanned.txt > {clean_repos_file}"
        subprocess.run(cmd, shell=True)
        print(f"✅ Saved unique repos to {clean_repos_file}")
        target_repos = clean_repos_file
    else:
        print("⚠️ No already_scanned.txt found. Scanning all generated repos.")
        target_repos = repos_file

    # 3. Scan with TruffleHog
    run_command(["python3", "scan.py", "--repos-file", target_repos, "--workers", "4", "--progress", progress_file])

    # 4. Extract Credentials
    run_command(["python3", "check_secrets.py", progress_file, creds_file])

    # 5. Filter Noise
    run_command(["python3", "filter_credentials.py", creds_file, worth_file])

    # 6. Update Excel
    run_command(["python3", "make_excel.py"])

    # 7. Add the newly scanned repos to the master already_scanned list
    print(f"\n[{'+'}] Updating already_scanned.txt...")
    with open(target_repos, "r") as f:
        new_repos = f.readlines()
    with open("already_scanned.txt", "a") as f:
        for r in new_repos:
            if not r.startswith("#") and r.strip():
                f.write(r)

    print(f"\n🎉 PIPELINE COMPLETE FOR SEED {seed}!")
    print(f"Results added to all_investigating_credentials.xlsx")

if __name__ == "__main__":
    main()