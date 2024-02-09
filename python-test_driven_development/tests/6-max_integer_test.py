#!/usr/bin/python3
"""Unittest for max_integer([..])"""

import unittest
max_integer = __import__('6-max_integer').max_integer

class TestMaxInteger(unittest.TestCase):
    """test for max integer"""

    def test_max_at_the_end(self):
        """tests max at the end"""
        self.assertEqual(max_integer([1, 2, 3, 4]), 4)
    
    def test_max_at_the_beginning(self):
        """tests max at the beginning"""
        self.assertEqual(max_integer([4, 2, 3, 1]), 4)
        
    def test_max_in_the_middle(self):
        """tests max in the middle"""
        self.assertEqual(max_integer([1, 4, 3, 2]), 4)
    
if __name__ == '__main__':
    unittest.main()
