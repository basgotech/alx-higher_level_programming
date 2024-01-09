#!/usr/bin/python3
"""
8-class_to_json module
"""

def class_to_json(obj):
    """Returns the dictionary description with simple data structures
    for JSON serialization of an object.

    Args:
        obj: An instance of a class.

    Returns:
        dict: The dictionary representation of the object.
    """
    return obj.__dict__
