#!/usr/bin/python3
"""Finds the biggest integer of a list"""


def max_integer(my_list=[]):
    """Returns the maximum integer"""
    if len(my_list) == 0:
        return None
    maximum = my_list[0]
    for i in my_list:
        if i > maximum:
            maximum = i
    return maximum
