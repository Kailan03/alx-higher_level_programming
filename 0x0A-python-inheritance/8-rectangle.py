#!/usr/bin/python3
"""
defining a class representing rectangle
"""
class Rectangle(BaseGeometry):
    """
    A class representing a rectangle, inheriting from BaseGeometry.

    Attributes:
    - width (int): The width of the rectangle.
    - height (int): The height of the rectangle.
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

if __name__ == "__main__":
    # Example Test
    rectangle = Rectangle(5, 10)
    print(f"Rectangle width: {rectangle._Rectangle__width}")
    # Accessing private attribute
    print(f"Rectangle height: {rectangle._Rectangle__height}")  
    # Accessing private attribute
