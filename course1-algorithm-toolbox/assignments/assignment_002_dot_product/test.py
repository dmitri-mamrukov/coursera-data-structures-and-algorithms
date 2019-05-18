#!/usr/bin/python3

import math
import unittest

from dot_product import min_dot_product

class MinDotProductTestCase(unittest.TestCase):

    @unittest.expectedFailure
    def test_with_unbalanced_lists_as_larger_a(self):
        self.assertEqual(0, min_dot_product([ 1 ], []))

    @unittest.expectedFailure
    def test_with_unbalanced_lists_as_larger_b(self):
        self.assertEqual(0, min_dot_product([], [ 1 ]))

    def test_with_empty_lists(self):
        self.assertEqual(0, min_dot_product([], []))

    def test_with_one_element_lists(self):
        self.assertEqual(6, min_dot_product([ 2 ], [ 3 ]))
        self.assertEqual(-6, min_dot_product([ 2 ], [ -3 ]))
        self.assertEqual(-6, min_dot_product([ -2 ], [ 3 ]))
        self.assertEqual(6, min_dot_product([ -2 ], [ -3 ]))

        self.assertEqual(897, min_dot_product([ 23 ], [ 39 ]))

    def test_with_one_element_lists_as_lower_bound_values(self):
        self.assertEqual(int(math.pow(10, 10)),
            min_dot_product([ -1 * int(math.pow(10, 5)) ],
                [ -1 * int(math.pow(10, 5)) ]))

    def test_with_one_element_lists_as_upper_bound_values(self):
        self.assertEqual(int(math.pow(10, 10)),
            min_dot_product([ int(math.pow(10, 5)) ],
                [ int(math.pow(10, 5)) ]))

    def test_with_one_element_lists_as_opposite_bound_values(self):
        self.assertEqual(-1 * int(math.pow(10, 10)),
            min_dot_product([ -1 * int(math.pow(10, 5)) ],
                [ int(math.pow(10, 5)) ]))
        self.assertEqual(-1 * int(math.pow(10, 10)),
            min_dot_product([ int(math.pow(10, 5)) ],
                [ -1 * int(math.pow(10, 5)) ]))

    def test_with_two_element_lists(self):
        self.assertEqual(10, min_dot_product([ 1, 2 ], [ 3, 4 ]))
        self.assertEqual(-5, min_dot_product([ 1, 2 ], [ 3, -4 ]))
        self.assertEqual(-2, min_dot_product([ 1, 2 ], [ -3, 4 ]))
        self.assertEqual(-11, min_dot_product([ 1, 2 ], [ -3, -4 ]))

        self.assertEqual(-5, min_dot_product([ 1, -2 ], [ 3, 4 ]))
        self.assertEqual(-10, min_dot_product([ 1, -2 ], [ 3, -4 ]))
        self.assertEqual(-11, min_dot_product([ 1, -2 ], [ -3, 4 ]))
        self.assertEqual(2, min_dot_product([ 1, -2 ], [ -3, -4 ]))

        self.assertEqual(2, min_dot_product([ -1, 2 ], [ 3, 4 ]))
        self.assertEqual(-11, min_dot_product([ -1, 2 ], [ 3, -4 ]))
        self.assertEqual(-10, min_dot_product([ -1, 2 ], [ -3, 4 ]))
        self.assertEqual(-5, min_dot_product([ -1, 2 ], [ -3, -4 ]))

        self.assertEqual(-11, min_dot_product([ -1, -2 ], [ 3, 4 ]))
        self.assertEqual(-2, min_dot_product([ -1, -2 ], [ 3, -4 ]))
        self.assertEqual(-5, min_dot_product([ -1, -2 ], [ -3, 4 ]))
        self.assertEqual(10, min_dot_product([ -1, -2 ], [ -3, -4 ]))

    def test_with_three_element_lists(self):
        self.assertEqual(-25, min_dot_product([ 1, 3, -5 ], [ -2, 4, 1 ]))

if __name__ == '__main__':
    unittest.main()
