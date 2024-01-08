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
