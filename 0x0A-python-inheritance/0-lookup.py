#!/usr/bin/python3


def lookup(obj):
    """
    Returns the list of available attributes and methods of an object.

    Parameters:
    - obj: any object.

    Returns:
    - list: A list containing the names of attributes and methods of obj.

    Example:
    >>> class ExampleClass:
    ...     def __init__(self):
    ...         self.attribute1 = 42
    ...     def method1(self):
    ...         return "Hello, World!"
    ...
    >>> obj_instance = ExampleClass()
    >>> lookup(obj_instance)
    ['__init__', 'attribute1', 'method1']
    """

    return dir(obj)
