#!/usr/bin/python3

import unittest

from fractional_knapsack import get_optimal_value

class GetChangeTestCase(unittest.TestCase):

    @unittest.expectedFailure
    def test_with_preceeding_lower_bound_capacity(self):
        get_optimal_value(-1, [], [])

    @unittest.expectedFailure
    def test_with_preceeding_lower_bound_weight(self):
        get_optimal_value(0, [ -1 ], [])

    @unittest.expectedFailure
    def test_with_preceeding_lower_bound_among_weights(self):
        get_optimal_value(0, [ 1, -1, 3 ], [])

    @unittest.expectedFailure
    def test_with_preceeding_lower_bound_value(self):
        get_optimal_value(0, [], [ -1 ])

    @unittest.expectedFailure
    def test_with_preceeding_lower_bound_among_values(self):
        get_optimal_value(0, [], [ 1, -1, 3 ])

    @unittest.expectedFailure
    def test_with_empty_weights_and_non_empty_values(self):
        get_optimal_value(0, [], [ 1 ])

    @unittest.expectedFailure
    def test_with_non_empty_weights_and_empty_values(self):
        get_optimal_value(0, [ 1 ], [])

    @unittest.expectedFailure
    def test_with_unbalanced_weights_and_values(self):
        get_optimal_value(0, [ 1 ], [ 1, 2, 3])

    def test_with_zero_capacity_and_empty_weights_and_empty_values(self):
        self.assertEqual(0., get_optimal_value(0, [], []))

    def test_with_zero_capacity_and_weights_and_values(self):
        self.assertEqual(0., get_optimal_value(0, [ 1 ], [ 10 ]))
        self.assertEqual(0.,
            get_optimal_value(0, [ 1, 2, 3 ], [ 10, 20, 30 ]))

    def test_with_capacity_and_one_item_of_lesser_total_weight(self):
        self.assertAlmostEqual(500,
            get_optimal_value(10, [ 5 ], [ 500 ]),
            places = 3)

    def test_with_capacity_and_one_item_of_larger_total_weight(self):
        self.assertAlmostEqual(166.6667,
            get_optimal_value(10, [ 30 ], [ 500 ]),
            places = 3)

    def test_with_capacity_and_two_items_of_lesser_total_weight(self):
        self.assertAlmostEqual(160.0000,
            get_optimal_value(50, [ 10, 20 ], [ 60, 100 ]),
            places = 4)

    def test_with_capacity_and_two_items_of_larger_total_weight(self):
        self.assertAlmostEqual(120.0000,
            get_optimal_value(50, [ 20, 50 ], [ 60, 100 ]),
            places = 4)

    def test_with_capacity_and_three_items_of_lesser_total_weight(self):
        self.assertAlmostEqual(280.0000,
            get_optimal_value(50, [ 5, 10, 20 ], [ 60, 100, 120 ]),
            places = 4)

    def test_with_capacity_and_three_items_of_larger_total_weight(self):
        self.assertAlmostEqual(180.0000,
            get_optimal_value(50, [ 20, 50, 30 ], [ 60, 100, 120 ]),
            places = 4)

if __name__ == '__main__':
    unittest.main()
