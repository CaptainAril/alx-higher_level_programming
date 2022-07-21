#!/usr/bin/python3
"""Defines a class Square."""


class Square:
    """Creates a class for Squares."""

    def __init__(self, size=0):
        """Defines the attributes for Square instance(s).

        Args:
            size (int): Size of the Square. Defaults to 0.
        """
        self.__size = size

    @property
    def size(self):
        """Gets the size of the square."""
        return self.__size

    @size.setter
    def size(self, value):
        """Sets the size of the square.

        Args:
            value (int): The size of the square.

        Raises:
            TypeError: If size is not an int type.
            ValueError: If size is less than zero.
        """

        if not isinstance(value, int):
            raise TypeError("size must be integer")
        if value < 0:
            raise ValueError("size must be >= 0")
        self.__size = value

    def area(self):
        """Returns the Area of the square."""
        return (self.__size ** 2)