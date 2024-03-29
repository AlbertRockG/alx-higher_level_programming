#!/usr/bin/python3
# AlbertRockG
# 1-rectangle.py
# -*- coding: utf-8 -*-
"""Defines a class named Rectangle"""


class Rectangle():
    """Represents a Rectangle.

    Attributes:
        Number_of_instances (int): The number of Rectangle instances.
        print_symbol (str): The print symbol to represent Rectangle instances.
    """
    number_of_instances = 0
    print_symbol = '#'

    def __init__(self, width=0, height=0):
        """Initialize a new Rectangle object.

        Args:
            width (int): The width of the Rectangle.
            height (int): The height of the Rectangle.
        """
        Rectangle.number_of_instances += 1
        self.width = width
        self.height = height

    @property
    def width(self):
        """Get/Set width of the Rectangle."""
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
        """Get/Set height of the Rectangle."""
        return self.__height

    @height.setter
    def height(self, value):
        if not isinstance(value, int):
            raise TypeError("height must be an integer")
        if value < 0:
            raise ValueError("height must be >= 0")
        self.__height = value

    def area(self):
        """Computes the area of the Rectangle."""
        return self.__width * self.__height

    def perimeter(self):
        """Computes the perimeter of the Rectangle."""
        if self.__width == 0 or self.__height == 0:
            return 0
        return 2 * (self.__width + self.__height)

    def __str__(self):
        """Returns the printable representation of the Rectangle."""
        if self.__width == 0 or self.__height == 0:
            return ""
        rect = []
        for i in range(self.__height):
            [rect.append(str(self.print_symbol)) for j in range(self.__width)]
            if i != self.__height - 1:
                rect.append('\n')
        return "".join(rect)

    def __repr__(self):
        """Returns a string representation of the Rectangle"""
        return "Rectangle({}, {})".format(self.__width, self.__height)

    def __del__(self):
        """Prints a message for every Rectangle's instance destroyed"""
        Rectangle.number_of_instances -= 1
        print("Bye rectangle...")

    @staticmethod
    def bigger_or_equal(rect_1, rect_2):
        """Returns the biggest rectangle based on the area.

        Args:
            rect_1 (Rectangle): The first Rectangle instance.
            rect_2 (Rectangle): The second Rectangle instance.
        """
        if not isinstance(rect_1, Rectangle):
            raise TypeError("rect_1 must be an instance of Rectangle")
        if not isinstance(rect_2, Rectangle):
            raise TypeError("rect_2 must be an instance of Rectangle")
        rect_1_area = rect_1.__width * rect_1.__height
        rect_2_area = rect_2.__width * rect_2.__height

        return rect_1 if rect_1_area >= rect_2_area else rect_2

    @classmethod
    def square(Rectangle, size=0):
        """Returns a new Rectangle instance with width=height==size."""
        return Rectangle(size, size)
