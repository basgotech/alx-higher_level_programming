#!/usr/bin/python3
"""Finds a peak in a list of unsorted integers"""


def find_peak(list_of_integers):
    """Finds a peak in list_of_integers"""

    # Check if the list is empty or None
    if not list_of_integers:
        return None

    # Get the indices for the range of the list
    lo = 0
    hi = len(list_of_integers)

    # Binary search for a peak
    while lo < hi:
        # Calculate the midpoint
        mid = lo + (hi - lo) // 2

        # Check if mid is a peak
        if (mid == 0 or list_of_integers[mid] >= list_of_integers[mid - 1]) and \
                (mid == hi - 1 or list_of_integers[mid] >= list_of_integers[mid + 1]):
            return list_of_integers[mid]
        # If mid element is less than next, peak must be on the right side
        elif mid < hi - 1 and list_of_integers[mid] < list_of_integers[mid + 1]:
            lo = mid + 1
        # Otherwise, peak must be on the left side
        else:
            hi = mid

    # If peak is not found (should never reach here)
    return None
