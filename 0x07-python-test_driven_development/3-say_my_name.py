#!/usr/bin/python3
"""This module defines a function that prints out name."""


def say_my_name(first_name, last_name=""):
    """_summary_

    Args:
        first_name (str): First name.
        last_name (str, optional): Last name. Defaults to "".

    Raises:
        TypeError: if first_name is not a string, an empty string or is None.
        TypeError: if last_name is not a string.
    """
    if not isinstance(first_name, str) or first_name in ("", None):
        raise TypeError("first_name must be a string")
    if not isinstance(last_name, str):
        raise TypeError("last_name must be a string")
    print("My name is {} {}".format(first_name, last_name))
