#!/usr/bin/python3
"""Define a rectangle"""


class Rectangle:
    """Represent the area and perimeter of a rectangle."""

    def __init__(self, width=0, height=0):
        """Initialize a new rectangle.

        Args:
            width (int): The width of the rectangle.
            height (int): The height of the rectangle.
        Raises:
            TypeError: if the width or the height is not an integer.
            ValueError: if the width or the height is less than zero.
        """
        self.width = width
        self.height = height

    @property
    def width(self):
        """Get/set the current width of the rectangle"""
        return (self.__width)

    @width.setter
    def width(self, value):
        if not isinstance(value, int):
            raise TypeError("width must be an integer")
        elif value < 0:
            raise ValueError("width must be >= 0")
        self.__width = value

    @property
    def height(self):
        """Get/set the current width of the rectangle."""
        return (self.__height)

    @height.setter
    def height(self, value):
        if not isinstance(value, int):
            raise TypeError("height must be an integer")
        elif value < 0:
            raise ValueError("height must be >= 0")
        self.__height = value

    def area(self):
        """Return the current area of the rectangle"""
        return (self.__width * self.__height)

    def perimeter(self):
        """Return the current perimeter of the rectangle."""
        if self.__width == 0 or self.__height == 0:
            return (0)
        return ((self.__width * 2) + (self.__height * 2))

    def __str__(self):
        """Print the diagram of a rectangle with # character"""
        if self.__width == 0 or self.__height == 0:
            return ("")
        new_rect = []
        for column in range(self.__height):
            [new_rect.append('#') for row in range(self.__width)]
        if column != self.__height - 1:
            new_rect.append("\n")
        return ("".join(new_rect))

