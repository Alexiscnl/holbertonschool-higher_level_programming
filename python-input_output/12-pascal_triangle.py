#!/usr/bin/python3
"""
This module provides a function to generate Pascal's Triangle.

The function `pascal_triangle(n)` returns a list of lists of integers,
representing the first `n` rows of Pascal's Triangle.
"""


def pascal_triangle(n):
    """
    Generate Pascal's Triangle up to the nth row.

    Args:
        n (int): The number of rows to generate.

    Returns:
        list: A list of lists, where each inner list represents
              a row of Pascal's Triangle.

    Example:
        >>> pascal_triangle(4)
        [[1], [1, 1], [1, 2, 1], [1, 3, 3, 1]]
    """
    if n <= 0:
        return []
    else:
        triangle = [[1]]
        for i in range(1, n):
            prev_row = triangle[-1]
            new_row = [1]
            for j in range(1, len(prev_row)):
                new_value = prev_row[j - 1] + prev_row[j]
                new_row.append(new_value)

            new_row.append(1)
            triangle.append(new_row)

        return triangle
