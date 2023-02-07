#!/usr/bin/python3
"""This module writes text to a file"""


def write_file(filename="", text=""):
    """Writes content to a file

    if a file exists, it is overwritten
    Args:
        filename (str): name of the file
        text (str): string to write to the file

    Return: number of characters written
    """

    with open(filename, 'w', encoding='utf-8') as f:
        nwrite = f.write(text)

    return nwrite
