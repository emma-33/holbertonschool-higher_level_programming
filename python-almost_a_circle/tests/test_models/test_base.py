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

    def test_new_id(self):
        new_id = Base(3)
        self.assertEqual(new_id.id, 3)


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


class Test_create(unittest.TestCase):
    """tests for create method"""
    
    def test_create_rectangle(self):
        r1 = Rectangle(3, 5, 1)
        r1_dictionary = r1.to_dictionary()
        r2 = Rectangle.create(**r1_dictionary)
        self.assertEqual("[Rectangle] (2) 1/0 - 3/5", str(r2))


class Test_save_to_file(unittest.TestCase):
    """tests for save to file method"""
    
    def test_save_to_file_rectangle(self):
       r1 = Rectangle(10, 7, 2, 8)
       r2 = Rectangle(2, 4)
       res = Rectangle.save_to_file([r1, r2])
       with open("Rectangle.json", "r") as file:
            self.assertTrue([{"id": 1, "width": 10, "height": 7, "x": 2, "y": 8},
                             {"id": 2, "width": 2, "height": 4, "x": 0, "y": 0}], res)

    def test_save_to_file_square(self):
       s1 = Square(10, 2, 8)
       s2 = Square(2)
       res = Rectangle.save_to_file([s1, s2])
       with open("Square.json", "r") as file:
            self.assertTrue([{"id": 1, "width": 10, "height": 7, "x": 2, "y": 8},
                             {"id": 2, "width": 2, "height": 4, "x": 0, "y": 0}], res)
 
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
