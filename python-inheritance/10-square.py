#!/usr/bin/python3
"""
Module 10-square

Defines a Square class that inherits from Rectangle.
"""

Rectangle = __import__('9-rectangle').Rectangle


class Square(Rectangle):
    """
    Square class that inherits from Rectangle.

    Initializes a square with a given size, which is validated
    as a positive integer and used as both width and height.
    """

    def __init__(self, size):
        """
        Initializes the square with validated size.

        Args:
            size (int): The size of the square (must be a positive integer).
        """
        self.integer_validator("size", size)
        super().__init__(size, size)
        self.__size = size

    def area(self):
        """
        Returns the area of the square.

        Returns:
            int: The area computed as size * size.
        """
        return self._Rectangle__width * self._Rectangle__height
