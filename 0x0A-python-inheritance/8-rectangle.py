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
