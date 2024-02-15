#!/usr/bin/python3
"""Defines a function that check if an object
is an instance of a class"""


def is_same_class(obj, a_class):
    """Checks if obj is an instance of a_class

    Args:
        obj: object to check
        a_class: class to compare to

    Returns:
        True if obj is an instance of a_class, otherwise False
    """
    if type(obj) is a_class:
        return True
    else:
        return False
