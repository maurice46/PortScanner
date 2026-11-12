# Python TCP Port Scanner

A simple TCP port scanner written in Python. Give it an IPv4 address and a port range, and it reports which ports are open, closed, or filtered, identifies the common service on each open port, and can save the results to a CSV file.

## Features

- Scans any IPv4 address across a custom port range (1-65535)
- Classifies each port as `Open`, `Closed`, `Filtered`, or `Error`
- Looks up service names (ssh, http, etc.) for open ports only
- Shows only open ports by default, with an option to show everything
- Exports results to CSV
- Input validation for IP addresses and port ranges
- Ctrl+C during a scan keeps the partial results
- Option to scan again without restarting the program

## Requirements

- Python 3.6 or newer
- No third-party packages

## Usage

You'll be prompted for the target and port range:

```
Enter IPv4 address: 127.0.0.1
Enter first port: 1
Enter last port: 1024

Show closed/filtered ports too? (y/n): n

             TCP Port Scans
----------------------------------------
Port: 22 | ssh | Status: Open
Port: 80 | http | Status: Open
----------------------------------------
Scanned 1024 ports: 2 open, 1022 closed

Save results as CSV? (y/n): y
Enter filename (ie. scan_results.csv): scan_results.csv
Results saved to scan_results.csv

Scan more ports? (y/n): n
Goodbye.
```

### Port statuses

| Status | Meaning |
|---|---|
| Open | The connection succeeded; something is listening |
| Closed | The host actively refused the connection; nothing is listening |
| Filtered | No response before the timeout, likely blocked by a firewall |
| Error | Any other socket error |

### CSV output

The CSV file has three columns:

```
port,service,status
22,ssh,Open
80,http,Open
```

## Project structure

```
.
├── main.py        # Interactive command-line flow
├── scanner.py     # PortScanner: TCP connect scanning
├── lookup.py      # ServiceLookup: port number to service name
├── validator.py   # IP address and port range validation
└── results.py     # Result display and CSV export
```

## How it works

The scanner uses a TCP connect scan: for each port in the range it opens a new socket with a timeout, calls `connect_ex()`, and interprets the return code. A successful connection means the port is open, a refusal means it is closed, and a timeout suggests a firewall is dropping packets. Ports are scanned one at a time, and ports that were already scanned are skipped.

Service names come from a small built-in table of common ports, with `socket.getservbyport()` as a fallback. Names are the conventional service for that port number, not a verified identification of what is actually running, which is why only open ports are labeled.

## Limitations

- IPv4 only
- TCP connect scans only (no SYN scans or UDP)
- Ports are scanned sequentially, so large ranges with many filtered ports can take a long time (each unresponsive port waits for the timeout)

## Customization

`PortScanner` accepts an optional timeout in seconds in `scanner.py`:

```python
PortScanner(target, timeout=1)
```

Raise it for slow or distant hosts, or lower it to finish faster on hosts that drop packets.

