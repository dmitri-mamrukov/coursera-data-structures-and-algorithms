#!/usr/bin/python3

import unittest

from max_number import solve

class SolveTestCase(unittest.TestCase):

    @unittest.expectedFailure
    def test_with_preceeding_lower_bound_digit(self):
        solve([ -1 ])

    @unittest.expectedFailure
    def test_with_preceeding_lower_bound_among_digits(self):
        solve([ 0, -1, 2 ])

    @unittest.expectedFailure
    def test_with_exceeding_upper_bound_digit(self):
        solve([ 10 ])

    @unittest.expectedFailure
    def test_with_exceeding_upper_bound_among_digits(self):
        solve([ 0, 10, 2 ])

    def test_with_one_digit(self):
        for i in range(0, 9):
            self.assertEqual(i, solve([ i ]))

    def test_with_two_digits(self):
        for i in range(0, 9):
            for j in range(0, 9):
                digits = [ i, j ]
                d1 = max(digits)
                digits.remove(d1)
                d2 = max(digits)
                self.assertEqual(d1 * 10 + d2,
                    solve([ i, j ]))

    def test_with_three_digits(self):
        for i in range(0, 9):
            for j in range(0, 9):
                for k in range(0, 9):
                    digits = [ i, j, k ]
                    d1 = max(digits)
                    digits.remove(d1)
                    d2 = max(digits)
                    digits.remove(d2)
                    d3 = max(digits)
                    self.assertEqual(d1 * 100 + d2 * 10 + d3,
                        solve([ i, j, k ]))

    def test_with_several_digits(self):
        self.assertEqual(997531, solve([ 5, 7, 3, 9, 1, 9 ]))

    def test_with_all_digits_unsorted(self):
        self.assertEqual(9876543210, solve([ 0, 1, 2, 3, 4, 5, 6, 7, 8, 9 ]))

    def test_with_all_digits_already_sorted(self):
        self.assertEqual(9876543210, solve([ 9, 8, 7, 6, 5, 4, 3, 2, 1, 0 ]))

if __name__ == '__main__':
    unittest.main()
