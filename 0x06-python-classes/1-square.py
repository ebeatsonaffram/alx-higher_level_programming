#!/usr/bin/python3
"""A module for square with private attribute"""


class Square:
    """Defines a square."""

    def __init__(self, size):
        """
        Initializes a square with a given size.

        Args:
            size (int): The side length of the square.
        """

        self.__size = size
