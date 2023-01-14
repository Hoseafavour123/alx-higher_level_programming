#!/usr/bin/python3
"""This module defines a text file-reading function 'read_file()'"""


def read_file(filename=""):
    """Prints the contents of a UTF-8 text file to stdout"""
    with open(filename, encoding='utf-8') as f:
        for line in f:
            print(f.read(), end="")
