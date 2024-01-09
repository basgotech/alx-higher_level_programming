#!/usr/bin/python3
"""
Prints a text with 2 new lines after each of the characters: ., ? and : """

def text_indentation(text):
    """
    Prints a text with 2 new lines after each of the characters: ., ? and :

    Parameters:
    - text: A string representing the input text.

    Raises:
    - TypeError: If text is not a string.
    """
    # Check if text is a string
    if not isinstance(text, str):
        raise TypeError("text must be a string")

    # Define the characters that trigger a new line
    newline_chars = ['.', '?', ':']

    # Process the text and print with 2 new lines after specified characters
    current_line = ""
    for char in text:
        current_line += char
        if char in newline_chars:
            print(current_line.strip())
            print()  # Print 2 new lines
            current_line = ""

    # Print the remaining part of the text if any
    if current_line:
        print(current_line.strip())
