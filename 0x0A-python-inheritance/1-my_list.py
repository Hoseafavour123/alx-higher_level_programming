#!/usr/bin/python3
"""Defines an inherited list class MyClass"""


class MyList(list):
    """This class uses inheritance from builtin module 'list'"""

    def print_sorted(self):
        """sorts the list in ascending order"""

        print(sorted(self))
