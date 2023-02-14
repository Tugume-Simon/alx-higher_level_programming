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
            if type(id) is not int:
                raise TypeError("id must be an integer")
            if id <= 0:
                raise ValueError("id must be >= 0")
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

    @staticmethod
    def from_json_string(json_string):
        """returns the list of the JSON string representation"""

        if json_string is None or json_string == "":
            return []
        if type(json_string) is not str:
            raise TypeError("not a string representing a list of dictionaries")
        return json.loads(json_string)

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

    @classmethod
    def create(cls, **dictionary):
        """creates new class instance and updates it, setting all attributes"""

        classname = cls.__name__
        if classname == 'Rectangle':
            dummy = cls(1, 2)
        elif classname == 'Square':
            dummy = cls(1)

        dummy.update(**dictionary)
        return dummy

    @classmethod
    def load_from_file(cls):
        """returns a list of instances from json file"""

        filename = cls.__name__ + '.json'

        try:
            with open(filename, 'r', encoding='utf-8') as f:
                json_string = f.readline()
                if json_string == '':
                    raise Exception('file empty')
        except Exception:
            return []
        else:
            list_dicts = cls.from_json_string(json_string)

        instances = []
        for el in list_dicts:
            instances.append(cls.create(**el))

        return instances
