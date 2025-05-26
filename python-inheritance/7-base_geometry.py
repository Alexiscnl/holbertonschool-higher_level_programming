#!/usr/bin/python3
"""
Module 6-base_geometry

Defines a BaseGeometry class with an unimplemented area method and
a validator for integer values.
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
