from core.scanner import MultiThreadedScanner
from core.fingerprint import get_service_banner
from core.analyzer import check_vulnerabilities
from core.reporting import save_report

def main():
    target = input("Enter Target (e.g., 127.0.0.1): ")
    scanner = MultiThreadedScanner(target)
    open_ports = scanner.run(range(1, 1025))
    
    results = {}
    for port in open_ports:
        banner = get_service_banner(target, port)
        results[port] = {"banner": banner, "analysis": check_vulnerabilities(banner)}
    
    save_report(target, results)

if __name__ == "__main__":
    main()