#!/usr/bin/python3

"""Defines a subclass Rectangle of BaseGeometry."""
BaseGeometry = __import__('7-base_geometry').BaseGeometry


class Rectangle(BaseGeometry):
    """Represents a rectangle with inheritted attributes from BaseGeometry"""

    def __init__(self, width, height):
        """Instantiation:

        Args:
            width(int): width of rectangle
            height(int): height of rectangle
        """

        self.integer_validator("width", width)
        self.__width = width

        self.integer_validator("height", height)
        self.__height = height

    def area(self):
        """"Returns the area of rectangle"""
        return self.__width * self.__height

    def __str__(self):
        """Returns string representation of rectangle"""
        string = "[" + str(self.__class__.__name__) + "] "
        string += str(self.__width) + "/" + (self.__height)

        return string
