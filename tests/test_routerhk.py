import unittest
from routerhk import RouterHk

class TestHkClient(unittest.TestCase):
    def setUp(self):
        self.client = RouterHk()

    def test_get_ip(self):
        self.client.ip_address = None
        response = self.client.get_ip()
        self.assertIsNotNone(self.client.ip_address)

if __name__ == '__main__':
    unittest.main()
