#!/usr/bin/python3
"""Defines a class Student"""


class Student():
    """Defines a student"""
    def __init__(self, first_name, last_name, age):
        """Initialize instances"""
        self.first_name = first_name
        self.last_name = last_name
        self.age = age

    def to_json(self, attrs=None):
        """Retrieves a dictionary representation of a Student instance"""
        if type(attrs) is list:
            new_dict = {}
            for names in self.__dict__:
                for name in attrs:
                    if names == name:
                        new_dict[names] = self.__dict__[names]
            return new_dict
        else:
            return self.__dict__

    def reload_from_json(self, json):
        """Replaces all atributes of the Student instance"""
        for names in json:
            if names == "first_name":
                self.first_name = json[names]
            if names == "last_name":
                self.last_name = json[names]
            if names == "age":
                self.age = json[names]
