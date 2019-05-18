#!/usr/bin/python3

import math
import unittest

from covering_segments import optimal_points
from covering_segments import Segment

class OptimalPointsTestCase(unittest.TestCase):

    @unittest.expectedFailure
    def test_with_empty_segments(self):
        optimal_points([])

    @unittest.expectedFailure
    def test_with_preceeding_lower_bound_of_start(self):
        segments = [ Segment(-1, 0) ]
        optimal_points(segments)

    @unittest.expectedFailure
    def test_with_preceeding_lower_bound_of_start_among_elements(self):
        segments = [ Segment(0, 0), Segment(-1, 0), Segment(1, 1) ]
        optimal_points(segments)

    @unittest.expectedFailure
    def test_with_preceeding_lower_bound_of_end(self):
        segments = [ Segment(0, -1) ]
        optimal_points(segments)

    @unittest.expectedFailure
    def test_with_preceeding_lower_bound_of_end_among_elements(self):
        segments = [ Segment(0, 0), Segment(0, -1), Segment(1, 1) ]
        optimal_points(segments)

    @unittest.expectedFailure
    def test_with_start_bigger_than_end(self):
        segments = [ Segment(1, 0) ]
        optimal_points(segments)

    def test_with_one_segment_of_same_start_and_end(self):
        segments = \
        [
            Segment(0, 0)
        ]
        points = optimal_points(segments)
        self.assertEqual(1, len(points))
        self.assertEqual(0, points[0])

    def test_with_one_segment_of_different_start_and_end(self):
        segments = \
        [
            Segment(0, 1)
        ]
        points = optimal_points(segments)
        self.assertEqual(1, len(points))
        self.assertEqual(1, points[0])

    def test_with_two_continuous_segments(self):
        segments = \
        [
            Segment(0, 1),
            Segment(1, 2)
        ]
        points = optimal_points(segments)
        self.assertEqual(1, len(points))
        self.assertEqual(1, points[0])

    def test_with_two_overlapping_segments(self):
        segments = \
        [
            Segment(0, 2),
            Segment(1, 3)
        ]
        points = optimal_points(segments)
        self.assertEqual(1, len(points))
        self.assertEqual(2, points[0])

    def test_with_two_disjoint_segments(self):
        segments = \
        [
            Segment(0, 1),
            Segment(2, 3)
        ]
        points = optimal_points(segments)
        self.assertEqual(2, len(points))
        self.assertEqual(1, points[0])
        self.assertEqual(3, points[1])

    def test_with_three_segments(self):
        segments = \
        [
            Segment(1, 3),
            Segment(2, 5),
            Segment(3, 6)
        ]
        points = optimal_points(segments)
        self.assertEqual(1, len(points))
        self.assertEqual(3, points[0])

    def test_with_four_segments(self):
        segments = \
        [
            Segment(4, 7),
            Segment(1, 3),
            Segment(2, 5),
            Segment(5, 6)
        ]
        points = optimal_points(segments)
        self.assertEqual(2, len(points))
        self.assertEqual(3, points[0])
        self.assertEqual(6, points[1])

    def test_with_four_segments_of_large_numbers(self):
        segments = \
        [
            Segment(4000, 7000),
            Segment(1000, 3000),
            Segment(2000, 5000),
            Segment(5000, int(math.pow(10, 9)))
        ]
        points = optimal_points(segments)
        self.assertEqual(2, len(points))
        self.assertEqual(3000, points[0])
        self.assertEqual(7000, points[1])

if __name__ == '__main__':
    unittest.main()
