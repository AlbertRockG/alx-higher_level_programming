#!/usr/bin/python3
def magic_string():
    magic_string.iterations = getattr(magic_string, 'iterations', 0) + 1
    return "BestSchool, " * (magic_string.iterations - 1) + "BestSchool"
