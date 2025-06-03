#!/usr/bin/python3
"""
This module defines a Student class that supports serialization
to and from JSON-compatible dictionaries.

It provides:
- Attribute filtering when converting to dict
- Dynamic update from dictionary using reload_from_json
"""


class Student:
    """
    Represents a student with first name, last name, and age.

    Methods:
        to_json(attrs=None):
        Returns a dictionary representation of the instance.
        reload_from_json(json):
        Replaces instance attributes using a dictionary.
    """

    def __init__(self, first_name, last_name, age):
        """
        Initialize a Student instance.

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
        Returns a dictionary representation of the instance.

        If `attrs` is a list of strings, only those attributes
        are included if they exist.

        Args:
            attrs (list, optional): List of attribute names to include.

        Returns:
            dict: Dictionary of selected or all attributes.
        """
        if isinstance(attrs, list):
            empty_dict = {}
            for names in attrs:
                if names in self.__dict__:
                    empty_dict[names] = self.__dict__[names]
            return empty_dict
        else:
            return self.__dict__

    def reload_from_json(self, json):
        """
        Replace all attributes of the Student instance using a dictionary.

        Args:
            json (dict): Dictionary with keys matching public attribute names.
        """
        for key, value in json.items():
            setattr(self, key, value)
