#!/usr/bin/python3
"""Module that finds a peak in a list of integers"""


def find_peak(list_of_integers):
    """function that finds a peak in a list of unsorted integers.

    Args:
        list_of_integers (list): a list of integers

    Your algorithm must have the lowest complexity.
    Note: there may be more than one peak in the list.

    """

    list_ = list_of_integers
    # if there is no list of integers return None
    if list_ == []:
        return None
    lengthz = len(list_)

    start, end = 0, lengthz - 1
    while start < end:
        mid = start + (end - start) // 2
        if list_[mid] > list_[mid - 1] and list_[mid] > list_[mid + 1]:
            return list_[mid]
        if list_[mid - 1] > list_[mid + 1]:
            end = mid
        else:
            start = mid + 1
    return list_[start]
