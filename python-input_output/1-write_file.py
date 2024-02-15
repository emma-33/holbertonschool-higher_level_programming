#!/usr/bin/python3
"""Defines a function to write a string to a file"""


def write_file(filename="", text=""):
    """Return the number of characters written"""
    with open(filename, 'w', encoding="utf-8") as f:
        return f.write(text)
