#!/usr/bin/python3
"""
Module 2-matrix_divided
Divides all elements of a matrix by a given number.
Each element is rounded to 2 decimal places.
"""


def matrix_divided(matrix, div):
    """
    Divides all elements of the matrix by `div`.
    Rounds each result to 2 decimal places.
    Returns a new matrix.

    Args:
        matrix (list of lists of int/float): The matrix to divide.
        div (int or float): The number to divide by.

    Raises:
        TypeError: If matrix is not a list of lists of integers/floats.
        TypeError: If each row of the matrix is not the same size.
        TypeError: If div is not a number.
        ZeroDivisionError: If div is zero.
    """

    if not isinstance(matrix, list) or not all(isinstance(row, list)
                                               for row in matrix):
        raise TypeError("matrix must be a matrix (list of lists)"
                        " of integers/floats")
    for row in matrix:
        for x in row:
            if not isinstance(x, (int, float)):
                raise TypeError("matrix must be a matrix (list of lists)"
                                " of integers/floats")

    lenght = len(matrix[0])
    for row in matrix:
        if len(row) != lenght:
            raise TypeError("Each row of the matrix must have the same size")

    if not isinstance(div, (int, float)):
        raise TypeError("div must be a number")
    if div == 0:
        raise ZeroDivisionError("division by zero")

    new_matrix = []
    for row in matrix:
        new_row = []
        for el in row:
            new_row.append(round(el / div, 2))
        new_matrix.append(new_row)
    return new_matrix
