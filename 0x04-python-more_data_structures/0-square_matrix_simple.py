#!/usr/bin/python3

def square_matrix_simple(matrix=[]):
    """Takes a 2D matrix and square the values"""
    if (len(matrix) == 0):
        return None

    return list(list(map(lambda a: a*a, num_list)) for num_list in matrix)
