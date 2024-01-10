#!/usr/bin/python3
"""
defines a function that writes an ogject to a text file
using a JSON representation
"""


def save_to_json_file(my_obj, filename):
    """
    Writes an object to a text file using a JSON representation.

    Parameters:
    - my_obj: The object to be serialized to JSON and saved to the file.
    - filename (str): The name of the file to save the JSON representation.

    Returns:
    - None

    Example:
    >>> save_to_json_file(
            {"name": "John", "age": 30, "city": "New York"}, "output.json")

    Additional Tests:
    >>> save_to_json_file([1, 2, 3, 4],
            "array_output.json")
    # Saving a list to a file
    # Output: (File named 'array_output.json'
            containing the JSON representation of the list)

    >>> save_to_json_file(42, "integer_output.json")
    # Saving an integer to a file
    # Output: (File named 'integer_output.json'
            containing the JSON representation of the integer)
    """

    import json

    with open(filename, mode="w", encoding="utf-8") as file:
        json.dump(my_obj, file)
