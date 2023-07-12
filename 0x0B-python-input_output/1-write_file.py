#!/usr/bin/python3
# 1-write_file.py
# AlbertRockG
"""Defines a text file-writing function."""


def write_file(filename="", text=""):
    """Writes a string to text file and count the number of character."""
    with open(filename, mode="w", encoding="utf-8") as file:
        file.write(text)
        return len(text)
