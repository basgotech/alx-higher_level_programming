#!/usr/bin/python3
"""
load_from_json_file module
"""

def load_from_json_file(filename):
    """Creates an object from a JSON file.

    Args:
        filename (str): The name of the JSON file.

    Returns:
        object: The Python data structure represented by the JSON file.
    """
    import json
    with open(filename, 'r', encoding='utf-8') as file:
        return json.load(file)
