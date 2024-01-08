#!/usr/bin/python3
"""
This module provides a function for printing a square with the character #.

Functions:
    - print_square(size): Prints a square with the character #.

Examples:
    >>> print_square(5)
    #####
    #####
    #####
    #####
    #####

    >>> print_square(3)
    ###
    ###
    ###

    >>> print_square(0)

    >>> print_square(-2)
    Traceback (most recent call last):
    ...
    ValueError: size must be >= 0

    >>> print_square(3.5)
    Traceback (most recent call last):
    ...
    TypeError: size must be an integer
"""

def print_square(size):
    """
    Prints a square with the character #.

    Parameters:
    - size (int): The size length of the square.

    Raises:
    - TypeError: If size is not an integer.
    - ValueError: If size is less than 0.
    """
    # Check if size is an integer
    if not isinstance(size, int):
        raise TypeError("size must be an integer")

    # Check if size is less than 0
    if size < 0:
        raise ValueError("size must be >= 0")

    # Print the square
    for _ in range(size):
        print("#" * size)
