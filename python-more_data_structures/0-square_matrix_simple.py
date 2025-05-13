#!/usr/bin/python3
def square_matrix_simple(matrix=[]):
    new_matrix = []
    for col in matrix:
        new_col = []
        for value in col:
            new_col.append(value ** 2)
        new_matrix.append(new_col)
    return new_matrix
