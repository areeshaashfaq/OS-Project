#!/usr/bin/env python3
import json
import glob
import pandas as pd
import os

def main():
    # Find all files matching the pattern
    files = glob.glob("worth_investigating*.jsonl")
    if not files:
        print("No worth_investigating*.jsonl files found in this directory.")
        return

    all_rows = []

    for file_path in files:
        with open(file_path, "r", encoding="utf-8") as f:
            for line in f:
                line = line.strip()
                if not line:
                    continue
                try:
                    data = json.loads(line)
                    # Add a column so you know which batch this came from
                    data["source_file"] = file_path
                    all_rows.append(data)
                except json.JSONDecodeError:
                    pass

    if not all_rows:
        print("Files found, but they were empty.")
        return

    # Convert to a Pandas DataFrame
    df = pd.DataFrame(all_rows)

    # Reorder columns for better readability
    columns = [
        "source_file", "repo", "user_id", "password", 
        "detector", "file", "line", "commit", "source_secret"
    ]
    # Keep only columns that exist in the data
    columns = [c for c in columns if c in df.columns]
    df = df[columns]

    # Drop exact duplicates (e.g., if a secret appears multiple times in the same repo)
    df = df.drop_duplicates(subset=["repo", "user_id", "password", "file", "line"])

    # Save to Excel
    out_file = "all_investigating_credentials.xlsx"
    df.to_excel(out_file, index=False, engine="openpyxl")

    print(f"✅ Successfully combined {len(files)} files.")
    print(f"✅ Wrote {len(df)} unique rows to {out_file}")

if __name__ == "__main__":
    main()