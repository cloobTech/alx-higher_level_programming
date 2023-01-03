#!/usr/bin/python3

""" A script with class that represents a Rectantangle"""


class Rectangle:
    """  A class Rectangle that defines a rectangle: """

    number_of_instances = 0
    print_symbol = "#"

    @classmethod
    def square(cls, size=0):
        """Return a new Rectangle with width and height equal to size.
        Args:
            size (int): The width and height of the new Rectangle.
        """
        return(cls(size, size))

    @staticmethod
    def bigger_or_equal(rect_1, rect_2):
        if not isinstance(rect_1, Rectangle):
            raise TypeError("rect_1 must be an instance of Rectangle")
        if not isinstance(rect_2, Rectangle):
            raise TypeError("rect_2 must be an instance of Rectangle")
        if rect_1.area() >= rect_2.area():
            return (rect_1)
        else:
            return (rect_2)

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
        Rectangle.number_of_instances += 1

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
                if not isinstance(self.print_symbol, str):
                    rec_str = rec_str.join(self.print_symbol)
                rec_str += (self.print_symbol * self.width)
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
        Rectangle.number_of_instances -= 1
        print("Bye rectangle...")
