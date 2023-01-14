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

    if roman_string == '' or roman_string is None or \
            not isinstance(roman_string, str):
        return 0

    prev = 0
    integer = 0
    list_roman = list(roman_string)
    list_roman.reverse()
    for letter in list_roman:
        inc = conversions[letter]
        if inc >= prev:
            integer += inc
        else:
            integer -= inc
        prev = inc
    return integer
