#!/usr/bin/python3

import math
from random import randint

MAX_SEGMENTS = 5 * int(math.pow(10, 5))
MAX_POINTS = 5 * int(math.pow(10, 5))
MAX_A = int(math.pow(10, 8))
MAX_B = int(math.pow(10, 8))

def generate_sequence(s, p):
    print('%s %s' % (s, p))

    for i in range(0, s):
        a = randint(-1 * MAX_A, MAX_A)
        b = randint(a, MAX_B)
        print('%s %s' % (a, b))

    for i in range(0, p):
        point = randint(-1 * MAX_A, MAX_A)
        if i == p - 1:
            print('%s' % point)
        else:
            print('%s' % point, end = ' ')

    print()

if __name__ == '__main__':
    s, p = MAX_SEGMENTS, MAX_POINTS
    generate_sequence(s, p)
