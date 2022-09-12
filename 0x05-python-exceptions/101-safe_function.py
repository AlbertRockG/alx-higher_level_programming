#!/usr/bin/python3
# 101-safe_function.py
# AlbertG <rafgangbadja@gmail.com>

import sys


def safe_function(fct, *args):
    """Executes a function safely.

    Args:
        fct: The function to execute.
        args: Arguments for fct.

    Returns:
        If an error occurs - None.
        Otherwise - the result of the call to fct.
    """
    try:
        result = fct(*args)
        return (result)
    except Exception as error:
        print("Exception: {}".format(error), file=sys.stderr)
        return (None)
