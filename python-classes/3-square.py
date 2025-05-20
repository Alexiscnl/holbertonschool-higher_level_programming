#!/usr/bin/python3
"""
Module 3-square
Defines a Square class with:
- a private instance attribute 'size'
- input validation in the constructor
- a public method to compute the area
"""


class Square:
    """
    Represents a square with size validation and area computation.
    """

    def __init__(self, size=0):
        """
        Initializes a new Square instance.

        Args:
            size (int): The size of the square (default is 0).

        Raises:
            TypeError: If size is not an integer.
            ValueError: If size is less than 0.
        """
        if not isinstance(size, int):
            raise TypeError("size must be an integer")
        if size < 0:
            raise ValueError("size must be >= 0")
        self.__size = size  # Private size attribute

    def area(self):
        """
        Computes and returns the area of the square.

        Returns:
            int: The current square area (size * size).
        """
        return self.__size * self.__size
