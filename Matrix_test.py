import unittest
from Matrix import *

class TestStringMethods(unittest.TestCase):
    def test_init(self):
    	self.assertEqual(self.test_instance.args, self.args)
    def test_add(self):
        self.assertEqual(self.test_instance.rhs, self.rhs)
    def test_mul(self):
        self.assertEqual(self.test_instance.rhs, self.rhs)

if __name__ == '__main__':
    unittest.main()