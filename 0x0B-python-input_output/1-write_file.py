#!/usr/bin/python3
""" A module containing a function tgat writes string to a file"""


def write_file(filename="", text=""):
    """ a function that writes a string to a text file (UTF8) and returns
    the number of characters written
    Args:
        filename(str): filename or source file
        text(str): Text string
    """
    with open(filename, 'w') as write_file:
        file_len = write_file.write(text)
        return (file_len)
