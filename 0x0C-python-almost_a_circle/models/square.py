#!/usr/bin/python3
""" Square Template """
from models import rectangle


class Square(rectangle.Rectangle):
    """class Square that inherits from Rectangle"""
    def __init__(self, size, x=0, y=0, id=None):
        """ class constructor """
        super().__init__(size, size, x, y, id)

    @property
    def size(self):
        """ Square prop. getter method for (size) """
        return (self.width)

    @size.setter
    def size(self, value):
        """ setter method """
        self.width = value
        self.height = value

    def __str__(self):
        """ str representation of the Square Class """
        str_repr = ""
        str_repr += f"[Square] ({self.id}) {self.x}/{self.y} - {self.width}"
        return (str_repr)

    def update(self, *args, **kwargs):
        """ Update the class Square attributes """
        if len(args) > 0:
            for index, value in enumerate(args):
                if index == 0:
                    self.id = value
                if index == 1:
                    self.width = value
                if index == 2:
                    self.x = value
                if index == 3:
                    self.y = value
        elif kwargs and len(kwargs) > 0:
            for key, value in kwargs.items():
                if key == "id":
                    self.id = value
                elif key == "size":
                    self.width = value
                elif key == "x":
                    self.x = value
                elif key == "y":
                    self.y = value

    def to_dictionary(self):
        """ Return dict rep. of the square obj. """
        dict_rep = {
            "id": self.id,
            "size": self.width,
            "x": self.x,
            "y": self.y
        }

        return (dict_rep)
