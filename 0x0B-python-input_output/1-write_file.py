#!/usr/bin/python3
"""
defines a function that writes in a file
"""


def write_file(filename="", text=""):
    """
    Writes a string to a text file & returns the number of characters written.

    Parameters:
    - filename (str): The name of the file to be written.
    - text (str): The string to be written to the file.

    Returns:
    - int: The number of characters written to the file.

    Example:
    >>> write_file("output.txt", "Hello, World!")
    13

    Additional Tests:
    >>> write_file("existing_file.txt", "New content.")
    # Overwriting an existing file
    # Output: 12

    >>> write_file("new_file.txt", "")
    # Writing an empty string
    # Output: 0
    """

    try:
        with open(filename, mode="w", encoding="utf-8") as file:
            file.write(text)
            return len(text)
    except TypeError:
        print("Invalid filename or text type. Please provide valid strings.")
        return 0
