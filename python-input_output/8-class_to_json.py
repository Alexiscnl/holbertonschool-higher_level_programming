#!/usr/bin/python3
"""
This module provides a function that returns the
dictionary representation of an object's attributes
for JSON serialization.
"""


def class_to_json(obj):
    """
    Returns a dictionary description of a simple Python object
    (containing only serializable attributes).

    Args:
        obj: An instance of a class with attributes that are
             basic data types (int, str, bool, list, dict).

    Returns:
        dict: A dictionary of all the object's attributes.
    """
    return obj.__dict__
