#!/usr/bin/python3


def list_division(my_list_1, my_list_2, list_length):
    new_listz = []
    for iz in range(0, list_length):
        try:
            divz = my_list_1[iz] / my_list_2[iz]
        except TypeError:
            print("wrong type")
            divz = 0
        except ZeroDivisionError:
            print("division by 0")
            divz = 0
        except IndexError:
            print("out of range")
            divz = 0
        finally:
            new_listz.append(divz)
    return (new_listz)
