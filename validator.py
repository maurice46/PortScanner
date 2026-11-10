"""
Validates IP addresses and port ranges

Don't want the scanner attempting to process invalid input
- valid IPv4 addresses have four octets (192.168.1.1)
- TCP/UDP ports range from 0-65535
- the starting point shouldn't exceed the ending port

"""

import ipaddress

def validate_ip(target):
    # Check whether the supplied IP address is valid
    pass

def validate_port(port):
    # Check whether a port is within the valid range
    pass

def validate_port_range(start_port, end_port):
    # Check whether the start and end ports make sense
    pass

