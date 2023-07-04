#!/usr/bin/python3
# AlbertRockG
# 1-rectangle.py
# -*- coding: utf-8 -*-
"""Defines a class named Rectangle"""


class Rectangle():
    """Represents a Rectangle"""

    def __init__(self, width=0, height=0):
        """Represents a Rectangle

        Args:
            width (int): The width of the Rectangle.
            height (int): The height of the Rectangle.
        """
        self.__width = width
        self.__height = height

    @property
    def width(self):
        """Get/Set width of the Rectangle."""
        return self.__width

    @width.setter
    def width(self, value):
        if not instance(width):
            raise TypeError("width must be an integer")
        if size < 0:
            raise ValueError("width must be >= 0")
        self.__width = value

    @property
    def height(self):
        """Get/Set height of the Rectangle."""
        return self.__height

    @height.setter
    def height(self, value):
        if not instance(height):
            raise TypeError("height must be an integer")
        if height < 0:
            raise ValueError("height must be >= 0")
        self.__height = value
