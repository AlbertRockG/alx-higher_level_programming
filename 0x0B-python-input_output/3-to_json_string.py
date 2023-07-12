#!/usr/bin/python3
# 3-to_json_string.py
# AlbertRockG
"""Defines string to JSON transformation fucntion."""
import json


def to_json_string(my_obj):
    """Returns a JSON representation from a string."""
    return json.dumps(my_obj)
