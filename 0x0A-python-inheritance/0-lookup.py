#!/usr/bin/python3
"""Return available attributes and methods of an object:."""


def lookup(obj):
    """The object for which attributes and methods are to be looked up."""
    attributes_and_methods = dir(obj)
    return (attributes_and_methods)
