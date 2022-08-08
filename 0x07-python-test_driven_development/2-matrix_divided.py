#!/usr/bin/python3
"""This module defines a matrix divisor function."""


def matrix_divided(matrix, div):
    """A function that divides all elements of a matrix,
    and returns a new matrix.

    Args:
        matrix (list of lists): a matrix of integers or floats.
        div (int or float): divisor.
    """

    if not isinstance(div, (int, float)) or div == float('inf')\
            or div == -float('inf') or div != div:
        raise TypeError("div must be a number")
    if div == 0:
        raise ZeroDivisionError("division by zero")

    div_matrix = []
    index = 0
    if matrix in ([], None):
        raise TypeError("matrix must be a matrix (list of lists)" +
                        " of integers/floats")
    for i in matrix:
        if not isinstance(i, list):
            raise TypeError("matrix must be a matrix (list of lists)" +
                            " of integers/floats")
        row1 = len(matrix[0])
        if len(i) != row1:
            raise TypeError("Each row of the matrix must have the same size")
        div_matrix.append([])
        for x in matrix[index]:
            if not isinstance(x, (int, float)):
                raise TypeError("matrix must be a matrix (list of lists)" +
                                " of integers/floats")
            div_matrix[index].append(float('%.2f' % (x/div)))
        index += 1
    return div_matrix
