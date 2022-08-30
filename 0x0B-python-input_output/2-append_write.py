#!/usr/bin/python3
"""This module a function `append_write(filename="", text="")`,
that appends a string to a text file and returns number of characters added.
"""


def append_write(filename="", text=""):
    """Appends string (text) at the end of file (filename),
    and returns the number of characters added.
    """
    with open(filename, 'a', encoding="utf-8") as f:
        numChar = f.write(text)
        return numChar
