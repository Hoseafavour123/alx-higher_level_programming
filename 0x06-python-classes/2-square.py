#!/usr/bin/python3
"""Class Square that defines a square"""


class Square():
    """Validating the input data"""
    def __init__(self, size=0):
        if (type(size) is not int):
            raise TypeError("size must be an integer")
        elif (size < 0):
            raise ValueError("size must be >= 0")

        self.__size = size
