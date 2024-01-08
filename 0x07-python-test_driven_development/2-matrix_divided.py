#!/usr/bin/python3
"""
This module provides a function for dividing all elements of a matrix.

Functions:
    - matrix_divided(matrix, div): Divides all elements of a matrix by a given number.

Examples:
    >>> matrix = [[1, 2, 3], [4, 5, 6]]
    >>> matrix_divided(matrix, 2)
    [[0.5, 1.0, 1.5], [2.0, 2.5, 3.0]]

    >>> matrix = [[1.5, 2.5, 3.5], [4.5, 5.5, 6.5]]
    >>> matrix_divided(matrix, 2)
    [[0.75, 1.25, 1.75], [2.25, 2.75, 3.25]]

    >>> matrix = [[1, 2, 3], [4, 5, 6], [7, 8, 9]]
    >>> matrix_divided(matrix, 3)
    [[0.33, 0.67, 1.0], [1.33, 1.67, 2.0], [2.33, 2.67, 3.0]]
"""

def matrix_divided(matrix, div):
    """
    Divides all elements of a matrix by a given number.

    Parameters:
    - matrix: list of lists of integers or floats, the matrix to be divided.
    - div: number (integer or float), the divisor.

    Returns:
    - list of lists of floats: The new matrix with elements divided by div, rounded to 2 decimal places.

    Raises:
    - TypeError: If the matrix is not a list of lists of integers or floats.
    - TypeError: If each row of the matrix does not have the same size.
    - TypeError: If div is not a number (integer or float).
    - ZeroDivisionError: If div is equal to 0.
    """
    # Check if matrix is a list of lists of integers or floats
    if not all(isinstance(row, list) and all(isinstance(element, (int, float)) for element in row) for row in matrix):
        raise TypeError("matrix must be a matrix (list of lists) of integers/floats")

    # Check if each row of the matrix has the same size
    if not all(len(row) == len(matrix[0]) for row in matrix):
        raise TypeError("Each row of the matrix must have the same size")

    # Check if div is a number (integer or float)
    if not isinstance(div, (int, float)):
        raise TypeError("div must be a number")

    # Check if div is not equal to 0
    if div == 0:
        raise ZeroDivisionError("division by zero")

    # Divide all elements of the matrix by div, rounded to 2 decimal places
    result_matrix = [[round(element / div, 2) for element in row] for row in matrix]

    return result_matrix

# Example usage:
matrix = [[1, 2, 3], [4, 5, 6]]
result = matrix_divided(matrix, 2)
print(result)
