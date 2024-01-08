#!/usr/bin/python3
"""Defines a class-checking function."""

def is_same_class(obj, a_class):
    """Check if the object is exactly an instance of the specified class."""
    return obj.__class__ is a_class
