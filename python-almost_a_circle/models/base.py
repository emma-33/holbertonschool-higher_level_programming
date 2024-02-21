#!/usr/bin/python3
"""Define a base Class"""

from fileinput import filename
import json


class Base():
    """Represents the base model"""
    __nb_objects = 0

    def __init__(self, id=None):
        """Initializing id"""
        if id is not None:
            self.id = id
        else:
            Base.__nb_objects += 1
            self.id = Base.__nb_objects

    @staticmethod
    def to_json_string(list_dictionaries):
        """returns the JSON string representation of list_dictionaries"""
        if list_dictionaries is None or list_dictionaries == []:
            return "[]"
        return json.dumps(list_dictionaries)

    @classmethod
    def save_to_file(cls, list_objs):
        """writes the JSON string representation of list_obj in a file"""
        filename = cls.__name__ + ".json"
        with open(filename, "w") as file:
            if list_objs is None:
                file.write("[]")
            else:
                for object in list_objs:
                    list_dicts = object.to_dictionary()
                    file.write(Base.to_json_string(list_dicts))
