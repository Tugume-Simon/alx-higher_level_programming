#!/usr/bin/python3
"""<class 'MyList'>"""


class MyList(list):
    """MyList class -- inherits from the list class""

    Methods:
        print_sorted - prints the list in ascending
        order
    """

    def __init__(self, iterable=()):
        super().__init__(iterable)

    def print_sorted(self):
        """prints a list in ascending order (sorted)"""
        print(sorted(self))
