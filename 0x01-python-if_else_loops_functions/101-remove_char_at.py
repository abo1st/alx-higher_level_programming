#!/usr/bin/python3
def remove_char_at(str, n):
        new = ""
            zz = 0
                for c in str:
                            if zz != n:
                                            new += c
                                                    zz += 1
                                                        return new
