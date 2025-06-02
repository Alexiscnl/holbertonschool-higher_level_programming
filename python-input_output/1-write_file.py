#!/usr/bin/python3
"""
Executable script using the Python 3 interpreter.

This shebang allows the script to be run directly from the terminal
without needing to explicitly call 'python3'.
"""


def write_file(filename="", text=""):
    """
    Writes a string to a text file using UTF-8 encoding.

    If the file does not exist, it will be created.
    If the file exists, its content will be overwritten.

    Args:
        filename (str): The name of the file to write to.
        text (str): The string to write to the file.

    Returns:
        int: The number of characters written to the file.
    """
    with open(filename, "w", encoding="UTF-8") as f:
        nb_written = f.write(text)
    return nb_written
