#!/usr/bin/python3
"""Unittest for rectangle class"""


import unittest
from models.base import Base
from models.rectangle import Rectangle


class Test_Rectangle_instantiation(unittest.TestCase):
    """test for instantiation of recatngle class"""

    def test_new_rectangle(self):
        new = Rectangle(1, 3, 5, 4, 7)
        self.assertEqual(new.width, 1)
        self.assertEqual(new.height, 3)
        self.assertEqual(new.x, 5)
        self.assertEqual(new.y, 4)
        self.assertEqual(new.id, 7)


if __name__ == '__main__':
    unittest.main()
