#!/usr/bin/python3
"""This module is responsible for appending content to a file"""


def append_write(filename="", text=""):
    """Appends text to a file

    if a file does not exist, it is created
    Args:
        filename (str): name of the file
        text (str): text to be appended to the file

    Return: number of characters added
    """

    with open(filename, 'a', encoding='utf-8') as f:
        f.seek(0, 2)
        nappend = f.write(text)

    return nappend
