""" identifies common services """

import socket

class ServiceLookup:
    def __init__(self):
        self.services = {
            20: "FTP (Data)",
            21: "FTP (Control)",
            22: "SSH",
            23: "Telnet",
            25: "SMTP",
            53: "DNS",
            80: "HTTP",
            110: "POP3",
            143: "IMAP",
            443: "HTTPS",
            3306: "MySQL",
            3389: "RDP"
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

        return service if service else "Unknown"

 