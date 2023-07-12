#!/usr/bin/python3
# 3-to_json_string.py
# AlbertRockG
"""Defines string to JSON transformation fucntion."""
import json


def from_json_string(my_str):
    """Returns a JSON representation from a string."""
    return json.loads(my_str)
