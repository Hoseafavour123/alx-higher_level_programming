#!/usr/bin/python3

def search_replace(my_list, search, replace):
    """Searches for an element and replaces it with another"""
    if not my_list:
        return my_list
    return [num if num != search else replace for num in my_list]
