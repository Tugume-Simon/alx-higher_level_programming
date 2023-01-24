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

    def __init__(self, size=0):
        self.__size = size

        if type(size) is not int:
            raise TypeError("size must be an integer")
        if size < 0:
            raise ValueError("size must be >= 0")

    @property
    def size(self):
        """getter for the private size attribute"""

        return self.__size

    @size.setter
    def size(self, value):
        """setter for the private size attribute"""

        if type(value) is not int:
            raise TypeError("size must be an integer")

        if value < 0:
            raise ValueError("size must be >= 0")

        self.__size = value

    def area(self):
        """Returns the area of the square"""

        return (self.__size ** 2)

    def my_print(self):
        """Prints to stdout the area of the square

        This area is in a visual representation,
        the # characters are used

        """

        for i in range(self.__size):
            for j in range(self.__size):
                print("#", end="")
            print("")
