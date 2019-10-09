#!/usr/bin/python3


def magic_string():
    setattr(magic_string, 'rcx', getattr(magic_string, 'rcx', 0) + 1)
    return ('Holberton, ' * getattr(magic_string, 'rcx', 0))[:-2]
