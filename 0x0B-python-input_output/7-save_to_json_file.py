#!/usr/bin/python3
"""
Save JSON to file
"""

import json


def save_to_json_file(my_obj, filename):
    """
    Save JSON to file
    """

    with open(filename, mode="w", encoding="utf-8") as f:
        json_str = json.dumps(my_obj)
        f.write(json_str)
