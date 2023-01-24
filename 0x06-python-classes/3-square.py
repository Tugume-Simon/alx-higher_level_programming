#!/usr/bin/python3
"""class: Module defines a class Square

The Square class is defined here which will be used to
create square objects.
"""


class Square():
    """make square class

    The size of the square is intentionally made private
    because many things depend on it so it must not be
    changed

    Attributes:
        size (int): size of the square

    """

    def __init__(self, size=0):
        self.__size = size

        if type(size) is not int:
            raise TypeError("size must be an integer")
        if size < 0:
            raise ValueError("size must be >= 0")

    def area(self):
        """Returns the area of the square"""

        return (self.__size ** 2)
