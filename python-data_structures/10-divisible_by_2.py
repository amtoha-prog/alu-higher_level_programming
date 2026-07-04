#!/usr/bin/python3
#Finds all multiples of 2 in a list


def divisible_by_2(my_list=[]):
   # Returns list of True/False for divisibility by 2
    return [i % 2 == 0 for i in my_list]
