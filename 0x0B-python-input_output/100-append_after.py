#!/usr/bin/python3
"""append after module"""

def append_after(filename="", search_string="", new_string=""):
    """Inserts a line of text to a file.

    Args:
        filename (str): The name of the file.
        search_string (str): The string to search for in each line.
        new_string (str): The string to the search string.
    """
    lines_cont = []

    with open(filename, 'r') as file:
        for line_s in file:
            lines_cont.append(line_s)
            if search_string in line_s:
                lines_cont.append(new_string)

    with open(filename, 'w') as file:
        file.writelines(lines_cont)
