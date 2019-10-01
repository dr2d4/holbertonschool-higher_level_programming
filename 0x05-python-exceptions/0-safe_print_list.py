#!/usr/bin/python3


def safe_print_list(my_list=[], x=0):
    eax = 0

    try:
        for ecx in range(x):
            print('{}'.format(my_list[ecx]), end='')
            eax += 1
    except IndexError:
        pass

    print()
    return eax
