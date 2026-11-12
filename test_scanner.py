from scanner import PortScanner
from results import display_results, save_results_as_csv

"""
TESTING SCANNER: Serving HTTP on 127.0.0.1 port 8000
Ran 'python -m http.server 8000 --bind 127.0.0.1' in Powershell
"""
scanner = PortScanner("127.0.0.1")
scanner.scan_range(7999, 8001)

results = scanner.get_results()
display_results(results)
"""
OUTPUT:

Enter IPv4 address: 127.0.0.1
Enter first port: 7999
Enter last port: 8001
             TCP Port Scans
----------------------------------------
Port: 7999 | Unknown | Status: Filtered

Port: 8000 | Unknown | Status: Open

Port: 8001 | Unknown | Status: Filtered
"""

# should create example.csv
save_results_as_csv(results, "example.csv")
"""
OUTPUT:

7999,Not Open
8000,Open
8001,Not Open
"""
