#!/usr/bin/python3
"""
This module provides a single function that retrieves
a list of available attributes and methods of an object.

It can be used for introspection to explore the capabilities
of a given Python object.
"""

def lookup(obj):
    """
    Returns a list of available attributes and methods of an object.

    Args:
        obj: The object to inspect.

    Returns:
        list: A list of attribute and method names available for the object.
    """

    return dir(obj)
