#!/usr/bin/python3
"""
Module: task_01_duck_typing

Defines:
- an abstract base class `Shape` with abstract methods `area()` and `perimeter()`
- two concrete classes `Circle` and `Rectangle` that implement these methods
- a function `shape_info()` that uses duck typing to display shape metrics
"""

from abc import ABC, abstractmethod
import math


class Shape(ABC):
    """
    Abstract base class for shapes.
    Requires implementing area and perimeter methods.
    """

    @abstractmethod
    def area(self):
        """Compute and return the area."""
        pass

    @abstractmethod
    def perimeter(self):
        """Compute and return the perimeter."""
        pass


class Circle(Shape):
    """
    Circle shape implementing the Shape interface.
    """

    def __init__(self, radius):
        """
        Initialize the circle with a radius.

        Args:
            radius (float): radius of the circle

        Raises:
            TypeError: if radius is not a number
        """
        self.radius = radius

    def area(self):
        """Return area of the circle."""
        return math.pi * abs(self.radius) ** 2

    def perimeter(self):
        """Return perimeter (circumference) of the circle."""
        return 2 * math.pi * abs(self.radius)


class Rectangle(Shape):
    """
    Rectangle shape implementing the Shape interface.
    """

    def __init__(self, width, height):
        """
        Initialize the rectangle with width and height.

        Args:
            width (float): width of the rectangle
            height (float): height of the rectangle

        Raises:
            TypeError: if width or height is not a number
        """
        self.width = width
        self.height = height

    def area(self):
        """Return area of the rectangle."""
        return self.width * self.height

    def perimeter(self):
        """Return perimeter of the rectangle."""
        return 2 * (self.width + self.height)

def shape_info(obj):
    """
    Display the area and perimeter of any shape object
    that implements area() and perimeter().
    """
    print("Area:", obj.area())
    print("Perimeter:", obj.perimeter())
