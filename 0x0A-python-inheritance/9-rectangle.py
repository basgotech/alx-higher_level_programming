#!/usr/bin/python3
"""a class Rectangle that inherits from BaseGeometry."""
BaseGeometry = __import__('7-base_geometry').BaseGeometry


class Rectangle(BaseGeometry):
    """Represent a rectangle using BaseGeometry."""

    def __init__(self, width, height):
        """Intialize a new Rectangle.

        Args:
            width (int): The width of Rectangle.
            height (int): The height of Rectangle.
        """
        super().integer_validator("width", width)
        self.__width = width
        super().integer_validator("height", height)
        self.__height = height

    def area(self):
        """Return the area of the rect."""
        return self.__width * self.__height

    def __str__(self):
        """Return the representation of a Rectangle."""
        string_col = "[" + str(self.__class__.__name__) + "] "
        string_col += str(self.__width) + "/" + str(self.__height)
        return string_col
