#!/usr/bin/python3
"""
defines a function that appends a string at the end of  a file
and returns the number of character added
"""
def append_write(filename="", text=""):
    """
    Appends a string at the end of a text file (UTF8) and returns the number of characters added.

    Parameters:
    - filename (str): The name of the file to be appended.
    - text (str): The string to be appended to the file.

    Returns:
    - int: The number of characters added to the file.

    Example:
    >>> append_write("existing_file.txt", " Appending new content.")
    25

    Additional Tests:
    >>> append_write("new_file.txt", "This is the first line.")
    # Appending to a new file
    # Output: 24

    >>> append_write("empty_file.txt", "")
    # Appending an empty string
    # Output: 0
    """

    try:
        with open(filename, mode="a", encoding="utf-8") as file:
            file.write(text)
            return len(text)
    except TypeError:
        print("Invalid filename or text type. Please provide valid strings.")
        return 0
