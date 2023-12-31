#!/usr/bin/python3
"""represents a square"""


class Square:
    """This class defines a square.

    Attributes:
        __size (int): The size of each side of the square.
    """

    def __init__(self, size=0):
        """Initializes a Square instance with an optional size.

        Args:
            size (int, optional):
            The size of each side of the square. Defaults to 0.

        Raises:
            TypeError: If size is not an integer.
            ValueError: If size is less than 0.
        """
        if not isinstance(size, int):
            raise TypeError("size must be an integer")

        if size < 0:
            raise ValueError("size must be >= 0")

        self.__size = size
