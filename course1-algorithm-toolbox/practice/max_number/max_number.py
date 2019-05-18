#!/usr/bin/python3

import sys

def __check_args(digits):
    for d in digits:
        assert(0 <= d and d <= 9)

def solve(digits):
    """The goal in this problem is to find the maximum number consisting of
    the given digits.

    Greedy Strategy:

    Select and remove the maximum digit and continue on the truncated digits.
    Otherwise, we are done.

    Safety Proof:

    We get the most significant digit every time, so the maximal
    result is guaranteed.
    """
    __check_args(digits)

    digits.sort(reverse = True)

    result = 0
    for i in digits:
        result = result * 10 + i

    return result

if __name__ == '__main__':
    input = sys.stdin.read()
    digits = list(map(int, input.split()))

    print(solve(digits))
