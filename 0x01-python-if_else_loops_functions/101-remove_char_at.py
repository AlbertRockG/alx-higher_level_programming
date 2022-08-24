#!/usr/bin/python3
def remove_char_at(str, n):
    """Create a copy of the string, removing the character at the position n"""
    if (n < 0):
        return (str)
    return (str[:n] + str[n+1:])
