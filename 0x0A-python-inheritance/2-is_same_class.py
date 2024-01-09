#!/usr/bin/python3
"""
This module defines a specified class
"""


def is_same_class(obj, a_class):
    """
    Returns True if the object is exactly an instance of the specified class;
                otherwise, False.

    Parameters:
    - obj: any object.
    - a_class: a class to compare against.

    Returns:
    - bool: True if obj is an instance of a_class, False otherwise.

    Example:
    >>> class ExampleClass:
    ...     pass
    ...
    >>> obj_instance = ExampleClass()
    >>> is_same_class(obj_instance, ExampleClass)
    True
    >>> is_same_class(obj_instance, int)
    False
    """

    return type(obj) == a_class
