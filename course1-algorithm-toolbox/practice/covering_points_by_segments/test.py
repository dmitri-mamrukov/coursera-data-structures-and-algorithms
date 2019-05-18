#!/usr/bin/python3

import unittest

from covering_points_by_segments import Segment
from covering_points_by_segments import solve

class SolveTestCase(unittest.TestCase):

    @unittest.expectedFailure
    def test_with_preceeding_lower_bound_of_length(self):
        solve([ 1, 2 ], -1)

    def test_with_empty_points_and_length_as_0(self):
        segments = solve([], 0)
        self.assertEqual(0, len(segments))

    def test_with_empty_points_and_length_as_1(self):
        segments = solve([], 1)
        self.assertEqual(0, len(segments))

    def test_with_one_point_and_length_as_0(self):
        segments = solve([ 0 ], 0)
        self.assertEqual(1, len(segments))
        self.assertEqual(0, segments[0].start)
        self.assertEqual(0, segments[0].end)

    def test_with_one_point_and_length_as_1(self):
        segments = solve([ 0 ], 1)
        self.assertEqual(1, len(segments))
        self.assertEqual(0, segments[0].start)
        self.assertEqual(1, segments[0].end)

    def test_with_two_points_and_length_as_0(self):
        segments = solve([ 0, 1 ], 0)
        self.assertEqual(2, len(segments))
        self.assertEqual(0, segments[0].start)
        self.assertEqual(0, segments[0].end)
        self.assertEqual(1, segments[1].start)
        self.assertEqual(1, segments[1].end)

    def test_with_two_close_points_and_length_as_1(self):
        segments = solve([ 0, 1 ], 1)
        self.assertEqual(1, len(segments))
        self.assertEqual(0, segments[0].start)
        self.assertEqual(1, segments[0].end)

    def test_with_two_close_points_and_length_as_2(self):
        segments = solve([ 0, 1 ], 2)
        self.assertEqual(1, len(segments))
        self.assertEqual(0, segments[0].start)
        self.assertEqual(2, segments[0].end)

    def test_with_two_distant_points_and_length_as_1(self):
        segments = solve([ 0, 2 ], 1)
        self.assertEqual(2, len(segments))
        self.assertEqual(0, segments[0].start)
        self.assertEqual(1, segments[0].end)
        self.assertEqual(2, segments[1].start)
        self.assertEqual(3, segments[1].end)

    def test_with_three_points_and_length_as_0(self):
        segments = solve([ 0, 1, 2 ], 0)
        self.assertEqual(3, len(segments))
        self.assertEqual(0, segments[0].start)
        self.assertEqual(0, segments[0].end)
        self.assertEqual(1, segments[1].start)
        self.assertEqual(1, segments[1].end)
        self.assertEqual(2, segments[2].start)
        self.assertEqual(2, segments[2].end)

    def test_with_three_points_and_length_as_1(self):
        segments = solve([ 0, 1, 2 ], 1)
        self.assertEqual(2, len(segments))
        self.assertEqual(0, segments[0].start)
        self.assertEqual(1, segments[0].end)
        self.assertEqual(2, segments[1].start)
        self.assertEqual(3, segments[1].end)

    def test_with_three_points_and_length_as_2(self):
        segments = solve([ 0, 1, 2 ], 2)
        self.assertEqual(1, len(segments))
        self.assertEqual(0, segments[0].start)
        self.assertEqual(2, segments[0].end)

    def test_with_several_points_and_length_as_0(self):
        segments = solve([ -5, -4, -2, -1, 3, 4, 6, 9 ], 0)
        self.assertEqual(8, len(segments))
        self.assertEqual(-5, segments[0].start)
        self.assertEqual(-5, segments[0].end)
        self.assertEqual(-4, segments[1].start)
        self.assertEqual(-4, segments[1].end)
        self.assertEqual(-2, segments[2].start)
        self.assertEqual(-2, segments[2].end)
        self.assertEqual(-1, segments[3].start)
        self.assertEqual(-1, segments[3].end)
        self.assertEqual(3, segments[4].start)
        self.assertEqual(3, segments[4].end)
        self.assertEqual(4, segments[5].start)
        self.assertEqual(4, segments[5].end)
        self.assertEqual(6, segments[6].start)
        self.assertEqual(6, segments[6].end)
        self.assertEqual(9, segments[7].start)
        self.assertEqual(9, segments[7].end)

    def test_with_several_points_and_length_as_1(self):
        segments = solve([ -5, -4, -2, -1, 3, 4, 6, 9 ], 1)
        self.assertEqual(5, len(segments))
        self.assertEqual(-5, segments[0].start)
        self.assertEqual(-4, segments[0].end)
        self.assertEqual(-2, segments[1].start)
        self.assertEqual(-1, segments[1].end)
        self.assertEqual(3, segments[2].start)
        self.assertEqual(4, segments[2].end)
        self.assertEqual(6, segments[3].start)
        self.assertEqual(7, segments[3].end)
        self.assertEqual(9, segments[4].start)
        self.assertEqual(10, segments[4].end)

    def test_with_several_points_and_length_as_2(self):
        segments = solve([ -5, -4, -2, -1, 3, 4, 6, 9 ], 2)
        self.assertEqual(5, len(segments))
        self.assertEqual(-5, segments[0].start)
        self.assertEqual(-3, segments[0].end)
        self.assertEqual(-2, segments[1].start)
        self.assertEqual(0, segments[1].end)
        self.assertEqual(3, segments[2].start)
        self.assertEqual(5, segments[2].end)
        self.assertEqual(6, segments[3].start)
        self.assertEqual(8, segments[3].end)
        self.assertEqual(9, segments[4].start)
        self.assertEqual(11, segments[4].end)

    def test_with_several_points_and_length_as_3(self):
        segments = solve([ -5, -4, -2, -1, 3, 4, 6, 9 ], 3)
        self.assertEqual(4, len(segments))
        self.assertEqual(-5, segments[0].start)
        self.assertEqual(-2, segments[0].end)
        self.assertEqual(-1, segments[1].start)
        self.assertEqual(2, segments[1].end)
        self.assertEqual(3, segments[2].start)
        self.assertEqual(6, segments[2].end)
        self.assertEqual(9, segments[3].start)
        self.assertEqual(12, segments[3].end)

    def test_with_several_points_and_length_as_4(self):
        segments = solve([ -5, -4, -2, -1, 3, 4, 6, 9 ], 4)
        self.assertEqual(3, len(segments))
        self.assertEqual(-5, segments[0].start)
        self.assertEqual(-1, segments[0].end)
        self.assertEqual(3, segments[1].start)
        self.assertEqual(7, segments[1].end)
        self.assertEqual(9, segments[2].start)
        self.assertEqual(13, segments[2].end)

    def test_with_several_points_and_length_as_5(self):
        segments = solve([ -5, -4, -2, -1, 3, 4, 6, 9 ], 5)
        self.assertEqual(3, len(segments))
        self.assertEqual(-5, segments[0].start)
        self.assertEqual(0, segments[0].end)
        self.assertEqual(3, segments[1].start)
        self.assertEqual(8, segments[1].end)
        self.assertEqual(9, segments[2].start)
        self.assertEqual(14, segments[2].end)

    def test_with_several_points_and_length_as_6(self):
        segments = solve([ -5, -4, -2, -1, 3, 4, 6, 9 ], 6)
        self.assertEqual(2, len(segments))
        self.assertEqual(-5, segments[0].start)
        self.assertEqual(1, segments[0].end)
        self.assertEqual(3, segments[1].start)
        self.assertEqual(9, segments[1].end)

    def test_with_several_points_and_length_as_7(self):
        segments = solve([ -5, -4, -2, -1, 3, 4, 6, 9 ], 7)
        self.assertEqual(2, len(segments))
        self.assertEqual(-5, segments[0].start)
        self.assertEqual(2, segments[0].end)
        self.assertEqual(3, segments[1].start)
        self.assertEqual(10, segments[1].end)

    def test_with_several_points_and_length_as_8(self):
        segments = solve([ -5, -4, -2, -1, 3, 4, 6, 9 ], 8)
        self.assertEqual(2, len(segments))
        self.assertEqual(-5, segments[0].start)
        self.assertEqual(3, segments[0].end)
        self.assertEqual(4, segments[1].start)
        self.assertEqual(12, segments[1].end)

    def test_with_several_points_and_length_as_9(self):
        segments = solve([ -5, -4, -2, -1, 3, 4, 6, 9 ], 9)
        self.assertEqual(2, len(segments))
        self.assertEqual(-5, segments[0].start)
        self.assertEqual(4, segments[0].end)
        self.assertEqual(6, segments[1].start)
        self.assertEqual(15, segments[1].end)

    def test_with_several_points_and_length_as_10(self):
        segments = solve([ -5, -4, -2, -1, 3, 4, 6, 9 ], 10)
        self.assertEqual(2, len(segments))
        self.assertEqual(-5, segments[0].start)
        self.assertEqual(5, segments[0].end)
        self.assertEqual(6, segments[1].start)
        self.assertEqual(16, segments[1].end)

    def test_with_several_points_and_length_as_11(self):
        segments = solve([ -5, -4, -2, -1, 3, 4, 6, 9 ], 11)
        self.assertEqual(2, len(segments))
        self.assertEqual(-5, segments[0].start)
        self.assertEqual(6, segments[0].end)
        self.assertEqual(9, segments[1].start)
        self.assertEqual(20, segments[1].end)

    def test_with_several_points_and_length_as_12(self):
        segments = solve([ -5, -4, -2, -1, 3, 4, 6, 9 ], 12)
        self.assertEqual(2, len(segments))
        self.assertEqual(-5, segments[0].start)
        self.assertEqual(7, segments[0].end)
        self.assertEqual(9, segments[1].start)
        self.assertEqual(21, segments[1].end)

    def test_with_several_points_and_length_as_13(self):
        segments = solve([ -5, -4, -2, -1, 3, 4, 6, 9 ], 13)
        self.assertEqual(2, len(segments))
        self.assertEqual(-5, segments[0].start)
        self.assertEqual(8, segments[0].end)
        self.assertEqual(9, segments[1].start)
        self.assertEqual(22, segments[1].end)

    def test_with_several_points_and_length_as_14(self):
        segments = solve([ -5, -4, -2, -1, 3, 4, 6, 9 ], 14)
        self.assertEqual(1, len(segments))
        self.assertEqual(-5, segments[0].start)
        self.assertEqual(9, segments[0].end)

    def test_with_several_points_and_length_as_15(self):
        segments = solve([ -5, -4, -2, -1, 3, 4, 6, 9 ], 15)
        self.assertEqual(1, len(segments))
        self.assertEqual(-5, segments[0].start)
        self.assertEqual(10, segments[0].end)

if __name__ == '__main__':
    unittest.main()
