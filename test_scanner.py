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

   TCP Port Scans   
--------------------
Port 7999: Not Open
Port 8000: Open
Port 8001: Not Open
"""

# should create example.csv
save_results_as_csv(results, "example.csv")
"""
OUTPUT:

7999,Not Open
8000,Open
8001,Not Open
"""
