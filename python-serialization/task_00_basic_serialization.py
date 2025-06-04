#!/usr/bin/python3
import json

def serialize_and_save_to_file(data, filename):
    """
    Serializes a Python dictionary and saves it to a JSON file.

    Args:
        data (dict): The Python dictionary to serialize.
        filename (str): The name of the file where the JSON data will be saved.
    """
    with open(filename, "w") as f:
        json.dump(data, f)

def load_and_deserialize(filename):
    """
    Loads data from a JSON file and deserializes it into a Python dictionary.

    Args:
        filename (str): The name of the JSON file to read.

    Returns:
        dict: The deserialized Python dictionary.
    """
    with open(filename, "r") as f:
        return json.load(f)
