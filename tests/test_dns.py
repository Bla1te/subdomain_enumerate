import unittest
from unittest.mock import patch

from infrastructure.dns import get_ip

class TestDNS(unittest.TestCase):
    @patch('socket.gethostbyname')
    def test_get_ip_success(self, mock_gethost):
        mock_gethost.return_value = '1.1.1.1'

        res = get_ip('test.com')
        
        assert res == '1.1.1.1'
        self.assertEqual(res, '1.1.1.1')

    @patch('socket.gethostbyname')
    def test_get_ip_fail(self,mock_gethost):
        mock_gethost.return_value = None

        res = get_ip('test.com')

        #assert res is None
        self.assertEqual(res, None)



