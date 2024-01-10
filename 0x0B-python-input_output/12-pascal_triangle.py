#!/usr/bin/python3
"""
definining pascal's triangle
"""


def pascal_triangle(n):
    """
    Generates Pascal's Triangle up to the specified number of rows.

    Parameters:
        n (int): The number of rows for Pascal's Triangle.

    Returns:
        list of lists: A list of lists representing Pascal's Triangle.

    Example:
    >>> pascal_triangle(5)
    [[1], [1, 1], [1, 2, 1], [1, 3, 3, 1], [1, 4, 6, 4, 1]]

    Additional Tests:
    >>> pascal_triangle(0)
    # Output: []
    >>> pascal_triangle(1)
    # Output: [[1]]
    >>> pascal_triangle(2)
    # Output: [[1], [1, 1]]
    >>> pascal_triangle(3)
    # Output: [[1], [1, 1], [1, 2, 1]]
    >>> pascal_triangle(6)
    # Output: [[1], [1, 1], [1, 2, 1], [1, 3, 3, 1],
            [1, 4, 6, 4, 1], [1, 5, 10, 10, 5, 1]]
    """

    if n <= 0:
        return []

    triangle = [[1] * (i + 1) for i in range(n)]

    for i in range(2, n):
        for j in range(1, i):
            triangle[i][j] = triangle[i - 1][j - 1] + triangle[i - 1][j]

    return triangle
