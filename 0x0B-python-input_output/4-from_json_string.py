#!/usr/bin/python3
""" convert json to python object """
import json


def from_json_string(my_str):
    """ convert json to python object
    Args:
        my_str(str): parameter
    """
    py_obj = json.loads(my_str)
    return (py_obj)
