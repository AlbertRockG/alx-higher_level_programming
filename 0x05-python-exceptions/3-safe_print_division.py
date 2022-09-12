#!/usr/bin/python3
# 3-safe_print_division.py
# AlbertG <rafgangbadja@gmail.com>

def safe_print_division(a, b):
    """Divides 2 integers and prints the result.

    Args:
        a (int): The dividend.
        b (int): The divisor.

    Returns:
        The quotient of a/b.
        Otherwise, None.
    """

    try:
        div = a / b
    except (TypeError, ZeroDivisionError):
        div = None
    finally:
        print("Inside result:{}".format(div))
    return (div)
