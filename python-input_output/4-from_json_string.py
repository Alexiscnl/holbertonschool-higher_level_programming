#!/usr/bin/python3
"""
This script defines a function to deserialize a JSON-formatted string
into a native Python data structure.
"""
import json


def from_json_string(my_str):
    """
    Converts a JSON-formatted string into a corresponding Python object.

    Args:
        my_str (str): A string in JSON format.

    Returns:
        object: The Python data structure represented by the JSON string.
    """
    string_json = json.loads(my_str)
    return string_json
