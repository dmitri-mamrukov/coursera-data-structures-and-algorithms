#!/usr/bin/python3

import sys

def __check_args(points, refill_length):
    assert(2 <= len(points))
    assert(0 <= refill_length)

def solve(points, refill_length):
    """The goal in this problem is to find the minimum number of refills
    to get from A to B, besides refill at A. The points contain
    A = x0 <= x1 <= x2 <= ... <= xn-1 <= xn <= xn+1 = B.

    Greedy Strategy:

    Start at A. Refill at the farthest reachable gas station G.
    Make G the new A and continue on the subproblem.

    Safety Proof:

    We minimize the number of refills by using the farthest reachable
    gas station every time.
    """
    __check_args(points, refill_length)

    points.sort()

    n = len(points) - 2
    refills = 0
    current_refill = 0

    while current_refill <= n:
        last_refill = current_refill
        while (current_refill <= n and
            (points[current_refill + 1] - points[last_refill] <=
            refill_length)):
            current_refill += 1

        if current_refill == last_refill:
            return -1

        if current_refill <= n:
            refills += 1

    return refills

if __name__ == '__main__':
    points = list(map(int, input().split()))
    refill_length = int(input())

    print(solve(points, refill_length))
