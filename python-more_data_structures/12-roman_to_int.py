#!/usr/bin/python3
def roman_to_int(roman_string):
    if not roman_string:
        return 0
    result = 0

    for i in roman_string:

        if roman_string[i] == "I":
            if roman_string[i + 1] == "V":
                result += 4
            if roman_string[i + 1] == 'X':
                result += 9
            result += 1

        elif roman_string[i] == 'V':
            result += 5

        elif roman_string[i] == 'X':
            if roman_string[i + 1] == 'L':
                result += 40
            if roman_string[i + 1] == 'C':
                result += 90
            result += 10

        elif roman_string[i] == 'C':
            if roman_string[i + 1] == 'D':
                result += 400
            if roman_string[i + 1] == 'M':
                result += 900
            result += 100

        elif roman_string[i] == 'D':
            result += 500

        elif roman_string[i] == 'M':
            result += 1000

    return result
