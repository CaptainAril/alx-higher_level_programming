#!/usr/bin/python3
"""This module defines a function `write_file(filename="", text="")`,
that writes a string to text file and returns the number of characters written.
"""


def write_file(filename="", text=""):
    """Writes the text string into the textfile `filename`,
    and returns the number of characters written.
    """
    with open(filename, 'w', encoding="utf-8") as f:
        charNum = f.write(text)
        return charNum
