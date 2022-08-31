#!/usr/bin/python3
"""This script adds all arguments to a Python list,
and then save them to JSON file.
"""
import sys import argv
from os.path import exists as file_exists


save_to_json_file = __import__('5-save_to_json_file').save_to_json_file
load_from_json_file = __import__('6-load_from_json_file').load_from_json_file

filename = "add_item.json"
if file_exists(filename) is False:
    with open(filename, 'w+', encoding="utf-8") as f:
        save_to_json_file([], filename)

json_obj = load_from_json_file(filename)
json_obj.extend(argv[1:])
save_to_json_file(json_obj, filename)
