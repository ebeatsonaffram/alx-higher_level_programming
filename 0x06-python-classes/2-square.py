#!/usr/bin/python3
# 2-square.py by Enyonam Beatson-Afrram
"""Square Model"""


class Square:
    """The square class"""

    def __init__(self, size=0):
        """Initializing the class
        Args:
            size: represnets the size of the square defined
        Raises:
            TypeError: if size is not integer
            ValueError: if size is less than zero
        """

        if not isinstance(size, int):
            raise TypeError('size must be an integer')
        if size < 0:
            raise ValueError('size must be >= 0')

        self.__size = size
