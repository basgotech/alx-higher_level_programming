#!/usr/bin/python3
"""Print the list in ascending sorted order."""

class MyList(list):
    def print_sorted(self):
        """
        Print the list in ascending sorted order.

        This method sorts the elements of the list in ascending order
        and then prints the sorted list.

        Returns:
        - None
        """
        sorted_list = sorted(self)
        print(sorted_list)
