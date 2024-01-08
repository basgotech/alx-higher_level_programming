#!/usr/bin/python3
"""Defines an inherited class-checking function."""

def inherits_from(obj, a_class):
    """
    Check if the object is an instance of a class that inherited (directly or indirectly) from the specified class.

    Parameters:
    - obj: The object to be checked.
    - a_class: The class to check against.

    Returns:
    - True if the object is an instance of a class that inherited from the specified class; otherwise, False.
    """
    # Check if the object's class is a subclass of the specified class
    current_class = type(obj)

    # Keep track of visited classes to avoid infinite loops in case of circular inheritance
    visited_classes = set()

    while current_class is not None:
        if current_class == a_class:
            return True

        # Check if we have already visited this class
        if current_class in visited_classes:
            break

        # Add the current class to the set of visited classes
        visited_classes.add(current_class)

        # Move up the class hierarchy
        current_class = current_class.__base__

    return False
