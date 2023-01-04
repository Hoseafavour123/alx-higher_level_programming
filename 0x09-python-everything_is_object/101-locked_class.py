#!/usr/bin/python3
"""Module for a class that prevents dynamic attribute creation"""


class LockedClass():
    """prevents dynamic attribute creation"""
    __slots__ = ['first_name']

    def __init__(self):
        """init method"""
        pass
