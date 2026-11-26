import json
from urllib.parse import urlparse, unquote

def load_credentials(source_type="json", file_path="findings.json"):
    """
    Loads credentials and normalizes them into a standard format.
    Standard Format: {
        'type': 'mongodb' | 'postgres' | 'web',
        'raw': 'original_string',
        'user': 'user',
        'password': 'pass',
        'host': 'host',
        'port': 27017,
        'db': 'dbname',
        'url': 'full_url'
    }
    """
    credentials = []
    
    if source_type == "json":
        with open(file_path, 'r') as f:
            # Assuming your file is JSONL (JSON Lines) or a JSON array
            # If JSONL:
            for line in f:
                line = line.strip()
                if not line: continue
                data = json.loads(line)
                credentials.append(process_entry(data))
    elif source_type == "mock":
        # For your current mock tests
        return [
            {"type": "mongodb", "raw": "mongodb+srv://usuario1:123456a.@cluster0.24yvhip.mongodb.net/ecommerce?appName=Cluster0&retryWrites=true&w=majority", "user": "usuario1", "password": "123456a.", "host": "cluster0.24yvhip.mongodb.net", "port": 27017, "db": "ecommerce", "url": "mongodb+srv://usuario1:123456a.@cluster0.24yvhip.mongodb.net/ecommerce?appName=Cluster0&retryWrites=true&w=majority"},
            {"type": "postgres", "raw": "postgresql://postgres:pgs3cr3t@postgres:5432", "user": "postgres", "password": "pgs3cr3t", "host": "postgres", "port": 5432, "db": "postgres", "url": "postgresql://postgres:pgs3cr3t@postgres:5432"}
        ]
        
    return credentials

def process_entry(data):
    detector = data.get('detector', '').lower()
    secret = data.get('source_secret', '')
    user = data.get('user_id', '')
    password = data.get('password', '')
    
    # Determine Type
    if 'mongodb' in detector or secret.startswith('mongodb'):
        return parse_mongo(secret, user, password)
    elif 'postgres' in detector or secret.startswith('postgresql') or secret.startswith('postgres'):
        return parse_postgres(secret, user, password)
    else:
        # Fallback to Web if it looks like a URL or standard email/pass
        return {
            "type": "web",
            "raw": secret,
            "user": user,
            "password": password,
            "host": "web",
            "port": 443,
            "db": None,
            "url": secret
        }

def parse_mongo(secret, user, password):
    try:
        # Remove scheme for parsing if necessary, but urlparse handles mongodb+srv
        parsed = urlparse(secret)
        # Unquote is crucial because passwords often have %20, %3A, etc.
        pw = unquote(parsed.password) if parsed.password else password
        usr = unquote(parsed.username) if parsed.username else user
        
        return {
            "type": "mongodb",
            "raw": secret,
            "user": usr,
            "password": pw,
            "host": parsed.hostname,
            "port": parsed.port or 27017,
            "db": parsed.path.strip('/') or 'admin', # Default to admin or extract
            "url": secret
        }
    except Exception as e:
        print(f"Failed to parse mongo: {e}")
        return {"type": "mongodb", "raw": secret, "user": user, "password": password, "host": "unknown", "port": 27017, "db": "admin", "url": secret}

def parse_postgres(secret, user, password):
    try:
        parsed = urlparse(secret)
        pw = unquote(parsed.password) if parsed.password else password
        usr = unquote(parsed.username) if parsed.username else user
        
        return {
            "type": "postgres",
            "raw": secret,
            "user": usr,
            "password": pw,
            "host": parsed.hostname,
            "port": parsed.port or 5432,
            "db": parsed.path.strip('/') or 'postgres',
            "url": secret
        }
    except Exception as e:
        print(f"Failed to parse postgres: {e}")
        return {"type": "postgres", "raw": secret, "user": user, "password": password, "host": "unknown", "port": 5432, "db": "postgres", "url": secret}