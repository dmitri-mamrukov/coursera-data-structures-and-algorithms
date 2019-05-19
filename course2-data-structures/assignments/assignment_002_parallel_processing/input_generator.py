#!/usr/bin/python3

import math
from random import randint

N = int(math.pow(10, 5))
M = int(math.pow(10, 5))
MAX_TIME = int(math.pow(10, 9))

def generate_sequence():
#     n = randint(1, N)
#     m = randint(1, M)
    n = randint(1, N)
    m = M
    print('%s %s' % (n, m))

    for i in range(0, m):
        t = randint(0, MAX_TIME)
        print('%s' % t, end=' ')

    print()

if __name__ == '__main__':
    generate_sequence()
