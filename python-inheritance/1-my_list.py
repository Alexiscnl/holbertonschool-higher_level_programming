#!/usr/bin/python3

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
