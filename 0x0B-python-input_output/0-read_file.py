#!/usr/bin/python3
"""This module contains a function read_file that reads file content"""


def read_file(filename=""):
    """Reads file content

    Args:
        filename (str): name of the file to be read

    Prints read content to stdout
    """

    with open(filename, 'r', encoding='utf-8') as f:
        file_read = f.read()
    print(file_read, end="")
