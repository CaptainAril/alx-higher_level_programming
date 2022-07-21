#!/usr/bin/python3
"""Defines a class Square."""


class Square:
    """Creates a class for Squares."""

    def __init__(self, size=0, position=(0, 0)):
        """Defines the attributes for Square instance(s).

        Args:
            size (int): Size of the square. Defaults to 0.
            position (tuple): Position of the square. Defaults to (0, 0).
        """
        self.__size = size
        self.__position = position

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

    @property
    def position(self):
        """Gets the position value."""
        return self.__position

    @position.setter
    def position(self, value):
        """Sets the position of the square

        Args:
            value (tuple): The position of square

        Raises:
            TypeError: if position is not a tuple of two integers.
        """
        if (not isinstance(value, tuple) or len(value) != 2 or
                not all(isinstance(val, int) for val in value) or
                not all(val >= 0 for val in value)):
            raise TypeError("position must be a tuple of 2 positive integers")

    def area(self):
        """Returns the Area of the square."""
        return self.__size ** 2

    def my_print(self):
        """Prints the square with '#' character."""
        if self.__size == 0:
            print()
        else:
            [print("") for i in range(0, self.__position[1])]
        for i in range(0, self.__size):
            [print(" ", end="") for j in range(0, self.__position[0])]
            [print("#", end="") for k in range(0, self.__size)]
            print("")
