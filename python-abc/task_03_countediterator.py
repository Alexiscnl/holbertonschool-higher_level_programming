#!/usr/bin/python3
"""
This module defines the CountedIterator class,
which wraps around a Python iterator and keeps track
of how many items have been iterated over.
"""

class CountedIterator:
    """
    A custom iterator that counts how many items have been retrieved
    during iteration.
    """

    def __init__(self, iterable):
        """
        Initialize the CountedIterator with an iterable object.

        Args:
            iterable (iterable): Any iterable (like list, tuple, etc.)
        """
        self.iterator = iter(iterable)
        self.count = 0

    def __next__(self):
        """
        Return the next item from the iterator and increment the counter.

        Returns:
            The next item in the sequence.

        Raises:
            StopIteration: When there are no more items.
        """
        item = next(self.iterator)
        self.count += 1
        return item

    def get_count(self):
        """
        Return the number of items that have been iterated over so far.

        Returns:
            int: The count of items fetched.
        """
        return self.count
