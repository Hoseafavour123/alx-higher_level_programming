#!/usr/bin/python3

def element_at(my_list, idx):
    """Retrieves element at an index

    Args:
        my_list: list
        idx: index

    Returns:
        None: if idx is out of range
        None: if idx is negative
        Element at idx otherwise.
    """
    if (idx < 0 or idx > len(my_list) - 1):
        return (None)
    else:
        return (my_list[idx])
