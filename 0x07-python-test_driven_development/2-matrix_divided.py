#!/usr/bin/python3
"""Works on the division of a matrix by a scalar

The function matrix_divided() returns a new
matrix with each value divided by given value.

Arguments:
    matrix (list of list): of floats and/or integers
    div (int, float): scalar/dividend

Return:
    new matrix with each of its elements in each row
    divided by div
"""


def matrix_divided(matrix, div):
    """Divides matrix by a scalar

    row - represents a row in a matrix
    el - represents an element in a row of a matrix

    """

    if type(matrix) is not list:
        raise TypeError(' '.join(("matrix must be a matrix",
                        "(list of lists) of integers/floats")))

    for row in matrix:
        if type(row) is not list:
            raise TypeError(' '.join(("matrix must be a matrix",
                            "(list of lists) of integers/floats")))

    row_len = len(matrix[1])
    for row in matrix:
        if len(row) != row_len:
            raise TypeError(' '.join(("Each row of the matrix must",
                            "have the same size")))

    if row_len == 0:
        raise TypeError(' '.join(("matrix must be a matrix",
                            "(list of lists) of integers/floats")))

    for row in matrix:
        for el in row:
            if type(el) not in [int, float]:
                raise TypeError(' '.join(("matrix must be a matrix",
                                "(list of lists) of integers/floats")))

    if type(div) not in [int, float]:
        raise TypeError("div must be a number")

    if div == 0:
        raise ZeroDivisionError("division by zero")

    return [[round((el/div), 2) for el in row] for row in matrix]
