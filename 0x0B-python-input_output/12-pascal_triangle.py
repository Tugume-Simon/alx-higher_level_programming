#!/usr/bin/python3
"""Pascal's triangle"""


def pascal_triangle(n):
    """Makes a pascal's triangle up to 'n' level

    Args:
        n (int): level

    Return: a list of integers representing the Pascal's
    triangle or an empty list if n <= 0

    """
    pascal = []

    if n > 0:
        for i in range(n):
            if i == 0:
                pascal.append([1])
            elif i == 1:
                pascal.append([1, 1])
            else:
                pascal.append([1, 1])
                prev = pascal[i - 1]
                for k in range(len(prev) - 1):
                    sum = prev[k] + prev[k + 1]
                    pascal[i].insert(k + 1, sum)

    return pascal
