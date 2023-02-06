#!/usr/bin/python3
"""<class 'MyList'>"""


class MyList(list):
    """MyList class

    instantiates the list class it inherits and
    adds one new method print_sorted

    Attributes:
        none

    Methods:
        __init__ - instantiates the class plus base
        class(es)
        print_sorted - prints the list in ascending
        order
    """

    def __init__(self, iterable=()):
        super().__init__(iterable)

    def print_sorted(self):
        """prints a list in ascending order (sorted)"""
        self.sort()
        print(self)
