#!/usr/bin/python3
def roman_to_int(roman_string):
    if not roman_string:
        return 0

    result = 0

    roman_letters = {
        "I": 1,
        "V": 5,
        "X": 10,
        "L": 50,
        "C": 100,
        "D": 500,
        "M": 1000,
        }

    for i in range(len(roman_string)):
        current_letter = roman_letters[roman_string[i]]
        previous_letter = roman_letters[roman_string[i-1]]

        if i > 0 and current_letter > previous_letter:
            result += current_letter - 2 * previous_letter

        else:
            result += current_letter

    return result
