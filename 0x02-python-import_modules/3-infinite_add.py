#!/usr/bin/python3
def add_arg(argv):
    nz = len(argv) - 1
    if nz == 0:
        print("{:d}".format(nz))
        return
    else:
        iz = 1
        addz = 0
        while iz <= nz:
            addz += int(argv[iz])
            iz += 1
        print("{:d}".format(addz))


if __name__ == "__main__":
    import sys
    add_arg(sys.argv)
