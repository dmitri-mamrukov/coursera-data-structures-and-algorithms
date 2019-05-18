#!/usr/bin/python3

from collections import namedtuple
import sys

Segment = namedtuple('Segment', 'start end')

DEBUG = False

def __check_args(segments):
    assert(1 <= len(segments))
    for s in segments:
        assert(0 <= s.start)
        assert(0 <= s.end)
        assert(s.start <= s.end)

def optimal_points(segments):
    """Given a set of segments on a line, the goal is to mark as few
    points on a line as possible so that each segment contains at least
    one marked point.

    Formally, given a set of n segments

        {[a₀, b₀], [a₁, b₁], ..., [aₙ₋₁, bₙ₋₁]}

    with integer coordinates on a line, finds the minimum number m of points
    such that each segment contains at least one point. That is, find a
    set of integers X of the minimum size such that for any segment
    [aᵢ, bᵢ] there is a point x ∈ X such that aᵢ ≤ x ≤ bᵢ.

    Greedy Strategy:

    Select a segment with the minimum right endpoint e. Remove all segments
    that contain e. Continue on the subproblem.

    Safety Proof:

    Every time we find a segment with the minimum right endpoint e, we have to
    mark it, so it is included in the coverage set of points.
    """
    __check_args(segments)

    points = []

    while len(segments) > 0:
        if DEBUG:
            print('segments: %s' % segments)

        min_right_end_index = -1
        for i, s in enumerate(segments):
            if (s.end < segments[min_right_end_index].end):
                min_right_end_index = i

        points.append(segments[min_right_end_index].end)

        segments = [x for x in segments
            if x.start > segments[min_right_end_index].end]

    return points

if __name__ == '__main__':
    input = sys.stdin.read()
    n, *data = map(int, input.split())

    start_points = data[::2]
    end_points = data[1::2]
    positions = zip(start_points, end_points)
    segments = list(map(lambda x: Segment(x[0], x[1]), positions))

    if DEBUG:
        print('n: %s' % n)
        print('data: %s' % data)
        print('start_points: %s' % start_points)
        print('end_points: %s' % end_points)
        print('segments: %s' % segments)

    points = optimal_points(segments)

    print(len(points))
    for p in points:
        print(p, end = ' ')
    print()
