#!/usr/bin/python3
"""
This module contains a function that divides all elements of a matrix.

"""

def matrix_divided(matrix, div):
    """
    Divides all elements of a matrix by a given divisor.

    Parameters:
        matrix (list of lists): The matrix containing integers or floats.
        div (number): The divisor (integer or float) to divide all elements by.

    Returns:
        list of lists: A new matrix with elements rounded to 2 decimal places.

    """
    
    for list in matrix:
        if len(matrix[0]) != len(list):
            raise TypeError("Each row of the matrix must have the same size")
        for element in list:
            if not type(element) in [int, float]:
                raise TypeError(
                    "matrix must be a matrix " +
                    "(list of lists) of integers/floats"
                )
    if not type(div) in [int, float]:
        raise TypeError("div must be a number")
    if div == 0:
        raise ZeroDivisionError("division by zero")

    result_matrix = []
    for i in matrix:
        result_matrix.append(list(map(lambda x: round(x / div, 2), i)))
    return result_matrix
