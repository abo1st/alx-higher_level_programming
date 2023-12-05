#!/usr/bin/python3
def max_integer(my_list=[]):
    if len(my_list) == 0:
        return ("None")
    az = my_list[0]
    for bz in my_list:
        if bz > az:
            az = bz
    return (az)
