#!/usr/bin/python3

import math
from random import randint

def generate_sequence(n):
    for i in range(0, n):
        v = randint(int(-1 * math.pow(10, 5)), int(math.pow(10, 5)))
        if (i == n - 1):
            print(v)
        else:
            print(v, end = ' ')

if __name__ == '__main__':
    n = int(math.pow(10, 3))
    print(n)
    generate_sequence(n)
    generate_sequence(n)
