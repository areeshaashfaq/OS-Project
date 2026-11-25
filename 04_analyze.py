
import json
import csv
from pathlib import Path

# --- Configuration ---
FINDINGS_FILE = "findings.json"
CSV_OUTPUT = "findings_annotated.csv"
NOISE_MARKERS = [
    "node_modules", ".min.", "site-packages",
    "vendor/", ".git/", "dist/", "build/"
]

def is_noise(file_path, noise_list):
    """Checks if the file path contains any noise strings."""
    path_lower = file_path.lower()
    for marker in noise_list:
        if marker.lower() in path_lower:
            return True
    return False

def write_reports():
    # 1. Load the raw findings
    try:
        with open(FINDINGS_FILE, 'r') as f:
            data = json.load(f)
    except FileNotFoundError:
        print(f"Error: {FINDINGS_FILE} not found. Run scan.py first!")
        return

    # 2. Flatten and Structure
    # Trufflehog outputs a list of objects. Each object has 'path', 'type', 'match'
    report_rows = []

    for finding in data:
        path = finding.get('path', '')
        match = finding.get('match', finding.get('value', '')) # Handle different versions
        detector = finding.get('detector', 'Unknown')
        fingerprint = finding.get('fingerprint', '')

        # Add CSV specific columns
        report_rows.append({
            'path': path,
            'value': match, # Trufflehog v3 might use 'value', check yours
            'detector': detector,
            'type': finding.get('type', 'file'),
            'fingerprint': fingerprint,
            'is_noise': is_noise(path, NOISE_MARKERS),
            'masked_preview': f"{match[:30]}..." if len(match) > 30 else match
        })

    # 3. Write Annotated CSV
    with open(CSV_OUTPUT, 'w', newline='') as csvfile:
        fieldnames = ['path', 'detector', 'type', 'fingerprint', 'is_noise', 'masked_preview', 'value']
        writer = csv.DictWriter(csvfile, fieldnames=fieldnames)

        writer.writeheader()
        for row in report_rows:
            writer.writerow({k: row.get(k, '') for k in fieldnames})

    print(f"Analyzed {len(report_rows)} findings.")
    print(f"Output written to {CSV_OUTPUT}")

    # Print quick stats
    noise_count = sum(1 for r in report_rows if r.get('is_noise'))
    print(f"Noisy files detected: {noise_count}")

if __name__ == "__main__":
    write_reports()