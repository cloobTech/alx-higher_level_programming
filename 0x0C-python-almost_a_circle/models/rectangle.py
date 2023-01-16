#!/usr/bin/python3
""" Rectangle class Template """
from models import base


class Rectangle(base.Base):
    """ A representation of a Rectangle """
    def __init__(self, width, height, x=0, y=0, id=None):
        """ Initialize several instance variables """
        super().__init__(id)
        self.width = width
        self.height = height
        self.x = x
        self.y = y

    @property
    def width(self):
        """ getter method """
        return (self.__width)

    @width.setter
    def width(self, value):
        """ setter method """
        if type(value) != int:
            raise TypeError("width must be an integer")
        elif value <= 0:
            raise ValueError("width must be > 0")
        else:
            self.__width = value

    @property
    def height(self):
        """ getter method """
        return (self.__height)

    @height.setter
    def height(self, value):
        """ setter method """
        if type(value) != int:
            raise TypeError("height must be an integer")
        elif value <= 0:
            raise ValueError("height must be > 0")
        else:
            self.__height = value

    @property
    def x(self):
        """ getter method """
        return (self.__x)

    @x.setter
    def x(self, value):
        """ setter method """
        if type(value) != int:
            raise TypeError("x must be an integer")
        elif value < 0:
            raise ValueError("x must be >= 0")
        else:
            self.__x = value

    @property
    def y(self):
        """ getter method """
        return (self.__y)

    @y.setter
    def y(self, value):
        """ setter method """
        if type(value) != int:
            raise TypeError("y must be an integer")
        elif value < 0:
            raise ValueError("y must be >= 0")
        else:
            self.__y = value

    def area(self):
        """" Update the class Rectangle by adding the public method
             def area(self): that returns the area value of the
             Rectangle instance.
        """
        return (self.width * self.height)

    def display(self):
        """prints in stdout the Rectangle instance with the character # """
        for ver in range(self.y):
            """ vertical offset """
            print("")
        for i in range(self.height):
            """ Horinzontal offset """
            print(" " * self.x, end="")
            print("#" * self.width)

    def __str__(self):
        """ return a string representation of the class obj """
        str_rep = ""
        str_rep += f"[Rectangle] ({self.id}) {self.x}/{self.y}"
        str_rep += f" - {self.width}/{self.height}"
        return (str_rep)

    def update(self, *args, **kwargs):
        """Update the class Rectangle"""
        if len(args) > 0:
            for index, value in enumerate(args):
                if index == 0:
                    self.id = value
                if index == 1:
                    self.width = value
                if index == 2:
                    self.height = value
                if index == 3:
                    self.x = value
                if index == 4:
                    self.y = value
        elif len(kwargs) > 0:
            for key, value in kwargs.items():
                if key == "id":
                    self.id = value
                elif key == "width":
                    self.width = value
                elif key == "height":
                    self.height = value
                elif key == "x":
                    self.x = value
                elif key == "y":
                    self.y = value

    def to_dictionary(self):
        """ Return the dictionary represation of the class """
        dict_rep = {
            "id": self.id,
            "width": self.width,
            "height": self.height,
            "x": self.x,
            "y": self.y
        }
        return (dict_rep)
