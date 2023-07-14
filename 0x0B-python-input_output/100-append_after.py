#!/usr/bin/python3
# 100-append_after.py
# AlbertRockG
"""Defines a file line-inserting function after a pattern."""


def append_after(filename="", search_string="", new_string=""):
    """Inserts a line of text to a file after a specific pattern.

    Args:
        filename (str): The path to the file.
        search_string (str): The string to search.
        new_string (str): The string to insert.
    """
    with open(filename, mode="r+", encoding="utf-8") as handle:
        text = handle.readlines()
        tmp = []
        for line in text:
            tmp.append(line)
            if search_string in line:
                tmp.append(new_string)
        handle.seek(0)
        handle.writelines(tmp)
