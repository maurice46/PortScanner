""" Displays and saves scan results """

import csv

def display_results(results, show_all=False):
    print("             TCP Port Scans")
    print("-" * 40)

    ports = results if show_all else [res for res in results if res['status'] == "Open"]

    if not ports:
        print("No open ports found.")

    for result in ports:
        port = result['port']
        status = result['status']
        service = result['service']
        print(f"Port: {port} | {service} | Status: {status}")

    print(f"Scanned {len(ports)} ports.")


def save_results_as_csv(results, filename):
    fieldnames = ["port", "service", "status"]

    with open(filename, "w", newline="") as csvfile:
        port_writer = csv.DictWriter(csvfile, fieldnames=fieldnames)

        port_writer.writeheader()
        port_writer.writerows(results)

    