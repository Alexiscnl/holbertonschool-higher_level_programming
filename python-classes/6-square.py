#!/usr/bin/python3
"""
This module defines a Square class used to represent a square shape.

Classes:
    Square: Represents a square with a private size attribute.
"""


class Square:
    """
    Represents a square.

    Attributes:
        __size (int): The size of the square (private).
    """
    def __init__(self, size=0, position=(0, 0)):
        """
        Initializes a Square instance with a given size.

        Args:
            size (int): The size of the square.
        """

        if not isinstance(size, int):
            raise TypeError("size must be an integer")
        elif size < 0:
            raise ValueError("size must be >= 0")
        self.__size = size
        self.position = position

    @property
    def size(self):
        """Get the current size of the square."""
        return self.__size

    @size.setter
    def size(self, value):
        """
        Set the size of the square.
        Args:
        value (int): New size, must be integer >= 0.
        Raises:
        TypeError: If value is not an integer.
        ValueError: If value is negative.
        """

        if not isinstance(value, int):
            raise TypeError("size must be an integer")
        elif value < 0:
            raise ValueError("size must be >= 0")
        self.__size = value

    @property
    def position(self):
        return self.__position

    @position.setter
    def position(self, value):
        if not isinstance(value, tuple) or len(value) != 2:
            raise TypeError("position must be a tuple of 2 positive integers")
        x, y = value
        if not isinstance(x, int) or not isinstance(y, int):
            raise TypeError("position must be a tuple of 2 positive integers")
        if x < 0 or y < 0:
            raise TypeError("position must be a tuple of 2 positive integers")
        else:
            self.__position = value

    def area(self):
        """
        Computes and returns the area of the square.

        Returns:
            int: The current square’s area, computed as size squared.
        """
        return self.__size ** 2

    def my_print(self):
        """
        Print the square with the '#' character.

        Prints an empty line if size is 0. Applies vertical and horizontal
        offsets based on position.
        """
        if self.__size == 0:
            print()
            return

        for _ in range(self.__position[1]):
            print()
        for _ in range(self.__size):
            print(" " * self.__position[0] + "#" * self.__size)
