#!/usr/bin/python3
# 8-class_to_json.py
# AlbertRockG
"""Defines a dictionary object-describing function."""


def class_to_json(obj):
    """Returns the dictionary description."""
    return obj.__dict__
