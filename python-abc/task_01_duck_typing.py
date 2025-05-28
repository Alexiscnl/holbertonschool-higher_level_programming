#!/usr/bin/python3
"""
Module: task_01_duck_typing

This module defines an abstract base class `Shape` with two abstract
methods: `area()` and `perimeter()`.
It also implements two concrete shape classes: `Circle` and `Rectangle`,
each providing specific logic
to calculate area and perimeter.

Additionally, it defines a utility function `shape_info()` that demonstrates
duck typing by operating
on any object that implements the expected interface, regardless of its actual
type.
"""

from abc import ABC, abstractmethod
import math


class Shape(ABC):
    """
    Abstract class defining the interface for all shapes.
    Subclasses must implement the `area` and `perimeter` methods.
    """

    @abstractmethod
    def area(self):
        """
        Compute and return the area of the shape.
        Must be implemented by all subclasses.
        """
        pass

    @abstractmethod
    def perimeter(self):
        """
        Compute and return the perimeter of the shape.
        Must be implemented by all subclasses.
        """
        pass


class Circle(Shape):
    """
    Circle class implementing the Shape interface.

    Attributes:
        radius (float): The radius of the circle.
    """

    def __init__(self, radius):
        """
        Initialize a Circle instance with the given radius.

        Args:
            radius (float): The radius of the circle.
        """
        self.radius = radius

    def area(self):
        """
        Calculate and return the area of the circle.

        Returns:
            float: The area of the circle.
        """
        return math.pi * self.radius ** 2

    def perimeter(self):
        """
        Calculate and return the perimeter (circumference) of the circle.

        Returns:
            float: The perimeter of the circle.
        """
        return 2 * math.pi * self.radius


class Rectangle(Shape):
    """
    Rectangle class implementing the Shape interface.

    Attributes:
        width (float): The width of the rectangle.
        height (float): The height of the rectangle.
    """

    def __init__(self, width, height):
        """
        Initialize a Rectangle instance with the given width and height.

        Args:
            width (float): The width of the rectangle.
            height (float): The height of the rectangle.
        """
        if not isinstance(width, (int, float)):
            raise TypeError("width must be a number")
        if not isinstance(height, (int, float)):
            raise TypeError("height must be a number")
        self.width = width
        self.height = height

    def area(self):
        """
        Calculate and return the area of the rectangle.

        Returns:
            float: The area of the rectangle.
        """
        return self.width * self.height

    def perimeter(self):
        """
        Calculate and return the perimeter of the rectangle.

        Returns:
            float: The perimeter of the rectangle.
        """
        return 2 * (self.width + self.height)


def shape_info(obj):
    """
    Display the area and perimeter of any shape object
    that implements the area() and perimeter() methods.

    This function uses duck typing and does not check the object's class.

    Args:
        obj (Shape): Any object implementing area() and perimeter().
    """
    area = obj.area()
    perimeter = obj.perimeter()
    print("Area:", area)
    print("Perimeter:", perimeter)
