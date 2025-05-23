#!/usr/bin/python3
"""
Module 6-square
Defines a Square class with:
- private size and position attributes
- getters and setters with validation
- area computation
- visual representation using '#' and respecting position
"""

class Square:
    """
    Represents a square with size and position attributes,
    and provides methods for area computation and visual output.
    """

    def __init__(self, size=0, position=(0, 0)):
        """
        Initializes a new Square instance.

        Args:
            size (int): The size of the square (default is 0).
            position (tuple): Tuple of 2 positive integers (default is (0, 0)).

        Raises:
            TypeError or ValueError: If size or position are invalid.
        """
        self.size = size
        self.position = position

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

    @property
    def position(self):
        """Getter for position."""
        return self.__position

    @position.setter
    def position(self, value):
        """
        Setter for position with validation.

        Args:
            value (tuple): a tuple of 2 positive integers

        Raises:
            TypeError: if value is not a tuple of 2 positive integers
        """
        if (not isinstance(value, tuple) or
            len(value) != 2 or
            not all(isinstance(num, int) for num in value) or
            not all(num >= 0 for num in value)):
            raise TypeError("position must be a tuple of 2 positive integers")
        self.__position = value

    def my_print(self):
        """
        Prints the square using '#' characters, respecting the position.

        If size is 0, prints an empty line.
        """
        if self.__size == 0:
            print()
            return

        for _ in range(self.__position[1]):
            print()

        for _ in range(self.__size):
            print(" " * self.__position[0] + "#" * self.__size)

