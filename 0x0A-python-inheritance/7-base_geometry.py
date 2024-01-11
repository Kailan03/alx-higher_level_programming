#!/usr/bin/python3
"""
defining class with integer validator
"""
class BaseGeometry:
    """
    A base class for geometry-related functionality.

    Public Methods:
    - area(self): Raises an Exception with the message 'area() is not implemented.'
    - integer_validator(self, name, value): Validates the value for an integer attribute.

    Attributes:
    - None
    """

    def area(self):
        """
        Raises:
        - Exception: 'area() is not implemented.'
        """
        raise Exception('area() is not implemented.')

    def integer_validator(self, name, value):
        """
        Validates the value for an integer attribute.

        Parameters:
        - name (str): The name of the attribute.
        - value: The value to be validated.

        Raises:
        - TypeError: If the value is not an integer.
        - ValueError: If the value is less than or equal to 0.
        """
        if not isinstance(value, int):
            raise TypeError(f'{name} must be an integer')
        if value <= 0:
            raise ValueError(f'{name} must be greater than 0')


if __name__ == "__main__":
    # Example Test
    geometry = BaseGeometry()

    # Test area() method
    try:
        geometry.area()
    except Exception as e:
        print(f"Test 1 Passed: {str(e)}")

    # Test integer_validator() method
    try:
        geometry.integer_validator("side_length", 5)
        print("Test 2 Passed: Validation successful for positive integer.")
    except Exception as e:
        print(f"Test 2 Failed: {str(e)}")

    try:
        geometry.integer_validator("side_length", "invalid")
        print("Test 3 Failed: Validation passed for non-integer (expected failure).")
    except TypeError as e:
        print(f"Test 3 Passed: {str(e)}")

    try:
        geometry.integer_validator("side_length", 0)
        print("Test 4 Failed: Validation passed for non-positive integer (expected failure).")
    except ValueError as e:
        print(f"Test 4 Passed: {str(e)}")
