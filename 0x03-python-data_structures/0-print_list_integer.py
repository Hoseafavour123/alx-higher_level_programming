#!/usr/bin/python3

def print_list_integer(my_list=[]):
    """Prints a list of integers

    Args:
        my_list: list to print
    Returns:
        Nothing.
    """
    for i in range(len(my_list)):
        print("{:d}".format(my_list[i]))
