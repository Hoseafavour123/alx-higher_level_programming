#!/usr/bin/python3
"""Initialising a rectangle class"""


class Rectangle:
    """Defines a rectangle and initiaises it"""

    def __init__(self, width=0, height=0):
        """Initialises an instance of a rectangle

        Args:
            width: width of rectangle, defaults to 0 if not given
            height: height of triangle, defaults to 0 if not given
        """
        self.width = width
        self.height = height

    # Setter and getter methods for the width
    @property
    def width(self):
        """retrieve width"""
        return self.__width

    @width.setter
    def width(self, value):
        """set the width"""
        if type(value) is not int:
            raise TypeError("width must be an integer")
        if value < 0:
            raise ValueError("width must be >= 0")
        self.__width = value

    # Setter and getter methods for the height
    @property
    def height(self):
        """retrieve height"""
        return self.__height

    @height.setter
    def height(self, value):
        """set height"""
        if type(value) is not int:
            raise TypeError("height must be an integer")
        if value < 0:
            raise ValueError("height must be >= 0")
        self.__height = value
