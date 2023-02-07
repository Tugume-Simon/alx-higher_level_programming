#!/usr/bin/python3
"""<function `is_same_class`>"""


def is_same_class(obj, a_class):
    """is_same_class tests if an object is an instance of a class

    Args:
        obj (any): object
        a_class: built-in or defined class

    Return: True if test is successful, otherwise false
    """

    if type(obj) == a_class:
        return True
    else:
        return False
