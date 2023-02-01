#!/usr/bin/python3
"""A function say_my_name definded
prints a name in a sentence.
"""


def say_my_name(first_name, last_name=""):
    """Function simply prints the name based on args provided

    the combination of first and second name, preceeded by the
    text "My name is" is made from arguments, seperated by a space.

    @Params:
        first_name (str): first name
        last_name (str): last name

    """
    if type(first_name) is not str:
        raise TypeError("first_name must be a string")
    if type(last_name) is not str:
        raise TypeError("last_name must be a string")
    print("My name is {} {}".format(first_name, last_name))
