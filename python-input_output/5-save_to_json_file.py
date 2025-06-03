#!/usr/bin/python3
"""
This script defines a function to save a Python object
to a text file using its JSON representation.
"""

import json

def save_to_json_file(my_obj, filename):
    """
    Writes an object to a text file using JSON representation.

    Args:
        my_obj (any): The Python object to serialize.
        filename (str): The name of the file to write to.

    The file is overwritten if it already exists.
    """
    with open(filename, "w") as f:
        json.dump(my_obj, f)
