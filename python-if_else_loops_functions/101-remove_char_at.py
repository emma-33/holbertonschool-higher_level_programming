#!/usr/bin/python3
def remove_char_at(str, n):
    new_str = ""

    for char in range(len(str)):
        if char != n:
            new_str += str[char]

    return new_str
