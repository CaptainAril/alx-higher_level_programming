#!/usr/bin/python3
"""This module defines a function `to_json_string`,
that returns the JSON representaion of an object.
"""
import json


def to_json_string(my_obj):
    """Return the JSON representation of `my_obj`."""
    json_obj = json.dumps(my_obj)
    return json_obj
