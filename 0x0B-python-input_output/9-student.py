#!/usr/bin/python3
"""<class 'Student'>"""


class Student:
    """This class defines a student

    Attributes:
        first_name (str): first name
        last_name (str): last name
        age (int): student age

    """

    def __init__(self, first_name, last_name, age):
        self.first_name = first_name
        self.last_name = last_name
        self.age = age

    def to_json(self):
        return self.__dict__
