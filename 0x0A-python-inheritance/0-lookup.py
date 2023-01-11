#!/usr/bin/python3
"""Object attribute lookup module"""


def lookup(obj):
    """Returns the available attributes available to obj"""
    return (dir(obj))
