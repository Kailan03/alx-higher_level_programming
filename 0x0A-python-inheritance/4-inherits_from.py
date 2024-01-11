#!/usr/bin/python3
"""
This module provides a function for checking if an object is an instance
of a class that inherited (directly or indirectly) from the specified class.
"""


def inherits_from(obj, a_class):
    """
    Check if the object is an instance of a class that inherited (directly
    or indirectly) from the specified class.

    Parameters:
    - obj: The object to be checked.
    - a_class: The class to check against.

    Returns:
    - bool: True if the object is an instance of a class that inherited
            (directly or indirectly) from the specified class, otherwise False.

    Example:
    >>> class Animal:
    ...     pass
    ...
    >>> class Mammal(Animal):
    ...     pass
    ...
    >>> class Dog(Mammal):
    ...     pass
    ...
    >>> obj = Dog()
    >>> inherits_from(obj, Animal)
    True

    Additional Tests:
    >>> obj2 = Animal()
    >>> inherits_from(obj2, Dog)
    False
    >>> inherits_from(obj, int)
    False
    """
    return issubclass(type(obj), a_class)
