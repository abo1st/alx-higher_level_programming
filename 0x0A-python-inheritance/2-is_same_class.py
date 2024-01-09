#!/usr/bin/python3
"""This defines the class-checking function."""


def is_same_class(obj, a_class):
    """This checks if an object is exactly an instance of a given class.

    Args:
        obj (any): This is the  object to be checked.
        a_class (type): This is the class to match the type of obj to.
    Returns:
        If obj is exactly an instance of a_class - True.
        Otherwise - False.
    """
    if type(obj) == a_class:
        return True
    return False
