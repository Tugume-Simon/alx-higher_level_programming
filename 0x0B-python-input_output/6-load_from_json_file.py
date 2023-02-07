#!/usr/bin/python3
"""Object from JSON file"""
import json


def load_from_json_file(filename):
    """Creates an Object from a JSON file

    Args:
        filename (str): name of the file

    Return: Object

    """

    with open(filename, 'r', encoding='utf-8') as f:
        return json.load(f)
