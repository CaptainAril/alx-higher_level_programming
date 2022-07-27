#!/usr/bin/python3
"""Defines a class Rectangle."""


class Rectangle:
    """Represents a class Rectangle."""
    def __init__(self, width=0, height=0):
        """Defines the attributes for class Rectangle instance(s).

        Args:
            width (int, optional): width of Rectangle. Defaults to 0.
            height (int, optional): height of rectangle. Defaults to 0.
        """
        self.width = width
        self.height = height

    @property
    def width(self):
        """Gets the width of Rectangle."""
        return self.__width

    @width.setter
    def width(self, value):
        """Sets the width of Rectangle.

        Args:
            value (int): value passed for width of Rectangle.

        Raises:
            TypeError: if width passed is not an int type.
            ValueError: if width passed is less than 0.
        """
        if not isinstance(value, int):
            raise TypeError("width must be an integer")
        if value < 0:
            raise ValueError("width must be >= 0")
        self.__width = value

    @property
    def height(self):
        """Gets the height of Rectangle."""
        return self.__height

    @height.setter
    def height(self, value):
        """Sets the height of Rectangle.

        Args:
            value (int): value passed for height of Rectangle

        Raises:
            TypeError: if height passed is not an int type
            ValueError: if height passed is less than 0.
        """
        if not isinstance(value, int):
            raise TypeError("height must be an integer")
        if value < 0:
            raise ValueError("height must be >= 0")
        self.__height = value

    def area(self):
        """Returns the area of Rectangle."""
        area = self.__width * self.__height
        return area

    def perimeter(self):
        """Returns the perimeter of rectangle."""
        if self.__height == 0 or self.__width == 0:
            perimeter = 0
        else:
            perimeter = 2 * (self.__height + self.__width)
        return perimeter

    def __str__(self):
        """Returns the string representation of Rectangle."""
        rect = ""
        if self.__height == 0 or self.__width == 0:
            return ""
        for i in range(self.__height):
            rect += "#" * self.__width
            if i != self.__height - 1:
                rect += "\n"
        return rect
