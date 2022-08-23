#!/usr/bin/python3
def print_last_digit(number):
    """prints the last digit of a number"""
    last_digit = number % 10
    if (number < 0):
        last_digit = 10 - last_digit
    print("{}".format(last_digit), end="")
    return (last_digit)
