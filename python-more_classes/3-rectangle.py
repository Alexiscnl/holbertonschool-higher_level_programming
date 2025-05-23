#!/usr/bin/python3
"""
This module provides the Rectangle class.

It supports computing area, perimeter, and text-based rendering.
"""

class Rectangle:
    """
    Representation of a rectangle.

    Attributes:
        width (int): Rectangle width (must be >= 0).
        height (int): Rectangle height (must be >= 0).
    """

    def __init__(self, width=0, height=0):
        """
        Initialize a new Rectangle instance.

        Args:
            width (int): The width of the rectangle (default is 0).
            height (int): The height of the rectangle (default is 0).
        """
        self.width = width
        self.height = height

    @property
    def width(self):
        """
        Getter for the width attribute.

        Returns:
            int: The width of the rectangle.
        """
        return self.__width

    @width.setter
    def width(self, value):
        """
        Setter for the width attribute with validation.

        Args:
            value (int): New value for width.

        Raises:
            TypeError: If value is not an integer.
            ValueError: If value is less than 0.
        """
        if not isinstance(value, int):
            raise TypeError("width must be an integer")
        elif value < 0:
            raise ValueError("width must be >= 0")
        self.__width = value

    @property
    def height(self):
        """
        Getter for the height attribute.

        Returns:
            int: The height of the rectangle.
        """
        return self.__height

    @height.setter
    def height(self, value):
        """
        Setter for the height attribute with validation.

        Args:
            value (int): New value for height.

        Raises:
            TypeError: If value is not an integer.
            ValueError: If value is less than 0.
        """
        if not isinstance(value, int):
            raise TypeError("height must be an integer")
        elif value < 0:
            raise ValueError("height must be >= 0")
        self.__height = value

    def area(self):
        """
        Calculate and return the area of the rectangle.

        Returns:
            int: The area (width * height).
        """
        return self.__height * self.__width

    def perimeter(self):
        """
        Calculate and return the perimeter of the rectangle.

        Returns:
            int: The perimeter (2 * width + 2 * height),
                 or 0 if either width or height is 0.
        """
        if self.__width == 0 or self.__height == 0:
            return 0
        else:
            return (self.__height * 2) + (self.__width * 2)

    def __str__(self):
        """
        Return a string representation of the rectangle
        using '#' characters.

        Returns:
            str: Rectangle drawn using '#' characters, or
                 an empty string if width or height is 0.
        """
        if self.__width == 0 or self.__height == 0:
            return ""
        else:
            lines = []
            for _ in range(self.__height):
                lines.append("#" * self.__width)
            return "\n".join(lines)
