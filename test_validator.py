"""Unit tests for validator.py"""

import unittest
from validator import validate_ip, validate_port, validate_port_range

class TestValidator(unittest.TestCase):
    # testing IP addresses
    def test_valid_ip(self):
        self.assertTrue(validate_ip("192.168.1.1"))

    def test_invalid_ip(self):
        self.assertFalse(validate_ip("999.999.999.999"))

    def test_invalid_ip_string(self):
        self.assertFalse(validate_ip("hello"))

    def test_ipv6_address(self):
        self.assertFalse(validate_ip("2001:db8::1"))

    # testing ports 
    def test_valid_port(self):
        self.assertTrue(validate_port(80))

    def test_minimum_port(self):
        self.assertTrue(validate_port(1))

    def test_maximum_port(self):
        self.assertTrue(validate_port(65535))

    def test_port_below_range(self):
        self.assertFalse(validate_port(0))

    def test_port_above_range(self):
        self.assertFalse(validate_port(65536))

    def test_port_string(self):
        self.assertFalse(validate_port("80"))

    def test_port_boolean(self):
        self.assertFalse(validate_port(True))

    # testing port ranges
    def test_valid_port_range(self):
        self.assertTrue(validate_port_range(1, 100))

    def test_reversed_port_range(self):
        self.assertFalse(validate_port_range(100, 1))

    def test_port_range_below_minimum(self):
        self.assertFalse(validate_port_range(0, 100))

    def test_port_range_above_maximum(self):
        self.assertFalse(validate_port_range(1, 65536))

    def test_port_range_with_invalid_type(self):
        self.assertFalse(validate_port_range("80", 100))


if __name__ == "__main__":
    unittest.main()



