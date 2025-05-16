#!/usr/bin/python3
"""
Function to divide all elements of a matrix by a given number.
Checks input types and returns a new matrix with rounded values.
Raises errors for invalid inputs or division by zero.
"""
def matrix_divided(matrix, div):
    """
    Divides all elements of a matrix by div and returns a new matrix.
    """
    if not isinstance(div, (int, float)):
        raise TypeError("div must be a number")
    if div != div:
        raise ValueError("cannot convert float NaN to integer")
    if div == 0:
        raise ZeroDivisionError("division by zero")
    if not isinstance(matrix, list) or not matrix:
        raise TypeError(
            "matrix must be a matrix (list of lists) "
            "of integers/floats"
        )
    if not isinstance(matrix[0], list):
        raise TypeError(
            "matrix must be a matrix (list of lists) "
            "of integers/floats"
        )
    row_len = len(matrix[0])
    new_matrix = []
    for row in matrix:
        if not isinstance(row, list):
            raise TypeError(
                "matrix must be a matrix (list of lists) "
                "of integers/floats"
            )
        if len(row) != row_len:
            raise TypeError(
                "Each row of the matrix must have the same size"
            )
        new_row = []
        for i in row:
            if not isinstance(i, (int, float)):
                raise TypeError(
                    "matrix must be a matrix (list of lists) "
                    "of integers/floats"
                )
            if i != i:
                raise ValueError(
                    "cannot convert float NaN to integer"
                )
            if i == float('inf') or i == -float('inf'):
                raise OverflowError(
                    "cannot convert float infinity to integer"
                )
            new_row.append(round(i / div, 2))
        new_matrix.append(new_row)
    return new_matrix
