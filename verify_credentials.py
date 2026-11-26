import pandas as pd
import logging
import time
import concurrent.futures
import socket
from urllib.parse import unquote
from typing import Dict, Optional, Tuple

# --- OPTIONAL DATABASE DRIVERS ---
try:
    from pymongo import MongoClient
    from pymongo.errors import PyMongoError
    HAS_MONGO = True
except ImportError:
    HAS_MONGO = False

try:
    import psycopg2
    from psycopg2 import OperationalError
    HAS_POSTGRES = True
except ImportError:
    HAS_POSTGRES = False

try:
    import pymysql
    from pymysql import err as pymysql_err
    HAS_MYSQL = True
except ImportError:
    HAS_MYSQL = False

try:
    import redis
    from redis.exceptions import RedisError
    HAS_REDIS = True
except ImportError:
    HAS_REDIS = False

try:
    import requests
    HAS_REQUESTS = True
except ImportError:
    HAS_REQUESTS = False

logging.basicConfig(level=logging.INFO, format='%(asctime)s - %(levelname)s - %(message)s')
logger = logging.getLogger(__name__)

# --- CONFIGURATION ---
TIMEOUT = 5  # Seconds
MAX_WORKERS = 10  # Concurrency level

class CredentialVerifier:
    def __init__(self, input_file: str, output_file: str):
        self.input_file = input_file
        self.output_file = output_file
        
        # Load input data
        self.df = pd.read_csv(input_file)
        logger.info(f"Loaded {len(self.df)} records from {input_file}")

        # Initialize verified_keys to an empty set by default
        self.verified_keys = set()

        # Resume logic: Load existing results if they exist
        try:
            self.results_df = pd.read_csv(output_file)
            # Create a set of verified keys for fast lookup
            self.verified_keys = set(zip(
                self.results_df['repo'].fillna(''), 
                self.results_df['file'].fillna(''), 
                self.results_df['line'].fillna('')
            ))
            logger.info(f"Resuming: {len(self.verified_keys)} items already verified.")
        except FileNotFoundError:
            self.results_df = pd.DataFrame(columns=[
                'status', 'error', 'repo', 'user_id', 'file', 'line', 'commit', 
                'server_version', 'latency_ms', 'host', 'port', 'protocol'
            ])
            logger.info(f"Output file {output_file} not found. Starting fresh.")

    def _extract_creds(self, source_secret: str) -> Optional[Dict]:
        """
        Robustly extracts user, pass, host, port, protocol from a connection string.
        Handles multi-host replica sets by extracting the first host.
        """
        if not source_secret:
            return None

        conn = source_secret.strip()
        
        # Detect Protocol & Default Port
        protocol = 'unknown'
        default_port = 0
        
        if conn.startswith('mongodb+srv://'):
            protocol = 'mongodb'
            default_port = 27017
        elif conn.startswith('mongodb://'):
            protocol = 'mongodb'
            default_port = 27017
        elif conn.startswith('postgresql://') or conn.startswith('postgres://'):
            protocol = 'postgres'
            default_port = 5432
        elif conn.startswith('mysql://'):
            protocol = 'mysql'
            default_port = 3306
        elif conn.startswith('redis://') or conn.startswith('rediss://'):
            protocol = 'redis'
            default_port = 6379
        elif conn.startswith('http://') or conn.startswith('https://'):
            protocol = 'http'
            default_port = 443 if conn.startswith('https') else 80
        else:
            return None

        # Extract User:Pass
        after_proto = conn.split('://', 1)[1]
        
        user = None
        password = None
        
        if '@' in after_proto:
            auth_part, host_part = after_proto.rsplit('@', 1)
            
            if ':' in auth_part:
                user, password = auth_part.split(':', 1)
            else:
                user = auth_part
                password = ""
            
            user = unquote(user)
            password = unquote(password)
        else:
            host_part = after_proto
            user = None
            password = None

        # Extract Host and Port
        # Remove query params and path
        host_str = host_part.split('/', 1)[0].split('?', 1)[0]
        
        host = None
        port = default_port
        
        # Handle multi-host replica sets (comma-separated)
        # We only need the first host for the initial test
        if ',' in host_str:
            host_str = host_str.split(',')[0]

        if ':' in host_str:
            # Handle IPv6 [::1]:port
            if host_str.startswith('['):
                bracket_end = host_str.find(']')
                if bracket_end != -1:
                    host = host_str[1:bracket_end]
                    port_str = host_str[bracket_end+1:].lstrip(':')
                    if port_str:
                        try: port = int(port_str)
                        except: pass
            else:
                host, port_str = host_str.rsplit(':', 1)
                try:
                    port = int(port_str)
                except ValueError:
                    host = host_str
        else:
            host = host_str

        if not host:
            return None

        return {
            'protocol': protocol,
            'host': host,
            'port': port,
            'user': user,
            'password': password,
            'original': source_secret
        }

    def _check_dns(self, host: str) -> Tuple[bool, str]:
        """
        Quick DNS check. Returns (success, error_message).
        """
        try:
            socket.gethostbyname(host)
            return True, "OK"
        except socket.gaierror as e:
            return False, f"DNS_FAIL: {e}"
        except Exception as e:
            return False, f"DNS_ERROR: {e}"

    def _test_mongodb(self, creds: Dict) -> Dict:
        if not HAS_MONGO:
            return {"status": "SKIPPED", "error": "Pymongo not installed", "server_version": None}
        
        try:
            client = MongoClient(
                creds['original'], 
                serverSelectionTimeoutMS=TIMEOUT*1000, 
                connectTimeoutMS=TIMEOUT*1000
            )
            client.admin.command('ping')
            server_info = client.server_info()
            client.close()
            return {"status": "SUCCESS", "server_version": server_info.get('version'), "error": None}
        except PyMongoError as e:
            err_str = str(e)
            # Specific Atlas SRV Lookup Failure
            if "The DNS query name does not exist" in err_str and "_mongodb._tcp" in err_str:
                return {"status": "CLUSTER_DELETED", "server_version": None, "error": "Atlas SRV record missing"}
            elif "Authentication failed" in err_str or "AuthenticationFailed" in err_str or "bad auth" in err_str:
                return {"status": "INVALID_CREDENTIALS", "server_version": None, "error": err_str}
            elif "ServerSelectionTimeout" in err_str or "timed out" in err_str.lower():
                return {"status": "TIMEOUT_OR_FIREWALL", "server_version": None, "error": err_str}
            else:
                return {"status": "FAILED", "server_version": None, "error": err_str}
        except Exception as e:
            return {"status": "ERROR", "server_version": None, "error": str(e)}
    def _test_postgres(self, creds: Dict) -> Dict:
        if not HAS_POSTGRES:
            return {"status": "SKIPPED", "error": "Psycopg2 not installed", "server_version": None}
        
        try:
            conn = psycopg2.connect(
                host=creds['host'],
                port=creds['port'],
                user=creds['user'],
                password=creds['password'],
                connect_timeout=TIMEOUT
            )
            with conn.cursor() as cur:
                cur.execute("SELECT version();")
                version = cur.fetchone()[0]
            conn.close()
            return {"status": "SUCCESS", "server_version": version, "error": None}
        except OperationalError as e:
            err_str = str(e)
            if "password authentication failed" in err_str:
                return {"status": "INVALID_CREDENTIALS", "server_version": None, "error": err_str}
            elif "timeout" in err_str.lower() or "could not connect" in err_str.lower():
                return {"status": "TIMEOUT_OR_FIREWALL", "server_version": None, "error": err_str}
            else:
                return {"status": "FAILED", "server_version": None, "error": err_str}
        except Exception as e:
            return {"status": "ERROR", "server_version": None, "error": str(e)}

    def _test_mysql(self, creds: Dict) -> Dict:
        if not HAS_MYSQL:
            return {"status": "SKIPPED", "error": "PyMySQL not installed", "server_version": None}
        
        try:
            conn = pymysql.connect(
                host=creds['host'],
                port=creds['port'],
                user=creds['user'],
                password=creds['password'],
                connect_timeout=TIMEOUT
            )
            with conn.cursor() as cur:
                cur.execute("SELECT VERSION();")
                version = cur.fetchone()[0]
            conn.close()
            return {"status": "SUCCESS", "server_version": version, "error": None}
        except pymysql_err.OperationalError as e:
            err_str = str(e)
            if "Access denied" in err_str or "1045" in err_str:
                return {"status": "INVALID_CREDENTIALS", "server_version": None, "error": err_str}
            elif "timed out" in err_str.lower() or "unable to connect" in err_str.lower():
                return {"status": "TIMEOUT_OR_FIREWALL", "server_version": None, "error": err_str}
            else:
                return {"status": "FAILED", "server_version": None, "error": err_str}
        except Exception as e:
            return {"status": "ERROR", "server_version": None, "error": str(e)}

    def _test_redis(self, creds: Dict) -> Dict:
        if not HAS_REDIS:
            return {"status": "SKIPPED", "error": "Redis not installed", "server_version": None}
        
        try:
            r = redis.Redis(
                host=creds['host'],
                port=creds['port'],
                password=creds['password'],
                socket_timeout=TIMEOUT,
                socket_connect_timeout=TIMEOUT
            )
            r.ping()
            info = r.info('server')
            version = info.get('redis_version')
            return {"status": "SUCCESS", "server_version": version, "error": None}
        except redis.exceptions.AuthenticationError as e:
            return {"status": "INVALID_CREDENTIALS", "server_version": None, "error": str(e)}
        except RedisError as e:
            err_str = str(e)
            if "timed out" in err_str.lower():
                return {"status": "TIMEOUT_OR_FIREWALL", "server_version": None, "error": err_str}
            else:
                return {"status": "FAILED", "server_version": None, "error": err_str}
        except Exception as e:
            return {"status": "ERROR", "server_version": None, "error": str(e)}

    def _test_http_basic_auth(self, creds: Dict) -> Dict:
        if not HAS_REQUESTS:
            return {"status": "SKIPPED", "error": "Requests not installed", "server_version": None}

        scheme = 'https' if creds['port'] == 443 else 'http'
        if (creds['port'] == 80 and scheme == 'http') or (creds['port'] == 443 and scheme == 'https'):
            base_url = f"{scheme}://{creds['host']}"
        else:
            base_url = f"{scheme}://{creds['host']}:{creds['port']}"
        
        url = base_url + "/"
        
        try:
            response = requests.get(
                url, 
                auth=(creds['user'], creds['password']),
                timeout=TIMEOUT,
                allow_redirects=False
            )
            
            status_code = response.status_code
            
            if 200 <= status_code < 300:
                return {"status": "SUCCESS", "server_version": f"HTTP {status_code}", "error": None}
            elif 300 <= status_code < 400:
                return {"status": "SUCCESS_REDIRECT", "server_version": f"HTTP {status_code}", "error": None}
            elif status_code in [401, 403]:
                return {"status": "INVALID_CREDENTIALS", "server_version": f"HTTP {status_code}", "error": "Access Denied"}
            elif status_code == 404:
                return {"status": "PATH_NOT_FOUND", "server_version": f"HTTP {status_code}", "error": "Server reachable, path missing"}
            else:
                return {"status": "FAILED", "server_version": f"HTTP {status_code}", "error": "Unexpected Status"}
                
        except requests.exceptions.Timeout:
            return {"status": "TIMEOUT_OR_FIREWALL", "server_version": None, "error": "Request Timeout"}
        except requests.exceptions.ConnectionError as e:
            return {"status": "CONNECTION_ERROR", "server_version": None, "error": str(e)}
        except Exception as e:
            return {"status": "ERROR", "server_version": None, "error": str(e)}

    def _verify_single(self, row: pd.Series) -> Dict:
        """
        Main verification logic for a single row.
        """
        key = (row['repo'], row['file'], row['line'])
        
        # Check if already verified
        if key in self.verified_keys:
            return None

        source_secret = row['source_secret']
        
        # Quick filter: Only verify if it looks like a connection string
        if not source_secret or '://' not in source_secret:
            return {
                'status': 'SKIPPED', 'error': 'No URI detected', 
                'repo': row['repo'], 'user_id': row['user_id'], 'file': row['file'], 
                'line': row['line'], 'commit': row['commit'], 'server_version': None,
                'latency_ms': 0, 'host': None, 'port': None, 'protocol': None
            }

        creds = self._extract_creds(source_secret)
        
        if not creds:
            return {
                'status': 'PARSE_ERROR', 'error': 'Failed to parse credentials', 
                'repo': row['repo'], 'user_id': row['user_id'], 'file': row['file'], 
                'line': row['line'], 'commit': row['commit'], 'server_version': None,
                'latency_ms': 0, 'host': None, 'port': None, 'protocol': None
            }

        host = creds['host']
        port = creds['port']
        protocol = creds['protocol']

        # Private/Docker Host Check
        if host in ['localhost', '127.0.0.1', 'mongo', 'postgres', 'db', 'database', 'redis', 'mysql', 'postgresql']:
            return {
                'status': 'INTERNAL_HOST', 'error': f"Host {host} is internal/docker service name", 
                'repo': row['repo'], 'user_id': row['user_id'], 'file': row['file'], 
                'line': row['line'], 'commit': row['commit'], 'server_version': None,
                'latency_ms': 0, 'host': host, 'port': port, 'protocol': protocol
            }

        # DNS Check (Optional but helpful for fast fails)
        # Skip DNS check for mongodb+srv as it requires TXT record lookup
        if protocol != 'mongodb' or 'mongodb+srv' not in source_secret:
            dns_ok, dns_msg = self._check_dns(host)
            if not dns_ok:
                return {
                    'status': 'DNS_FAIL', 'error': dns_msg, 
                            'repo': row['repo'], 'user_id': row['user_id'], 'file': row['file'], 
                    'line': row['line'], 'commit': row['commit'], 'server_version': None,
                    'latency_ms': 0, 'host': host, 'port': port, 'protocol': protocol
                }

        start_time = time.time()
        
        # Dispatch to correct tester
        if protocol == 'mongodb':
            result = self._test_mongodb(creds)
        elif protocol == 'postgres':
            result = self._test_postgres(creds)
        elif protocol == 'mysql':
            result = self._test_mysql(creds)
        elif protocol == 'redis':
            result = self._test_redis(creds)
        elif protocol in ['http', 'https']:
            result = self._test_http_basic_auth(creds)
        else:
            result = {
                "status": "UNSUPPORTED_PROTOCOL", 
                "server_version": None, 
                "error": f"Protocol {protocol} not supported"
            }

        latency_ms = int((time.time() - start_time) * 1000)

        # Construct final result row
        final_result = {
            'status': result['status'],
            'error': result.get('error'),
            'repo': row['repo'],
            'user_id': row['user_id'],
            'file': row['file'],
            'line': row['line'],
            'commit': row['commit'],
            'server_version': result.get('server_version'),
            'latency_ms': latency_ms,
            'host': host,
            'port': port,
            'protocol': protocol
        }
        
        # Log specific interesting findings
        if result['status'] == 'SUCCESS':
            logger.info(f"[VERIFIED] {protocol}://{creds['user']}@{host}:{port} (Latency: {latency_ms}ms)")
        elif result['status'] == 'INVALID_CREDENTIALS':
            logger.info(f"[INVALID] {protocol}://{creds['user']}@{host}:{port} - Auth Failed")
            
        return final_result

    def run(self):
        """
        Executes the verification process using a thread pool.
        """
        # Prepare list of indices to process
        indices_to_process = []
        for idx, row in self.df.iterrows():
            key = (row['repo'], row['file'], row['line'])
            if key not in self.verified_keys:
                indices_to_process.append(idx)

        if not indices_to_process:
            logger.info("No new items to verify.")
            return

        logger.info(f"Starting verification for {len(indices_to_process)} items with {MAX_WORKERS} workers...")
        
        new_results = []
        
        # Use ThreadPoolExecutor for I/O bound network tasks
        with concurrent.futures.ThreadPoolExecutor(max_workers=MAX_WORKERS) as executor:
            future_to_idx = {
                executor.submit(self._verify_single, self.df.loc[idx]): idx 
                for idx in indices_to_process
            }
            
            # Process as they complete
            for future in concurrent.futures.as_completed(future_to_idx):
                idx = future_to_idx[future]
                try:
                    result = future.result()
                    if result:
                        new_results.append(result)
                        # Small pause to avoid overwhelming a single host if many creds point to same IP
                        if len(new_results) % 50 == 0:
                            time.sleep(0.1)
                except Exception as exc:
                    logger.error(f"Row {idx} generated an exception: {exc}")
                    row = self.df.loc[idx]
                    new_results.append({
                        'status': 'EXCEPTION',
                        'error': str(exc),
                        'repo': row['repo'],
                        'user_id': row['user_id'],
                        'file': row['file'],
                        'line': row['line'],
                        'commit': row['commit'],
                        'server_version': None,
                        'latency_ms': 0,
                        'host': None,
                        'port': None,
                        'protocol': None
                    })

        if new_results:
            new_df = pd.DataFrame(new_results)
            # Append to existing results
            self.results_df = pd.concat([self.results_df, new_df], ignore_index=True)
            
            # Save to disk
            self.results_df.to_csv(self.output_file, index=False)
            logger.info(f"Saved {len(new_results)} new results. Total verified: {len(self.results_df)}")
        else:
            logger.info("No new results to save.")

if __name__ == "__main__":
    import argparse
    parser = argparse.ArgumentParser(description="Verify extracted credentials against live services.")
    parser.add_argument("--input", default="findings_annotated.csv", help="Input CSV file with extracted credentials")
    parser.add_argument("--output", default="verified_credentials.csv", help="Output CSV file for verification results")
    parser.add_argument("--workers", type=int, default=MAX_WORKERS, help="Number of concurrent workers")
    args = parser.parse_args()
    
    # Override global MAX_WORKERS if provided

    MAX_WORKERS = args.workers
    
    verifier = CredentialVerifier(args.input, args.output)
    verifier.run()