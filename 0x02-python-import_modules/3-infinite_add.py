#!/usr/bin/python3
from sys import argv


def main():
    argc = len(argv) - 1
    s = 0

    if not argc:
        print('0')
    else:
        for x in argv[1:]:
            s += int(x)

        print('{:d}'.format(s))


if __name__ == '__main__':
    main()
