#!/usr/bin/python3

"""This defines a class Square."""


class Square:
    """This represents a square."""

    def __init__(self, size=0, position=(0, 0)):
        """This initializes a new square.

        Args:
            size (int): The size of the new square.
            position (int, int): The position of the new square.
        """
        self.size = size
        self.position = position

    @property
    def size(self):
        """This gets the current size of the square."""
        return (self.__size)

    @size.setter
    def size(self, value):
        if not isinstance(value, int):
            raise TypeError("The size must be an integer")
        elif value < 0:
            raise ValueError("The size must be >= 0")
        self.__size = value

    @property
    def position(self):
        """This gets the current position of the square."""
        return (self.__position)

    @position.setter
    def position(self, value):
        if (not isinstance(value, tuple) or
                len(value) != 2 or
                not all(isinstance(num, int) for num in value) or
                not all(num >= 0 for num in value)):
            raise TypeError("The position must be a tuple of 2 positive integers")
        self.__position = value

    def area(self):
        """This returns the current area of the square."""
        return (self.__size * self.__size)

    def my_print(self):
        """This prints the square with the # character."""
        if self.__size == 0:
            print("")
            return

        [print("") for iz in range(0, self.__position[1])]
        for iz in range(0, self.__size):
            [print(" ", end="") for jz in range(0, self.__position[0])]
            [print("#", end="") for kz in range(0, self.__size)]
            print("")
