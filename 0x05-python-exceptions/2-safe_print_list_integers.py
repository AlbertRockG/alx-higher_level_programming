#!/usr/bin/python3
# 2-safe_print_list_integers.py
# AlbertG (rafgangbadja@gmail.com)

def safe_print_list_integers(my_list=[], x=0):
    """Prints the first x elements of a list and only integers. 

    Args:
        my_list (list): The given list.
        x (int): The number of elements to print.

    Returns:
        The real number of integers printed.
    """
    intNumber = 0
    for i in range(x):
        try:
            print("{:d}".format(my_list[i]), end="")
            intNumber += 1
        except (TypeError, ValueError):
            continue
    print("")

    return (intNumber)
