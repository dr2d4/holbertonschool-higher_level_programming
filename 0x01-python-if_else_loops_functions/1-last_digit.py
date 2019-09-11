#!/usr/bin/python3
import random
number = random.randint(-10000, 10000)
tmp = number % 10

print('Last digit of {:d} is {:d} '.format(number, tmp), end='')

if tmp > 5 and tmp != 6:
        print('and is greater that 5')
elif not tmp:
	print('and is 0')
else:
	print('and is less 6 and not 0')
	
