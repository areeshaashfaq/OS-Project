import json
import re

def clean_secrets(input_file, output_file):
    print(f"🔍 Reading secrets from {input_file}...")

    with open(input_file, 'r', encoding='utf-8') as f:
        lines = f.readlines()

    cleaned_records = []

    for line in lines:
        # Skip empty lines
        if not line.strip():
            continue

        # We look for the pattern: "...email..." followed by "password: ..."
        # Regex breakdown:
        # (.+?password): Captures the ID up until the word "password"
        # (password):\s*: Captures the word "password:" and the colon
        # (["']?([^"'\s]+)["']?): Captures the password, handling quotes and stripping them

        pattern = r'^(.+?)(password):\s*(["\']?)([^"\'\s]+)(["\']?)$'

        # If the line isn't a perfect match (e.g., it has extra metadata), use a more flexible pattern
        # This fallback handles cases like "user: password: ..." or nested structures
        fallback_pattern = r'^(.+)(password):\s*(["\']?)([^"\'\s]+)(["\']?)'

        match = re.search(pattern, line)
        if not match:
            match = re.search(fallback_pattern, line)

        if match:
            email = match.group(1) # The part before "password:"
            # Get the raw password part (group 4)
            password_raw = match.group(4)

            # Clean up the password (strip surrounding quotes if we captured them)
            # This ensures "trial" becomes just trial, or "trial" stays as trial
            clean_password = password_raw.strip('"').strip("'")

            # Construct the clean record
            record = {
                "user_id": email,
                "password": clean_password,
                "source_line": line # Optional: keep the original line for debugging
            }
            cleaned_records.append(record)
            print(f"  ✓ Processed: {email} | {clean_password}")
        else:
            # If it didn't match the strict pattern, try just grabbing the ID and Password manually
            # Fallback for messy data:
            parts = line.split('password:')
            if len(parts) > 1:
                email = parts[0].strip()
                password_raw = parts[1].strip()
                clean_password = password_raw.split('"')[0] # Rough chop for messy data

                record = {
                    "user_id": email,
                    "password": clean_password,
                    "source_line": line
                }
                cleaned_records.append(record)

    # Write the result back to a new file (or overwrite if you prefer)
    with open(output_file, 'w', encoding='utf-8') as f:
        for record in cleaned_records:
            f.write(json.dumps(record) + '\n')

    print(f"✨ Done! Cleaned data saved to {output_file}")

if __name__ == "__main__":
    # Run the function
    clean_secrets("progress_v2.jsonl", "progress_v2_clean.jsonl")