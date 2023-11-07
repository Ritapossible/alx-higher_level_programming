#!/usr/bin/python3
"""
file: 10-class_to_json.py
functions:
-> class_to_json
"""


def class_to_json(obj):
    """ Retuns the dictionary description with a simple data structure """

    structure = {}
    if hasattr(obj, "__dict__"):
        structure = obj.__dict__.copy()
    return structure
