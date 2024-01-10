#!/usr/bin/python3
"""
defines a function
returns the dictionary description with simple data structure
"""


def class_to_json(obj):
    """
    Returns the dictionary description with a simple data structure
    for JSON serialization of an object.

    Parameters:
    - obj: An instance of a Class.

    Returns:
    - dict: A dictionary representation of the object suitable
    for JSON serialization.

    Example:
    >>> class_to_json({"name": "John", "age": 30, "city": "New York"})
    {'name': 'John', 'age': 30, 'city': 'New York'}

    Additional Tests:
    >>> class_to_json([1, 2, 3, 4])
    # JSON representation of a list
    # Output: [1, 2, 3, 4]

    >>> class_to_json(True)
    # JSON representation of a boolean
    # Output: True
    """

    # Check if the object is a dictionary, list, string, integer, or boolean
    if isinstance(obj, dict):
        return {key: class_to_json(value) for key, value in obj.items()}
    elif isinstance(obj, list):
        return [class_to_json(item) for item in obj]
    elif isinstance(obj, str) or isinstance(obj, int) or isinstance(obj, bool):
        return obj
    else:
        # Handle other types (including custom classes)
        # For simplicity, assuming that custom classes have
        attributes that are serializable
        return {key: class_to_json(getattr(obj, key))
                for key in dir(obj) if not key.startswith("__")}
