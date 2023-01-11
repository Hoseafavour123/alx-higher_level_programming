#!/usr/bin/python3
"""Defines a base geometry class BaseGeometry"""


class BaseGeometry:
    """represents base geometry"""

    def area(self):
        """Not implemented"""
        raise Exception("area() is not implemented")

    def integer_validator(self, name, value):
        """Validates a parameter as integer

        Args:
            name(str): The name of the parameter.
            value(int): The parameter to validate
        Raises:
            TypeError: if value is not an integer
            ValueError: if value is <= 0
        """
        if type(value) != int:
            raise TypeError("{} must be an integer".format(name))
        if value <= 0:
            raise ValueError("{} must be greater than 0".format(name))
