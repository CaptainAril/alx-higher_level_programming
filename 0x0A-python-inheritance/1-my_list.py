#!/usr/bin/python3
"""This module defines a class MyList."""


class MyList(list):
    """Defines class MyList that inherits from list."""

    def print_sorted(self):
        """prints the list sorted in ascending order.
        """
        sort_list = self.copy()
        sort_list.sort()
        print(sort_list)
