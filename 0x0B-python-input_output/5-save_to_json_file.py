#!/usr/bin/python3
# 5-save_to_json_file.py
# AlbertRockG
"""Defines a JSON file-writing function."""
import json


def save_to_json_file(my_obj, filename):
    """Writes an Object to a text file using JSON."""
    with open(filename, mode="w", encoding="utf-8") as fp:
        json.dump(my_obj, fp)
