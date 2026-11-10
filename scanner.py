""" TCP port scanning """

import socket

class PortScanner:
    def __init__(self, target, timeout=1):
        self.target_ip = target
        self.connection_timeout = timeout
        self.scan_results = []

    def scan_port(self, port): # attempt a TCP connection to one port

        # initialize tcp socket (Address family for IPv4, Socket type for TCP)
        sock = socket.socket(socket.AF_INET, socket.SOCK_STREAM)

        try:
            # set connection timeout
            sock.settimeout(self.connection_timeout)

            # attempt TCP connection
            tcp_connection = sock.connect_ex((self.target_ip, port))

            # port status 
            if tcp_connection == 0: # open port 
                return "Open"
            else: # closed port
                return "Closed"
            
        finally:
            sock.close()

    def scan_range(self, start_port, end_port): # loop through the requested range 
        # scan each port and store results (ie. ports 3-5) 
        port_range = range(start_port, end_port + 1) # +1 includes last port

        for port in port_range:
            self.scan_results.append({
                "port": port,
                "status": self.scan_port(port)
            })


    def get_results(self): # return collected scan results
        return self.scan_results




