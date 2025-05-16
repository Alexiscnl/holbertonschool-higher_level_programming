#!/usr/bin/python3
"""
Module 5-text_indentation

This module defines the text_indentation(text) function, which displays text
by inserting two newlines after each '.', '?', or ':'.
The text must not begin or end with a space on any line.
"""
def text_indentation(text):
    """
    Prints a text with 2 new lines after each '.', '?' and ':'.

    Args:
        text (str): The text to indent.

    Raises:
        TypeError: If text is not a string.
    """
    if not isinstance(text, str):
        raise TypeError("text must be a string")
    temp = ""
    for i in text:
        temp += i
        if i in '.:?':
            print(temp.strip())
            print()
            temp = ""
    if temp.strip():
        print(temp.strip(), end="")
