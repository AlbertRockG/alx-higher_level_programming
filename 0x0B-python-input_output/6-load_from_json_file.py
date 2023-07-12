#!/usr/bin/python3
# 6-load_from_json_file.py
# AlbertRockG
"""Defines JSON file-deserializing function."""
import json


def load_from_json_file(filename):
    """Creates an Object from a JSON file."""
    with open(filename, mode="r", encoding="utf-8") as fp:
        return json.load(fp)
