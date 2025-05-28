#!/usr/bin/env python3
"""
This module defines the VerboseList class,
which extends Python's built-in list.
It overrides standard list modification methods to print informative messages
whenever the list is modified.
"""


class VerboseList(list):
    """A subclass of list that prints messages when modified."""

    def append(self, item):
        """Append an item to the list and print a notification."""
        super().append(item)
        print(f"Added [{item}] to the list.")

    def extend(self, iterable):
        """Extend the list with an iterable and print a notification."""
        super().extend(iterable)
        print(f"Extended the list with [{len(iterable)}] items.")

    def remove(self, item):
        """Remove an item from the list and print a notification."""
        super().remove(item)
        print(f"Removed [{item}] from the list.")

    def pop(self, index=-1):
        """Remove and return item at index (default last),
        with notification."""
        item = super().pop(index)
        print(f"Popped [{item}] from the list.")
        return item
