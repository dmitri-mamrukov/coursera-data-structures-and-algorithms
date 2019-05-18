#!/usr/bin/python3

import sys

from util import Util

if __name__ == '__main__':
    input = sys.stdin.read()
    tokens = input.split()
    a = int(tokens[0])
    b = int(tokens[1])

    print(Util.sum(a, b))
