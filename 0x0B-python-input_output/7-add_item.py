#!/usr/bin/python3
"""
add item module
"""

def add_item(args, filename="add_item.json"):
    """Adds all arguments to a Python list and saves them to a file.

    Args:
        args (list): List of arguments.
        filename (str): The name of the file.
    """
    import json

    try:
        with open(filename, 'r', encoding='utf-8') as file:
            my_list_saved = json.load(file)
    except FileNotFoundError:
        my_list_saved = []

    my_list_saved.extend(args)

    with open(filename, 'w', encoding='utf-8') as file:
        json.dump(my_list_saved, file)
