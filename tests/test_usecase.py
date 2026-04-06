import unittest
from usecases.func import get_subdomain_list

import asyncio

def get_ip(domain: str) -> str:
    return '1.1.1.1'

class TestGetList(unittest.TestCase):
    async def test_get_subdomain_list(self):
        res = await get_subdomain_list('test.com', ['1','2'],get_ip)
        #assert len(res) == 2
        #assert res[0].name == '1.test.com' and res[0].ip == '1.1.1.1'
        #assert res[1].name == '2.test.com' and res[1].ip == '1.1.1.1'

        self.assertEqual(len(res), 2)
        self.assertEqual(res[0].name, '1.test.com', res[0].ip,'1.1.1.1')
        self.assertEqual(res[1].name, '2.test.com', res[1].ip,'1.1.1.1')
