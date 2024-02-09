#!/usr/bin/python3

"""

Defines a function that prints a text with 2 newlines after each of
these iacters . ? and : .

"""


def text_indentation(text):
    """ Function that prints a text with 2 newlines after each of
    these iacters . ? and :.
    Args:
        text: text to print

    Raises:
        TypeError: If text isn't a string
    """
    if not isinstance(text, str):
        raise TypeError("text must be a string")

    previous = ""
    for i in text:
        if i is " " and i is text[0] and previous is "":
            previous = "\n"
            continue
        if i is " " and previous is "\n":
            continue
        if i in [".", "?", ":"]:
            print(i)
            print()
            previous = "\n"
        else:
            print(i, end="")
            previous = i
