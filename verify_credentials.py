import pandas as pd
import json
import random
import socket
import time
from urllib.parse import urlparse, unquote
from pymongo import MongoClient
from pymongo.errors import PyMongoError
import psycopg2
import socks

# --- PROXY POOL ---
# Format: "host:port" for SOCKS5
# If you don't have proxies, leave this empty.
PROXY_POOL = [
    # Add more SOCKS5 proxies here
]

def get_proxy():
    if not PROXY_POOL:
        return None
    return random.choice(PROXY_POOL)

def set_socks_proxy(proxy_addr):
    """
    Sets the global socket to use a SOCKS5 proxy.
    """
    if not proxy_addr:
        return
    host, port = proxy_addr.split(':')
    socks.set_default_proxy(socks.PROXY_TYPE_SOCKS5, host, int(port))
    socket.socket = socks.socksocket

def reset_socks_proxy():
    """
    Resets the global socket to normal.
    """
    socket.socket = socket.socket
    socks.set_default_proxy(None)

def parse_connection_string(conn_string):
    """
    Parses a connection string to extract host, port, and credentials.
    Handles MongoDB replica sets (multiple hosts) by extracting the first host.
    """
    # Handle mongodb+srv:// specially
    if conn_string.startswith("mongodb+srv://"):
        # mongodb+srv://user:pass@host/db?opts
        # Remove protocol
        parsed = urlparse(conn_string)
        host = parsed.hostname
        port = 27017  # Default for Atlas
        user = unquote(parsed.username) if parsed.username else None
        pass_ = unquote(parsed.password) if parsed.password else None
        
    elif conn_string.startswith("mongodb://"):
        # Handle multi-host connection strings (replica sets)
        # Example: mongodb://user:pass@host1:27017,host2:27017,host3:27017/db
        # We only need the first host for testing
        if '@' in conn_string:
            # Split off the auth part
            auth_part, rest = conn_string.split('@', 1)
            # The rest contains the host(s) and database
            # Find the first host:port pair
            # Look for the first comma or slash
            first_host_part = rest.split(',')[0].split('/')[0]
            
            # Parse the first host:port
            if ':' in first_host_part:
                host, port_str = first_host_part.rsplit(':', 1)
                try:
                    port = int(port_str)
                except ValueError:
                    port = 27017
            else:
                host = first_host_part
                port = 27017
                
            # Extract user:pass from auth_part
            if ':' in auth_part:
                user, pass_ = auth_part.rsplit(':', 1)
                user = unquote(user)
                pass_ = unquote(pass_)
            else:
                user = unquote(auth_part)
                pass_ = None
        else:
            # No auth part
            parsed = urlparse(conn_string)
            host = parsed.hostname
            port = parsed.port or 27017
            user = None
            pass_ = None
            
    elif conn_string.startswith("postgresql://"):
        parsed = urlparse(conn_string)
        host = parsed.hostname
        port = parsed.port or 5432
        user = unquote(parsed.username) if parsed.username else None
        pass_ = unquote(parsed.password) if parsed.password else None
    else:
        return None
    
    return {
        "host": host,
        "port": port,
        "user": user,
        "password": pass_,
        "original": conn_string
    }

def is_private_host(host):
    """
    Checks if a host is a private IP or a known Docker service name.
    """
    # Check for Docker service names
    if host in ["mongo", "postgres", "postgresql", "db", "database"]:
        return True
        
    # Check for private IP ranges
    try:
        import ipaddress
        ip = ipaddress.ip_address(host)
        return ip.is_private or ip.is_loopback or ip.is_reserved
    except ValueError:
        # It's a domain name, not an IP. Assume public unless it fails to resolve.
        return False

def check_host_reachability(host, port, proxy_addr=None, timeout=5):
    """
    Checks if a host is reachable on a specific port, optionally through a proxy.
    """
    set_socks_proxy(proxy_addr)
    try:
        with socket.create_connection((host, port), timeout=timeout):
            return True
    except (socket.timeout, ConnectionRefusedError, OSError) as e:
        return False
    finally:
        reset_socks_proxy()

def test_mongodb_connection(conn_string, timeout=5, proxy_addr=None):
    """
    Tests a MongoDB connection string.
    """
    result = {
        "status": "UNKNOWN",
        "error": None,
        "server_version": None
    }
    
    set_socks_proxy(proxy_addr)
    try:
        # serverSelectionTimeoutMS: Don't wait forever if the host is unreachable
        client = MongoClient(conn_string, serverSelectionTimeoutMS=timeout * 1000)
        
        # Force a connection by running a command
        client.admin.command('ping')
        
        # Get server info
        server_info = client.server_info()
        result["server_version"] = server_info.get("version")
        result["status"] = "SUCCESS"
        
    except PyMongoError as e:
        error_str = str(e)
        if "Authentication failed" in error_str or "AuthenticationFailed" in error_str:
            result["status"] = "INVALID_CREDENTIALS"
        elif "ServerSelectionTimeout" in error_str:
            result["status"] = "UNREACHABLE"
        else:
            result["status"] = "FAILED"
        result["error"] = error_str
    finally:
        reset_socks_proxy()
        try:
            client.close()
        except:
            pass
    return result

def test_postgres_connection(conn_string, timeout=5, proxy_addr=None):
    """
    Tests a PostgreSQL connection string.
    """
    result = {
        "status": "UNKNOWN",
        "error": None,
        "server_version": None
    }
    
    set_socks_proxy(proxy_addr)
    try:
        # Create a connection
        conn = psycopg2.connect(conn_string, connect_timeout=timeout)
        
        # Run a simple query
        with conn.cursor() as cur:
            cur.execute("SELECT version();")
            version_row = cur.fetchone()
            result["server_version"] = version_row[0]
            result["status"] = "SUCCESS"
        
        conn.close()
        
    except psycopg2.OperationalError as e:
        error_str = str(e)
        if "password authentication failed" in error_str:
            result["status"] = "INVALID_CREDENTIALS"
        elif "timeout" in error_str.lower() or "could not connect" in error_str.lower():
            result["status"] = "UNREACHABLE"
        else:
            result["status"] = "FAILED"
        result["error"] = error_str
    finally:
        reset_socks_proxy()
    return result

def test_all_findings(input_file="findings_annotated.csv", output_file="db_test_results.csv"):
    df = pd.read_csv(input_file)
    
    # Filter for database-related findings
    db_df = df[df['detector'].str.contains('MongoDB|Postgres', case=False, na=False)]
    
    results = []
    for index, row in db_df.iterrows():
        conn_string = row['source_secret']
        detector = row['detector']
        
        # Parse connection string
        parsed = parse_connection_string(conn_string)
        if not parsed:
            results.append({
                "status": "PARSE_ERROR",
                "error": "Could not parse connection string",
                "repo": row['repo'],
                "user_id": row['user_id'],
                "file": row['file'],
                "line": row['line'],
                "commit": row['commit']
            })
            continue
            
        # Check if host is private
        if is_private_host(parsed['host']):
            results.append({
                "status": "PRIVATE_HOST",
                "error": f"Host {parsed['host']} is private or a Docker service name",
                "repo": row['repo'],
                "user_id": row['user_id'],
                "file": row['file'],
                "line": row['line'],
                "commit": row['commit']
            })
            continue
            
        # Get a proxy
        proxy_addr = get_proxy()
        
        print(f"[TESTING] {detector}: {parsed['host']}:{parsed['port']} (Proxy: {proxy_addr or 'DIRECT'})")
        
        # Check reachability first
        if not check_host_reachability(parsed['host'], parsed['port'], proxy_addr):
            results.append({
                "status": "UNREACHABLE",
                "error": "Host not reachable",
                "repo": row['repo'],
                "user_id": row['user_id'],
                "file": row['file'],
                "line": row['line'],
                "commit": row['commit']
            })
            continue
            
        # Test credentials
        if "MongoDB" in detector:
            result = test_mongodb_connection(conn_string, proxy_addr=proxy_addr)
        elif "Postgres" in detector:
            result = test_postgres_connection(conn_string, proxy_addr=proxy_addr)
        else:
            result = {"status": "SKIPPED", "error": "Unknown database type"}
            
        result["repo"] = row['repo']
        result["user_id"] = row['user_id']
        result["file"] = row['file']
        result["line"] = row['line']
        result["commit"] = row['commit']
        results.append(result)
        
        print(f"[DONE] {result['status']}: {result['error']}")
        
        # Small delay to avoid rate limiting
        time.sleep(random.uniform(1, 3))
    
    # Save results
    results_df = pd.DataFrame(results)
    results_df.to_csv(output_file, index=False)
    print(f"Results saved to {output_file}")

if __name__ == "__main__":
    import argparse
    parser = argparse.ArgumentParser(description="Test database credentials from findings.")
    parser.add_argument("--input", default="findings_annotated.csv", help="Input CSV file")
    parser.add_argument("--output", default="db_test_results.csv", help="Output CSV file")
    args = parser.parse_args()
    
    test_all_findings(args.input, args.output)