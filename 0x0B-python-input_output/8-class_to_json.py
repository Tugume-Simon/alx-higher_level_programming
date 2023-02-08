#!/usr/bin/python3
"""Dictionary description of objects"""


def class_to_json(obj):
    """Serializes a given object in JSON

    Description: The function uses the dictionary
    description with simple data structure (list,
    integer, dictionary, string and boolean) that
    it turns object to.

    Args:
        obj (obj): instance of a class

    Return: dictionary description
    """

    return obj.__dict__
