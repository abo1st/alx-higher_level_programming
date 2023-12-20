#!/usr/bin/python3

"""This defines a class Square."""


class Square:
    """This represents a square."""

    def __init__(self, size=0):
        """This initializes a new square.

        Args:
            size (int): This is the  size of the new square.
        """
        if not isinstance(size, int):
            raise TypeError("The size must be an integer")
        elif size < 0:
            raise ValueError("The size must be >= 0")
        self.__size = size

    def area(self):
        """This return the current area of the square."""
        return (self.__size * self.__size)
