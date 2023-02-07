#!/usr/bin/python3
"""<class `BaseGeometry`>"""


class BaseGeometry:
    """BaseGeometry class"""

    def area(self):
        raise Exception("area() is not implemented")

    def integer_validator(self, name, value):
        """check if the value provided is a valid integer

        Args:
            name (any): string assumed
            value (int): integer

        Raises exceptions when value provided isn't an integer
        or if it is less than 1
        """

        if type(value) is not int:
            raise TypeError("{} must be an integer".format(name))

        if value < 1:
            raise ValueError("{} must be greater than 0".format(name))
