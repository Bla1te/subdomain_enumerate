import unittest
from infrastructure.load_list import load_subdamins_list




class TestLoadList(unittest.TestCase):
    def test_load_subdamins_list(self):
        with open('test.txt', 'w') as f:
            f.write('www\napi')
            f.close
    
        res = load_subdamins_list('test.txt')
    
        #assert res == ['www','api']

        self.assertEqual(res, ['www','api'])