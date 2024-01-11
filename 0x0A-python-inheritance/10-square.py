#!/usr/bin/python3
"""
defining a class Square that inherits from Rectangle
"""


class BaseGeometry:
    """
    A base class for geometry-related functionality.

    Public Methods:
    - area(self): Raises an Exception with the message
    'area() is not implemented.'
    - integer_validator(self, name, value): Validates the value.

    Attributes:
    - __width (int): The width of the rectangle.
    - __height (int): The height of the rectangle.
    """

    def area(self):
        """
        Raises:
        - Exception: 'area() is not implemented.'
        """
        raise Exception('area() is not implemented.')

    def integer_validator(self, name, value):
        """
        Validates the value.

        Parameters:
        - name (str): The name of the value.
        - value: The value to be validated.

        Raises:
        - TypeError: If the value is not an integer.
        - ValueError: If the value is less than or equal to 0.
        """
        if not isinstance(value, int):
            raise TypeError(f"{name} must be an integer")
        if value <= 0:
            raise ValueError(f"{name} must be greater than 0")


class Rectangle(BaseGeometry):
    """
    A class representing a rectangle, inheriting from BaseGeometry.

    Attributes:
    - __width (int): The width of the rectangle.
    - __height (int): The height of the rectangle.
    """

    def __init__(self, width, height):
        """
        Initializes a Rectangle instance with width and height.

        Parameters:
        - width (int): The width of the rectangle.
        - height (int): The height of the rectangle.
        """
        super().integer_validator("width", width)
        super().integer_validator("height", height)
        self.__width = width
        self.__height = height

    def area(self):
        """
        Computes the area of the rectangle.

        Returns:
        - int: The area of the rectangle.
        """
        return self.__width * self.__height

    def __str__(self):
        """
        Returns the rectangle description.

        Returns:
        - str: The rectangle description in the format
        [Rectangle] <width>/<height>.
        """
        return f"[Rectangle] {self.__width}/{self.__height}"


class Square(Rectangle):
    """
    A class representing a square, inheriting from Rectangle.

    Attributes:
    - __size (int): The size of the square.
    """

    def __init__(self, size):
        """
        Initializes a Square instance with size.

        Parameters:
        - size (int): The size of the square.
        """
        super().__init__(size, size)
        self.__size = size

    def __str__(self):
        """
        Returns the square description.

        Returns:
        - str: The square description in the format [Square] <size>/<size>.
        """
        return f"[Square] {self.__size}/{self.__size}"


if __name__ == "__main__":
    # Example Test
    square = Square(5)
    print(square)  # Output: [Square] 5/5
    print(f"Area: {square.area()}")  # Output: Area: 25
