#!/usr/bin/python3

class Square:
    """
    A class that defines a square with size and position.
    """

    def __init__(self, size=0, position=(0, 0)):
        """
        Initialize a Square instance with optional size and position.

        Args:
            size (int): The size of the square (length of each side).
            position (tuple): A tuple of 2 positive integers for offset (x, y).
        """
        if not isinstance(size, int):
            raise TypeError("size must be an integer")
        if size < 0:
            raise ValueError("size must be >= 0")
        self.__size = size
        self.__position = position

    @property
    def size(self):
        """Getter for the private attribute __size."""
        return self.__size

    @size.setter
    def size(self, value):
        """
        Setter for the size attribute, with validation.

        Args:
            value (int): The new size of the square.

        Raises:
            TypeError: If value is not an integer.
            ValueError: If value is negative.
        """
        if not isinstance(value, int):
            raise TypeError("size must be an integer")
        if value < 0:
            raise ValueError("size must be >= 0")
        self.__size = value

    @property
    def position(self):
        """Getter for the private attribute __position."""
        return self.__position

    @position.setter
    def position(self, value):
        """
        Setter for the position attribute, with validation.

        Args:
            value (tuple): A tuple of 2 positive integers (x, y).

        Raises:
            TypeError: If value is not a valid tuple.
        """
        if (not isinstance(value, tuple) or
            len(value) != 2 or
            not all(isinstance(num, int) for num in value) or
            not all(num >= 0 for num in value)):
            raise TypeError("position must be a tuple of 2 positive integers")
        self.__position = value

    def area(self):
        """
        Computes and returns the area of the square.

        Returns:
            int: Area = size * size
        """
        return self.__size ** 2

    def my_print(self):
        """
        Prints the square using '#' characters to stdout,
        respecting the size and position offset.
        """
        if self.__size == 0:
            print()
            return

        for _ in range(self.__position[1]):
            print()

        for _ in range(self.__size):
            print(" " * self.__position[0] + "#" * self.__size)
