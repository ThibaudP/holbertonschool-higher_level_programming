#!/usr/bin/python3
"""add_item module"""
import json
from sys import argv
save_to_json_file = __import__('5-save_to_json_file').save_to_json_file
load_from_json_file = __import__('6-load_from_json_file').load_from_json_file


if __name__ == "__main__":
    argc = len(argv)
    file = "add_item.json"

    try:
        list = load_from_json_file(file)
    except:
        list = []

    for i in range(1, argc):
        list.append(argv[i])

    save_to_json_file(list, file)
