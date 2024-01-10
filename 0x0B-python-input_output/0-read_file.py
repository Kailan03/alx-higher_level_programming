#!/usr/bin/python3
"""
This module defines a funcion that reads a file
"""


def read_file(filename=""):
    """
    Reads a text file (UTF8) and prints its content to stdout.

    Parameters:
    - filename (str): The name of the file to be read.

    Example:
    >>> read_file("example.txt")
    This is an example text file.
    It contains multiple lines.
    >>> read_file("empty_file.txt")
    # Empty file scenario
    # Output: ""

    >>> read_file("nonexistent_file.txt")
    # Nonexistent file scenario
    # Output: FileNotFoundError

    >>> read_file()
    # No filename provided
    # Output: TypeError

    >>> read_file(123)
    # Invalid filename type
    # Output: TypeError
    """

    with open(filename, encoding="utf-8") as file:
        for line in file:
            print(line, end="")
