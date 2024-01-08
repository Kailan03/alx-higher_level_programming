#!/usr/bin/python3
"""
This module provides a function for printing a personalized greeting.

Functions:
    - say_my_name(first_name, last_name=""): Prints a personalized greeting.

Examples:
    >>> say_my_name("Rahmat", "Kilani")
    My name is Rahmat Kilani

    >>> say_my_name("Rahmat")
    My name is Rahmat

    >>> say_my_name(123, "Rahmat")
    Traceback (most recent call last):
    ...
    TypeError: first_name must be a string or last_name must be a string
"""


def say_my_name(first_name, last_name=""):
    """
    Prints a personalized greeting.

    Parameters:
    - first_name (str): The first name for the greeting.
    - last_name (str): The last name for the greeting.
    Default is an empty string.

    Raises:
    - TypeError: If first_name or last_name is not a string.
    """
    # Check if first_name is a string
    if not isinstance(first_name, str):
        raise TypeError("first_name must be a string")

    # Check if last_name is a string
    if not isinstance(last_name, str):
        raise TypeError("last_name must be a string")

    # Print the personalized greeting
    if last_name:
        print("My name is {} {}".format(first_name, last_name))
    else:
        print("My name is {}".format(first_name))
