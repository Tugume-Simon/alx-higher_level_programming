#!/usr/bin/python3
"""This module writes content to a file in JSON"""
import json


def save_to_json_file(my_obj, filename):
    """Writes JSON representation of objects to a file

    Args:
        my_obj: Python object
        filename (str): name of the file

    """

    with open(filename, 'w', encoding='utf-8') as f:
        json.dump(my_obj, f)
