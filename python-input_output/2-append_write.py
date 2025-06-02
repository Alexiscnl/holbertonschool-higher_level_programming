#!/usr/bin/python3
"""
Executable script using the Python 3 interpreter.

This script defines a function that appends a string
to the end of a UTF-8 text file and returns the number
of characters added.
"""
def append_write(filename="", text=""):
    """
    Appends a string at the end of a text file (UTF-8 encoded).

    If the file does not exist, it will be created.
    If it exists, the text is added to the end without overwriting.

    Args:
        filename (str): The name of the file to append to.
        text (str): The string to append to the file.

    Returns:
        int: The number of characters written.
    """
    with open(filename, "a", encoding="UTF-8") as f:
        nb_written = f.write(text)
    return nb_written
