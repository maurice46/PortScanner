"""
Identifies common services 

A port # is commonly associated with a particular network service 
FTP - 20/21 | SSH - 22 | Telent - 23 | SMTP - 25 | DNS - 53 | HTTP - 80
POP3 - 110 | HTTPS - 443 | MySQL - 3306 | RDP - 3389

Python already has a useful socket function for this: socket.getservbyport().

Your responsibility is to create a function that accepts a port 
number and returns its associated service name.

"""

import socket

def get_service(port):
    # Look up the service associated with a port
    # Handle ports without a known service
    pass

