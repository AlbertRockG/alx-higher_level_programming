#!/usr/bin/python3
# 11-student.py
# AlbertRockG
"""Defines a class Student."""


class Student:
    """Represents a student."""

    def __init__(self, first_name, last_name, age):
        """Initialize a new student.

        Args:
            first_name (str): The first name of the student.
            last_name (str): The last name of the student.
            age (int): The age of the student.
        """
        self.first_name = first_name
        self.last_name = last_name
        self.age = age

    def to_json(self, attrs=None):
        """Get a dictionary representation of a student.

        if a list of strings is provided,
        only the attributes name in the list is retrieved.
        Args:
            attrs (list): (optional) List of attributes to be retrieved.
        """
        if (type(attrs) == list and
                all(type(elts) == str for elts in attrs)):
            return {k: getattr(self, k) for k in attrs if hasattr(self, k)}
        return self.__dict__

    def reload_from_json(self, json):
        """Replaces all attributes of a student.

        It'S assumed that json is always a dictionary with:
            key as public attribute name
            value as the value of the public attribute
        Args:
            json (dict): Dictionary representation of a student.
        """
        for k, v in json.items():
            setattr(self, k, v)
