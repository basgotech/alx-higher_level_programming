#!/usr/bin/python3
"""
9-student module
"""

class Student:
    """Defines a student with attributes: first_name, last_name, and age."""
    def __init__(self, first_name, last_name, age):
        """Initializes a new instance of the Student class."""
        self.first_name = first_name
        self.last_name = last_name
        self.age = age

    def to_json(self):
        """Retrieves a dictionary representation of a Student instance."""
        return self.__dict__
