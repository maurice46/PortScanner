from scanner import PortScanner
from validator import validate_ip, validate_port_range
from lookup import ServiceLookup
from results import display_results, save_results_as_csv

def run_scan():
    # 1. get target ip address
    target_ip = input("Enter IPv4 address: ").strip()

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
    try:
        scanner.scan_range(first_port, last_port)
    except KeyboardInterrupt:
        print("\nScan interrupted. Showing partial results.")

    # 7. get results
    results = scanner.get_results()

    if not results:
        print("No results.")
        return

    # 8. identify and display services
    lookup = ServiceLookup()

    for result in results: 
        if result['status'] == 'Open':
            result['service'] = lookup.get_service(result['port'])
        else:
            result['service'] = "-"

    # 9. display results
    show_all = input("\nShow closed/filtered ports too? (y/n): ").strip().lower()

    if show_all == "y":
        display_results(results, show_all=True)
    else:
       display_results(results, show_all=False)

    # 10. save results
    while True: 
        save_choice = input("\nSave results as CSV? (y/n): ").strip().lower()

        if save_choice in ('y', 'n'): break

        print("Invalid choice. Enter y or n.")

    if save_choice == "y":
        filename = input("Enter filename (ie. scan_results.csv): ").strip()

        if not filename:
            print("No filename given. Results not saved.")
            return

        try:
            save_results_as_csv(results=results, filename=filename)
            print(f"Results saved to {filename}")
        except OSError as e:
            print(f"Could not save file: {e}")

    elif save_choice != "n":
        print("Invalid choice.")

def main():
    try:
        while True:
            run_scan()

            # ask to scan again or close
            while True:
                again = input("\nScan more ports? (y/n): ").strip().lower()

                if again in ('y', 'n'):
                    break

                print("Invalid choice. Enter y or n.")

            if again == "n":
                break

            print()

    except KeyboardInterrupt:
        print("Keyboard interupted.")

    finally:
        print("Goodbye!")


if __name__ == "__main__":
    main()


