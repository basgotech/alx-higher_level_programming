#!/usr/bin/python3
"""
10-student module
"""

class Student:
    """Defines a student with attributes: first_name, last_name, and age."""
    def __init__(self, first_name, last_name, age):
        """Initializes a new instance of the Student class."""
        self.first_name = first_name
        self.last_name = last_name
        self.age = age

    def to_json(self, attrs=None):
        """Retrieves a dictionary representation of a Student instance.

        Args:
            attrs (list): List of attributes to retrieve.

        Returns:
            dict: The dictionary representation of the object.
        """
        if attrs is None:
            return self.__dict__
        return {key: value for key, value in self.__dict__.items() if key in attrs}
