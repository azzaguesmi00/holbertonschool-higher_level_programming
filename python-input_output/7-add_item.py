#!/usr/bin/python3
""" defining add_item function"""

import sys
save_to_json_file = __import__('5-save_to_json_file').save_to_json_file
load_from_json_file = __import__('6-load_from_json_file').load_from_json_file

arglist = list(sys.argv[1:])

try:
    ol_da = load_from_json_file('add_item.json')
except Exception:
    ol_da = []
    
ol_da.extend(arglist)
save_to_json_file(ol_da, 'add_item.json')
