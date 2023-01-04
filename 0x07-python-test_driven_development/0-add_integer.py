#!/usr/bin/python3
"""This is a dummy module for
the addition of two numbers
"""


def add_integer(a, b=98):
    """computes the sum of a and b

    Args:
        a: first integer
        b: second integer, defaults to 98 if not given
    Returns:
        the sum of a and b
    """

    if type(a) not in [int, float]:
        raise TypeError("a must be an integer")
    if type(b) not in [int, float]:
        raise TypeError("b must be an integer")

    return (int(a) + int(b))
