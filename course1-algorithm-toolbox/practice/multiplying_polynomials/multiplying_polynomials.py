#!/usr/bin/python3

from math import ceil
import sys

def __check_args(a, b, n):
    assert(len(a) == len(b))
    assert(0 <= n)
    assert(len(a) == n)
    assert(len(b) == n)

def solve_naively(a, b, n):
    """Computes multiplication of the 2 polynomials and returns their product.
    """
    __check_args(a, b, n)

    product = [ 0 ] * (2 * n - 1)

    for i in range(0, n):
        for j in range(0, n):
            product[i + j] = product[i + j] + a[i] * b[j]

    return product

if __name__ == '__main__':
    n = int(input());
    a = list(map(int, input().split()))
    b = list(map(int, input().split()))

    print(solve_naively(a, b, n))
