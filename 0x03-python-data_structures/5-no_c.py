#!/usr/bin/python3
def no_c(my_string):
    new_str = ""
    for zz in my_string:
        if (zz != 'c') and (zz != 'C'):
            new_str += zz
    return (new_str)
