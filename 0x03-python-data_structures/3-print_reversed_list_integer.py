#!/usr/bin/python3

def print_reversed_list_integer(my_list=[]):
    """Prints all integers of a list in reverse order."""
    if isinstance(my_list, list):
        my_list.reverse()
        i = 0
        while (i < len(my_list)):
            print("{:d}".format(my_list[i]))
            i = i + 1
