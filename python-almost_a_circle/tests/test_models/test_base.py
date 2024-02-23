#!/usr/bin/python3
"""Unittest for base class"""


import json
import os
import unittest
from models.base import Base
from models.rectangle import Rectangle
from models.square import Square


class Test_Base(unittest.TestCase):
    """test for base class"""

    def test_default_id(self):
        new_id = Base()
        self.assertEqual(new_id.id, 1)

    def test_none_id(self):
        new_id = Base(None)
        self.assertEqual(new_id.id, 2)

    def test_new_id(self):
        new_id = Base(3)
        self.assertEqual(new_id.id, 3)

    def test_two_args(self):
        with self.assertRaises(TypeError):
            Base(1, 2)


class Test_from_json_string(unittest.TestCase):
    """tests for from_json_string method"""

    def test_json_string(self):
        list_input = [{'id': 89, 'width': 10, 'height': 4}]
        json_list_input = Rectangle.to_json_string(list_input)
        list_output = Rectangle.from_json_string(json_list_input)
        self.assertEqual(list_input, list_output)

    def test_type_json(self):
        list_input = [{'id': 89, 'width': 10, 'height': 4}]
        json_list_input = Rectangle.to_json_string(list_input)
        list_output = Rectangle.from_json_string(json_list_input)
        self.assertEqual(list, type(list_output))


class Test_to_json_string(unittest.TestCase):
    """tets for to_json_string method"""

    def test_empty_list(self):
        json_dictionary = Base.to_json_string([])
        self.assertEqual("[]", json_dictionary)

    def test_none_list(self):
        json_dictionary = Base.to_json_string(None)
        self.assertEqual("[]", json_dictionary)

    def test_to_json_no_args(self):
        with self.assertRaises(TypeError):
            Base.to_json_string()

    def test_to_json_one_args(self):
        with self.assertRaises(TypeError):
            Base.to_json_string([], 1)

    def test_to_json_type_rectangle(self):
        r = Rectangle(10, 7, 2, 8)
        string = Base.to_json_string([r.to_dictionary()])
        self.assertEqual(str, type(string))

    def test_to_json_string_rectangle_one_dict(self):
        r = Rectangle(10, 7, 2, 8, 6)
        string = Base.to_json_string([r.to_dictionary()])
        self.assertTrue(len(string) == 53)

    def test_to_json_string_rectangle_two_dict(self):
        r1 = Rectangle(10, 7, 2, 8, 6)
        r2 = Rectangle(3, 4, 10, 7, 1)
        list_dict = [r1.to_dictionary(), r2.to_dictionary()]
        string = Base.to_json_string(list_dict)
        self.assertTrue(len(string) == 106)

    def test_to_json_type_square(self):
        s = Square(10, 2, 8)
        string = Base.to_json_string([s.to_dictionary()])
        self.assertEqual(str, type(string))

    def test_to_json_string_square_one_dict(self):
        s = Square(10, 2, 8, 6)
        string = Base.to_json_string([s.to_dictionary()])
        self.assertTrue(len(string) == 39)

    def test_to_json_string_square_two_dict(self):
        s1 = Square(10, 7, 2, 8)
        s2 = Square(3, 4, 10, 7)
        list_dict = [s1.to_dictionary(), s2.to_dictionary()]
        string = Base.to_json_string(list_dict)
        self.assertTrue(len(string) == 78)


class Test_create(unittest.TestCase):
    """tests for create method"""

    def test_create_rectangle(self):
        r1 = Rectangle(3, 5, 1)
        r1_dictionary = r1.to_dictionary()
        r2 = Rectangle.create(**r1_dictionary)
        self.assertEqual("[Rectangle] (3) 1/0 - 3/5", str(r2))


class Test_save_to_file(unittest.TestCase):
    """tests for save to file method"""

    def delete_any_files(self):
        try:
            os.remove("Rectangle.json")
        except IOError:
            pass
        try:
            os.remove("Square.json")
        except IOError:
            pass
        try:
            os.remove("Base.json")
        except IOError:
            pass

    def test_save_to_file_rectangle(self):
        r1 = Rectangle(10, 7, 2, 8)
        r2 = Rectangle(2, 4)
        res = Rectangle.save_to_file([r1, r2])
        rect1 = {"id": 1, "width": 10, "height": 7, "x": 2, "y": 8}
        rect2 = {"id": 2, "width": 2, "height": 4, "x": 0, "y": 0}
        with open("Rectangle.json", "r") as file:
            self.assertTrue([rect1, rect2], res)

    def test_save_to_file_square(self):
        s1 = Square(10, 2, 8)
        s2 = Square(2)
        res = Rectangle.save_to_file([s1, s2])
        square1 = {"id": 1, "width": 10, "height": 7, "x": 2, "y": 8}
        square2 = {"id": 2, "width": 2, "height": 4, "x": 0, "y": 0}
        with open("Square.json", "r") as file:
            self.assertTrue([square1, square2], res)


class Test_load_from_file(unittest.TestCase):
    """tests for load from file method"""

    def test_load_from_file_rectangle(self):
        r1 = Rectangle(10, 7, 2, 8)
        r2 = Rectangle(2, 4)
        list_rectangle_input = [r1, r2]

        Rectangle.save_to_file(list_rectangle_input)
        list_rectangle_output = Rectangle.load_from_file()

        self.assertTrue(str(r1), str(list_rectangle_output[0]))

    def test_load_from_file_square(self):
        s1 = Square(10, 7, 2, 8)
        s2 = Square(2, 4)
        list_square_input = [s1, s2]

        Square.save_to_file(list_square_input)
        list_square_output = Square.load_from_file()

        self.assertTrue(str(s1), str(list_square_output[0]))


if __name__ == '__main__':
    unittest.main()
