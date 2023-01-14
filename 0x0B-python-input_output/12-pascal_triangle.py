#!/usr/bin/python3
"""Defines a Pascal Triangle function."""


def pascal_triangle(n):
    """Print Pascal triangle.

    Args:
        n(int): The number of rows to print.
    Returns:
        A list of list of numbers of each row.
    """

    if n <= 0:
        return []

    result = [[1]]
    for i in range(n - 1):
        tmp = [0] + result[-1] + [0]
        row = []
        for j in range(len(result[-1]) + 1):
            row.append(tmp[j] + tmp[j + 1])
        result.append(row)
    return result
