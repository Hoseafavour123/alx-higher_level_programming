#!/usr/bin/python3
"""Defines a string serialization function."""
import json


def to_json_string(my_obj):
    """Returns JSON representation of a string object."""
    return (json.dumps(my_obj))
