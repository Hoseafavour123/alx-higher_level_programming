#!/usr/bin/python3
"""Working with oop in python"""


class Square():
    """Model a square with a private data, size"""
    def __init__(self, size):
        """Initialise the square

        Args:
            size(int): size of square
        """
        self.__size = size
