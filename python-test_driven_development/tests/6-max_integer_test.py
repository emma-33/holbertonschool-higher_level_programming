#!/usr/bin/python3
"""Unittest for max_integer([..])
"""
import unittest
max_integer = __import__('6-max_integer').max_integer

class TestMaxInteger(unittest.TestCase):
    """test for max integer"""

    def valid_input(self):
        """tests valid inputs"""
        self.assertEqual(max_integer([1, 2, 3, 4]), 4)
    
    def not_an_int(self):
        self.assertIsInstance(max_integer("Hello"), int)
    
    if __name__ == '__main__':
        unittest.main()
