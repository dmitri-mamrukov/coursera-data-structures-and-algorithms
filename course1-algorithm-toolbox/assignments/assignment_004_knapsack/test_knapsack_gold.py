#!/usr/bin/python3

import unittest

from knapsack_gold import optimal_weight, optimal_weight_simplified

class KnapsackGoldTestCase(unittest.TestCase):

    def assert_items_within_capacity(self, capacity, weights, value, items):
        total_weight = 0
        total_value = 0
        for i in items:
            total_weight += weights[i]
            total_value += weights[i]

        self.assertTrue(capacity >= total_weight)
        self.assertEqual(value, total_value)

    def test_with_preceeding_lower_bound_of_capacity(self):
        with self.assertRaisesRegex(AssertionError, ''):
            capacity = -1
            weights = []
            optimal_weight(capacity, weights)

    def test_with_preceeding_lower_bound_of_weights(self):
        with self.assertRaisesRegex(AssertionError, ''):
            capacity = 1
            weights = [ 1, -1, 2 ]
            optimal_weight(capacity, weights)

    def test_with_zero_capacity(self):
        capacity = 0
        weights = []
        value, items = optimal_weight(capacity, weights)
        self.assertEqual(0, value)
        self.assertEqual([], items)
        self.assert_items_within_capacity(capacity, weights, value, items)

    def test_with_non_zero_capacity_and_empty_weights(self):
        capacity = 123
        weights = []
        value, items = optimal_weight(capacity, weights)
        self.assertEqual(0, value)
        self.assertEqual([], items)
        self.assert_items_within_capacity(capacity, weights, value, items)

    def test_with_capacity_as_1_and_weights_as_1(self):
        capacity = 1
        weights = [ 1 ]
        value, items = optimal_weight(capacity, weights)
        self.assertEqual(1, value)
        self.assertEqual([ 0 ], items)
        self.assert_items_within_capacity(capacity, weights, value, items)

    def test_with_capacity_as_1_and_duplicate_weights(self):
        capacity = 1
        weights = [ 1, 1 ]
        value, items = optimal_weight(capacity, weights)
        self.assertEqual(1, value)
        self.assertEqual([ 0 ], items)
        self.assert_items_within_capacity(capacity, weights,
            value, items)

    def test_with_capacity_as_1_and_weights_as_2(self):
        capacity = 1
        weights = [ 2 ]
        value, items = optimal_weight(capacity, weights)
        self.assertEqual(0, value)
        self.assertEqual([], items)
        self.assert_items_within_capacity(capacity, weights, value, items)

    def test_with_capacity_as_1_and_weights_as_1_and_2(self):
        capacity = 1
        weights = [ 1, 2 ]
        value, items = optimal_weight(capacity, weights)
        self.assertEqual(1, value)
        self.assertEqual([ 0 ], items)
        self.assert_items_within_capacity(capacity, weights, value, items)

    def test_with_capacity_as_1_and_weights_as_2_and_3(self):
        capacity = 1
        weights = [ 2, 3 ]
        value, items = optimal_weight(capacity, weights)
        self.assertEqual(0, value)
        self.assertEqual([], items)
        self.assert_items_within_capacity(capacity, weights, value, items)

    def test_with_capacity_as_2_and_weights_as_1_and_2(self):
        capacity = 2
        weights = [ 1, 2 ]
        value, items = optimal_weight(capacity, weights)
        self.assertEqual(2, value)
        self.assertEqual([ 1 ], items)
        self.assert_items_within_capacity(capacity, weights, value, items)

    def test_with_capacity_as_10_and_several_weights(self):
        capacity = 10
        weights = [ 2, 4, 3, 6 ]
        value, items = optimal_weight(capacity, weights)
        self.assertEqual(10, value)
        self.assertEqual([ 3, 1 ], items)
        self.assert_items_within_capacity(capacity, weights, value, items)

    def test_with_capacity_as_10_and_several_weights_with_duplicates(self):
        capacity = 10
        weights = [ 2, 4, 3, 6, 2, 4, 3, 6 ]
        value, items = optimal_weight(capacity, weights)
        self.assertEqual(10, value)
        self.assertEqual([ 3, 1 ], items)
        self.assert_items_within_capacity(capacity, weights, value, items)

    def test_with_capacity_as_11_and_several_weights(self):
        capacity = 11
        weights = [ 2, 4, 3, 6 ]
        value, items = optimal_weight(capacity, weights)
        self.assertEqual(11, value)
        self.assertEqual([ 3, 2, 0 ], items)
        self.assert_items_within_capacity(capacity, weights, value, items)

    def test_with_capacity_as_12_and_several_weights(self):
        capacity = 12
        weights = [ 2, 4, 3, 6 ]
        value, items = optimal_weight(capacity, weights)
        self.assertEqual(12, value)
        self.assertEqual([ 3, 1, 0 ], items)
        self.assert_items_within_capacity(capacity, weights, value, items)

    def test_with_capacity_as_13_and_several_weights(self):
        capacity = 13
        weights = [ 2, 4, 3, 6 ]
        value, items = optimal_weight(capacity, weights)
        self.assertEqual(13, value)
        self.assertEqual([ 3, 2, 1 ], items)
        self.assert_items_within_capacity(capacity, weights, value, items)

    def test_with_capacity_as_14_and_several_weights(self):
        capacity = 14
        weights = [ 2, 4, 3, 6 ]
        value, items = optimal_weight(capacity, weights)
        self.assertEqual(13, value)
        self.assertEqual([ 3, 2, 1 ], items)
        self.assert_items_within_capacity(capacity, weights,
            value, items)

    def test_with_capacity_as_10_and_bars_as_1_4_8(self):
        capacity = 10
        weights = [ 1, 4, 8 ]
        value, items = optimal_weight(capacity, weights)
        self.assertEqual(9, value)
        self.assertEqual([ 2, 0 ], items)
        self.assert_items_within_capacity(capacity, weights, value, items)

class KnapsackGoldSimplifiedTestCase(unittest.TestCase):

    def test_with_preceeding_lower_bound_of_capacity(self):
        with self.assertRaisesRegex(AssertionError, ''):
            capacity = -1
            weights = []
            optimal_weight_simplified(capacity, weights)

    def test_with_preceeding_lower_bound_of_weights(self):
        with self.assertRaisesRegex(AssertionError, ''):
            capacity = 1
            weights = [ 1, -1, 2 ]
            optimal_weight_simplified(capacity, weights)

    def test_with_zero_capacity(self):
        capacity = 0
        weights = []
        value = optimal_weight_simplified(capacity, weights)
        self.assertEqual(0, value)
        self.assertTrue(capacity >= value)

    def test_with_non_zero_capacity_and_empty_weights(self):
        capacity = 123
        weights = []
        value = optimal_weight_simplified(capacity, weights)
        self.assertEqual(0, value)
        self.assertTrue(capacity >= value)

    def test_with_capacity_as_1_and_weights_as_1(self):
        capacity = 1
        weights = [ 1 ]
        value = optimal_weight_simplified(capacity, weights)
        self.assertEqual(1, value)
        self.assertTrue(capacity >= value)

    def test_with_capacity_as_1_and_duplicate_weights(self):
        capacity = 1
        weights = [ 1, 1 ]
        value = optimal_weight_simplified(capacity, weights)
        self.assertEqual(1, value)
        self.assertTrue(capacity >= value)

    def test_with_capacity_as_1_and_weights_as_2(self):
        capacity = 1
        weights = [ 2 ]
        value = optimal_weight_simplified(capacity, weights)
        self.assertEqual(0, value)
        self.assertTrue(capacity >= value)

    def test_with_capacity_as_1_and_weights_as_1_and_2(self):
        capacity = 1
        weights = [ 1, 2 ]
        value = optimal_weight_simplified(capacity, weights)
        self.assertEqual(1, value)
        self.assertTrue(capacity >= value)

    def test_with_capacity_as_1_and_weights_as_2_and_3(self):
        capacity = 1
        weights = [ 2, 3 ]
        value = optimal_weight_simplified(capacity, weights)
        self.assertEqual(0, value)
        self.assertTrue(capacity >= value)

    def test_with_capacity_as_2_and_weights_as_1_and_2(self):
        capacity = 2
        weights = [ 1, 2 ]
        value = optimal_weight_simplified(capacity, weights)
        self.assertEqual(2, value)
        self.assertTrue(capacity >= value)

    def test_with_capacity_as_10_and_several_weights(self):
        capacity = 10
        weights = [ 2, 4, 3, 6 ]
        value = optimal_weight_simplified(capacity, weights)
        self.assertEqual(10, value)
        self.assertTrue(capacity >= value)

    def test_with_capacity_as_10_and_several_weights_with_duplicates(self):
        capacity = 10
        weights = [ 2, 4, 3, 6, 2, 4, 3, 6 ]
        value = optimal_weight_simplified(capacity, weights)
        self.assertEqual(10, value)
        self.assertTrue(capacity >= value)

    def test_with_capacity_as_11_and_several_weights(self):
        capacity = 11
        weights = [ 2, 4, 3, 6 ]
        value = optimal_weight_simplified(capacity, weights)
        self.assertEqual(11, value)
        self.assertTrue(capacity >= value)

    def test_with_capacity_as_12_and_several_weights(self):
        capacity = 12
        weights = [ 2, 4, 3, 6 ]
        value = optimal_weight_simplified(capacity, weights)
        self.assertEqual(12, value)
        self.assertTrue(capacity >= value)

    def test_with_capacity_as_13_and_several_weights(self):
        capacity = 13
        weights = [ 2, 4, 3, 6 ]
        value = optimal_weight_simplified(capacity, weights)
        self.assertEqual(13, value)
        self.assertTrue(capacity >= value)

    def test_with_capacity_as_14_and_several_weights(self):
        capacity = 14
        weights = [ 2, 4, 3, 6 ]
        value = optimal_weight_simplified(capacity, weights)
        self.assertEqual(13, value)
        self.assertTrue(capacity >= value)

    def test_with_capacity_as_10_and_bars_as_1_4_8(self):
        capacity = 10
        weights = [ 1, 4, 8 ]
        value = optimal_weight_simplified(capacity, weights)
        self.assertEqual(9, value)
        self.assertTrue(capacity >= value)

if __name__ == '__main__':
    unittest.main()
