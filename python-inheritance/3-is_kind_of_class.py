#!/usr/bin/python3
"""
This module provides a function to check if an object is an instance
of a given class or an instance of a subclass of that class.
"""


def is_kind_of_class(obj, a_class):
    """
    Check if an object is an instance of, or if it is an instance of a class
    that inherited from, the specified class.

    Args:
        obj: The object to check.
        a_class: The class to compare against.

    Returns:
        bool: True if obj is an instance or inherits from a_class,
        False otherwise.
    """
    return isinstance(obj, a_class)
