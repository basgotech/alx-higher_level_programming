#!/usr/bin/python3
"""Finds a peak in a list of unsorted integers"""


def find_peak(list_of_integers):
    """Finds a peak in lis of int """

    if list_of_integers is None or list_of_integers == []:
        return None
    lower = 0
    higher = len(list_of_integers)
    m = ((higher - lower) // 2) + lower
    m = int(m)
    if higher == 1:
        return list_of_integers[0]
    if higher == 2:
        return max(list_of_integers)
    if list_of_integers[m] >= list_of_integers[m - 1] and\
            list_of_integers[m] >= list_of_integers[m + 1]:
        return list_of_integers[m]
    if m > 0 and list_of_integers[m] < list_of_integers[m + 1]:
        return find_peak(list_of_integers[m:])
    if m > 0 and list_of_integers[m] < list_of_integers[m - 1]:
        return find_peak(list_of_integers[:m])
