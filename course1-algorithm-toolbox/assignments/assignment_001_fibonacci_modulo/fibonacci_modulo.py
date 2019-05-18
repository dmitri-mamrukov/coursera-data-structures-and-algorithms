#!/usr/bin/python3

import sys

DEBUG = False

def __check_args(n, m):
    assert(1 <= n)
    assert(2 <= m)

def calc_fibonacci(n):
    """Given an integer n, finds the nth Fibonacci number Fn.
    """
    a, b = 0, 1

    for i in range(0, n):
        a, b = b, a + b

    return a

def calc_fibonacci_modulo(n, m):
    """Given two integers n and m, outputs Fn mod m
    (that is, the remainder of Fn when divided by m).

    In this problem, the given number n may be really huge. Hence an algorithm
    looping for n iterations will not fit into one second (of running time)
    for sure. Therefore we need to avoid such a loop.

    To get an idea how to solve this problem without going through all Fi
    for i from 0 to n, let’s see what happens when m is small — say,
    m = 2 or m = 3.

    i        | 0    1    2    3    4    5    6     7     8     9    10    11
    Fi       | 0    1    1    2    3    5    8    13    21    34    55    89
    Fi mod 2 | 0    1    1    0    1    1    0     1     1     0     1     1
    Fi mod 3 | 0    1    1    2    0    2    2     1     0     1     1     2
    Fi mod 4 | 0    1    1    2    3    1    0     1     1     2     3     1

    Take a detailed look at this table. Do you see? Both these sequences are
    periodic! For m = 2, the period is 011 and has length 3, while for m = 3
    the period is 01120221 and has length 8. Therefore, to compute, say,
    F2015 mod 3 we just need to find the remainder of 2015 when divided
    by 8. Since 2015 = 251 * 8 + 7, we conclude that F2015 mod 3 =
    F7 mod 3 = 1.

    For any integer m >= 2, the sequence Fn mod m is periodic.
    The period always starts with 01 and is known as Pisano period.
    """
    __check_args(n, m)

    r1, r2 = 0, 1
    sequence_length = 1

    for i in range(0, n):
        r1, r2 = r2, (r1 + r2) % m
        if (r1 == 0 and r2 == 1):
            # The Pisano period is encountered.
            break
        else:
            sequence_length += 1

    if DEBUG:
        print ('n = %s, seq = %s, m = %s, n -> %s' % \
            (n, sequence_length, m, n % sequence_length))

    return calc_fibonacci(n % sequence_length) % m

def calc_fibonacci_modulo_still_slow(n, m):
    """Given two integers n and m, outputs Fn mod m
    (that is, the remainder of Fn when divided by m).
    """
    __check_args(n, m)

    r1, r2 = 0, 1
    sequence_length = 1

    a, b = 0, 1

    for i in range(0, n):
        a, b = b, a + b
        r1, r2 = a % m, b % m
        if (r1 == 0 and r2 == 1):
            # The Pisano period is encountered.
            break
        else:
            sequence_length += 1

    if DEBUG:
        print ('n = %s, seq = %s, m = %s, n -> %s' % \
            (n, sequence_length, m, n % sequence_length))

    return calc_fibonacci(n % sequence_length) % m

def calc_fibonacci_modulo_slow(n, m):
    """Given two integers n and m, outputs Fn mod m
    (that is, the remainder of Fn when divided by m).
    """
    __check_args(n, m)

    a, b = 0, 1

    for i in range(0, n):
        a, b = b, a + b

    return a % m

if __name__ == '__main__':
    input = sys.stdin.read()
    n, m = map(int, input.split())

    print(calc_fibonacci_modulo(n, m))
