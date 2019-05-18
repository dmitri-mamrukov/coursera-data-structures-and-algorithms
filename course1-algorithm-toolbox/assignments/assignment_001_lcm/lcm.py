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

def lcm(a, b):
    """Given two integers a and b, finds their least common multiple.

    The least common multiple LCM(a, b) of two positive integers a and b is
    the least positive integer m that is divisible by both a and b.

    For any two positive integers a and b, LCM(a, b) * GCD(a, b) = a * b.

    Therefore, LCM(a, b) = (a * b) / GCD(a, b)
    """
    return (a * b) // gcd(a, b)

if __name__ == '__main__':
    input = sys.stdin.read()
    a, b = map(int, input.split())

    print(lcm(a, b))
