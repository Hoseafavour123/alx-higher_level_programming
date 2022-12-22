#!/usr/bin/python3

def uniq_add(my_list=[]):
    """Adds the unique elements of a list"""
    if not my_list:
        pass
    add = 0
    for num in set(my_list):
        add += num

    return add
