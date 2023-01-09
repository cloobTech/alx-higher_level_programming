#!/usr/bin/python3

def lookup(obj):
    """ a function that returns the list of available attributes
        and methods of an object:

        Args:
            obj(obj): Parameter
    """
    return (dir(obj))
