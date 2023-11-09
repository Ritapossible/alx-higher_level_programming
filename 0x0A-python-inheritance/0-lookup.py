#!/usr/bin/python3
"""lookup module"""


def lookup(obj):
    """lookup method
    Returns: a list of the available attributes and methods of an object"""
    return dir(obj)
