#!/usr/bin/python3
"""Defines locked class"""


class LockedClass:
    """
    Only allows instructions of an attribute called first_name
    """

    __slots__ = ["first_name"]
