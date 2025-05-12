#!/usr/bin/python3

def print_matrix_integer(matrix=[[]]):

    for column in matrix:
        for i in range(len(column)):
            if i == len(column) - 1:
                print("{:d}".format(column[i]), end="")
            else:
                print("{:d}".format(column[i]), end=" ")
        print()
