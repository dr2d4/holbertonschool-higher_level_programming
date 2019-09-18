#!/usr/bin/python3


def add_tuple(tuple_a=(), tuple_b=()):
	a = list(tuple_a)
	b = list(tuple_b)

	for x in range(len(a), 2):
		a.append(0)

	for x in range(len(b), 2):
		b.append(0)

	return (a[0] + b[0], a[1] + b[1])