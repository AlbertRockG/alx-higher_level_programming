#!/usr/bin/python3
# 1-write_file.py
# AlbertRockG
"""Defines a text file-appending function."""


def append_write(filename="", text=""):
    """Appends a string to text file and count the number of character."""
    with open(filename, mode="a", encoding="utf-8") as file:
        file.write(text)
        return len(text)
