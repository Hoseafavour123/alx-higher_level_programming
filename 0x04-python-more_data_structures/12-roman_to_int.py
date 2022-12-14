#!/usr/bin/python3

def roman_to_int(roman_string):
    """Converts roman numerals to int"""
    if (roman_string is None) or (type(roman_string) is not str):
        return 0

    roman = {
        "I": 1,
        "V": 5,
        "X": 10,
        "L": 50,
        "C": 100,
        "D": 500,
        "M": 1000
        }

    str_len = len(roman_string)
    value_int = roman[roman_string[str_len - 1]]

    for i in range(str_len - 1, 0, -1):
        current_value = roman[roman_string[i]]
        previous_value = roman[roman_string[i - 1]]

        if previous_value >= current_value:
            value_int += previous_value
        else:
            value_int -= previous_value

    return value_int
