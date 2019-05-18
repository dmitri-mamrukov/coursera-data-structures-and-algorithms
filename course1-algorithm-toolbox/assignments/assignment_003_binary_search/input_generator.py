#!/usr/bin/python3

import math
from random import randint
from random import shuffle

def print_data(data):
    for i, v in enumerate(data):
        if (i == n - 1):
            print(v)
        else:
            print(v, end = ' ')

def generate_sequence(n):
    data = []
    for i in range(0, n):
        v = randint(0, int(math.pow(10, 9)))
        data.append(v)
    data.sort()

    print(n, end = ' ')
    print_data(data)

    shuffle(data)

    print(n, end = ' ')
    print_data(data)

if __name__ == '__main__':
    n = int(math.pow(10, 5))
    generate_sequence(n)
