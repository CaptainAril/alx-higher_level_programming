#!/usr/bin/python3
"""This module defines a function `load_from_json_file`,
that creates an Object from a JSON file.
"""
import json
 

def load_from_json_file(filename):
    """Creates an Object from `filename`."""
    with open(filename, encoding="utf-8") as f:
        return json.load(f)
