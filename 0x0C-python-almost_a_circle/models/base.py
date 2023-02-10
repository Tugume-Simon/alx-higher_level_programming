#!/usr/bin/python3
"""Class Base"""
import json


class Base:
    """Base class

    Attributes:
        __nb_objects: private, counts instances
        id (int): public, defaults to None

    """
    __nb_objects = 0

    def __init__(self, id=None):
        """initializes class attributes"""
        if id is not None:
            self.id = id
        else:
            Base.__nb_objects += 1
            self.id = Base.__nb_objects

    @staticmethod
    def to_json_string(list_dictionaries):
        """returns the JSON string representation of a list of dictionaries"""

        if type(list_dictionaries) is not list:
            raise TypeError("list_dictionaries must be a list of dictionaries")
        for val in list_dictionaries:
            if type(val) is not dict:
                raise TypeError("""list_dictionaries must be\
 a list of dictionaries""")
        return json.dumps(list_dictionaries)
