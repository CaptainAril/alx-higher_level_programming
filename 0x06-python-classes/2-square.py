#!/usr/bin/python3
"""Define a class Square."""


class Square:
    """A class for Square objects."""

    def __init__(self, size=0):
        """Initialize a class Square.

        Args:
            size (int): Size of the square object. Defaults to 0.

        Raises:
            TypeError: Exception raised if size is not of int type
            ValueError: Exception raised if size is less than 0
        """
        self.__size = size

        if isinstance(size, int) == False:
            raise TypeError("size must be an integer")
        if size < 0:
            raise ValueError("size must be >= 0")

