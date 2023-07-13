#!/usr/bin/python3
# 10-student.py
# AlbertRockG
"""Defines a class Student."""


class Student:
    """Represents a student."""

    def __init__(self, first_name, last_name, age):
        """Initialize a Student instance.

        Args:
            first_name (str): The first name of the student.
            last_name (str): The last name of the student.
            age (int): The age of the student.
        """
        self.first_name = first_name
        self.last_name = last_name
        self.age = age

    def to_json(self, attrs=None):
        """Get the dictionary representation of Student.

        if attrs is a list of strings, get only attribute names
        contained in this list.
        Args:
            attrs (list):  List of attributes to be retrieved.
        """
        if (type(attrs) == list and
                all(type(elts) == str for elts in attrs)):
            return {k: getattr(self, k) for k in attrs if hasattr(self, k)}
        return self.__dict__
