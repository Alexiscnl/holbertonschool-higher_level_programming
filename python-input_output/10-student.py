#!/usr/bin/python3
"""
This module defines the Student class with support
for selective JSON serialization.
"""

class Student:
    """
    Represents a student with first name, last name, and age.
    """

    def __init__(self, first_name, last_name, age):
        """
        Initializes a Student instance.

        Args:
            first_name (str): The student's first name.
            last_name (str): The student's last name.
            age (int): The student's age.
        """
        self.first_name = first_name
        self.last_name = last_name
        self.age = age

    def to_json(self, attrs=None):
        """
        Retrieves a dictionary representation of the Student instance.
        If 'attrs' is a list of strings, only those attributes will be included.

        Args:
            attrs (list, optional): A list of attribute names to include.

        Returns:
            dict: A dictionary of attribute names and values.
        """
        if isinstance(attrs, list):
            new_dict = {}
            for name in attrs:
                if name in self.__dict__:
                    new_dict[name] = self.__dict__[name]
            return new_dict
        else:
            return self.__dict__
