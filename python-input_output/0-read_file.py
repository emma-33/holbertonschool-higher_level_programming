#!/usr/bin/python3
"""Defines a function to read and print a file"""


def read_file(filename=""):
    """Print the content of a file"""
    with open(filename, 'r', encoding="utf-8") as f:
        read = f.read()
        print(read, end="")
