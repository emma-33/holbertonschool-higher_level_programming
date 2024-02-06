#!/usr/bin/python3

"""

Defines a function to divide all elements of a matrix.

"""


def matrix_divided(matrix, div):
    """ Function that divides all elements of a matrix.
    Args:
        matrix: matrix of integers /floats
        div: number to divide the matrix with

    Returns:
        A new matrix with the results of the division of each elements.
    Raises:
        TypeError: If matrix isn't a list of lists of integers or floats
                   If matrix has different size rows
                   If div is not an integer or a float

        ZeroDivisionError: If div == 0
    """
    message = "matrix must be a matrix (list of lists) of integers/floats"

    if not isinstance(div, (int, float)):
        raise TypeError("div must be a number")

    if div == 0:
        raise ZeroDivisionError("division by zero")

    if not isinstance(matrix, list) or len(matrix) == 0 or len(matrix[0]) == 0:
        raise TypeError(message)

    for row in matrix:
        if not isinstance(row, list):
            raise TypeError(message)

        if len(row) != len(matrix[0]):
            raise TypeError("Each row of the matrix must have the same size")

        for element in row:
            if not isinstance(element, (int, float)):
                raise TypeError(message)

    return list(map(lambda x: list(map(lambda y:
                round(y / div, 2), x)), matrix))
