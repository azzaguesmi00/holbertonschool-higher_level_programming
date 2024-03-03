#!/usr/bin/python3
"""defining load_from_json_file"""

import json

def load_from_json_file(filename):
    """
    create an object from json file
    Args:
        filename : file
    """
    with open(filename, 'r', encoding="utf-8") as f:
        return json.load(f)
