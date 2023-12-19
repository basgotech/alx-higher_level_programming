#!/usr/bin/python3

""" Define a Square class"""
class Square:
    """
    Represents a square.

    Attributes:
        size (number): The size of the square.
    """

    def __init__(self, size=0):
        """
        Initializes a new square.

        Args:
            size (number): The size of the square (default is 0).

        Raises:
            TypeError: If size is not a number.
            ValueError: If size is less than 0.
        """
        self.size = size

    @property
    def size(self):
        """Get or set the size of the square."""
        return self.__size

    @size.setter
    def size(self, value):
        """
        Set the size of the square.

        Args:
            value (number): The new size of the square.

        Raises:
            TypeError: If size is not a number.
            ValueError: If size is less than 0.
        """
        if not isinstance(value, (int, float)):
            raise TypeError("size must be a number")
        elif value < 0:
            raise ValueError("size must be >= 0")
        self.__size = value

    def area(self):
        """
        Calculate the area of the square.

        Returns:
            number: The area of the square.
        """
        return self.__size ** 2

    def __eq__(self, other):
        """Equal comparison based on area."""
        if isinstance(other, Square):
            return self.area() == other.area()
        return False

    def __ne__(self, other):
        """Not equal comparison based on area."""
        return not self.__eq__(other)

    def __lt__(self, other):
        """Less than comparison based on area."""
        if isinstance(other, Square):
            return self.area() < other.area()
        return False

    def __le__(self, other):
        """Less than or equal comparison based on area."""
        return self.__lt__(other) or self.__eq__(other)

    def __gt__(self, other):
        """Greater than comparison based on area."""
        if isinstance(other, Square):
            return self.area() > other.area()
        return False

    def __ge__(self, other):
        """Greater than or equal comparison based on area."""
        return self.__gt__(other) or self.__eq__(other)
