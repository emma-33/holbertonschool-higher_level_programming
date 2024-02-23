#!/usr/bin/python3
"""Unittest for base class"""


import json
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


if __name__ == '__main__':
    unittest.main()
