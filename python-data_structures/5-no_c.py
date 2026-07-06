#!/usr/bin/python3
# Removes all c and C from a string


def no_c(my_string):
    # Returns string without c and c
    return "".join([i for i in my_string if i != 'c' and i != 'C'])
