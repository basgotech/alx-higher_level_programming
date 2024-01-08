#!/usr/bin/python3
"""Defines a class and inherited class-checking function."""

def is_kind_of_class(obj, a_class):
    """
    Check if the object is an instance of, or if it is an instance of a class that inherited from, the specified class.

    Parameters:
    - obj: The object to be checked.
    - a_class: The class to check against.

    Returns:
    - True if the object is an instance of the specified class or its subclasses; otherwise, False.
    """
    # Check if the object's class matches the specified class or its subclasses
    current_class = type(obj)
    while current_class is not None:
        if current_class == a_class:
            return True
        current_class = current_class.__base__

    return False
