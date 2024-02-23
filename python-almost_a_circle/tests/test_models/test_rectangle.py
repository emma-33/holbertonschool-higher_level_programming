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

    def test_negative_y(self):
        """Trying to pass a negative value as y"""
        with self.assertRaises(ValueError):
            rectangle = Rectangle(10, 7, 2, -4)


class Test_area(unittest.TestCase):
    """Test for area method"""
    
    def test_area(self):
        rect = Rectangle(2, 10)
        self.assertTrue(rect.area, 20)


class Test_Rectangle_Update_Args(unittest.TestCase):
    """test for update method"""

    def test_update_arg_0(self):
        r = Rectangle(10, 10, 10, 10, 1)
        r.update()
        self.assertEqual("[Rectangle] (1) 10/10 - 10/10", str(r))

    def test_update_one_arg(self):
        r = Rectangle(10, 10, 10, 10, 1)
        r.update(89)
        self.assertEqual("[Rectangle] (89) 10/10 - 10/10", str(r))

    def test_update_2_args(self):
        r = Rectangle(10, 10, 10, 10, 1)
        r.update(89, 2)
        self.assertEqual("[Rectangle] (89) 10/10 - 2/10", str(r))

    def test_update_3_args(self):
        r = Rectangle(10, 10, 10, 10, 1)
        r.update(89, 2, 3)
        self.assertEqual("[Rectangle] (89) 10/10 - 2/3", str(r))

    def test_update_4_args(self):
        r = Rectangle(10, 10, 10, 10, 1)
        r.update(89, 2, 3, 4)
        self.assertEqual("[Rectangle] (89) 4/10 - 2/3", str(r))

    def test_update_5_args(self):
        r = Rectangle(10, 10, 10, 10, 1)
        r.update(89, 2, 3, 4, 5)
        self.assertEqual("[Rectangle] (89) 4/5 - 2/3", str(r))


class Test_Rectangle_Update_Kwargs(unittest.TestCase):
    """test for update method with kwargs"""

    def test_update_arg_0(self):
        r = Rectangle(10, 10, 10, 10, 1)
        r.update()
        self.assertEqual("[Rectangle] (1) 10/10 - 10/10", str(r))

    def test_update_height(self):
        r = Rectangle(10, 10, 10, 10, 1)
        r.update(height=1)
        self.assertEqual("[Rectangle] (1) 10/10 - 10/1", str(r))

    def test_update_width_x(self):
        r = Rectangle(10, 10, 10, 10, 1)
        r.update(width=1, x=2)
        self.assertEqual("[Rectangle] (1) 2/10 - 1/10", str(r))

    def test_update_y_width_x_id(self):
        r = Rectangle(10, 10, 10, 10, 1)
        r.update(y=1, width=2, x=3, id=89)
        self.assertEqual("[Rectangle] (89) 3/1 - 2/10", str(r))

    def test_update_x_height_y_width(self):
        r = Rectangle(10, 10, 10, 10, 1)
        r.update(x=1, height=2, y=3, width=4)
        self.assertEqual("[Rectangle] (1) 1/3 - 4/2", str(r))


class Test_Rectangle_to_dictionnary(unittest.TestCase):
    """tests for to_dictionary method"""
    
    def test_to_dictionary(self):
        r1 = Rectangle(10, 2, 1, 9)
        r1_dictionary = r1.to_dictionary()
        self.assertEqual({'id': 3, 'width': 10, 'height': 2, 'x': 1, 'y':9}, r1_dictionary)


class Test_Rectangle_str(unittest.TestCase):
    """tests for str method"""
    
    def test_str(self):
        r1 = Rectangle(4, 6, 2, 1, 12)
        r1_str= r1.__str__()
        self.assertEqual("[Rectangle] (12) 2/1 - 4/6", str(r1_str))
   
if __name__ == '__main__':
    unittest.main()
