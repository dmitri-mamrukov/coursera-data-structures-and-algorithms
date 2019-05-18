#!/usr/bin/python3

import unittest

from binary_search import binary_search

class BinarySearchTestCase(unittest.TestCase):

    def test_with_empty_data(self):
        self.assertEqual(-1, binary_search([], 5))

    def test_with_one_element_data_and_missing_key(self):
        self.assertEqual(-1, binary_search([ 3 ], 5))

    def test_with_one_element_data_and_present_key(self):
        self.assertEqual(0, binary_search([ 5 ], 5))

    def test_with_two_element_data_and_missing_key(self):
        self.assertEqual(-1, binary_search([ 1, 2 ], 5))

    def test_with_two_element_data_and_present_key(self):
        self.assertEqual(0, binary_search([ 1, 2 ], 1))
        self.assertEqual(1, binary_search([ 1, 2 ], 2))

    def test_with_three_element_data_and_missing_key(self):
        self.assertEqual(-1, binary_search([ 1, 2, 3 ], 5))

    def test_with_three_element_data_and_present_key(self):
        self.assertEqual(0, binary_search([ 1, 2, 3 ], 1))
        self.assertEqual(1, binary_search([ 1, 2, 3 ], 2))
        self.assertEqual(2, binary_search([ 1, 2, 3 ], 3))

    def test_with_several_element_data_and_missing_key(self):
        self.assertEqual(-1, binary_search([ -7, -1, 0, 3, 5, 8, 9 ], 4))

    def test_with_several_element_data_and_present_key(self):
        self.assertEqual(5, binary_search([ -7, -1, 0, 3, 5, 8, 9 ], 8))

    def test_with_several_element_data_with_duplicates_and_missing_key(self):
        self.assertEqual(-1, binary_search([ -7, -1, 0, 3, 5, 9, 9 ], 4))

    def test_with_several_element_data_with_duplicates_and_present_key(self):
        self.assertEqual(2, binary_search([ -7, -1, 0, 3, 5, 9, 9 ], 0))

if __name__ == '__main__':
    unittest.main()
