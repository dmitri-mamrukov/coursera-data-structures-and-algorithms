#!/usr/bin/python3

import math
import sys

def __check_args(n):
    assert(1 <= n and n <= int(math.pow(10, 3)))

def get_change(n):
    """The goal in this problem is to find the minimum number of coins
    needed to change the input value (an integer) into coins with
    denominations 1, 5, and 10.

    Greedy Strategy:

    Select a coin of the maximum denomination d that fits n.
    and continue on n - d. Otherwise, we are done.

    Safety Proof:

    Suppose we have an *optimal* solution of k changes of n and we can
    replace a subset of the k coins with one coin of the denomination d.
    The total value stays the same but we can reduce k. Contradiction.
    """
    __check_args(n)

    denominations = [ 1, 5, 10 ]
    m = n
    changes = 0
    while m > 0:
        for d in reversed(denominations):
            if m - d >= 0:
                m -= d
                changes += 1
                break

    return changes

if __name__ == '__main__':
    input = sys.stdin.read()
    n = int(input)

    print(get_change(n))
