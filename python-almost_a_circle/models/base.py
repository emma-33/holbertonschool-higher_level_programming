#!/usr/bin/python3
"""Define a base Class"""


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
