#!/usr/bin/python3
"""Defines class Rectangle that inherits from BaseGeometry"""
BaseGeometry = __import__('7-base_geometry').BaseGeometry


class Rectangle(BaseGeometry):
    """Represents a rectangle"""
    def __init__(self, width, height):
        """Initialize instances"""
        self.integer_validator("width", width)
        self.integer_validator("height", height)
        self.__width = width
        self.__height = height

    def area(self):
        """Return the area of the rectangle"""
        return self.__width * self.__height

    def __str__(self):
        """Returns the representation of the rectangle"""
        string = "[Rectangle] " + str(self.__width) + "/" + str(self.__height)
        return string
