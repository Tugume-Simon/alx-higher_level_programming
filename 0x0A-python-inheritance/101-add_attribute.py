#!/usr/bin/python3
"""Attribute >> object"""


def add_attribute(obj, attribute, value):
    """Adds new attribute to an object

    if the object cannot have a new attribute,
    a TypeError is raised with the message
    "can't add new attribute".

    Args:
        obj (any): instance of a class
        attribute: key of property to be set
        value: the property

    """
    if not hasattr(obj, "__dict__"):
        raise TypeError("can't add new attribute")
    setattr(obj, attribute, value)
