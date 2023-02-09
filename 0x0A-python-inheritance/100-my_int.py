#!/usr/bin/python3
"""MyInt class, subclass of int"""


class MyInt(int):
    """Inherits the int class"""

    def __init__(self, value):
        super().__init__()

    def __eq__(self, value):
        """Override the default equality operator"""
        if isinstance(value, MyInt):
            return self != value
        else:
            return False

    def __ne__(self, value):
        return not self.__eq__(value)
