#!/usr/bin/python3
"""Initialising a rectangle class and some methods"""


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

    def __str__(self):
        """Diagramatic representation of rectangle"""
        if (self.__width == 0) or (self.__height == 0):
            return ""
        rec = []
        for i in range(self.__height):
            [rec.append("#") for j in range(self.__width)]
            if i != self.__height - 1:
                rec.append("\n")
        return ("".join(rec))

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

    def area(self):
        """computes area of a rectangle"""
        return (self.__width * self.__height)

    def perimeter(self):
        """computes perimeter of rectangle"""
        if (self.__width == 0) or (self.__height == 0):
            return 0
        return (2 * (self.__width + self.__height))
