#!/usr/bin/python3
"""This defines an object attribute lookup function."""


def lookup(obj):
    """This returns a list of an object's attributes that are available."""
    return (dir(obj))
