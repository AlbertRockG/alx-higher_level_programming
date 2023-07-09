#!/usr/bin/python3
"""Adds two integers"""


def add_integer(a, b=98):
    """Adds two integers.
    Args:
        a (int): The first given integer.
        b (int): The second given integer (default:98).
    """
    if not isinstance(a, (int, float)):
        raise TypeError("a must be an integer")
    if not isinstance(b, (int, float)):
        raise TypeError("b must be an integer")
    return int(a) + int(b)
