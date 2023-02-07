#!/usr/bin/python3
"""This module returns JSON representation of objects"""
json = __import__('json')


def to_json_string(my_obj):
    return json.dumps(my_obj)
