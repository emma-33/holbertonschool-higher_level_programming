#!/usr/bin/python3
"""Unittest for rectangle class"""


import unittest
from models.base import Base
from models.rectangle import Rectangle


class Test_Rectangle_Instantiation(unittest.TestCase):
    """test for instantiation of rectangle class"""

    def test_new_rectangle(self):
        new = Rectangle(1, 3, 5, 4, 7)
        self.assertEqual(new.width, 1)
        self.assertEqual(new.height, 3)
        self.assertEqual(new.x, 5)
        self.assertEqual(new.y, 4)
        self.assertEqual(new.id, 7)


class Test_Width(unittest.TestCase):
    """test for width instance"""

    def test_valid(self):
        """Valid value"""
        rectangle = Rectangle(5, 7)
        self.assertEqual(rectangle.width, 5)

    def test_string_width(self):
        """Trying to pass a string as width"""
        with self.assertRaises(TypeError):
            rectangle = Rectangle("5", 7)

    def test_negative_width(self):
        """Trying to pass a negative value as width"""
        with self.assertRaises(ValueError):
            rectangle = Rectangle(-10, 7)


class Test_Height(unittest.TestCase):
    """test for height instance"""

    def test_valid(self):
        "Valid value"
        rectangle = Rectangle(5, 7)
        self.assertEqual(rectangle.height, 7)

    def test_string_height(self):
        """Trying to pass a string as height"""
        with self.assertRaises(TypeError):
            rectangle = Rectangle(5, "7")

    def test_negative_height(self):
        """Trying to pass a negative value as height"""
        with self.assertRaises(ValueError):
            rectangle = Rectangle(10, -7)


class Test_x(unittest.TestCase):
    """Test for x instance"""

    def test_valid(self):
        """Valid value"""
        rectangle = Rectangle(5, 7, 2)
        self.assertEqual(rectangle.x, 2)

    def test_string_x(self):
        """Trying to pass a string as x"""
        with self.assertRaises(TypeError):
            rectangle = Rectangle(5, 7, "2")

    def test_negative_x(self):
        """Trying to pass a negative value as x"""
        with self.assertRaises(ValueError):
            rectangle = Rectangle(10, 7, -2)


class Test_y(unittest.TestCase):
    """Test for y instance"""

    def test_valid(self):
        """Valid value"""
        rectangle = Rectangle(5, 7, 2, 4)
        self.assertEqual(rectangle.y, 4)

    def test_string_y(self):
        """Trying to pass a string as y"""
        with self.assertRaises(TypeError):
            rectangle = Rectangle(5, 7, 2, "4")

    def test_negative_y(self):
        """Trying to pass a negative value as y"""
        with self.assertRaises(ValueError):
            rectangle = Rectangle(10, 7, 2, -4)


class Test_Rectangle_Area(unittest.TestCase):
    """test for area method"""

    def test_width_and_height(self):
        r1 = Rectangle(3, 2)
        self.assertEqual(r1.area, 6)

    def test_all_instances(self):
        r2 = Rectangle(8, 7, 0, 0, 12)
        self.assertEqual(r2.area, 56)

class Test_Rectangle_Update_Args(unittest.TestCase):
    """test for update method"""

    def test_update_arg_0(self):
        r = Rectangle(10, 10, 10, 10, 10)
        r.update()
        self.assertEqual("[Rectangle] (1) 10/10 - 10/10", str(r))

    def test_update_one_arg(self):
        r = Rectangle(10, 10, 10, 10, 10)
        r.update(89)
        self.assertEqual("[Rectangle] (89) 10/10 - 10/10", str(r))

    def test_update_2_args(self):
        r = Rectangle(10, 10, 10, 10, 10)
        r.update(89, 2)
        self.assertEqual("[Rectangle] (89) 10/10 - 2/10", str(r))

    def test_update_3_args(self):
        r = Rectangle(10, 10, 10, 10, 10)
        r.update(89, 2, 3)
        self.assertEqual("[Rectangle] (89) 10/10 - 2/3", str(r))

    def test_update_4_args(self):
        r = Rectangle(10, 10, 10, 10, 10)
        r.update(89, 2, 3, 4)
        self.assertEqual("[Rectangle] (89) 4/10 - 2/3", str(r))

    def test_update_5_args(self):
        r = Rectangle(10, 10, 10, 10, 10)
        r.update(89, 2, 3, 4, 5)
        self.assertEqual("[Rectangle] (89) 4/5 - 2/3", str(r))



if __name__ == '__main__':
    unittest.main()
