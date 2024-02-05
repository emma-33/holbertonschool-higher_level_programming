#!/usr/bin/python3
class Square:
    """defines a square"""
    def __init__(self, size=0):
        """Initializing size
        Args :
            size: size of square
        """

        self.__size = size

    def area(self):
        """returns the current square area"""
        return self.__size * self.__size

    @property
    def size(self):
        """returns curent size"""
        return self.__size
    
    @size.setter
    def size(self, value):
        if not isinstance(value, int):
            raise TypeError("size must be an integer")
        elif value < 0:
            raise ValueError("size must be >= 0")

        self.__size = value
