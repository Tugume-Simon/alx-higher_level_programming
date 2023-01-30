#!/usr/bin/python3
"""Rectangle class"""


class Rectangle:
    """Defines a rectangle from its dimensions

    The dimensions i.e the width and height of
    the rectangle are either initialized (by the
    __init__ method) or by the setters and are
    accessed through the getters.

    Attributes:
        public:
            number_of_instances (int): counts the
            number active instances of this class

        private:
            width (int): width of the rectangle
            height (int): height of the rectangle

    """

    number_of_instances = 0

    def __init__(self, width=0, height=0):
        self.width = width
        self.height = height
        Rectangle.number_of_instances += 1

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
        """returns the print of the rectangle"""

        ret_str = ""
        if self.__width != 0 and self.__height != 0:
            for i in range(self.__height):
                for j in range(self.__width):
                    ret_str += "#"
                if i != self.__height - 1:
                    ret_str += "\n"

        return ret_str

    def __repr__(self):
        """returns the string representation of the Rectangle instance"""
        return f'Rectangle({self.__width}, {self.__height})'

    def __del__(self):
        """destroys the instance of Rectangle"""
        Rectangle.number_of_instances -= 1
        print("Bye rectangle...")
