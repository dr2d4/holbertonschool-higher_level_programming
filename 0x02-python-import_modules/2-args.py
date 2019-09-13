#!/usr/bin/python3
from sys import argv


def main():
    argc = len(argv) - 1

    if not argc:
        print('0 arguments.')
    else:
        print('{:d} argument{}:'.format(argc, "s" if argc > 1 else ""))

        for i, x in enumerate(argv[1:], 1):
            print('{:d}: {:s}'.format(i, x))


if __name__ == '__main__':
    main()
