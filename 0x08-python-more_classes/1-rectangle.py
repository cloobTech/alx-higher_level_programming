#!/usr/bin/python3

""" A script with class that represents a Rectantangle"""


class Rectangle:
    """  A class Rectangle that defines a rectangle: """
    def __init__(self, width=0, height=0):
        """ Initialize an instance of the class Rectangle.
        Args:
            width(int): width of the rectangle
            height(int): Height of the rectangle
        Raises:
            TypeError: width must be an integer
            TypeError: height must be an integer
            ValueError: width must be >= 0
            ValueError: height must be >= 0
        """
        self.width = width
        self.height = height

    @property
    def width(self):
        """getter method"""
        return (self.__width)

    @width.setter
    def width(self, value):
        """ setter method """
        if not isinstance(value, int):
            raise TypeError("width must be an integer")
        elif value < 0:
            raise ValueError("width must be >= 0")
        self.__width = value

    @property
    def height(self):
        """getter method"""
        return (self.__height)

    @height.setter
    def height(self, value):
        """ setter method """
        if not isinstance(value, int):
            raise TypeError("height must be an integer")
        elif value < 0:
            raise ValueError("height must be >= 0")
        self.__height = value
