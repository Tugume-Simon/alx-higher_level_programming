#!/usr/bin/python3
"""<class `Rectangle`>"""
BaseGeometry = __import__('7-base_geometry').BaseGeometry


class Rectangle(BaseGeometry):
    """Rectangle class inherits from BaseGeometry

    Args:
        width (int): rectangle width
        height (int): rectangle height

    """

    def __init__(self, width, height):
        """instantiates the Rectangle object"""
        self.integer_validator("width", width)
        self.integer_validator("height", height)

        self.__width = width
        self.__height = height
