#!/usr/bin/python3
"""
This module provides a function for checking if an object is an instance
of, or if it is an instance of a class that inherited from,
the specified class.
"""

def is_kind_of_class(obj, a_class):
    """
    Check if the object is an instance of,
    or if it is an instance of a class
    that inherited from, the specified class.

    Parameters:
    - obj: The object to be checked.
    - a_class: The class to check against.

    Returns:
    - bool: True if the object is an instance of the specified class or any
            of its subclasses, otherwise False.

    Example:
    >>> class Animal:
    ...     pass
    ...
    >>> class Dog(Animal):
    ...     pass
    ...
    >>> obj = Dog()
    >>> is_kind_of_class(obj, Animal)
    True

    Additional Tests:
    >>> obj2 = Animal()
    >>> is_kind_of_class(obj2, Dog)
    False
    >>> is_kind_of_class(obj, int)
    False
    """
    return isinstance(obj, a_class)
