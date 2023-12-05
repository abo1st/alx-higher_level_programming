#!/usr/bin/python3
def divisible_by_2(my_list=[]):
    boolistz = my_list[:]
    for countz, iz in enumerate(my_list):
        if iz % 2 == 0:
            boolistz[countz] = True
        else:
            boolistz[countz] = False
    return(boolistz)
