#!/usr/bin/python3
"""<function `inherits_from`>"""


def inherits_from(obj, a_class):
    """check to see if an object is derived from a class

    Args:
        obj (any): object
        a_class: class

    Return: True if true, otherwise False
    """

    return obj.__class__ is not a_class and\
        issubclass(obj.__class__, a_class)
