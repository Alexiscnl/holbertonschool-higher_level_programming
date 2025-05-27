#!/usr/bin/python3
"""
This module defines the VerboseList class,
which extends the built-in Python list to provide
notifications for list modifications such as append, extend,
remove, and pop operations.
"""


class VerboseList(list):
    """
    A custom list class that prints notifications when items are
    added or removed. Inherits from the built-in list class.
    """

    def append(self, item):
        """
        Add an item to the end of the list and print a notification.

        Args:
            item: The item to be appended to the list.
        """
        super().append(item)
        print(f"Added [{item}] to the list.")

    def extend(self, iterable):
        """
        Extend the list by appending elements from the iterable,
        and print how many items were added.

        Args:
            iterable: An iterable containing items to add to the list.
        """
        count = len(iterable)
        super().extend(iterable)
        print(f"Extended the list with [{count}] items.")

    def remove(self, value):
        """
        Remove the first occurrence of the specified value
        from the list and print a notification.

        Args:
            value: The value to remove from the list.
        """
        super().remove(value)
        print(f"Removed [{value}] from the list.")

    def pop(self, index=-1):
        """
        Remove and return the item at the given position in the list.
        If no index is specified, the last item is removed.
        Prints a notification with the removed item.

        Args:
            index (int, optional): The position of the item to remove.
            Defaults to -1.
        """
        item = self[index]
        super().pop(index)
        print(f"Popped [{item}] from the list.")
