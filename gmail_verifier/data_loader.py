import json
import pandas as pd
from mock_data import generate_mock_credentials

def load_credentials(source_type="mock", file_path="findings.json"):
    """
    Loads credentials from various sources.
    Returns a list of dictionaries: [{"email": ..., "password": ..., "totp_secret": ...}]
    """
    if source_type == "mock":
        print("[INFO] Loading mock data for testing...")
        return generate_mock_credentials(count=5)
    
    elif source_type == "json":
        print(f"[INFO] Loading real data from {file_path}...")
        # This is the function your team will eventually use.
        # It assumes findings.json contains a list of objects.
        # You will need to adjust this regex/logic once you have the sample line.
        try:
            with open(file_path, 'r') as f:
                raw_data = json.load(f)
            
            # Placeholder logic: 
            # Your team needs to tell us which keys in findings.json hold the email/password.
            # For now, we assume a structure like: [{"secret": "user:pass", "type": "password"}]
            cleaned = []
            for item in raw_data:
                # Example: If the secret is in the 'secret' field
                secret_str = item.get("secret", "")
                if "@" in secret_str:
                    # Simple split logic (to be replaced by team's specific parsing)
                    parts = secret_str.split(":", 1)
                    if len(parts) == 2:
                        cleaned.append({
                            "email": parts[0].strip(),
                            "password": parts[1].strip(),
                            "totp_secret": None,
                            "source": item.get("repo", "unknown")
                        })
            return cleaned
        except Exception as e:
            print(f"[ERROR] Failed to load JSON: {e}")
            return []
            
    else:
        raise ValueError(f"Unknown source type: {source_type}")