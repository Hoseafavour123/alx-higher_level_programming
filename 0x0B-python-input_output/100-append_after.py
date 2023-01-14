#!/usr/bin/python3
"""Defines a text-file insertion function."""


def append_after(filename="", search_string="", new_string=""):
    """Insert text after each line containing a given string.

    Args:
        filename(str): Name of file.
        search_string(str): String to insert after.
        new_string(str): String to insert.
    """
    text = ""
    with open(filename) as r:
        for line in r:
            text += line
            if search_string in line:
                text += new_string
    with open(filename, "w") as w:
        w.write(text)
