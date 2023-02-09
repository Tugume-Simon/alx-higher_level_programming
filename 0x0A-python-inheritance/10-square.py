#!/usr/bin/python3
"""Square class subclass of Rectangle class"""
Rectangle = __import__('9-rectangle').Rectangle


class Square(Rectangle):
    """Square inherits the Rectangle class

    Attributes:
        size (int): length of side of a square

    """

    def __init__(self, size):
        self.integer_validator("size", size)
        super().__init__(size, size)

        self.__size = size

    def area(self):
        return self.__size * self.__size
