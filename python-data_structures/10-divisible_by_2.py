#!/usr/bin/python3
# Finds all multiples of 2 in a list


def divisible_by_2(my_list=[]):
    return [i % 2 == 0 for i in my_list]
