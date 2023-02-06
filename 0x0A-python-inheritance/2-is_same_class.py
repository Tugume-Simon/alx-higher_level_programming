#!/usr/bin/python3
"""<function `is_same_class`>"""


def is_same_class(obj, a_class):
    """is_same_class tests if an object is an instance of a class

    Args:
        obj (any): object
        a_class: built-in or defined class

    Return: True if test is successful, otherwise false
    """

    name = a_class.__name__
    return hasattr(obj, "__{}__".format(name)) and isinstance(obj, a_class)
