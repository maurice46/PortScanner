""" displays and saves scan results """

import csv

def display_results(results):
    print("   TCP Port Scans   ")
    print("-" * 20)

    for result in results:
        port = result['port']
        status = result['status']
        print(f"Port {port}: {status}")


def save_results_as_csv(results, filename): 
    with open(filename, 'w', newline='') as csvfile:
        

