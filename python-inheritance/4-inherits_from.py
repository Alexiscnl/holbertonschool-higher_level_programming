#!/usr/bin/python3
"""
Module 4-inherits_from

Defines a function that checks if an object is a subclass instance of a specified class.
"""
def inherits_from(obj, a_class):
    """
    Returns True if obj is an instance of a subclass of a_class,
    False if it is exactly an instance of a_class or not related.
    """
    return issubclass(type(obj), a_class) and type(obj) is not a_class
