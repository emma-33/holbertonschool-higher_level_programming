#!/usr/bin/python3

"""

Defines a function that prints a text with 2 newlines after each of
these characters . ? and : .

"""


def text_indentation(text):
    """ Function that prints a text with 2 newlines after each of
    these characters . ? and :.
    Args:
        text: text to print

    Raises:
        TypeError: If text isn't a string
    """
    if not isinstance(text, str):
        raise TypeError("text must be a string")

    i = 0
    while i < len(text):
        if text[i] == '.' or text[i] == '?' or text[i] == ':':
            print(text[i])
            print("")
            i += 1
        else:
            print(text[i], end='')
        i += 1
