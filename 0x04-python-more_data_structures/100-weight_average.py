#!/usr/bin/python3
def weight_average(my_list=[]):
    if not my_list:
        return 0

    numz = 0
    denz = 0

    for tupz in my_list:
        numz += tupz[0] * tupz[1]
        denz += tupz[1]

    return (numz / denz)
