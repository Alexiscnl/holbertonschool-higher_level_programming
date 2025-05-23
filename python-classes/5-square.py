#!/usr/bin/python3
"""
Module 5-square
Defines a Square class with:
- private size attribute
- getter and setter with validation
- area computation
- print method to display the square with '#'
"""

class Square:
    """
    Represents a square with size validation,
    area computation, and visual representation.
    """

    def __init__(self, size=0):
        """
        Initializes a new Square instance.

        Args:
            size (int): The size of the square (default 0).
        """
        self.size = size

    def area(self):
        """
        Returns the current square area.

        Returns:
            int: area = size * size
        """
        return self.__size * self.__size

    @property
    def size(self):
        """Getter for size."""
        return self.__size

    @size.setter
    def size(self, value):
        """
        Setter for size with validation.

        Args:
            value (int): new size

        Raises:
            TypeError: if value is not int
            ValueError: if value is negative
        """
        if not isinstance(value, int):
            raise TypeError("size must be an integer")
        if value < 0:
            raise ValueError("size must be >= 0")
        self.__size = value

    def my_print(self):
        """
        Prints the square using '#' characters.

        If size is 0, prints an empty line.
        """
        if self.__size == 0:
            print()
        else:
            for _ in range(self.__size):
                print("#" * self.__size)
