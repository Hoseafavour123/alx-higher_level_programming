#!/usr/bin/python3

def new_in_list(my_list, idx, element):
    """Replace an element at a given index without
       modifying the original list"""

    copy = []
    for num in my_list:
        copy.append(num)
    if (idx < 0 or idx > len(my_list)):
        return (copy)
    copy[idx] = element

    return (copy)
