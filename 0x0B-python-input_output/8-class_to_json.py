#!/usr/bin/python3
"""Module definition of a Python class-to-JSON function"""


def class_to_json(obj):
    """Returns the dictionary representation of a simple data structure"""
    return obj.__dict__
