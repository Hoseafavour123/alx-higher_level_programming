#!/usr/bin/python3
"""Defines file-appending function"""


def append_write(filename="", text=""):
    """Appends text to a UTF-8 text file.

    Args:
        filename(str): The file name.
        text(str): The text to append.
    Returns:
        The number of characters appended.
    """
    with open(filename, "a", encoding="utf-8") as f:
        return (f.write(text))
