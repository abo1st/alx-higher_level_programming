#!/usr/bin/python3
"""This defines a class Rectangle that inherits from BaseGeometry."""
BaseGeometry = __import__('7-base_geometry').BaseGeometry


class Rectangle(BaseGeometry):
    """This represents a rectangle using BaseGeometry."""

    def __init__(self, width, height):
        """This intializes a new rectangle.

        Args:
            width (int): This is the width of the new Rectangle.
            height (int): This is the height of the new Rectangle.
        """
        self.integer_validator("width", width)
        self.__width = width
        self.integer_validator("height", height)
        self.__height = height
