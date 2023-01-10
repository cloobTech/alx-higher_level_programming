#!/usr/bin/python3
""" A script with a function that checks type """


def inherits_from(obj, a_class):
    """ returns True if the object is a subclass of a
         specified class ; otherwise False.

    Args:
        obj(obj): first parameter
        a_class (class or obj): Second Parameter
    """
    return issubclass(obj, a_class)
