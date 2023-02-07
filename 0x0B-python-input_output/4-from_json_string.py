#!/usr/bin/python3
"""Covert JSON back to object"""
import json


def from_json_string(my_str):
    """Converts JSON back to object format

    Args:
        my_str (str): JSON string

    Return: Python object
    """

    return json.loads(my_str)
