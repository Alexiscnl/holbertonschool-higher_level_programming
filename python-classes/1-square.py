#!/usr/bin/python3
"""
Module 1-square
Defines a Square class with a private attribute size
"""


class Square:
    """
    Class that represents a square.
    """

    def __init__(self, size):
        """
        Initializes the square with a given size.

        Args:
            size (int): The size of the square (no type or value check here).

        Note:
            No validation is performed in this version.
            Type and value checks will be introduced in the next tasks.
        """
        self.__size = size
