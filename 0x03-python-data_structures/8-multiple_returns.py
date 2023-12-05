#!/usr/bin/python3
def multiple_returns(sentence):
    lengthz = len(sentence)
    first_charz = sentence[0] if lengthz > 0 else "None"
    tup = lengthz, first_charz
    return(tup)

