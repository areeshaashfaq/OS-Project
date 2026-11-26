#!/usr/bin/env python3
import json
import glob
import pandas as pd
import os

def main():
    out_file = "all_investigating_credentials.xlsx"
    
    # 1. Find all worth_investigating files
    files = glob.glob("worth_investigating*.jsonl")
    if not files:
        print("❌ No worth_investigating*.jsonl files found.")
        return

    all_rows = []
    
    # 2. Read all JSONL files into a list
    for file_path in files:
        with open(file_path, "r", encoding="utf-8") as f:
            for line in f:
                line = line.strip()
                if not line:
                    continue
                try:
                    data = json.loads(line)
                    data["source_file"] = file_path
                    all_rows.append(data)
                except json.JSONDecodeError:
                    pass

    if not all_rows:
        print("🤷‍♂️ Files found, but they were empty.")
        return

    df_new = pd.DataFrame(all_rows)

    # Ensure standard column order
    columns = ["source_file", "repo", "user_id", "password", "detector", "file", "line", "commit", "source_secret"]
    columns = [c for c in columns if c in df_new.columns]
    df_new = df_new[columns]

    # 3. Check if the Excel file already exists
    if os.path.exists(out_file):
        print(f"📖 Found existing {out_file}. Reading data...")
        df_excel = pd.read_excel(out_file, engine="openpyxl")
        
        # We need to match columns between the old excel and the new data
        common_cols = [c for c in df_new.columns if c in df_excel.columns]
        
        # Create a unique fingerprint for each row to check for duplicates
        # A duplicate means the same repo, user, password, and file
        excel_keys = set(df_excel["repo"].astype(str) + "|" + df_excel["user_id"].astype(str) + "|" + df_excel["password"].astype(str) + "|" + df_excel["file"].astype(str))
        
        added_count = 0
        
        # 4. Loop through new rows and add only the unique ones
        for index, row in df_new.iterrows():
            key = f"{row['repo']}|{row['user_id']}|{row['password']}|{row['file']}"
            
            if key not in excel_keys:
                # This is a brand new finding! Add it.
                new_row_df = pd.DataFrame([row[common_cols]])
                df_excel = pd.concat([df_excel, new_row_df], ignore_index=True)
                excel_keys.add(key)
                added_count += 1
                print(f"  [+] Added new finding from: {row['repo'].split('/')[-1]}")
                
        # 5. Save back to Excel
        if added_count > 0:
            df_excel.to_excel(out_file, index=False, engine="openpyxl")
            print(f"\n✅ Successfully added {added_count} new unique rows to {out_file}.")
            print(f"📊 Total rows in Excel is now: {len(df_excel)}")
        else:
            print("\n🤷‍♂️ No new rows added. All findings in the JSONL files are already in the Excel file.")
            
    else:
        # If the Excel file doesn't exist, just create it from scratch
        print(f"📝 Creating new {out_file}...")
        df_new = df_new.drop_duplicates(subset=["repo", "user_id", "password", "file"])
        df_new.to_excel(out_file, index=False, engine="openpyxl")
        print(f"✅ Wrote {len(df_new)} findings to {out_file}")

if __name__ == "__main__":
    main()