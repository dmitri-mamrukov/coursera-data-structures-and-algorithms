#!/usr/bin/python3

import unittest

from util import Util

class UtilTestCase(unittest.TestCase):

    @unittest.expectedFailure
    def test_with_data_of_length_0(self):
        Util.max_pairwise_product([])

    @unittest.expectedFailure
    def test_with_data_of_length_1(self):
        Util.max_pairwise_product([ 1 ])

    @unittest.expectedFailure
    def test_with_preceeding_lower_bound_element(self):
        Util.max_pairwise_product([ -1 ])

    @unittest.expectedFailure
    def test_with_preceeding_lower_bound_among_elements(self):
        Util.max_pairwise_product([ 1, -1, 3 ])

    def test_with_two_small_in_ascending_order(self):
        data = [ 2, 3 ]
        self.assertEqual(6, Util.max_pairwise_product(data))

    def test_with_two_small_in_descending_order(self):
        data = [ 3, 2 ]
        self.assertEqual(6, Util.max_pairwise_product(data))

    def test_with_two_medium_in_ascending_order(self):
        data = [ 123, 456 ]
        self.assertEqual(56088, Util.max_pairwise_product(data))

    def test_with_two_medium_in_descending_order(self):
        data = [ 456, 123 ]
        self.assertEqual(56088, Util.max_pairwise_product(data))

    def test_with_two_large_in_ascending_order(self):
        data = [ 90000, 100000 ]
        self.assertEqual(9000000000, Util.max_pairwise_product(data))

    def test_with_two_large_in_descending_order(self):
        data = [ 100000, 90000 ]
        self.assertEqual(9000000000, Util.max_pairwise_product(data))

    def test_with_two_large_and_two_maximums(self):
        data = [ 100000, 100000 ]
        self.assertEqual(10000000000,
            Util.max_pairwise_product(data))

    def test_with_three_small_in_ascending_order(self):
        data = [ 1, 2, 3 ]
        self.assertEqual(6, Util.max_pairwise_product(data))

    def test_with_three_small_in_descending_order(self):
        data = [ 3, 2, 1 ]
        self.assertEqual(6, Util.max_pairwise_product(data))

    def test_with_several_in_ascending_order(self):
        data = [ 1, 2, 3, 4, 5, 6, 7, 8, 9, 10 ]
        self.assertEqual(90, Util.max_pairwise_product(data))

    def test_with_several_in_desscending_order(self):
        data = [ 10, 9, 8, 7, 6, 5, 4, 3, 2, 1 ]
        self.assertEqual(90, Util.max_pairwise_product(data))

    def test_with_several_numbers_and_two_maximums(self):
        data = [ 4, 6, 2, 6, 1 ]
        self.assertEqual(36, Util.max_pairwise_product(data))

    def test_with_several_numbers(self):
        data = [ 7, 5, 14, 2, 8, 8, 10, 1, 2, 3 ]
        self.assertEqual(140, Util.max_pairwise_product(data))

if __name__ == '__main__':
    unittest.main()
