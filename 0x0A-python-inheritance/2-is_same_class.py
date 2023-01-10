#!/usr/bin/python3
""" A script with a function that checks type """

def is_same_class(obj, a_class):
    """ returns True if the object is exactly an instance of the
         specified class ; otherwise False.

    Args:
        obj(obj): first parameter
        a_class (class or obj): Second Parameter
    """
    if isinstance(obj, a_class):
        return (True)
    else:
        return (False)
