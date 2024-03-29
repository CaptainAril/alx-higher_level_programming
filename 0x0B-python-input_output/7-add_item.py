#!/usr/bin/python3
"""adds all arguments to a Python list, and saves them in a JSON file."""
from sys import argv
from os.path import exists as file_exists


save_to_json_file = __import__('5-save_to_json_file').save_to_json_file
load_from_json_file = __import__('6-load_from_json_file').load_from_json_file

filename = "add_item.json"
if file_exists(filename):
    json_obj = load_from_json_file(filename)
else:
    json_obj = []

json_obj.extend(argv[1:])
save_to_json_file(json_obj, filename)
