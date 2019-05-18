#!/usr/bin/python3

import random

import unittest

from multiplying_polynomials import solve_naively

class SolveNaivelyTestCase(unittest.TestCase):

    @unittest.expectedFailure
    def test_with_a_larger_than_b(self):
        solve_naively([ 1 ], [], 1)

    @unittest.expectedFailure
    def test_with_b_larger_than_a(self):
        solve_naively([], [ 1 ], 1)

    @unittest.expectedFailure
    def test_with_lists_of_size_greater_than_n(self):
        solve_naively([ 1, 2 ], [ 3, 4 ], 1)

    @unittest.expectedFailure
    def test_with_lists_of_size_less_than_n(self):
        solve_naively([], [], 1)
        solve_naively([ 1 ], [ 2 ], 3)

    @unittest.expectedFailure
    def test_with_preceeding_lower_bound_of_n(self):
        solve_naively([ 1, 2 ], [ 3, 4 ], -1)

    def test_with_n_as_0(self):
        self.assertEqual([],
            solve_naively([], [], 0))

    def test_with_n_as_1(self):
        self.assertEqual([ 2 * 3 ],
            solve_naively([ 2 ], [ 3 ], 1))

    def test_with_n_as_2(self):
        self.assertEqual([
            2 * 4,
            2 * 5 + 3 * 4,
            3 * 5 ],
            solve_naively([ 2, 3 ], [ 4, 5 ], 2))

    def test_with_n_as_3(self):
        self.assertEqual([
            3 * 5,
            3 * 1 + 2 * 5,
            3 * 2 + 2 * 1 + 5 * 5,
            2 * 2 + 5 * 1,
            5 * 2 ],
            solve_naively([ 3, 2, 5 ], [ 5, 1, 2 ], 3))

    def test_with_n_as_4(self):
        self.assertEqual([
            4 * 1,
            4 * 2 + 3 * 1,
            4 * 3 + 3 * 2 + 2 * 1,
            4 * 4 + 3 * 3 + 2 * 2 + 1 * 1,
            3 * 4 + 2 * 3 + 1 * 2,
            2 * 4 + 1 * 3,
            1 * 4 ],
            solve_naively([ 4, 3, 2, 1 ], [ 1, 2, 3, 4 ], 4))

    def test_with_n_as_7(self):
        self.assertEqual([
            5 * 0,
            5 * 0 + 3 * 0,
            5 * 0 + 3 * 0 + 0 * 0,
            5 * 0 + 3 * 0 + 0 * 0 + 0 * 0,
            5 * 0 + 3 * 0 + 0 * 0 + 0 * 0 + 2 * 0,
            5 * 0 + 3 * 0 + 0 * 0 + 0 * 0 + 2 * 0 + 0 * 0,
            5 * 1 + 3 * 0 + 0 * 0 + 0 * 0 + 2 * 0 + 0 * 0 + 1 * 0,
            3 * 1 + 0 * 0 + 0 * 0 + 2 * 0 + 0 * 0 + 1 * 0,
            0 * 1 + 0 * 0 + 2 * 0 + 0 * 0 + 1 * 0,
            0 * 1 + 2 * 0 + 0 * 0 + 1 * 0,
            2 * 1 + 0 * 0 + 1 * 0,
            0 * 1 + 1 * 0,
            1 * 1, ],
            solve_naively([ 5, 3, 0, 0, 2, 0, 1 ],
                [ 0, 0, 0, 0, 0, 0, 1 ], 7))

if __name__ == '__main__':
    unittest.main()
