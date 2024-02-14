#!/usr/bin/python3
"""Defines a class BaseGeometry"""


class BaseGeometry:
    """Represents base geometry"""
    def area(self):
        """Not implemented"""
        raise Exception("area() is not implemented")

    def integer_validator(self, name, value):
        """Validates integers

        Args:
            name (str): name of parameter
            value (int): parameter to check

        Raises:
            TypeError: if value isn't an int
            ValueError: if value <= 0 
        """
        if type(value) != int:
            raise TypeError("{} must be an integer".format(name))
        if value <= 0:
            raise ValueError("{} must be greater than 0".format(name))
