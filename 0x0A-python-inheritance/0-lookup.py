#!/usr/bin/python3
""" Defines a lookup function """


def lookup(obj):
    """ a function that returns the list of available attributes
        and methods of an object:

        Args:
            obj(obj): Parameter
    """
    return (dir(obj))
