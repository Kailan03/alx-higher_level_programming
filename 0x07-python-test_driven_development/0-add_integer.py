#!/usr/bin/python3
"""
This module provides a function for adding two integers.

Functions:
    - add_integer(a, b=98): Adds two integers.

Examples:
    >>> add_integer(5, 3)
    8

    >>> add_integer(5.5, 3)
    8

    >>> add_integer(5, 3.5)
    8

    >>> add_integer(5.5, 3.5)
    8

    >>> add_integer("5", 3)
    Traceback (most recent call last):
    ...
    TypeError: a must be an integer or b must be an integer

    >>> add_integer([5], 3)
    Traceback (most recent call last):
    ...
    TypeError: a must be an integer or b must be an integer

    >>> add_integer("5", "3")
    Traceback (most recent call last):
    ...
    TypeError: a must be an integer or b must be an integer
"""

def add_integer(a, b=98):
    """
    Adds two integers.

    Parameters:
    - a: int or float, the first operand.
    - b: int or float, the second operand. Default is 98.

    Returns:
    - int: The addition of a and b.

    Raises:
    - TypeError: If either a or b is not an integer or float.
    """
    # Check if a and b are integers or floats
    if not (isinstance(a, (int, float)) and isinstance(b, (int, float))):
        raise TypeError("a must be an integer or b must be an integer")

    # Cast a and b to integers if they are floats
    a = int(a)
    b = int(b)

    # Return the addition of a and b
    return a + b
