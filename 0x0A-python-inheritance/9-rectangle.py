#!/usr/bin/python3
"""This defines a class rectangle that inherits from BaseGeometry."""
BaseGeometry = __import__('7-base_geometry').BaseGeometry


class Rectangle(BaseGeometry):
    """This represents a rectangle using BaseGeometry."""

    def __init__(self, width, height):
        """This intializes a new Rectangle.

        Args:
            width (int): This is the width of the new rectangle.
            height (int): This the height of the new rectangle.
        """
        super().integer_validator("width", width)
        self.__width = width
        super().integer_validator("height", height)
        self.__height = height

    def area(self):
        """This returns the area of the rectangle."""
        return self.__width * self.__height

    def __str__(self):
        """This returns the print() and str() representation of a rectangle."""
        string = "[" + str(self.__class__.__name__) + "] "
        string += str(self.__width) + "/" + str(self.__height)
        return string
