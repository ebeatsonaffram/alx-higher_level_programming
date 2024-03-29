#!/usr/bin/python3
"""docstring Module"""
import math


class MagicClass:
    """setting MagicClass"""

    def __init__(self, radius=0):
        """  another docstring """
        self.__radius = 0
        if type(radius) is not int and type(radius) is not float:
            raise TypeError('radius must be a number')
        self.__radius = radius

    def area(self):
        """another docstring"""
        return self.__radius ** 2 * math.pi

    def circumference(self):
        """docstring"""
        return 2 * math.pi * self.__radius
