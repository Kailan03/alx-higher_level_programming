#!/usr/bin/python3


import sys
from 5-save_to_json_file import save_to_json_file
from 6-load_from_json_file import load_from_json_file
"""
defines a script that adds all arguments to a Python list,
and then save them to a file
"""


def add_and_save_to_file():
    """
    Adds all arguments to a Python list and saves them to a file.

    Usage:
    python script.py arg1 arg2 arg3 ...

    The list will be saved as a JSON representation
    in a file named add_item.json.

    Example:
    python script.py apple banana cherry
    # Creates add_item.json with the content: ["apple", "banana", "cherry"]

    Additional Tests:
    python script.py 1 2 3 4 5
    # Creates add_item.json with the content: [1, 2, 3, 4, 5]
    """
# Load existing items from the file
try:
    existing_items = load_from_json_file("add_item.json")
except FileNotFoundError:
    existing_items = []

# Add new items from command line arguments
new_items = sys.argv[1:]

# Combine existing and new items
all_items = existing_items + new_items

# Save the combined list to the file
save_to_json_file(all_items, "add_item.json")
