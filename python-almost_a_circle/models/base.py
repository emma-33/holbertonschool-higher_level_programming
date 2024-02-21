#!/usr/bin/python3
"""Define a base Class"""


import json
import os


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
        lists = []

        if not list_objs:
            pass
        else:
            for object in range(len(list_objs)):
                lists.append(list_objs[object].to_dictionary())

        list_dict = cls.to_json_string(lists)

        with open(filename, "w") as file:
            file.write(list_dict)

    @staticmethod
    def from_json_string(json_string):
        """Returns the list of the JSON representation json_string"""
        if json_string is None or json_string == "[]":
            return []
        return json.loads(json_string)

    @classmethod
    def create(cls, **dictionary):
        """returns an instance with all atributes set"""
        if cls.__name__ == "Rectangle":
            new = cls(1, 1)
        else:
            new = cls(1)
        new.update(**dictionary)
        return new

    @classmethod
    def load_from_file(cls):
        """Returns a list of instances"""
        filename = cls.__name__ + ".json"
        list_instances = []

        if os.path.exists(filename) is False:
            return list_instances

        with open(filename, "r") as file:
            list = file.read()

        list_class = cls.from_json_string(list)

        for instance in range(len(list_class)):
            list_instances.append(cls.create(**list_class[instance]))

        return list_instances
