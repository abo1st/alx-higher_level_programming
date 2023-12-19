#!/usr/bin/python3


def safe_print_division(a, b):
    try:
        divz = a / b
    except (TypeError, ZeroDivisionError):
        divz = None
    finally:
        print("Inside result: {}".format(divz))
    return (divz)
