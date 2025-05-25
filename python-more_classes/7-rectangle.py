#!/usr/bin/python3
"""
This module provides the Rectangle class.

It supports computing area, perimeter, and text-based rendering.
"""


class Rectangle:
    """Representation of a rectangle.

    Attributes:
        number_of_instances (int): Tracks the number of Rectangle instances.
        print_symbol (any): Symbol used for string representation.
        width (int): Width of the rectangle (must be >= 0).
        height (int): Height of the rectangle (must be >= 0).
    """

    number_of_instances = 0
    print_symbol = "#"

    def __init__(self, width=0, height=0):
        """Initialize a new Rectangle and increment the instance counter.

        Args:
            width (int, optional): Initial width. Defaults to 0.
            height (int, optional): Initial height. Defaults to 0.

        Raises:
            TypeError: If `width` or `height` is not an int.
            ValueError: If `width` or `height` is < 0.
        """
        self.width = width
        self.height = height
        type(self).number_of_instances += 1

    @property
    def width(self):
        """int: The width of the rectangle.

        Must be an integer greater than or equal to 0.
        """
        return self.__width

    @width.setter
    def width(self, value):
        """Set the width of the rectangle.

        Args:
            value (int): The new width.

        Raises:
            TypeError: If `value` is not an int.
            ValueError: If `value` is < 0.
        """
        if not isinstance(value, int):
            raise TypeError("width must be an integer")
        if value < 0:
            raise ValueError("width must be >= 0")
        self.__width = value

    @property
    def height(self):
        """int: The height of the rectangle.

        Must be an integer greater than or equal to 0.
        """
        return self.__height

    @height.setter
    def height(self, value):
        """Set the height of the rectangle.

        Args:
            value (int): The new height.

        Raises:
            TypeError: If `value` is not an int.
            ValueError: If `value` is < 0.
        """
        if not isinstance(value, int):
            raise TypeError("height must be an integer")
        if value < 0:
            raise ValueError("height must be >= 0")
        self.__height = value

    def area(self):
        """Compute the area of the rectangle.

        Returns:
            int: The area, calculated as width * height.
        """
        return self.__width * self.__height

    def perimeter(self):
        """Compute the perimeter of the rectangle.

        Returns:
            int: The perimeter, calculated as 2 * (width + height).
                Returns 0 if either width or height is 0.
        """
        if self.__width == 0 or self.__height == 0:
            return 0
        return 2 * (self.__width + self.__height)

    def __str__(self):
        """Generate the string representation using `print_symbol`.

        Returns:
            str: Multiline string of `print_symbol` forming the rectangle
                dimensions, or an empty string if width or height is 0.
        """
        if self.__width == 0 or self.__height == 0:
            return ""
        line = str(self.print_symbol) * self.__width
        return "\n".join(line for _ in range(self.__height))

    def __repr__(self):
        """Generate an official string representation.

        Returns:
        str: A string that can be passed to eval() to recreate this instance.
        """
        return f"Rectangle({self.__idth}, {self.__height})"

    def __del__(self):
        """Print a message upon deletion and decrement the instance counter."""
        print("Bye rectangle...")
        type(self).number_of_instances -= 1
