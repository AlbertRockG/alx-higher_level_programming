#!/usr/bin/python3
# 100-safe_print_integer_err.py
# AlbertG <rafgangbadja@gmail.com>

import sys


def safe_print_integer_err(value):
    """Prints an integer.

    Args:
        value (int): The integer to print.

    Returns:
        if a TypeError or ValueError occurs - False.
        Otherwise - True.
    """
    try:
        print("{:d}".format(value))
        return (True)
    except (TypeError, ValueError):
        print("Exception: {}".format(sys.exc_info()[1], file=sys.stderr))
        return (False)
