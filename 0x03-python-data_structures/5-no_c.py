#!/usr/bin/python3
def no_c(my_string):
    str = ""
    for char in my_string:
        if not (char == 'c' or char == 'C'):
            str = str + char
    return str
