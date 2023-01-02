#!/usr/bin/python3

""" A script with class that represents a Rectantangle"""


class Rectangle:
    """  A class Rectangle that defines a rectangle: """

    number_of_instances = 0
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
        self.number_of_instances += 1

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

    def area(self):
        """ returns the area of the rectangle"""
        return (self.width * self.height)

    def perimeter(self):
        """ returns the perimeter of the rectangle"""
        if self.width == 0 or self.height == 0:
            p = 0
        else:
            p = 2 * (self.width + self.height)

        return (p)

    def __str__(self):
        """ Special method that returns a string from a class"""
        rec_str = ""
        if self.width == 0 or self.height == 0:
            rec_str = ""
        else:
            for i in range(self.height):
                rec_str += ("#" * self.width)
                if i != (self.height - 1):
                    rec_str += '\n'
        return (rec_str)

    def __repr__(self):
        """Return the string representation of the Rectangle."""
        rect = "Rectangle(" + str(self.__width)
        rect += ", " + str(self.__height) + ")"
        return (rect)

    def __del__(self):
        """Instance method called when an instance is deleted """
        self.number_of_instances -= 1
        print("Bye rectangle...")
