#!/usr/bin/python3
""" a function read a file"""

def read_file(filename=""):
    """
    Reads a text file (UTF8) and prints its content to stdout.

    Parameters:
    - filename: A string representing the name of the text file (default is an empty string).

    """

    # Use the with statement to open and read the file
    with open(filename, 'r', encoding='utf-8') as file:
        # Read the content of the file and print to stdout
        content = file.read()
        print(content)
