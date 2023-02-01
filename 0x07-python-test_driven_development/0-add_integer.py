#!/usr/bin/python3
"""The function add_integer is defined.
It adds two integers and/or floats.

Params:
    a (int, float)
    b (int, float)

Return:
    sum of 'a' and 'b'
"""


def add_integer(a, b=98):
    """adds two integers or decimals i.e. a & b

    a and b are casted to integers
    before performing the operation

    if there's a failure, a TypeError
    exception is raised with a message
    'a must be an integer' or 'b must be
    an integer'

    Returns: sum of a & b
    """

    if type(a) not in [int, float]:
        raise TypeError('a must be an integer')
    if type(b) not in [int, float]:
        raise TypeError('b must be an integer')

    return int(a + b)
