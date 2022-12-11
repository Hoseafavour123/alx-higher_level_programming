#!/usr/bin/python3

def print_last_digit(number):
    """Pirint last digit and return it."""
    last_digit = abs(number) % 10
    print("{}".format(last_digit), end="")
    return (last_digit)
