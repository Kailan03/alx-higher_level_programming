#!/usr/bin/python3
"""
defines a function that creates an Object from a “JSON file.
"""


def load_from_json_file(filename):
    """
    Creates an object from a JSON file.

    Parameters:
    - filename (str): The name of the JSON file to load.

    Returns:
    - object: The Python data structure represented by the JSON file.

    Example:
    >>> load_from_json_file("output.json")
    {'name': 'John', 'age': 30, 'city': 'New York'}

    Additional Tests:
    >>> load_from_json_file("array_output.json")
    # Loading a list from a file
    # Output: [1, 2, 3, 4]

    >>> load_from_json_file("integer_output.json")
    # Loading an integer from a file
    # Output: 42
    """

    import json

    with open(filename, mode="r", encoding="utf-8") as file:
        return json.load(file)
