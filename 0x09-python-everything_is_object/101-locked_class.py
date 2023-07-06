#!/usr/bin/python3
"""Defines a locked class named LockedClass"""


class LockedClass:
    """
    Represents a locked class that prevents
    attributes instantiation, except 'first_name'.
    """

    __slots__ = ["first_name"]
