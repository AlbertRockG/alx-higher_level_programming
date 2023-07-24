#!/usr/bin/python3
# square.py
# AlbertRockG
"""Defines a Square class."""
from models.rectangle import Rectangle


class Square(Rectangle):
    """Represent a square."""

    def __init__(self, size, x=0, y=0, id=None):
        """Initialize a new Square.

        Args:
            size (int): The size of the new Square.
            x (int): The x coordinate of the new Square.
            y (int): The y coordinate of the new Square.
            id (int): The identity of the new Square.
        """
        super().__init__(size, size, x, y, id)

    @property
    def size(self):
        """Get/set the size of the Square."""
        return self.__width

    @size.setter
    def size(self, value):
        self.__width = value
        self.__height = value

    def update(self, *args, **kwargs):
        """Update the Square.

        Args:
            *args (ints): New attribute values.
                - 1st argument represents id attribute
                - 2nd argument represents size attribute
                - 3rd argument represents x attribute
                - 4th argument represents y attribute
            **kwargs (dict): New key/value pairs of attributes.
        """
        if args is None:
            return

        if args and len(args):
            num_args = len(args)
            if num_args >= 1:
                self.id = args[0]
            if num_args >= 2:
                self.__width = args[1]
            if num_args >= 3:
                self.__height = args[2]
            if num_args >= 4:
                self.__x = args[3]
            if num_args >= 5:
                self.__y = args[4]

        elif kwargs and len(kwargs) != 0:
            for k, v in kwargs.items():
                if k == "id":
                    self.id = v
                elif k == "width":
                    self.__width = v
                elif k == "height":
                    self.__height = v
                elif k == "x":
                    self.__x = v
                elif k == "y":
                    self.__y = v

    def to_dictionary(self):
        """Return the dictionary representation of the Square."""
        return self.__dict__

    def __str__(self):
        """Return the print() and str() representation of a Square."""
        return "[Square] ({}) {}/{} - {}".format(
            self.id, self.x, self.y, self.width
            )
