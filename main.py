from scanner import PortScanner
from validator import validate_ip, validate_port_range
from lookup import ServiceLookup
from results import display_results, save_results_as_csv

def main():
    # 1. get target ip address
    target_ip = input("Enter IPv4 address: ")

    # 2. validate ip address
    if not validate_ip(address=target_ip):
        print("Invalid IPv4 Address.")
        return

    # 3. get port range
    try:
        first_port = int(input("Enter first port: "))
        last_port = int(input("Enter last port: "))
    except ValueError:
        print("Ports must be whole numbers.")
        return

    # 4. validate port range
    if not validate_port_range(start_port=first_port, end_port=last_port):
        print("Invalid port range (1-65535, start <= end).")
        return

    # 5. create scanner
    scanner = PortScanner(target_ip)

    # 6. scan ports
    scanner.scan_range(first_port, last_port)

    # 7. get results
    results = scanner.get_results()

    # 8. identify and display services
    lookup = ServiceLookup()

    for result in results: 
        result['service'] = lookup.get_service(result['port'])

    # 9. display results
    display_results(results)

    # 10. save results
    save_choice = input("\nSave results as CSV? (y/n): ").lower()

    if save_choice == "y":
        filename = input("Enter filename (ie. scan_results.csv): ")
        save_results_as_csv(results=results, filename=filename)
        print(f"Results saved to {filename}")
    elif save_choice != "n":
        print("Invalid choice.")


if __name__ == "__main__":
    main()

