#!/usr/bin/python3

""" Write a class Square that defines a square by: (based on 1-square.py)."""


class Square:
    """Represent a square."""

    def __init__(self, size=0):
        """Initialize a new Square.
        Args:
            size (integer): The size of the new square.
        """
        if not isinstance(size, int):
            raise TypeError("size must be an integer")
        elif size < 0:
            raise ValueError("size must be >= 0")
        self.__size = size

    def area(self):
        """ Return the area of the square """
        return (self.__size * self.__size)

    @property
    def size(self):
        """ Getter method to return size """
        return (self.__size)

    @size.setter
    def size(self, value):
        """ Setter method to set size """
        if not isinstance(value, int):
            raise TypeError("size must be an integer")
        elif value < 0:
            raise ValueError("size must be >= 0")
        self.__size = value
