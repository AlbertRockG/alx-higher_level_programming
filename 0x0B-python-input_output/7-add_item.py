#!/usr/bin/python3
# 7-add_item.py
# AlbertRockG
"""Adds all arguments to a Python list and save to a file."""
import json
import sys
from os.path import exists


def save_to_json_file(my_obj, filename):
    """Writes an Object to a text file using JSON."""
    with open(filename, mode="w", encoding="utf-8") as fp:
        json.dump(my_obj, fp)


def load_from_json_file(filename):
    """Creates an Object from a JSON file."""
    with open(filename, mode="r", encoding="utf-8") as fp:
        return json.load(fp)


args = sys.argv[1:]
filename = "add_item.json"

if exists(filename):
    my_list = load_from_json_file(filename)
else:
    my_list = []

my_list.extend(args)
save_to_json_file(my_list, filename)
