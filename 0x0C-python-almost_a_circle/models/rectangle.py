#!/usr/bin/python3
"""Defines a class Rectangle that inherits from base."""
from models.base import Base


class Rectangle(Base):
    """A subclass of Base."""

    def __init__(self, width, height, x=0, y=0, id=None):
        """Instantiation."""
        self.width = width
        self.height = height
        self.x = x
        self.y = y
        super().__init__(id)

    @property
    def width(self):
        """Get width."""
        return self.__width

    @width.setter
    def width(self, value):
        """Set width."""
        if type(value) is not int:
            raise TypeError("width must be an integer")
        if value <= 0:
            raise ValueError("width must be > 0")
        self.__width = value

    @property
    def height(self):
        """Get height."""
        return self.__height

    @height.setter
    def height(self, value):
        """Set height."""
        if type(value) is not int:
            raise TypeError("height must be an integer")
        if value <= 0:
            raise ValueError("height must be > 0")
        self.__height = value

    @property
    def x(self):
        """Get x."""
        return self.__x

    @x.setter
    def x(self, value):
        """set x."""
        if type(value) is not int:
            raise TypeError("x must be an integer")
        if value < 0:
            raise ValueError("x must be >= 0")
        self.__x = value

    @property
    def y(self):
        """get y."""
        return self.__y

    @y.setter
    def y(self, value):
        """set y."""
        if type(value) is not int:
            raise TypeError("y must be an integer")
        if value < 0:
            raise ValueError("y must be >= 0")
        self.__y = value

    def area(self):
        """Return the area of a Rectangle instance."""
        return (self.width * self.height)

    def display(self):
        """Prints the rectangle to stdout."""
        rectangle = self.y * "\n"
        for i in range(self.height):
            rectangle += (" " * self.x)
            rectangle += ("#" * self.width) + "\n"

        print(rectangle, end="")

    def __str__(self):
        """String representation of rectangle instance."""
        str_rec = "[Rectangle] "
        str_id = "({}) ".format(self.id)
        str_xy = "{}/{} - ".format(self.x, self.y)
        str_wh = "{}/{}".format(self.width, self.height)

        return str_rec + str_id + str_xy + str_wh

    def update(self, *args, **kwargs):
        """Update the instance attributes."""
        if (args is not None) and (len(args) != 0):
            list_atr = ["id", "width", "height", "x", "y"]
            for i in range(len(args)):
                setattr(self, list_atr[i], args[i])
        else:
            for k, v in kwargs.items():
                setattr(self, k, v)

    def to_dictionary(self):
        """Return a dictionary of attributes."""
        attr = ["id", "width", "height", "x", "y"]

        my_dict = {}
        for key in attr:
            my_dict[key] = getattr(self, key)
        return my_dict
