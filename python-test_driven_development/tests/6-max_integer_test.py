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
    
    def test_neg_num_in_list(self):
        """tests 1 negative number in list"""
        self.assertEqual(max_integer([1, 4, -3, 2]), 4)
    
    def test_only_neg_num(self):
        """tests only neative numbers in list"""
        self.assertEqual(max_integer([-1, -4, -3, -2]), -1)
    
    def test_only_one_element(self):
        """tests only one element"""
        self.assertEqual(max_integer([1]), 1)
    
    def test_list_is_empty(self):
        """tests list is empty"""
        self.assertEqual(max_integer([]), None)
    
    
if __name__ == '__main__':
    unittest.main()
