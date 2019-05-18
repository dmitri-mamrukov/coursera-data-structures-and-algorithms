#!/usr/bin/python3

import sys

from util import Util

if __name__ == '__main__':
    n = int(input())
    data = [ int(x) for x in input().split() ]

    print(Util.max_pairwise_product(data))
