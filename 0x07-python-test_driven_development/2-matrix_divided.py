#!/usr/bin/python3
""" This module containsa function that divides all
elements of a matrix(list of
lists)
"""


def matrix_divided(matrix, div):
    """Divideds all elements of matrix by div

    Args:
        matrix - a list of list
        div - an integer
    Returns:
        A new matrix divided by div
    """
    for elem in matrix:
        if type(elem) is not list:
            raise TypeError("matrix must be a matrix (list of lists) of "
                            "integers/floats")
        for num in elem:
            if type(num) not in [int, float]:
                raise TypeError("matrix must be a matrix (list of lists) of "
                                "integers/floats")

    for i in range(len(matrix)):
        if (i + 1) != len(matrix):
            if len(matrix[i]) != len(matrix[i + 1]):
                raise TypeError("Each row of the matrix "
                                "must have the same size")

    if type(div) not in [int, float]:
        raise TypeError("div must be a number")
    if div == 0:
        raise ZeroDivisionError("division by zero")

    return ([list(map(lambda x: round(x/div, 2), elem)) for elem in matrix])
