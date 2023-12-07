#!/usr/bin/python3
def roman_to_int(roman_string: str):
    if roman_string is None or type(roman_string) != str:
        return 0
    dataz = {'I': 1, 'V': 5, 'X': 10, 'L': 50, 'C': 100, 'D': 500, 'M': 1000}
    numbersz = [data[x] for x in roman_string] + [0]
    repz = 0

    for zz in range(len(numbers) - 1):
        if numbers[zz] >= numbers[zz+1]:
            repz += numbers[zz]
        else:
            repz -= numbers[zz]

    return repz
