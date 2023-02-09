#!/usr/bin/python3
"""Attribute >> object"""


def add_attribute(obj, attribute, value):
    """Adds new attribute to an object

    if the object cannot have a new attribute,
    the message "can't add new attribute is printed"

    """
    if type(obj) not in [int, float, str, tuple, bool, None]:
        setattr(obj, attribute, value)
    else:
        raise TypeError("can't add new attribute")
