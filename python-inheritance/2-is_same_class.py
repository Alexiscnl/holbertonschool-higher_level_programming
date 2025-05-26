#!/usr/bin/python3
"""
This module contains a function to check if an object
is **exactly** an instance of a given class,
without considering inheritance.

The function returns True if the object is a direct instance
of the specified class, otherwise False.
"""


def is_same_class(obj, a_class):
    """
    Retourne True si obj est exactement une instance de a_class,
    sinon False.
    """
    return type(obj) is a_class
