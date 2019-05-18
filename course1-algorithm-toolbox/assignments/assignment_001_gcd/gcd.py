#!/usr/bin/python3

import sys

def __check_args(a, b):
    assert(1 <= a)
    assert(1 <= b)

def __calc_gcd(a, b):
    if b == 0:
        return a

    return __calc_gcd(b, a % b)

def gcd(a, b):
    """Given two integers a and b, finds their greatest common divisor.

    The greatest common divisor GCD(a, b) of two non-negative integers
    a and b (which are not both equal to 0) is the greatest integer d
    that divides both a and b.
    """
    __check_args(a, b)

    if b > a:
        return __calc_gcd(b, a)
    else:
        return __calc_gcd(a, b)

def gcd_slow(a, b):
    __check_args(a, b)

    current_gcd = 1
    for d in range(2, min(a, b) + 1):
        if a % d == 0 and b % d == 0:
            if d > current_gcd:
                current_gcd = d

    return current_gcd

if __name__ == "__main__":
    input = sys.stdin.read()
    a, b = map(int, input.split())

    print(gcd(a, b))
