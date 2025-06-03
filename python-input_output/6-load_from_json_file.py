#!/usr/bin/python3
"""
This module provides a function to load a Python object
from a JSON-formatted file.
"""

import json

def load_from_json_file(filename):
    """
    Loads a Python object from a JSON file.

    Args:
        filename (str): The path to the file containing JSON data.

    Returns:
        object: The Python object represented by the JSON content.
    """
    with open(filename, "r") as f:
        json_file = json.load(f)
        return json_file
