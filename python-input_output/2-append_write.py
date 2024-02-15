#!/usr/bin/python3
"""Defines a function to append a string at the end of a file"""


def append_write(filename="", text=""):
    """Return the number of characters written"""
    with open(filename, 'a', encoding="utf-8") as f:
        return f.write(text)
