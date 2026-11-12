from scanner import PortScanner
from validator import validate_ip, validate_port_range
from lookup import ServiceLookup
from results import display_results, save_results_as_csv


def main():

    # 1. Get target IP address
    target_ip = input("Enter IPv4 address: ")

    # 2. Validate target
    validate_ip(target_ip)

    # 3. Get port range
    port_start = int(input("Enter first port: "))
    port_end = int(input("Enter last port: "))

    # 4. Validate port range
    validate_port_range(port_start, port_end)

    # 5. Create PortScanner object
    port_scanner = PortScanner(target_ip)

    # 6. Execute scan

    # 7. Identify services

    # 8. Display results

    # 9. Save results
    
    pass

if __name__ == "__main__":
    main()

