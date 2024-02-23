#!/usr/bin/python3
"""Unittest for Square class"""


import unittest
from models.base import Base
from models.rectangle import Rectangle
from models.square import Square


class Test_square_Instantiation(unittest.TestCase):
    """test for instantiation of Square class"""

    def test_new_square(self):
        """Test a new square"""
        new = Square(1, 3, 5, 4)
        self.assertEqual(new.size, 1)
        self.assertEqual(new.x, 3)
        self.assertEqual(new.y, 5)
        self.assertEqual(new.id, 4)


class Test_Size(unittest.TestCase):
    """test for size instance"""

    def test_string_size(self):
        """Trying to pass a string as size"""
        with self.assertRaises(TypeError):
            square = Square("5")

    def test_negative_size(self):
        """Trying to pass a negative value as size"""
        with self.assertRaises(ValueError):
            square = Square(-10)


class Test_Square_Update_Args_Kwargs(unittest.TestCase):
    """test for update method"""

    def test_update_arg_0(self):
        s = Square(5)
        s.update()
        self.assertEqual("[Square] (30) 0/0 - 5", str(s))

    def test_update_one_arg(self):
        s = Square(5)
        s.update(10)
        self.assertEqual("[Square] (10) 0/0 - 5", str(s))

    def test_update_2_args(self):
        s = Square(5)
        s.update(1, 2)
        self.assertEqual("[Square] (1) 0/0 - 2", str(s))

    def test_update_3_args(self):
        s = Square(5)
        s.update(1, 2, 3)
        self.assertEqual("[Square] (1) 3/0 - 2", str(s))

    def test_update_4_args(self):
        s = Square(5)
        s.update(1, 2, 3, 4)
        self.assertEqual("[Square] (1) 3/4 - 2", str(s))

    def test_update_x(self):
        s = Square(5)
        s.update(x=12)
        self.assertEqual("[Square] (34) 12/0 - 5", str(s))

    def test_update_size_y(self):
        s = Square(5)
        s.update(size=7, y=1)
        self.assertEqual("[Square] (33) 0/1 - 7", str(s))

    def test_update_size_id_y(self):
        s = Square(5)
        s.update(size=7, id=89, y=1)
        self.assertEqual("[Square] (89) 0/1 - 7", str(s))


class Test_Square_to_dictionnary(unittest.TestCase):
    """tests for to_dictionary method"""

    def test_to_dictionary(self):
        s1 = Square(10, 2, 1)
        s1_dictionary = s1.to_dictionary()
        self.assertEqual({'id': 36, 'size': 10, 'x': 2, 'y': 1}, s1_dictionary)


class Test_Square_str(unittest.TestCase):
    """tests for str method"""

    def test_str(self):
        s1 = Square(3, 1, 3)
        s1_str = s1.__str__()
        self.assertEqual("[Square] (35) 1/3 - 3", str(s1_str))


if __name__ == '__main__':
    unittest.main()
