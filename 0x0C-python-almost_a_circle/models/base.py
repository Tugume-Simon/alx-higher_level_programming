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

        if list_dictionaries is None:
            return "[]"
        if type(list_dictionaries) is not list:
            raise TypeError("list_dictionaries must be a list of dictionaries")
        if len(list_dictionaries) == 0:
            return "[]"
        for val in list_dictionaries:
            if type(val) is not dict:
                raise TypeError("""list_dictionaries must be\
 a list of dictionaries""")
        return json.dumps(list_dictionaries)

    @classmethod
    def save_to_file(cls, list_objs):
        """writes to a file string representation of list_objs

        list_objs is a list of instances that inherit from the
        Base class
        """

        json_string = []
        filename = cls.__name__ + '.json'
        if len(list_objs) != 0:
            for obj in list_objs:
                if not isinstance(obj, cls):
                    raise TypeError("non object found in list of objects")
                json_string.append(obj.to_dictionary())

        with open(filename, "w", encoding='utf-8') as f:
            json.dump(json_string, f)
