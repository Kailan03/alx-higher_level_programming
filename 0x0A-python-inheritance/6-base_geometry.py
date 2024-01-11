#!/usr/bin/python3
"""
defining a class
"""
class BaseGeometry:
    """
    A base class for geometry-related functionality.

    Public Methods:
    - area(self): Raises an Exception with the message 'area() is not implemented.'
    """
    def area(self):
        """
        Raises:
        - Exception: 'area() is not implemented.'
        """
        raise Exception('area() is not implemented.')
