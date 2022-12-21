#!/usr/bin/python3

""" Write a class Square that defines a square by: (based on 1-square.py)."""


class Square:
    """Represent a square."""

    def __init__(self, size=0, position=(0, 0)):
        """Initialize a new Square.
        Args:
            size (integer): The size of the new square.
            position (integer, integer): Sets the position of a square.
        """
        self.__size = size
        self.__position = position

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

    @property
    def position(self):
        """ Getter to retrieve position """
        return (self.__position)

    @position.setter
    def position(self, value):
        """ Set the position of the square """
        if (not isinstance(value, tuple) or len(value) != 2 or
                not all(isinstance(num, int) for num in value) or
                not all(num >= 0 for num in value)):
            raise TypeError("position must be a tuple of 2 positive integers")
        self.__position = value

    def my_print(self):
        """ print # """
        if self.__size == 0:
            print("{}".format('\n'), end="")
        for pos in range(0, self.__position[1]):
            print("")
            for i in range(0, self.__size):
                for pos1 in range(0, self.__position[0]):
                    print("_")
                for j in range(0, self.__size):
                    print("{}".format('#'), end="")
                print("{}".format('\n'), end="")
