#!/usr/bin/python3

""" Divides all elements of a matrix by a given number."""

def matrix_divided(matrix, div):
    """
    Divides all elements of a matrix by a given number.

    This function takes a matrix (list of lists) and a divisor (div), and divides
    each element of the matrix by the divisor. The result is a new matrix with
    the elements rounded to 2 decimal places.

    Parameters:
    - matrix: A list of lists containing integers or floats.
    - div: A number (integer or float) used as the divisor.

    Returns:
    A new matrix with elements rounded to 2 decimal places.

    Raises:
    TypeError: If the matrix is not a list of lists of integers or floats,
               if each row of the matrix does not have the same size, or
               if div is not a number.
    ZeroDivisionError: If div is equal to 0.
    """
    # Check if matrix is a list of lists of integers or floats
    if not isinstance(matrix, list) or not all(isinstance(row, list) for row in matrix):
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

    # Perform the matrix division and round to 2 decimal places
    new_matrix = [[round(element / div, 2) for element in row] for row in matrix]

    return new_matrix
