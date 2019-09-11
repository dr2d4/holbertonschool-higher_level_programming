#!/usr/bin/python3

for x in range(26):
    char = chr(ord('a') + x)

    if char not in ['q', 'e']:
        print('{}'.format(char), end='')
