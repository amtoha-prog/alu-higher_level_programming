#!/usr/bin/python3
# Prints a matrix of integers


def print_matrix_integer(matrix=[[]]):
    # Prints matrix row by row
    for row in matrix:
        print(" ".join("{:d}".format(i) for i in row))
