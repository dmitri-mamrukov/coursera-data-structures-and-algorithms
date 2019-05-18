#!/usr/bin/python3

from collections import namedtuple
import sys

Segment = namedtuple('Segment', 'start end')

def __check_args(points, unit_length):
    assert(0 <= unit_length)

def solve(points, unit_length):
    """The goal in this problem is to find the minimum number of segments
    of unit length needed to cover all the points.

    Greedy Strategy:

    Cover the leftmost point with a unit segment with its left end
    in this point. Remove points that are covered by the unit segment.
    Continue on the subproblem.

    Safety Proof:

    We minimize the number of segments by using the leftmost points
    every time.
    """
    __check_args(points, unit_length)

    points.sort()

    i = 0
    segments = []
    while i < len(points):
        segment = Segment(points[i], points[i] + unit_length)
        segments.append(segment)
        i += 1

        while i < len(points) and points[i] <= segment.end:
            i += 1

    return segments

if __name__ == '__main__':
    points = list(map(int, input().split()))
    unit_length = int(input())

    print(solve(points, unit_length))
