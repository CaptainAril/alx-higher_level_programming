#!/usr/bin/python3
"""This module defines a function `from_json_string,
that returns a python object represented by a JSON string.
"""
import json


def from_json_string(my_str):
    """Returns a Python object represented by JSON string `my_str`."""
    obj = json.loads(my_str)
    return obj
