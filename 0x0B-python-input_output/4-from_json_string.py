#!/usr/bin/python3
"""
returns an object (Python data structure) represented by a JSON string
"""


def from_json_string(my_str):
    """
    Returns an object represented by a JSON string.

    Parameters:
    - my_str (str): The JSON-formatted string.

    Returns:
    - object: The Python data structure represented by the JSON string.

    Example:
    >>> from_json_string('{"name": "John", "age": 30, "city": "New York"}')
    {'name': 'John', 'age': 30, 'city': 'New York'}

    Additional Tests:
    >>> from_json_string('[1, 2, 3, 4]')
    # Python list from JSON string
    # Output: [1, 2, 3, 4]

    >>> from_json_string('42')
    # Python integer from JSON string
    # Output: 42
    """

    import json

    return json.loads(my_str)
