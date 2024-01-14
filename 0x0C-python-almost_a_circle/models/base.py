#!/usr/bin/python3
"""
Module for the Base class.
"""


class Base:
    """
    The Base class for managing id attribute.

    Attributes:
        __nb_objects (int): Private class attribute to keep track of the number
                            of objects created.
    """

    __nb_objects = 0

    def __init__(self, id=None):
        """
        Constructor for the Base class.

        Args:
            id (int): If id is not None, assign it to the public instance
                      attribute id. Otherwise, increment __nb_objects and
                      assign the new value to the public instance attribute id.
        """

        if id is not None:
            self.id = id
        else:
            Base.__nb_objects += 1
            self.id = Base.__nb_objects
