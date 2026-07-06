#!/usr/bin/python3
# Replaces an element in a list without modifying original


def new_in_list(my_list, idx, element):
    # Returns new list with replaced element
    if idx < 0 or idx >= len(my_list):
        return my_list.copy()
    new_list = my_list.copy()
    new_list[idx] = element
    return new_list
