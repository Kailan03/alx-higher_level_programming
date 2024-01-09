#!/usr/bin/python3
"""
This module defines a class that inherits built in list
"""


class MyList(list):
    """
    A custom class MyList that inherits from the built-in list class.

    Public Methods:
    - print_sorted(self): Prints the list, but sorted in ascending order.

    Example:
    >>> my_list = MyList([3, 1, 4, 1, 5, 9, 2, 6, 5, 3, 5])
    >>> my_list.print_sorted()
    [1, 1, 2, 3, 3, 4, 5, 5, 5, 6, 9]
    """

    def print_sorted(self):
        """
        Prints the list, but sorted in ascending order.

        Example:
        >>> my_list = MyList([3, 1, 4, 1, 5, 9, 2, 6, 5, 3, 5])
        >>> my_list.print_sorted()
        [1, 1, 2, 3, 3, 4, 5, 5, 5, 6, 9]
        """
        sorted_list = sorted(self)
        print(sorted_list)
