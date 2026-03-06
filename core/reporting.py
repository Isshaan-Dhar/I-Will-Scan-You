from datetime import datetime
import os

def save_report(target, results):
    if not os.path.exists('reports'): os.makedirs('reports')
    filename = f"reports/scan_{target}.txt"
    with open(filename, 'w') as f:
        f.write(f"Vultron Scan Report - {target}\n" + "="*30 + "\n")
        for port, data in results.items():
            f.write(f"PORT {port}: {data['banner']}\nResult: {data['analysis']}\n\n")
    print(f"[+] Report generated: {filename}")