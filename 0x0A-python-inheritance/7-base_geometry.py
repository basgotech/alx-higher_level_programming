#!/usr/bin/python3
"""Defines a base geometry class BaseGeometry."""

class BaseGeometry:
    def area(self):
        """
        Raises an Exception with the message 'area() is not implemented'.

        This method should be overridden by subclasses to provide
        a specific implementation for calculating the area.
        """
        raise Exception('area() is not implemented')

    def integer_validator(self, name, value):
        """
        Validates the given value as an integer.

        Parameters:
        - name: A string representing the name of the value.
        - value: The value to be validated.

        Raises:
        - TypeError: If the value is not an integer.
        - ValueError: If the value is less than or equal to 0.
        """
        if not isinstance(value, int):
            raise TypeError(f"{name} must be an integer")

        if value <= 0:
            raise ValueError(f"{name} must be greater than 0")
