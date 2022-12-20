#!/usr/bin/python3

def print_reversed_list_integer(my_list=[]):
    """Print a list of integers in reverse"""
    if not my_list:
        pass

    i = len(my_list) - 1

    for j in range(len(my_list) - 1):
        if (j < i):
            tmp = my_list[j]
            my_list[j] = my_list[i]
            my_list[i] = tmp
        i -= 1
    for num in my_list:
        print("{:d}".format(num))
