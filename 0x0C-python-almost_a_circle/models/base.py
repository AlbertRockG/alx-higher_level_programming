#!/usr/bin/python3
# base.py
# AlbertRockG
"""Defines a class Base."""


class Base:
    """Represents a base.

    Attributes:
        __nb_objects (int): The number of instance.
    """
    __nb_objects = 0

    def __init__(self, id=None):
        """Initialize a Base instance.

        Args:
            id (int): Identity of base instance.
        """
        if id != None:
            self.id = id
        else:
            Base.__nb_objects += 1
            self.id = Base.__nb_objects
