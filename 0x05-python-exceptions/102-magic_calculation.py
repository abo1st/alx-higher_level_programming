#!/usr/bin/python3


def magic_calculation(a, b):
    resultz = 0
    for izz in range(1, 3):
        try:
            if izz > a:
                raise Exception('Too far')
            else:
                resultz += a ** b / izz
        except Exception:
            resultz = b + a
            break
    return (resultz)
