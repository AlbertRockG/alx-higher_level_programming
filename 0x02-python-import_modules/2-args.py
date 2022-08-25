#!/usr/bin/python3
# 1-calculation.py
# Albert G
# utf-8

def print_args(argv):
    if (len(argv) <= 1):
        print("0 arguments.")
    elif (len(argv) == 2):
        print("{:d} argument:".format(len(argv) - 1))
        print("1: {:d}".format(argv[1]))
    else:
        print("{:d} arguments:".format(len(argv) - 1))
        for i in range(1, len(argv)):
            print("{:d}: {:d}".format(i, argv[i]))

if __name__ == "__main__":
    import sys
    print_args(sys.argv)
