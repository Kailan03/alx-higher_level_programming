#!/usr/bin/python3
"""
This module provides a function for printing text with 2 new lines after specific characters.

Functions:
    - text_indentation(text): Prints text with 2 new lines after each of these characters: ., ? and :.

Examples:
    >>> text_indentation("This is a simple sentence.")
    This is a simple sentence.

    >>> text_indentation("A question? Should be on a new line.")
    A question?
    Should be on a new line.

    >>> text_indentation("Colons: Separate statements.")
    Colons:
    Separate statements.

    >>> text_indentation("Multiple. Sentences. In one line?")
    Multiple.
    Sentences.
    In one line?

    >>> text_indentation(123)
    Traceback (most recent call last):
    ...
    TypeError: text must be a string
"""

def text_indentation(text):
    """
    Prints text with 2 new lines after each of these characters: ., ? and :.

    Parameters:
    - text (str): The input text.

    Raises:
    - TypeError: If text is not a string.
    """
    # Check if text is a string
    if not isinstance(text, str):
        raise TypeError("text must be a string")

    # Iterate through the characters in the text
    for char in text:
        print(char, end='')

        # Print 2 new lines after specific characters
        if char in ('.', '?', ':'):
            print("\n\n", end='')

    # Print a newline at the end if the last character is not one of the specified characters
    if text and text[-1] not in ('.', '?', ':'):
        print()
