#!/usr/bin/python3

def safe_print_list(my_list=[], x=0):
    totalz = 0
    for zz in range(x):
        try:
            print("{}".format(my_list[zz]), end="")
            totalz += 1
        except IndexError:
            break
    print("")
    return (totalz)
