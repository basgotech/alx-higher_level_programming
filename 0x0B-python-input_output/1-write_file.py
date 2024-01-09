#!/usr/bin/python3
"""Writes a string to a text file (UTF8) and returns the number of characters written."""

def write_file(filename="", text=""):
    """
    Writes a string to a text file (UTF8) and returns the number of characters written.

    Parameters:
    - filename: A string representing the name of the text file (default is an empty string).
    - text: A string representing the content to be written to the file (default is an empty string).

    Returns:
    - int: The number of characters written.
    """

    # Use the with statement to open and write to the file
    with open(filename, 'w', encoding='utf-8') as file:
        # Write the content to the file
        characters_written = file.write(text)
    
    return characters_written
