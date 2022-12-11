#!/usr/bin/python3

def uppercase(str):
    """Print a string in reverse."""
    for i in str:
        if (ord(i) >= 97 and ord(i) <= 122):
            i = chr(ord(i) - 32)
        print("{}".format(i), end="")
    print("")
