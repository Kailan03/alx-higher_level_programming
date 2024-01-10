#!/usr/bin/python3
"""
returns a JSON representation of an object
"""


def to_json_string(my_obj):
    """
    Returns the JSON representation of an object.

    Parameters:
    - my_obj: The object to be serialized to JSON.

    Returns:
    - str: The JSON representation of the object.

    Example:
    >>> to_json_string({"name": "John", "age": 30, "city": "New York"})
    '{"name": "John", "age": 30, "city": "New York"}'

    Additional Tests:
    >>> to_json_string([1, 2, 3, 4])
    # JSON representation of a list
    # Output: '[1, 2, 3, 4]'

    >>> to_json_string(42)
    # JSON representation of an integer
    # Output: '42'
    """

    import json

    return json.dumps(my_obj)
