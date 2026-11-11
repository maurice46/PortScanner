""" TCP port scanning """

import socket

class PortScanner:
    def __init__(self, target, timeout=1):
        self.target_ip = target
        self.connection_timeout = timeout
        self.results = []

    def scan_port(self, port): # attempt a TCP connection to one port

        # initialize tcp socket (IPv4 Addressing, TCP Socket Type)
        sock = socket.socket(socket.AF_INET, socket.SOCK_STREAM)

        try:
            # set connection timeout - without it a connection attempt can take longer 
            # particularly when a destination isn't responding
            sock.settimeout(self.connection_timeout)

            # attempt TCP connection
            tcp_connection = sock.connect_ex((self.target_ip, port))

            # port status 
            if tcp_connection == 0: # open port 
                return "Open"
            elif tcp_connection == 10061: # Windows connection refused
                return "Closed"
            else: # closed or filtered port OR timeout
                return "Not Open"
            
        except socket.timeout: return "Timeout"

        except OSError: return "Error"
            
        finally: sock.close()

    def scan_range(self, start_port, end_port): # loop through the requested range 
        # scan each port and store results (ie. ports 3-5) 
        for port in range(start_port, end_port + 1): # +1 includes last port

            # check whether this port has already been scanned
            if any(results['port'] == port for results in self.results):
                continue

            self.results.append({
                "port": port,
                "status": self.scan_port(port)
            })

    def get_results(self): return self.results


