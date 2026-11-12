# Python TCP Port Scanner

A simple, multithreaded TCP port scanner written in Python. Give it an IPv4 address and a port range, and it reports which ports are open, closed, or filtered, identifies the common service on each open port, and can save the results to a CSV file.

Built with the standard library only, so there is nothing to install.

> **Legal and ethical use:** Only scan hosts you own or have explicit permission to test. Unauthorized port scanning may violate laws or your network's terms of service. This project is for learning and for testing your own systems.

## Features

- Scans any IPv4 address across a custom port range (1-65535)
- Concurrent scanning with a thread pool (100 workers by default), so large ranges finish quickly
- Classifies each port as `Open`, `Closed`, `Filtered`, `Unreachable`, or `Error`
- Looks up service names (ssh, http, etc.) for open ports only
- Shows only open ports by default, with an option to show everything and a summary count
- Exports results to CSV
- Input validation for IP addresses and port ranges
- Ctrl+C during a scan keeps the partial results
- Option to scan again without restarting the program

## Requirements

- Python 3.9 or newer (uses `ThreadPoolExecutor.shutdown(cancel_futures=True)`)
- No third-party packages

## Usage

```bash
git clone https://github.com/<your-username>/<your-repo>.git
cd <your-repo>
python main.py
```

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

The example above is illustrative. Your output will depend on the target.

### Port statuses

| Status | Meaning |
|---|---|
| Open | The connection succeeded; something is listening |
| Closed | The host actively refused the connection; nothing is listening |
| Filtered | No response before the timeout, likely blocked by a firewall |
| Unreachable | No route to the host or network |
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
├── scanner.py     # PortScanner: threaded TCP connect scanning
├── lookup.py      # ServiceLookup: port number to service name
├── validator.py   # IP address and port range validation
└── results.py     # Result display and CSV export
```

## How it works

The scanner uses a TCP connect scan: for each port it calls `connect_ex()` on a new socket with a timeout and interprets the return code. A successful connection means the port is open, a refusal means it is closed, and a timeout suggests a firewall is dropping packets. Ports are scanned concurrently with `ThreadPoolExecutor`, and results are stored in a dictionary keyed by port so repeat scans skip ports that were already checked.

Service names come from a small built-in table of common ports, with `socket.getservbyport()` as a fallback. Names are the conventional service for that port number, not a verified identification of what is actually running, which is why only open ports are labeled.

## Limitations

- IPv4 only
- TCP connect scans only (no SYN scans or UDP)
- No banner grabbing or service fingerprinting
- Very high worker counts or fast scans may trigger intrusion detection or rate limiting on the target network

## Customization

`PortScanner` accepts two optional arguments in `scanner.py`:

```python
PortScanner(target, timeout=1, max_workers=100)
```

Raise `timeout` for slow or distant hosts, and lower `max_workers` if you want a gentler scan.

## License

Add a license of your choice (for example, MIT) before publishing.
