#!/usr/bin/python3
""" convert string to json """
import json


def to_json_string(my_obj):
    """ convert string to json
    Args:
        obj(obj): argument to be converted
    """
    return json.dumps(my_obj)
