#!/usr/bin/python3
"""Finds a peak in a list of unsorted integers"""
def find_peak(list_of_integers):
    # Check if the list is empty
    if not list_of_integers:
        return None

    # Get the length of the list
    n = len(list_of_integers)

    # Binary search for a peak
    def binary_search_peak(low, high):
        # Calculate the midpoint
        mid = (low + high) // 2

        # Check if the midpoint is a peak
        if (mid == 0 or list_of_integers[mid] >= list_of_integers[mid - 1]) and \
           (mid == n - 1 or list_of_integers[mid] >= list_of_integers[mid + 1]):
            return list_of_integers[mid]

        # If the element to the right is greater, search right
        elif mid < n - 1 and list_of_integers[mid] < list_of_integers[mid + 1]:
            return binary_search_peak(mid + 1, high)

        # Otherwise, search left
        else:
            return binary_search_peak(low, mid - 1)

    # Start binary search from the entire list
    return binary_search_peak(0, n - 1)
