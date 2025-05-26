#!/usr/bin/python3
"""
Module 6-base_geometry

Defines a BaseGeometry class with an unimplemented area method.
"""


class BaseGeometry:
    """
    Base class for geometry-related calculations.

    Methods:
        area(self): raises an Exception to indicate it is not yet implemented.
    """

    def area(self):
        """
        Raises an Exception indicating that the area method is not implemented.
        """
        raise Exception("area() is not implemented")
