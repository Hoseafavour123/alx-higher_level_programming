#!/usr/bin/python3
"""Defines a class and inheritted class-checking function"""


def is_kind_of_class(obj, a_class):
    """Checks if an object is an instance or inheritted instance of a class.

    Args:
        obj: The object to check
        a_class: The class to match the type of object

    Return:
        True: If obj is an instance or inheritted instance of a_class
        False: otherwise
    """

    if isinstance(obj, a_class):
        return True
    return False
