#!/usr/bin/python3
def safe_print_list_integers(my_list=[], x=0):
    """Print the first 'x' values of my_list
    and only integers"""

    count = 0

    for i in range(x):
        try:
            print("{:d}".format(my_list[i]), end="")
        except (ValueError, TypeError):
            pass
        else:
            count += 1
    print()
    return count
