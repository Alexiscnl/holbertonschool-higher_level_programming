#!/usr/bin/python3
"""
Module 8-rectangle

Defines a Rectangle class that inherits from BaseGeometry.
"""

BaseGeometry = __import__('7-base_geometry').BaseGeometry


class Rectangle(BaseGeometry):
    """Rectangle class inheriting from BaseGeometry."""

    def __init__(self, width, height):
        """Initialize a rectangle with width and height (validated)."""
        self.integer_validator("width", width)
        self.__width = width

        self.integer_validator("height", height)
        self.__height = height

    def __str__(self):
        """Return string representation: [Rectangle] <width>/<height>"""
        return f"[Rectangle] {self.__width}/{self.__height}"
