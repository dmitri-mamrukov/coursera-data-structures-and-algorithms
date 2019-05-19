#!/usr/bin/python3

import math
from random import randint

NUM_OF_VERTICES = int(math.pow(10, 5))
NUM_OF_EDGESS = int(math.pow(10, 5))

def generate_sequence(n, m):
    print('%s %s' % (n, m))

    edges = []
    for i in range(0, m):
        u, v = 1, 2
        while (u, v) in edges:
            u = randint(1, NUM_OF_VERTICES)
            v = randint(1, NUM_OF_VERTICES)
        edges.append((u, v))
        print('%s %s' % (u, v))

if __name__ == '__main__':
    n, m = NUM_OF_VERTICES, NUM_OF_EDGESS
    generate_sequence(n, m)
