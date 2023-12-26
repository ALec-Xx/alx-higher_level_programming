#!/usr/bin/python3
"""Contains function that divides matrix elements"""

def matrix_divided(matrix, div):
    """Function divides all elements of a matrix

    Args:
        matrix: must be a lists of integers or floats
                div(int/float): must be a number(integer or float)
        Return: new matrix
    """
    if (not isinstance(matrix, list) or 
            not all(isinstance(row, list) for row in matrix)):
        raise TypeError("matrix must be a "
                "matrix (list of lists) of integers/floats")
    for row in matrix:
        for i in row:
            if not isinstance(i, (int, float)):
                raise TypeError("matrix must be a "
                        "matrix (list of lists) of integers/floats")
    if not all(len(row) == len(matrix[0]) for row in matrix):
        raise TypeError("Each row of the matrix must have the same size")
    if not isinstance(div, (int, float)):
        raise TypeError("div must be a number")
    elif div == 0:
        raise ZeroDivisionError("division by zero")
    return ([[round(i / div, 2) for i in row] for row in matrix])
