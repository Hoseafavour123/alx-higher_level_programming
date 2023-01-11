#!/usr/bin/python3
"""Defines an inheritance instance-checking function"""


def inherits_from(obj, a_class):
    """Checks if object is an inheritted instance of a class.

    Args:
        obj: The object instance to check
        a_class: The class to match the type of object to.
    Returns:
        True if obj is an inheritted instance.
        False otherwise
    """
    if issubclass(type(obj), a_class) and type(obj) != a_class:
        return True
    return False
