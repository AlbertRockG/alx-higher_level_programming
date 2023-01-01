#!/usr/bin/python3
# Albertg
# 0-rectangle.py
# -*- coding: utf-8 -*-
"""Defines a class named Rectangle"""


class Rectangle():
    """Reprensents a Rectangle"""

    def __init__(self, width=0, height=0):
        """Initialize a new Rectangle object.

        Args:
            width (int): The width of the Rectangle.
            height (int): The height of the Rectangle.
        """
        self.width = width
        self.height = height

    @property
    def width(self):
        """Get/set width of the Rectangle."""
        return self.__width

    @width.setter
    def width(self, value):
        if not isinstance(value, int):
            raise TypeError("width must be an integer")
        if value < 0:
            raise ValueError("width must be >= 0")
        self.__width = value

    @property
    def height(self):
        """Get/set height of the Rectangle."""
        return self.__height

    @height.setter
    def height(self, value):
        if not isinstance(value, int):
            raise TypeError("height must be an integer")
        if value < 0:
            raise ValueError("height must be >= 0")
        self.__height = value

    def area(self):
        """Computes the rectangle area."""
        return self.__width * self.__height

    def perimeter(self):
        """Computes the rectangle perimeter."""
        if self.__width == 0 or self.__height == 0:
            return 0
        return 2 * (self.__width + self.__height)
