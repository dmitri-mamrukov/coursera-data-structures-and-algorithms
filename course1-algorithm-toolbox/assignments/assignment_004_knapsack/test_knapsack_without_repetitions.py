#!/usr/bin/python3

import unittest

from knapsack_without_repetitions import optimal_value

class KnapsackWithoutRepetitionTestCase(unittest.TestCase):

    def assert_items_within_capacity(self, capacity, weights, values,
            value, items):
        total_weight = 0
        total_value = 0
        for i in items:
            total_weight += weights[i]
            total_value += values[i]

        self.assertTrue(capacity >= total_weight)
        self.assertEqual(value, total_value)

    def test_with_preceeding_lower_bound_of_capacity(self):
        with self.assertRaisesRegex(AssertionError, ''):
            capacity = -1
            weights = []
            values = []
            optimal_value(capacity, weights, values)

    def test_with_less_weights_than_values(self):
        with self.assertRaisesRegex(AssertionError, ''):
            capacity = 1
            weights = [ 1 ]
            values = [ 2, 3 ]
            optimal_value(capacity, weights, values)

    def test_with_more_weights_than_values(self):
        with self.assertRaisesRegex(AssertionError, ''):
            capacity = 1
            weights = [ 1, 2 ]
            values = [ 3 ]
            optimal_value(capacity, weights, values)

    def test_with_preceeding_lower_bound_of_weights(self):
        with self.assertRaisesRegex(AssertionError, ''):
            capacity = 1
            weights = [ 1, -1, 2 ]
            values = [ 1, 2, 3 ]
            optimal_value(capacity, weights, values)

    def test_with_preceeding_lower_bound_of_values(self):
        with self.assertRaisesRegex(AssertionError, ''):
            capacity = 1
            weights = [ 1, 2, 3 ]
            values = [ 1, -1, 2 ]
            optimal_value(capacity, weights, values)

    def test_with_zero_capacity(self):
        capacity = 0
        weights = []
        values = []
        value, items = optimal_value(capacity, weights, values)
        self.assertEqual(0, value)
        self.assertEqual([], items)
        self.assert_items_within_capacity(capacity, weights, values,
            value, items)

    def test_with_non_zero_capacity_and_empty_items(self):
        capacity = 123
        weights = []
        values = []
        value, items = optimal_value(capacity, weights, values)
        self.assertEqual(0, value)
        self.assertEqual([], items)
        self.assert_items_within_capacity(capacity, weights, values,
            value, items)

    def test_with_capacity_as_1_and_weights_as_1(self):
        capacity = 1
        weights = [ 1 ]
        values = [ 2 ]
        value, items = optimal_value(capacity, weights, values)
        self.assertEqual(2, value)
        self.assertEqual([ 0 ], items)
        self.assert_items_within_capacity(capacity, weights, values,
            value, items)

    def test_with_capacity_as_1_and_duplicate_weights_and_values(self):
        capacity = 1
        weights = [ 1, 1 ]
        values = [ 2, 2 ]
        value, items = optimal_value(capacity, weights, values)
        self.assertEqual(2, value)
        self.assertEqual([ 0 ], items)
        self.assert_items_within_capacity(capacity, weights, values,
            value, items)

    def test_with_capacity_as_1_and_duplicate_weights(self):
        capacity = 1
        weights = [ 1, 1 ]
        values = [ 2, 3 ]
        value, items = optimal_value(capacity, weights, values)
        self.assertEqual(3, value)
        self.assertEqual([ 1 ], items)
        self.assert_items_within_capacity(capacity, weights, values,
            value, items)

    def test_with_capacity_as_1_and_duplicate_values(self):
        capacity = 1
        weights = [ 1, 2 ]
        values = [ 2, 2 ]
        value, items = optimal_value(capacity, weights, values)
        self.assertEqual(2, value)
        self.assertEqual([ 0 ], items)
        self.assert_items_within_capacity(capacity, weights, values,
            value, items)

    def test_with_capacity_as_1_and_weights_as_2(self):
        capacity = 1
        weights = [ 2 ]
        values = [ 3 ]
        value, items = optimal_value(capacity, weights, values)
        self.assertEqual(0, value)
        self.assertEqual([], items)
        self.assert_items_within_capacity(capacity, weights, values,
            value, items)

    def test_with_capacity_as_1_and_weights_as_1_and_2(self):
        capacity = 1
        weights = [ 1, 2 ]
        values = [ 2, 3 ]
        value, items = optimal_value(capacity, weights, values)
        self.assertEqual(2, value)
        self.assertEqual([ 0 ], items)
        self.assert_items_within_capacity(capacity, weights, values,
            value, items)

    def test_with_capacity_as_1_and_weights_as_2_and_3(self):
        capacity = 1
        weights = [ 2, 3 ]
        values = [ 4, 5 ]
        value, items = optimal_value(capacity, weights, values)
        self.assertEqual(0, value)
        self.assertEqual([], items)
        self.assert_items_within_capacity(capacity, weights, values,
            value, items)

    def test_with_capacity_as_2_and_weights_as_1_and_2(self):
        capacity = 2
        weights = [ 1, 2 ]
        values = [ 2, 3 ]
        value, items = optimal_value(capacity, weights, values)
        self.assertEqual(3, value)
        self.assertEqual([ 1 ], items)
        self.assert_items_within_capacity(capacity, weights, values,
            value, items)

    def test_with_capacity_as_10_and_several_weights(self):
        capacity = 10
        weights = [ 2, 4, 3, 6 ]
        values = [ 9, 16, 14, 30 ]
        value, items = optimal_value(capacity, weights, values)
        self.assertEqual(46, value)
        self.assertEqual([ 3, 1 ], items)
        self.assert_items_within_capacity(capacity, weights, values,
            value, items)

    def test_with_capacity_as_10_and_several_weights_with_duplicates(self):
        capacity = 10
        weights = [ 2, 4, 3, 6, 2, 4, 3, 6 ]
        values = [ 9, 16, 14, 30, 9, 16, 14, 30 ]
        value, items = optimal_value(capacity, weights, values)
        self.assertEqual(48, value)
        self.assertEqual([ 4, 3, 0 ], items)
        self.assert_items_within_capacity(capacity, weights, values,
            value, items)

    def test_with_capacity_as_11_and_several_weights(self):
        capacity = 11
        weights = [ 2, 4, 3, 6 ]
        values = [ 9, 16, 14, 30 ]
        value, items = optimal_value(capacity, weights, values)
        self.assertEqual(53, value)
        self.assertEqual([ 3, 2, 0 ], items)
        self.assert_items_within_capacity(capacity, weights, values,
            value, items)

    def test_with_capacity_as_12_and_several_weights(self):
        capacity = 12
        weights = [ 2, 4, 3, 6 ]
        values = [ 9, 16, 14, 30 ]
        value, items = optimal_value(capacity, weights, values)
        self.assertEqual(55, value)
        self.assertEqual([ 3, 1, 0 ], items)
        self.assert_items_within_capacity(capacity, weights, values,
            value, items)

    def test_with_capacity_as_13_and_several_weights(self):
        capacity = 13
        weights = [ 2, 4, 3, 6 ]
        values = [ 9, 16, 14, 30 ]
        value, items = optimal_value(capacity, weights, values)
        self.assertEqual(60, value)
        self.assertEqual([ 3, 2, 1 ], items)
        self.assert_items_within_capacity(capacity, weights, values,
            value, items)

    def test_with_capacity_as_14_and_several_weights(self):
        capacity = 14
        weights = [ 2, 4, 3, 6 ]
        values = [ 9, 16, 14, 30 ]
        value, items = optimal_value(capacity, weights, values)
        self.assertEqual(60, value)
        self.assertEqual([ 3, 2, 1 ], items)
        self.assert_items_within_capacity(capacity, weights, values,
            value, items)

if __name__ == '__main__':
    unittest.main()
