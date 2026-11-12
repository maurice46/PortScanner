""" TCP port scanning """

import socket
import errno

class PortScanner:
    def __init__(self, target, timeout=1):
        self.target_ip = target
        self.connection_timeout = timeout
        self.results = []
        self.scanned = set() # fast lookup of ports already scanned

    def scan_port(self, port): # attempt a TCP connection to one port

        # initialize tcp socket (IPv4 Addressing, TCP Socket Type)
        sock = socket.socket(socket.AF_INET, socket.SOCK_STREAM)

        try:
            # set connection timeout - without it a connection attempt can take longer 
            # particularly when a destination isn't responding
            sock.settimeout(self.connection_timeout)

            # attempt TCP connection
            tcp_connection = sock.connect_ex((self.target_ip, port))

            if tcp_connection == 0: # open port 
                return "Open"

            # connection actively refused -> nothing listening
            if tcp_connection in (errno.ECONNREFUSED, 10061):
                return "Closed"

            return "Filtered" # timeout/no response/blocked -> likely firewalled
            
        except socket.timeout: return "Filtered"

        except OSError: return "Error"
            
        finally: sock.close()

    def scan_range(self, start_port, end_port): # loop through the requested range 
        # scan each port and store results (ie. ports 3-5) 
        for port in range(start_port, end_port + 1): # +1 includes last port

            # skip ports already scanned
            if port in self.scanned: continue

            self.results.append({
                "port": port,
                "status": self.scan_port(port)
            })

            self.scanned.add(port)

    def get_results(self): return self.results


