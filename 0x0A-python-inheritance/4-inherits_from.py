#!/usr/bin/python3
"""<function `inherits_from`>"""

def inherits_from(obj, a_class):
    """check to see if an object is derived from a class

    Args:
        obj (any): object
        a_class: class

    Return: True if true, otherwise False
    """

    cls = obj.__name__
    return isinstance(obj, a_class) and hasattr(obj, "__{}__".format(cls))
