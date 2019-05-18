#!/usr/bin/python3

from math import ceil
import sys

DEBUG = False

def __check_args(a, b, n):
    assert(len(a) == len(b))
    assert(0 <= n)
    assert(len(a) == n)
    assert(len(b) == n)

def karatsuba(x, y):
    """Recursive multiplication using the Karatsuba algorithm:

    Suppose we have two integers x and y where they each have n digits.

    x = a * 10^n/2 + b
    y = c * 10^n/2 + d

    So we have:

    x * y = ac * 10^n + (ad + bc) * 10^n/2 + bd,

    where (ad + bc) = (a + b)(c + d) - ac - bd.
    """
    if x < 10 or y < 10:
        if DEBUG:
            print ('x: %s, y: %s, x * y = %s' % (x, y, x * y))

        return x * y

    # get the maximum size of the numbers in base 10
    n = max(len(str(x)), len(str(y))) // 2

    # split the digit sequences around the middle
    cut = pow(10, n)
    a, b = x // cut, x % cut
    c, d = y // cut, y % cut

    if DEBUG:
        print ('x: %s -> a: %s, b: %s ### y: %s c: %s, d: %s, ' %
            (x, a, b, y, c, d))

    # divide and conquer
    z0 = karatsuba(a, c)
    z1 = karatsuba((a + b), (c + d))
    z2 = karatsuba(b, d)

    return z0 * pow(10, 2 * n) + (z1 - z0 - z2) * pow(10, n) + z2

if __name__ == '__main__':
    x, y = map(int, input().split())

    print(karatsuba(x, y))
