#!/usr/bin/python3
"""Print the list in ascending sorted order."""

class MyList(list):
     """a subclass of list"""
    def __init__(self):
        """initializes the object"""
        super().__init__()

    def print_sorted(self):
        """Print the list in ascending sorted order."""
        sorted_list = sorted(self)
        print(sorted_list)
