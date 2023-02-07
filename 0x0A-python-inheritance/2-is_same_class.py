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
    cls = obj.__class__
    #return isinstance(obj, a_class) and issubclass(cls, a_class)\
        #and hasattr(obj, "__{}__".format(name))
    return issubclass(cls, a_class) and hasattr(obj, "__{}__".format(name))
