#!/usr/bin/python3
"""Defines a class Square that inherits from Rectangle."""
from models.rectangle import Rectangle


class Square(Rectangle):
    """A subclass of rectangle."""

    def __init__(self, size, x=0, y=0, id=None):
        """Inherit instantiation logic from parent class."""
        self.size = size
        super().__init__(size, size, x, y, id)

    @property
    def size(self):
        """get size."""
        return (self.width)

    @size.setter
    def size(self, value):
        """set size."""
        self.width = value
        self.height = value

    def __str__(self):
        """String representation of a square."""
        str_sqr = "[Square] "
        str_id = "({}) ".format(self.id)
        str_xy = "{}/{} - ".format(self.x, self.y)
        str_size = "{}".format(self.size)

        return str_sqr + str_id + str_xy + str_size

    def update(self, *args, **kwargs):
        """Updates the attributes."""
        if args is not None and len(args) != 0:
            list_atr = ['id', 'size', 'x', 'y']
            for i in range(len(args)):
                if list_atr[i] == 'size':
                    setattr(self, 'width', args[i])
                    setattr(self, 'height', args[i])
                else:
                    setattr(self, list_atr[i], args[i])
        else:
            for k, v in kwargs.items():
                if k == 'size':
                    setattr(self, 'width', v)
                    setattr(self, 'height', v)
                else:
                    setattr(self, k, v)

    def to_dictionary(self):
        """ Returns a dictionary with attributes """
        list_atr = ['id', 'size', 'x', 'y']
        dict_res = {}

        for key in list_atr:
            if key == 'size':
                dict_res[key] = getattr(self, 'width')
            else:
                dict_res[key] = getattr(self, key)

        return dict_res
