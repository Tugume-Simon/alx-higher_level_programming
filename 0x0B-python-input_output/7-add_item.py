#!/usr/bin/python3
"""Adds arguments to a Python list and saves them to a file"""
from sys import argv
save_to_json_file = __import__('5-save_to_json_file').save_to_json_file
load_from_json_file = __import__('6-load_from_json_file').load_from_json_file

list_args = [arg for arg in argv if arg != argv[0]]
try:
    filename = "add_item.json"
    list_args = load_from_json_file(filename) + list_args
except Exception:
    pass
finally:
    save_to_json_file(list_args, filename)
