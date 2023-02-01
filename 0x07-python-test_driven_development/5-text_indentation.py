#!/usr/bin/python
"""Prints two new lines after a certain characters"""


def text_indentation(text):
    """Prints 2 newline characters everytime either of
    '.' or '?' or ':' characters are encountered.

    if there's whitespace at the beginning or end of a
    line, that space is eliminated.

    """
    if type(text) is not str:
        raise TypeError("text must be a string")

    n = 0
    for char in text:
        if n > 0:
            p = text[n - 1]
            if (p == '.' or p == '?' or p == ':' or p == ' ')\
                    and char == ' ':
                n += 1
                continue
        elif n == 0 and char == ' ':
            n += 1
            continue
        print("{}".format(char), end="")
        if char == '.' or char == ':' or char == '?':
            print("\n")
        n += 1
