#!/usr/bin/python3
"""Describes a class square"""


class Square:
    def __init__(self, size):
        """Initializes a Square instance with the given size.

        Args:
            size (int): The size of each side of the square.
        """
        self.__size = size
