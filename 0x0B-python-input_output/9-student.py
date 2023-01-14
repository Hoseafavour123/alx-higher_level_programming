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

    def to_json(self):
        """Returns the JSON representation of a Student instance."""
        return self.__dict__
