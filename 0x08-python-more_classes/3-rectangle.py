#!/usr/bin/python3
"""Rectangle class"""


class Rectangle:
    """Defines a rectangle from its dimensions

    The dimensions i.e the width and height of
    the rectangle are either initialized (by the
    __init__ method) or by the setters and are
    accessed through the getters.

    Attributes:
        width (int): width of the rectangle
        height (int): height of the rectangle

    """

    def __init__(self, width=0, height=0):
        self.width = width
        self.height = height

    @property
    def width(self):
        """int: width of the rectangle"""
        return self.__width

    @property
    def height(self):
        """int: height of the rectangle"""
        return self.__height

    @width.setter
    def width(self, value):
        """sets the width of the rectangle"""

        if type(value) is not int:
            raise TypeError("width must be an integer")
        if value < 0:
            raise ValueError("width must be >= 0")

        self.__width = value

    @height.setter
    def height(self, value):
        """sets the height of the rectangle"""

        if type(value) is not int:
            raise TypeError("height must be an integer")
        if value < 0:
            raise ValueError("height must be >= 0")

        self.__height = value

    def area(self):
        """Computes and returns the area of the rectangle"""
        return self.__width * self.__height

    def perimeter(self):
        """Computes and returns the perimeter of the rectangle"""

        if self.__width == 0 or self.__height == 0:
            perimeter = 0
        else:
            perimeter = 2 * (self.__width + self.__height)

        return perimeter

    def __str__(self):
        """Returns a string representation of the rectangle"""
        ret_str = ""
        for i in range(self.__height):
            for j in range(self.__width):
                ret_str += "#"
            ret_str += "\n"
        return ret_str
