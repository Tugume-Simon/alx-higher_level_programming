#!/usr/bin/python3
"""This module returns JSON representation of objects"""
import json


def to_json_string(my_obj):
    """Returns JSON representation of objects

    Args:
        my_obj (obj): any
    """

    return json.dumps(my_obj)
