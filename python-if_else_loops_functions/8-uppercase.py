#!/usr/bin/python3
def uppercase(str):
    upper_str = ""
    for i in str:
        if ord(i) >= 97 and ord(i) <= 122:
            upper_str = upper_str + chr(ord(i) - 32)
        else:
            upper_str = upper_str + chr(ord(i))
    print("{:s}".format(upper_str))
