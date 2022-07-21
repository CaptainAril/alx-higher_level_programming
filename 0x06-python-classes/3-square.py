#!/usr/bin/python3
"""Define a class Square."""


class Square:
    """Creates a class Square"""

    def __init__(self, size=0):
        """Defines attributes for Square instance(s).

        Args:
            size (int): The size of the square. Defaults to 0.

        Raises:
            TypeError: Exception raised if size is not int type.
            ValueError: Exception raised if size is less than zero.
        """

        self.__size = size

        if not isinstance(size, int):
            raise TypeError("size must be an integer")
        if size < 0:
            raise ValueError("size must be >= 0")

    def area(self):
        """Computes the area of square.

        Returns:
            int: Area of the sqaure.
        """
        return self.__size ** 2
