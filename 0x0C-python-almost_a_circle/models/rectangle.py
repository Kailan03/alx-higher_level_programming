#!/usr/bin/python3
"""
Module for the Square class.
"""
from models.rectangle import Rectangle


class Square(Rectangle):
    """
    The Square class that inherits from Rectangle.

    Attributes:
        size (int): Private instance attribute for the size of the square.
    """

    def __init__(self, size, x=0, y=0, id=None):
        """
        Constructor for the Square class.

        Args:
            size (int): Size of the square.
            x (int): x-coordinate of the square (default is 0).
            y (int): y-coordinate of the square (default is 0).
            id (int): Identifier for the square (default is None).
        """
        super().__init__(size, size, x, y, id)

    @property
    def size(self):
        """Getter for size attribute."""
        return self.width

    @size.setter
    def size(self, value):
        """Setter for size attribute with validation."""
        self.width = value
        self.height = value

    def __str__(self):
        """Returns a string representation of the Square instance."""
        return f"[Square] ({self.id}) {self.x}/{self.y} - {self.size}"
