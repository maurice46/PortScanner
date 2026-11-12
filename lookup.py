""" identifies common services """

import socket

class ServiceLookup:
    def __init__(self):
        self.services = {
            20: "ftp-data",
            21: "ftp",
            22: "ssh",
            23: "telnet",
            25: "smtp",
            53: "dns",
            80: "http"
        }

    def get_service(self, port):
        # known port
        if port in self.services:
            return self.services[port]

        # unknown port 
        try:
            service = socket.getservbyport(port, "tcp")
        except OSError:
            return "Unknown"

        self.services[port] = service

        return service 

 