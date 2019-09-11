#!/usr/bin/python3

for x in reversed(range(26)):
    if not x % 2:
        x = x - 32

    print('{:c}'.format(ord('a') + x), end='')
