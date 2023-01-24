#!/usr/bin/python3
"""class: Module defines a class Square

The Square class is defined here which will be used to
create square objects.
"""


class Square:
    """make square class

    The size of the square is intentionally made private
    because many things depend on it so it must not be
    changed

    Attributes:
        size (int): size of the square

    """

    def __init__(self, size):
        self.__size = size
