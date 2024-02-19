#!/usr/bin/python3
"""Unittest for base class"""

import unittest
from models.base import Base

class Test_Base(unittest.TestCase):
    """test for base class"""
    
    def test_default_id(self):
        new_id = Base()
        self.assertEqual(new_id.id, 1)

    def test_new_id(self):
        new_id = Base(3)
        self.assertEqual(new_id.id, 3)
    
    
if __name__ == '__main__':
    unittest.main()
