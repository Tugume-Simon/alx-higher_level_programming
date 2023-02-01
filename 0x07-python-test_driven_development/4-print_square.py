#!/usr/bin/python3
"""Square generator
This module prints a square according to size
"""


def print_square(size):
    """Prints a square with the '#' character

    @Params:
        size (int): positive integer

    Return: Nothing
    """
    if type(size) is not int:
        raise TypeError("size must be an integer")

    if size < 0:
        raise ValueError("size must be >= 0")

    for row in range(size):
        for col in range(size):
            print("#", end="")
        print("")
