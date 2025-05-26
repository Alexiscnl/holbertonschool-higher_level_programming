#!/usr/bin/python3
"""
This module defines a class that inherits from the built-in list class
and adds a method to print the list in sorted (ascending) order
without modifying the original list.
"""


class MyList(list):
    """
    A custom list class that inherits from Python's built-in list.
    Adds a method to print the list in sorted (ascending) order.
    """

    def print_sorted(self):
        """
        Prints the list elements in sorted (ascending) order.
        Does not modify the original list.
        """
        print(sorted(self))
