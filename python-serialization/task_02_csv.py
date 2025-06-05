#!/usr/bin/env python3
"""
Module task_02_csv

Converts a CSV file to a JSON file by serializing the content.
The output is saved to 'data.json'.

Example:
    Input CSV:
        name,age,city
        John,28,New York

    Output JSON:
        [
            {"name": "John", "age": "28", "city": "New York"}
        ]
"""
import csv
import json


def convert_csv_to_json(filename):
    """
    Converts the contents of a CSV file into a JSON file.

    Args:
        filename (str): The name of the input CSV file.

    Returns:
        bool: True if conversion succeeded, False otherwise.
    """
    try:
        with open(filename, "r", newline='') as f:
            data_dict = []
            data = csv.DictReader(f)
            for line in data:
                data_dict.append(line)
        with open("data.json", "w") as j:
            json.dump(data_dict, j)
        return True
    except Exception:
        return False
