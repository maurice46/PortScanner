""" Validates IP addresses and port ranges """

import ipaddress

def validate_ip(address):
    try:
        valid_ip = ipaddress.ip_address(address)
        return isinstance(valid_ip, ipaddress.IPv4Address)
    
    except ValueError: return False

def validate_port(port):
    if not isinstance(port, int) or isinstance(port, bool):
        return False

    return 1 <= port <= 65535

def validate_port_range(start_port, end_port):
    if not validate_port(start_port):
        return False

    if not validate_port(end_port):
        return False

    return start_port <= end_port

