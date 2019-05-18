#!/usr/bin/python3

import sys

def __check_args(n):
    assert(0 <= n)

def calc_fibonacci(n):
    """Given an integer n, finds the nth Fibonacci number Fn.
    """
    __check_args(n)

    a, b = 0, 1

    for i in range(0, n):
        a, b = b, a + b

    return a

def calc_fibonacci_slow(n):
    """Given an integer n, finds the nth Fibonacci number Fn.
    """
    __check_args(n)

    if n <= 1:
        return n

    return calc_fibonacci_slow(n - 1) + calc_fibonacci_slow(n - 2)

if __name__ == '__main__':
    n = int(input())

    print(calc_fibonacci(n))
