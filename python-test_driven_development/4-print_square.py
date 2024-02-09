#!/usr/bin/python3

"""

Defines a function that prints a square with #.

"""


def print_square(size):
    """ Function that prints a square with #.
    Args:
        size: size of square

    Raises:
        TypeError: If size isn't an integer
        ValueError: If size is less than 0
    """
    if not isinstance(size, int):
        raise TypeError("size must be an integer")

    if isinstance(size, float) and size < 0:
        raise ValueError("size must be >= 0")

    if size < 0:
        raise ValueError("size must be >= 0")

    for i in range(size):
        for j in range(size):
            print("#", end="")
        print("")
