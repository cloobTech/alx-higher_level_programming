#!/usr/bin/python3

""" Write a class Square that defines a square by: (based on 0-square.py)."""


class Square:
    """Represent a square."""
    def __init__(self, size):
        """Private instance attribute: size
        Args:
            size (integer): The size of the new square.
        """
        self.__size = size
