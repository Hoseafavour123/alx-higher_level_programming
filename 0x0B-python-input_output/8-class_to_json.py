#!/usr/bin/python3
"""Defines a module that returns the JSON representation of a class
instance."""


def class_to_json(obj):
    """Return the JSON representation of class instance."""
    return obj.__dict__
