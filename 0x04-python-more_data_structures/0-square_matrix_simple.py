#!/usr/bin/python3
def square_matrix_simple(matrix=[]):

    # creating a new matrix of the same size as the input matrix
    result_matrix = [[0] * len(matrix[0]) for _ in range(len(matrix))]

    # iterate through columns and rows
    for i in range(len(matrix)):
        for j in range(len(matrix[0])):
            # square the value and assign it to the corresponding position
            result_matrix[i][j] = matrix[i][j] ** 2

    return result_matrix
