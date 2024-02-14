#!/usr/bin/python3
"""Defines a class called MyList inherited from list"""


class MyList(list):
    """Prints the sorted list"""
    def print_sorted(self):
        print(sorted(self))
