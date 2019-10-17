#!/usr/bin/python3
"""
Load JSON from file
"""


import json


def load_from_json_file(filename):
    """
    Load JSON from file
    """

    with open(filename) as f:
        json_obj = json.load(f)

    return json_obj
