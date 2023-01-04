#!/usr/bin/python3

"""A script with a function that adds 2 integers."""


def add_integer(a, b=98):
    """function that adds 2 integers.
    Args:
        a (int or float): first parameter.
        b (int or float): second parameter.
    Raises:
        TypeError: If either a or b is a non-integer and non-float.
    Returns:
        an integer: the addition of a and b
    """

    if a is None:
        raise TypeError("add_integer() missing 1 required "
                        "positional argument: 'a'")
    if not isinstance(a, int) and not isinstance(a, float):
        raise TypeError("a must be an integer")
    if not isinstance(b, int) and not isinstance(b, float):
        raise TypeError("b must be an integer")
    return int(a + b)
