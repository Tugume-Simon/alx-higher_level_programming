#!/usr/bin/python3
"""attributes and methods of object"""


def lookup(obj):
    """checks for attributes and methods of an object

    Args:
        obj (object): any

    Return: list of all available attributes and methods
    """

    return dir(obj)
