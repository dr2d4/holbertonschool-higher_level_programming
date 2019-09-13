#!/usr/bin/python3
from calculator_1 import add, sub, mul, div
from sys import argv


def main():
    argc = len(argv) - 1

    if argc != 3:
        print('Usage: ./100-my_calculator.py <a> <operator> <b>')
        exit(1)

    if argv[2] not in ['+', '-', '*', '/']:
        print('Unknown operator. Available operators: +, -, * and /')
        exit(1)

    a = int(argv[1])
    b = int(argv[3])
    o = argv[2]

    if o == '+':
        fun = add
    elif o == '-':
        fun = sub
    elif o == '*':
        fun = mul
    else:
        fun = div

    print('{:d} {} {:d} = {:d}'.format(a, o, b, fun(a, b)))


if __name__ == '__main__':
    main()
