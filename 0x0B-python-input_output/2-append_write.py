#!/usr/bin/python3
""" A module containing a function tgat writes string to a file"""


def append_write(filename="", text=""):
    """  a function that appends a string at the end of a text file (UTF8)
    and returns the number of characters added
    Args:
        filename(str): filename or source file
        text(str): Text string
    """
    with open(filename, 'a') as append_file:
        file_len = append_file.write(text)
        return (file_len)
