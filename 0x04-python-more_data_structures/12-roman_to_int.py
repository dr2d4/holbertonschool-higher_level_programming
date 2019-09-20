#!/usr/bin/python3


def roman_to_int(roman_string):
    rd = {'I': 1, 'V': 5, 'X': 10, 'L': 50, 'C': 100, 'D': 500, 'M': 1000}
    ls = len(roman_string) // 2 + len(roman_string) % 2
    rs = roman_string
    s = 0

    for x in range(0, ls * 2, 2):
        lr = rs[x:x + 2]

        if (len(lr) == 2):
            l, r = lr

            l = rd.get(l, 0)
            r = rd.get(r, 0)

            if l < r:
                s += r - l
            else:
                s += r + l
        else:
            s += rd.get(lr)

    return s
