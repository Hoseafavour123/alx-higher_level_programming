#!/usr/bin/python3
"""Defines a class-checking function"""


def is_same_class(obj, a_class):
    """Determines if obj is of class 'a_class'

    Args:
        obj: The object
        a_class: class to check

    Return:
        True: if obj is of class 'a_class'
        False: otherwise
    """

    if type(obj) == a_class:
        return True
    return False
