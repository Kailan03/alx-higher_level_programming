#!/usr/bin/python3
""" it describes a class Rectangle """


class Rectangle:
    """ it defines a Rectangle with width and height attributes """
    def __init__(self, width=0, height=0):
        self.width = width
        self.height = height

    @property
    def width(self):
        return self.__width

    @width.setter
    def width(self, value):
        if not isinstance(value, int):
            raise TypeError("width must be an integer")
        elif value < 0:
            raise ValueError("width must be >= 0")
        self.__width = value

    @property
    def height(self):
        return self.__height

    @height.setter
    def height(self, value):
        if not isinstance(value, int):
            raise TypeError("height must be an integer")
        elif value < 0:
            raise ValueError("height must be >= 0")
        self.__height = value

    def area(self):
        """Calculates and returns the area of the rectangle."""
        return self.__width * self.__height

    def perimeter(self):
        """Calculates and returns the perimeter of the rectangle."""
        return (2 * (self.__width + self.__height)
                if self.__width and self.__height
                else 0)

    def __str__(self):
        """Returns a string representation of the rectangle."""
        if self.__width == 0 or self.__height == 0:
            return ""
        return ('#' * self.__width + '\n') * self.__height

    def __repr__(self):
        """Returns a string representation of the rectangle for recreation."""
        return "Rectangle({}, {})".format(self.__width, self.__height)
