#!/usr/bin/python3
def print_matrix_integer(matrix=[[]]):
    for sub_matrix in matrix:
        for i in range(len(sub_matrix)):
            print("{:d}".format(sub_matrix[i]), end='')
            if i < len(sub_matrix) - 1:
                print(' ', end='')
        print()
