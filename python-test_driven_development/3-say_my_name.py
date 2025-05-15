#!/usr/bin/python3
"""
Module for say_my_name function.
Prints a formatted full name from two strings.
Includes type validation for both arguments.
"""


def say_my_name(first_name, last_name=""):
    """
    Prints: My name is <first_name> <last_name>
    Raises TypeError if arguments are not strings.
    """
    if not isinstance(first_name, str):
        raise TypeError("first_name must be a string")
    if not isinstance(last_name, str):
        raise TypeError("last_name must be a string")
    print(f"My name is {first_name} {last_name}")
