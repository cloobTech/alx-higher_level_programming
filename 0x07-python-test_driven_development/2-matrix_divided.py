#!/usr/bin/python3

""" Module containing function that divides all elements of a matrix.
"""


def matrix_divided(matrix, div):
    """function that divides all elements of a matrix.
    Args:
        matrix(list): list of lists of integer or floats
        div(int or float): All elements of the matrix should
        be divided by div

    Raises:
        TypeError: TypeError exception with the message Each
        row of the matrix must have the same size
        ZeroDivisionError: division by zero
        TypeError: div must be a number

    Return:
        a new matrix
    """
    new_matrix = []
    if (not all(isinstance(item, list) for item in matrix) or
            not isinstance(matrix, list) or matrix == []):
        raise TypeError("matrix must be a matrix (list of lists)"
                        " of integers/floats")
    else:
        for item in matrix:
            if not all(isinstance(i, (int, float)) for i in item):
                raise TypeError("matrix must be a matrix (list of lists)"
                                " of integers/floats")
    if (matrix and div) is None:
        raise TypeError("matrix_divided() missing 2 required positional arguments: 'matrix' and 'div'")
    list_len = len(matrix[0])
    for item in matrix:
        if len(item) != list_len:
            raise TypeError("Each row of the matrix must have the same size")
    if not isinstance(div, (int, float)):
        raise TypeError("div must be a number")
    if div == 0:
        raise ZeroDivisionError("division by zero")
    if div == None:
        raise TypeError("matrix_divided() missing 1 required positional argument")

    for item in matrix:
        item = [round(num/div, 2) for num in item]
        new_matrix.append(item)
    return (new_matrix)
