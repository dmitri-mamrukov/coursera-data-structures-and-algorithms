#!/usr/bin/python3

import unittest

from car_refueling import solve

class SolveTestCase(unittest.TestCase):

    @unittest.expectedFailure
    def test_with_preceeding_lower_bound_of_points_length_as_0(self):
        solve([], 1)

    @unittest.expectedFailure
    def test_with_preceeding_lower_bound_of_points_length_as_1(self):
        solve([ 1 ], 1)

    @unittest.expectedFailure
    def test_with_preceeding_lower_bound_of_length(self):
        solve([ 1, 2 ], -1)

    def test_with_two_points_and_length_as_zero(self):
        self.assertEqual(-1, solve([ 1, 3 ], 0))

    def test_with_two_points_and_length_as_unreachable(self):
        self.assertEqual(-1, solve([ 1, 3 ], 1))

    def test_with_two_points_and_length_as_trip_distance(self):
        self.assertEqual(0, solve([ 1, 3 ], 2))

    def test_with_two_points_and_length_as_more_than_trip_distance(self):
        self.assertEqual(0, solve([ 1, 3 ], 2))

    def test_with_three_points_and_length_as_zero(self):
        self.assertEqual(-1, solve([ 1, 3, 5 ], 0))

    def test_with_three_points_and_length_as_unreachable(self):
        self.assertEqual(-1, solve([ 1, 3, 5 ], 1))

    def test_with_three_points_and_length_as_refill_distance(self):
        self.assertEqual(1, solve([ 1, 3, 5 ], 2))

    def test_with_three_points_and_length_as_more_than_refill_distance(self):
        self.assertEqual(1, solve([ 1, 3, 5 ], 3))

    def test_with_three_points_and_length_as_more_than_trip_distance(self):
        self.assertEqual(0, solve([ 1, 3, 5 ], 4))

    def test_with_several_points_and_length_as_unreachable(self):
        self.assertEqual(-1, solve([ 1, 3, 5, 7, 9, 11, 13 ], 1))
        self.assertEqual(-1, solve([ 1, 3, 5, 7, 9, 11, 14 ], 2))
        self.assertEqual(-1, solve([ 1, 3, 5, 7, 9, 13, 15 ], 2))

    def test_with_several_points_and_length_as_refill_distance(self):
        self.assertEqual(5, solve([ 1, 3, 5, 7, 9, 11, 13 ], 2))
        self.assertEqual(5, solve([ 1, 3, 5, 7, 9, 11, 13 ], 3))
        self.assertEqual(3, solve([ 1, 3, 5, 7, 9, 13, 15 ], 4))

    def test_with_several_points_and_length_as_than_trip_distance(self):
        self.assertEqual(0, solve([ 1, 3, 5, 7, 9, 13, 15 ], 14))

    def test_with_several_points_and_length_as_more_than_trip_distance(self):
        self.assertEqual(0, solve([ 1, 3, 5, 7, 9, 13, 15 ], 15))

if __name__ == '__main__':
    unittest.main()
