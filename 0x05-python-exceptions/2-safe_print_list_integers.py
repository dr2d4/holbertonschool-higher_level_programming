#!/usr/bin/python3


def safe_print_list_integers(my_list=[], x=0):
    eax = 0

    for ecx in range(x):
        try:
            print('{:d}'.format(my_list[ecx]), end='')
            eax += 1
        except (TypeError, ValueError):
            continue

    print()
    return eax
