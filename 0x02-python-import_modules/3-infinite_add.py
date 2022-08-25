#!/usr/bin/python3
# 3-infinite_add.py
# Albert G


def infinite_addition(argv):
    """ Computes the sum of all its arguments
    Args:
        argv: list of command line arguments

    Returns:
        The return value: sum of all of its arguments
    """
    sum = 0

    if (len(argv) <= 1):
        pass
    else:
        for i in range(1, len(argv)):
            sum = sum + int(argv[i])

    return (sum)


if __name__ == "__main__":
    import sys
    print("{:d}".format(infinite_addition(sys.argv)))
