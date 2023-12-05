#!/usr/bin/python3
def print_matrix_integer(matrix=[[]]):
    for iz in matrix:
        print(' '.join('{:d}'.format(jz)for jz in iz))
