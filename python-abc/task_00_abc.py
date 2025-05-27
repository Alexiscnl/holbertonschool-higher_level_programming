#!/usr/bin/python3
"""
This module defines an abstract base class 'Animal'
and its concrete subclasses 'Dog' and 'Cat'.
"""

from abc import ABC, abstractmethod


class Animal(ABC):
    """
    Abstract base class for animals.

    Subclasses must implement the `sound` method.
    """

    @abstractmethod
    def sound(self):
        """
        Abstract method that must be implemented
        by all subclasses to return the animal's sound.
        """
        pass


class Dog(Animal):
    """
    Concrete class that represents a Dog.
    Inherits from Animal and implements the sound method.
    """

    def sound(self):
        return "Bark"


class Cat(Animal):
    """
    Concrete class that represents a Cat.
    Inherits from Animal and implements the sound method.
    """

    def sound(self):
        return "Meow"
