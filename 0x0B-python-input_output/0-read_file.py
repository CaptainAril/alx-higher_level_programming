#!/usr/bin/python3
"""This module defines a function that prints a text file contents on stdout.
"""


def read_file(filename=""):
    """Reads the text file (filename), and prints it to stdout.
    """

    with open(filename, encoding="utf-8") as f:
        for line in f:
            print(line, end='')
