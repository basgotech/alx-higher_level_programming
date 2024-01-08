#!/usr/bin/python3
"""Defines a function that adds attributes to objects."""

def add_attribute(obj, attr_name, attr_value):
    """
    Add a new attribute to the object if it's possible.

    Parameters:
    - obj: The object to which the new attribute will be added.
    - attr_name: The name of the new attribute.
    - attr_value: The value of the new attribute.

    Raises:
    - TypeError: If the object cannot have a new attribute.
    """
    if hasattr(obj, '__dict__') or (hasattr(obj, '__slots__') and attr_name in obj.__slots__):
        setattr(obj, attr_name, attr_value)
    else:
        raise TypeError("can't add new attribute")
