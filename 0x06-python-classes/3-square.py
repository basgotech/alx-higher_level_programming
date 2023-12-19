#!/usr/bin/python3

class Square:

    """Define a class Square."""


    def __init__(self, size=0):
        """
        Initialize a square.

        Parameters:
        - size (int): Optional size of the square (default is 0).

        Raises:
        - TypeError: If size is not an integer.
        - ValueError: If size is less than 0.
        """
        if not isinstance(size, int):
            raise TypeError("size must be an integer")
        elif size < 0:
            raise ValueError("size must be >= 0")
        else:
            self.__size = size  # Private attribute

    def area(self):
        """
        Calculate the area of the square.

        Returns:
        - int: The area of the square.
        """
        return self.__size ** 2
