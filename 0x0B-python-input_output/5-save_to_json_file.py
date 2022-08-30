#!/usr/bin/python3
"""This module defines a function `save_to_json_file`,
that writes an object to a text file, usin JSON representation.
"""
import json


def save_to_json_file(my_obj, filename):
    """Writes an `my_obj` to `filename`, using a JSON representation.
    """
    with open(filename, 'w', encoding="utf-8") as f:
        json.dump(my_obj, f)
