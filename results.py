""" Displays and saves scan results """

import csv

def display_results(results):
    print("             TCP Port Scans")
    print("-" * 40)

    for result in results:
        port = result['port']
        status = result['status']
        service = result['service']
        print(f"Port: {port} | {service} | Status: {status}\n")


def save_results_as_csv(results, filename):
    fieldnames = ["port", "service", "status"]

    with open(filename, "w", newline="") as csvfile:
        port_writer = csv.DictWriter(csvfile, fieldnames=fieldnames)

        port_writer.writeheader()
        port_writer.writerows(results)

    