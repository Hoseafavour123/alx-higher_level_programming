#!/usr/bin/python3
"""Defines a class Student."""


class Student:
    """Represents the model of a student."""
    def __init__(self, first_name, last_name, age):
        """Instantiation.

        Args:
            fist_name(str): First name of student.
            last_name(str): Last name of student.
            age(int): age of student.
        """
        self.first_name = first_name
        self.last_name = last_name
        self.age = age

    def to_json(self, attrs=None):
        """Returns specifuc attribute names.

        If attrs is a list of strings, return only those attributes included in
        the list."""
        try:
            for ele in attrs:
                if type(ele) is not str:
                    return self.__dict__
        except Exception:
            return self.__dict__
        new_dict = dict()
        for k, v in self.__dict__.items():
            if k in attrs:
                new_dict[k] = v
        return new_dict
