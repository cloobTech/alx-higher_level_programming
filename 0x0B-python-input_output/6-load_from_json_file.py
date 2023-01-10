#!/usr/bin/python3
"""convert json to python object"""
import json


def load_from_json_file(filename):
    """convert json to python object
       Args:
        filename(json): parameter
    """
    with open(filename) as json_file:
        return (json.load(json_file))
