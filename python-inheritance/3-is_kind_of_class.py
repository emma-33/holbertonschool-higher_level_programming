#!/usr/bin/python3
"""Defines a function that check if an object is an instance of a class
or if the object is an instance of a class that inherited from
specified class"""


def is_kind_of_class(obj, a_class):
    """Checks if obj is an instance of a_class or if is an instance
    of a class that inherited from a_class

    Args:
        obj: object to check
        a_class: class to compare to

    Returns:
        True if obj is an instance of a_class or an instance
    of a class that inherited from a_class, otherwise False
    """
    if isinstance(obj, a_class):
        return True
    return False
