#!/usr/bin/python3
"""
Script that adds all command-line arguments to a Python list
and saves them to a file in JSON format.
"""

import sys

load_from_json_file = __import__('6-load_from_json_file').load_from_json_file
save_to_json_file = __import__('5-save_to_json_file').save_to_json_file

argument = sys.argv[1:]

try:
    items = load_from_json_file("add_item.json")
except FileNotFoundError:
    items = []


items.extend(argument)

save_to_json_file(items, "add_item.json")
