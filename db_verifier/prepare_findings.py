import pandas as pd
import os
import sys

def excel_to_annotated_csv(input_file, output_file="findings_annotated.csv"):
    """
    Converts an Excel or CSV file of raw findings into the annotated CSV format
    required for credential testing.
    
    Expected Output Columns:
    - source_file
    - repo
    - user_id
    - password
    - detector
    - file
    - line
    - commit
    - source_secret
    - noise
    - preview
    """
    
    # 1. Validate Input File
    if not os.path.exists(input_file):
        raise FileNotFoundError(f"Input file '{input_file}' not found.")
    
    if input_file.endswith(('.xlsx', '.xls')):
        print(f"Reading Excel file: {input_file}")
        try:
            df = pd.read_excel(input_file)
        except Exception as e:
            raise ValueError(f"Failed to read Excel file: {e}")
    elif input_file.endswith('.csv'):
        print(f"Reading CSV file: {input_file}")
        try:
            df = pd.read_csv(input_file)
        except Exception as e:
            raise ValueError(f"Failed to read CSV file: {e}")
    else:
        raise ValueError("Input file must be .xlsx, .xls, or .csv")
    
    print(f"Loaded {len(df)} rows.")
    print(f"Columns found: {list(df.columns)}")
    
    # 2. Normalize column names (strip whitespace, lowercase)
    df.columns = df.columns.str.strip().str.lower()
    
    # 3. Rename common column variations to standard names
    column_mapping = {
        'repo_url': 'repo',
        'github_repo': 'repo',
        'repository': 'repo',
        'username': 'user_id',
        'user': 'user_id',
        'pwd': 'password',
        'pass': 'password',
        'file_path': 'file',
        'filepath': 'file',
        'line_number': 'line',
        'commit_hash': 'commit',
        'secret': 'source_secret',
        'connection_string': 'source_secret',
        'detector_type': 'detector',
        'type': 'detector'
    }
    
    for old_name, new_name in column_mapping.items():
        if old_name in df.columns and new_name not in df.columns:
            df = df.rename(columns={old_name: new_name})
            print(f"Renamed column '{old_name}' to '{new_name}'")
    
    # 4. Ensure required columns exist
    required_columns = ['repo', 'user_id', 'password', 'detector', 'file', 'line', 'commit', 'source_secret']
    missing_cols = [col for col in required_columns if col not in df.columns]
    if missing_cols:
        raise ValueError(f"Missing required columns: {missing_cols}. Please ensure your input file contains these columns.")
    
    # 5. Add default 'source_file' if not present
    if 'source_file' not in df.columns:
        df['source_file'] = "manual_import"
    
    # 6. Add default 'noise' column (set to False for now)
    if 'noise' not in df.columns:
        df['noise'] = False
    
    # 7. Add default 'preview' column (copy of source_secret)
    if 'preview' not in df.columns:
        df['preview'] = df['source_secret']
    
    # 8. Clean data
    # Strip whitespace from string columns
    for col in df.columns:
        if df[col].dtype == 'object':
            df[col] = df[col].astype(str).str.strip()
    
    # Convert 'line' to integer if possible
    df['line'] = pd.to_numeric(df['line'], errors='coerce').fillna(0).astype(int)
    
    # Convert 'noise' to boolean
    df['noise'] = df['noise'].astype(str).str.lower().isin(['true', '1', 'yes'])
    
    # 9. Drop rows with missing critical fields
    before_drop = len(df)
    df = df.dropna(subset=['repo', 'source_secret'])
    after_drop = len(df)
    if before_drop > after_drop:
        print(f"Removed {before_drop - after_drop} rows with missing critical fields.")
    
    # 10. Reorder columns to match the expected format
    column_order = ['source_file', 'repo', 'user_id', 'password', 'detector', 'file', 'line', 'commit', 'source_secret', 'noise', 'preview']
    
    # Ensure all columns in column_order exist
    missing_order_cols = [col for col in column_order if col not in df.columns]
    if missing_order_cols:
        raise ValueError(f"Missing columns in final order: {missing_order_cols}")
    
    df = df[column_order]
    
    # 11. Save to CSV
    # Use 'utf-8-sig' to ensure Excel opens it correctly with special characters
    df.to_csv(output_file, index=False, encoding='utf-8-sig', quoting=1)  # quoting=1 is QUOTE_ALL
    
    print(f"Successfully saved {len(df)} rows to {output_file}")
    print("Column distribution:")
    print(df['detector'].value_counts())

if __name__ == "__main__":
    import argparse
    parser = argparse.ArgumentParser(description="Convert Excel/CSV findings to annotated CSV format.")
    parser.add_argument("--input", default="all_investigating_credentials.xlsx", help="Input Excel (.xlsx) or CSV file")
    parser.add_argument("--output", default="findings_annotated.csv", help="Output CSV file")
    args = parser.parse_args()
    
    try:
        excel_to_annotated_csv(args.input, args.output)
    except Exception as e:
        print(f"Error: {e}")
        sys.exit(1)