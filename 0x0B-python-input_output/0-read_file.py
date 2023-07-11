#!/usr/bin/python3
# 0-read_file.py
# AlbertRockG
"""Defines a text file-reading function."""


def read_file(filename=""):
    """Reads and prints to sdout the contents of a UTF8 text file."""
    with open(filename, encoding="utf-8") as file:
        print(file.read(), end="")
