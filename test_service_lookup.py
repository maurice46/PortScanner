"""unit tests for service_lookup.py"""

import unittest
from unittest.mock import patch
from lookup import ServiceLookup

class TestServiceLookup(unittest.TestCase):
    # new instance for each test
    def setup(self): 
        self.lookup = ServiceLookup()

    # known service testing 
    def test_known_service_http(self):
        self.assertEqual(self.lookup.get_service(80), "HTTP")

    def test_known_service_https(self):
        self.assertEqual(self.lookup.get_service(443), "HTTPS")

    def test_known_service_ssh(self):
        self.assertEqual(self.lookup.get_service(22), "SSH")

    # unknown service testing 
    @patch("service_lookup.socket.getservbyport")
    def test_unknown_service(self, mock_getservbyport):
        mock_getservbyport.side_effect = OSError

        result = self.lookup.get_service(9999)

        self.assertEqual(result, "Unknown")


if __name__ == "__main__":
    unittest.main()

