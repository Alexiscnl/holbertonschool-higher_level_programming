#!/usr/bin/python3
"""
Module 3-say_my_name
This module defines a function say_my_name that prints "My name is <first name>
<last name>".
"""


def say_my_name(first_name, last_name=""):
    """
    Prints "My name is <first name> <last name>".

    Args:
        first_name (str): Le prénom.
        last_name (str, optionnel): Le nom de famille.

    Raises:
        TypeError: Si `first_name` ou `last_name` ne sont pas des chaînes.
    """
    if not isinstance(first_name, str):
        raise TypeError("first_name must be a string")
    if not isinstance(last_name, str):
        raise TypeError("last_name must be a string")

    if last_name == "":
        print(f"My name is {first_name} ")
    else:
        print(f"My name is {first_name} {last_name}")
