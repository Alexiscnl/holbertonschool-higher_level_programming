#!/usr/bin/python3
"""
Module 11-square

Defines a Square class that inherits from Rectangle,
and overrides __str__ to provide a custom string representation.
"""

Rectangle = __import__('9-rectangle').Rectangle


class Square(Rectangle):
    """
    Square class that inherits from Rectangle.
    """

    def __init__(self, size):
        """
        Initializes a square using the rectangle logic,
        by passing size as both width and height.

        Args:
            size (int): Size of the square (must be a positive integer).
        """
        self.integer_validator("size", size)
        super().__init__(size, size)

    def area(self):
        """
        Returns the area of the square.

        Returns:
            int: The area computed as size * size.
        """
        return self._Rectangle__width * self._Rectangle__height

    def __str__(self):
        """
        Returns the string representation of the square.

        Returns:
            str: The square formatted as [Square] <size>/<size>
        """
        return f"[Square] {self._Rectangle__width}/{self._Rectangle__height}"
