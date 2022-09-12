#!/usr/bin/python3
# 0-safe_print_list.py
# Albertg (rafgangbadja@gmail.com)

def safe_print_list(my_list=[], x=0):
    """Print x elements of a list.

    Args:
        my_list (list): The list to print elements from.
        x (int): The number of elements of my_list to print.

    Returns:
        The number of elements printed.
    """
    elementsNumber = 0
    for i in range(x):
        try:
            print("{:d}".format(my_list[i]), end="")
            elementsNumber+=1
        except IndexError:
            break
    print("")

    return (elementsNumber)
