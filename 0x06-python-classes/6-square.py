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
        position (tuple): coordinates of the square

    """

    def __init__(self, size=0, position=(0, 0)):
        self.__size = size

        if type(size) is not int:
            raise TypeError("size must be an integer")
        if size < 0:
            raise ValueError("size must be >= 0")

        if type(position) is not tuple and len(position) != 2:
            raise TypeError("position must be a tuple of 2 positive integers")
        elif position[0] < 0 or position[1] < 0:
            raise TypeError("position must be a tuple of 2 positive integers")

        self.__position = position

    @property
    def size(self):
        """getter for the private size attribute"""

        return self.__size

    @property
    def position(self):
        """getter for the private position attribute"""

        return self.position

    @size.setter
    def size(self, value):
        """setter for the private size attribute"""

        if type(value) is not int:
            raise TypeError("size must be an integer")

        if value < 0:
            raise ValueError("size must be >= 0")

        self.__size = value

    @position.setter
    def position(self, value):
        """setter for the private position attribute"""

        if type(value) is not tuple and len(value) != 2:
            raise TypeError("position must be a tuple of 2 positive integers")
        elif value[0] < 0 or value[1] < 0:
            raise TypeError("position must be a tuple of 2 positive integers")

        self.__position = value

    def area(self):
        """Returns the area of the square"""

        return (self.__size ** 2)

    def my_print(self):
        """Prints to stdout the area of the square

        This area is in a visual representation,
        the # characters are used

        """
        if self.__size == 0:
            print("")
        else:
            for i in range(self.__size):
                for x in range(self.__position[0]):
                    print(" ", end="")

                for j in range(self.__size):
                    print("#", end="")
                print("")
