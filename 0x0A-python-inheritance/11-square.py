#!/usr/bin/python3

"""Defines a class Square that inherits from Rectangle"""
Rectangle = __import__('9-rectangle').Rectangle


class Square(Rectangle):
    """Represents a square"""

    def __init__(self, size):
        """Instantiating the square

        Args:
            size(int): size of square
        """
        self.integer_validator("size", size)
        super().__init__(size, size)
        self.__size = size
