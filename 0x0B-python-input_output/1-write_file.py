#!/usr/bin/python3
"""Defines a file-writing function"""


def write_file(filename="", text=""):
    """Write a string to a UTF-8 text file.

    Args:
        filename(str): The name of the file.
        text(str): The UTF-8 text content.

    Returns:
        The number of characters written.
    """
    with open(filename, "w", encoding="utf-8") as f:
        return (f.write(text))
