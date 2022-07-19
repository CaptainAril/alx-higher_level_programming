#!/usr/bin/python3
import sys


def safe_function(fct, *args):
    try:
        result = fct(*args)
        return result
    except Exception as ve:
        sys.stderr.write("Exception: {}{}".format(ve, '\n'))
