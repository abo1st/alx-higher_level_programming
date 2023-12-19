#!/usr/bin/python3


def safe_print_list_integers(my_list=[], x=0):
    retz = 0
    for zz in range(0, x):
        try:
            print("{:d}".format(my_list[zz]), end="")
            retz += 1
        except (ValueError, TypeError):
            continue
    print("")
    return (retz)
