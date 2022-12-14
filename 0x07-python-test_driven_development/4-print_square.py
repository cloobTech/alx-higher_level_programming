#!/usr/bin/python3

""" Script containing a simple function to print squares """


def print_square(size):
    """a function that prints a square with the character #."""
    if (not isinstance(size, int) or (isinstance(size, float) and size < 0)):
        raise TypeError("size must be an integer")
    if size < 0:
        raise ValueError("size must be >= 0")

    for item in range(size):
        print("#" * size)
