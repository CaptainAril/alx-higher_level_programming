#!/usr/bin/python3
import sys


def safe_print_integer_err(value):
    try:
        print("{:d}".format(value))
        return True
    except Exception as ve:
        sys.stderr.write("Exception: {}{}".format(ve, '\n'))
        return False
