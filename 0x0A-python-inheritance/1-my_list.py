#!/usr/bin/python3
"""This module defines a class MyList."""


class MyList(list):
    """Defines class MyList that inherits from list."""

    def print_sorted(self):
        """prints the list sorted in ascending order.
        """
        print(sorted(self))
    
