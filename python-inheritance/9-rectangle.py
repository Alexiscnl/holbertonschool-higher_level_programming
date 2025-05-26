#!/usr/bin/python3
"""
Module 9-rectangle

Defines a Rectangle class that inherits from BaseGeometry.
"""


class BaseGeometry:
    """
    Base class for geometry-related calculations.

    Methods:
        area(self): Raises an Exception to indicate it is not yet implemented.
        integer_validator(self, name, value): Validates that 'value'
          is a positive integer.
    """

    def area(self):
        """
        Raises an Exception indicating that the area method is not implemented.
        """
        raise Exception("area() is not implemented")

    def integer_validator(self, name, value):
        """
        Validates that the given value is an integer greater than 0.

        Args:
            name (str): The name of the parameter (for error messages).
            value (int): The value to validate.

        Raises:
            TypeError: If value is not an integer.
            ValueError: If value is less than or equal to 0.
        """
        if type(value) is not int:
            raise TypeError(f"{name} must be an integer")
        if value <= 0:
            raise ValueError(f"{name} must be greater than 0")


class Rectangle(BaseGeometry):
    """
    Rectangle class that inherits from BaseGeometry.

    Attributes:
        __width (int): The width of the rectangle.
        __height (int): The height of the rectangle.

    Methods:
        area(): Returns the area of the rectangle.
        __str__(): Returns the string representation of the rectangle.
    """

    def __init__(self, width, height):
        """
        Initializes a rectangle with validated private width and height.

        Args:
            width (int): The width of the rectangle.
            height (int): The height of the rectangle.
        """
        self.integer_validator("width", width)
        self.__width = width

        self.integer_validator("height", height)
        self.__height = height

    def area(self):
        """
        Returns the area of the rectangle.

        Returns:
            int: The area (width * height).
        """
        return self.__width * self.__height

    def __str__(self):
        """
        Returns a string representation of the rectangle.

        Returns:
            str: The rectangle formatted as [Rectangle] <width>/<height>
        """
        return f"[Rectangle] {self.__width}/{self.__height}"
