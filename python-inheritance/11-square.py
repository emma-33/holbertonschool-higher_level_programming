#!/usr/bin/python3
"""Defines class Square that inherits from Rectangle"""
Rectangle = __import__('9-rectangle').Rectangle


class Square(Rectangle):
    """Represents a square"""
    def __init__(self, size):
        """Initialize instances"""
        self.integer_validator("size", size)
        super().__init__(size, size)
        self.__size = size

    def area(self):
        """Return the area of the square"""
        return self.__size * self.__size

    def __str__(self):
        """Returns the representation of the square"""
        string = "[Square] " + str(self.__size) + "/" + str(self.__size)
        return string
