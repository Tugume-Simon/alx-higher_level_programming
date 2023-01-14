#!/usr/bin/python3
def roman_to_int(roman_string):
    conversions = {
            'I': 1,
            'V': 5,
            'X': 10,
            'L': 50,
            'C': 100,
            'D': 500,
            'M': 1000
            }

    if roman_string == '' or roman_string is None:
        return None

    prev = 0
    integer = 0
    for letter in roman_string:
        inc = conversions[letter]
        if inc > prev and prev != 0:
            integer -= inc
        else:
            integer += inc
        prev = inc
    return integer if integer > 0 else integer
