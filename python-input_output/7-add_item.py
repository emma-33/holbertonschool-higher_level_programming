#!/usr/bin/python3
"""Adds all arguments to a Python list, and
then save them to a file
"""
import sys
save_file = __import__('5-save_to_json_file').save_to_json_file
load_file = __import__('6-load_from_json_file').load_from_json_file

filename = "add_item.json"

try:
    my_list = load_file(filename)
except FileNotFoundError:
    my_list = []

for arg in sys.argv[1:]:
    my_list.append(arg)

save_file(my_list, filename)
