#!/usr/bin/python3
"""defining from_json_string"""

import json

def from_json_string(my_str):
    """
    return json string
    Args:
        my_str: str
    """
    return json.loads(my_str)
