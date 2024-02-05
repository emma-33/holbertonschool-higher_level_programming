#!/usr/bin/python3
class Square:
    """defines a square
    """
    def __init__(self, size=0):
        """Initializing size
        Args :
            size: size of square
        """
        if not isinstance(size, int):
            raise TypeError("size must be an integer")
        elif size < 0:
            raise ValueError("size must be >= 0")
        
        self.__size = size
        