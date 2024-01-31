#!/usr/bin/python3

def print_matrix_integer(matrix=[[]]):
    if not matrix:
        return
    for new in range(len(matrix)):
        for idx in range(len(matrix[new])):
            print("{:d}".format(matrix[new][idx]), end="")
            if idx < len(matrix[new]) - 1:
                print(end=" ")
        print()
