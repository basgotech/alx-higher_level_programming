#!/usr/bin/python3
import json
"""
save_to_json_file module
"""

def save_to_json_file(my_obj, filename):
    """Writes an object to a text file using JSON representation.

    Args:
        my_obj: The object to be written to the file.
        filename (str): The name of the file.
    """
    with open(filename, 'w', encoding='utf-8') as file:
        json.dump(my_obj, file)
