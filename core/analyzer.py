import json
import os

def check_vulnerabilities(banner):
    db_path = os.path.join('data', 'vuln_db.json')
    try:
        with open(db_path, 'r') as f:
            vuln_db = json.load(f)
        for service, info in vuln_db.items():
            if service.lower() in banner.lower():
                return f"[CRITICAL] {info}"
        return "No known vulnerabilities found in local DB."
    except Exception as e:
        return f"Database Error: {e}"