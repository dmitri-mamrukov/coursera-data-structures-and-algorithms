#!/usr/bin/python3

import unittest

from binary_search import solve_recursively
from binary_search import solve_iteratively

class SolveRecursivelyTestCase(unittest.TestCase):

    def test_with_empty_data(self):
        self.assertEqual(-1, solve_recursively([], 5))

    def test_with_one_element_data_and_missing_key(self):
        self.assertEqual(-1, solve_recursively([ 3 ], 5))

    def test_with_one_element_data_and_present_key(self):
        self.assertEqual(0, solve_recursively([ 5 ], 5))

    def test_with_two_element_data_and_missing_key(self):
        self.assertEqual(-1, solve_recursively([ 1, 2 ], 5))

    def test_with_two_element_data_and_present_key(self):
        self.assertEqual(0, solve_recursively([ 1, 2 ], 1))
        self.assertEqual(1, solve_recursively([ 1, 2 ], 2))

    def test_with_three_element_data_and_missing_key(self):
        self.assertEqual(-1, solve_recursively([ 1, 2, 3 ], 5))

    def test_with_three_element_data_and_present_key(self):
        self.assertEqual(0, solve_recursively([ 1, 2, 3 ], 1))
        self.assertEqual(1, solve_recursively([ 1, 2, 3 ], 2))
        self.assertEqual(2, solve_recursively([ 1, 2, 3 ], 3))

    def test_with_several_element_data_and_missing_key(self):
        self.assertEqual(-1, solve_recursively([ 5, -7, 3, 0, 9, -1, 9, ], 4))

    def test_with_several_element_data_and_present_key(self):
        self.assertEqual(5, solve_recursively([ 5, -7, 3, 0, 9, -1, 9, ], 9))

    def test_with_several_element_data_with_duplicates_and_missing_key(self):
        self.assertEqual(-1, solve_recursively([ 5, -7, 3, 0, 9, -1, 9, ], 4))

    def test_with_several_element_data_with_duplicates_and_present_key(self):
        self.assertEqual(2, solve_recursively([ 5, -7, 3, 0, 9, -1, 9, ], 0))

    def test_with_key_as_one_of_duplicates(self):
        self.assertEqual(4,
            solve_recursively([ 0, 1, 2, 4, 4, 4, 4, 7, 8, 9 ], 4))

    def test_with_all_duplicate_elements_and_lesser_key(self):
        self.assertEqual(-1,
            solve_recursively([ 3, 3, 3, 3, 3, 3, 3, 3, 3, 3 ], 1))

    def test_with_all_duplicate_elements_and_equal_key(self):
        self.assertEqual(4,
            solve_recursively([ 3, 3, 3, 3, 3, 3, 3, 3, 3, 3 ], 3))

    def test_with_all_duplicate_elements_and_greater_key(self):
        self.assertEqual(-1,
            solve_recursively([ 3, 3, 3, 3, 3, 3, 3, 3, 3, 3 ], 5))

class SolveIterativelyTestCase(unittest.TestCase):

    def test_with_empty_data(self):
        self.assertEqual(-1, solve_iteratively([], 5))

    def test_with_one_element_data_and_missing_key(self):
        self.assertEqual(-1, solve_iteratively([ 3 ], 5))

    def test_with_one_element_data_and_present_key(self):
        self.assertEqual(0, solve_iteratively([ 5 ], 5))

    def test_with_two_element_data_and_missing_key(self):
        self.assertEqual(-1, solve_iteratively([ 1, 2 ], 5))

    def test_with_two_element_data_and_present_key(self):
        self.assertEqual(0, solve_iteratively([ 1, 2 ], 1))
        self.assertEqual(1, solve_iteratively([ 1, 2 ], 2))

    def test_with_three_element_data_and_missing_key(self):
        self.assertEqual(-1, solve_iteratively([ 1, 2, 3 ], 5))

    def test_with_three_element_data_and_present_key(self):
        self.assertEqual(0, solve_iteratively([ 1, 2, 3 ], 1))
        self.assertEqual(1, solve_iteratively([ 1, 2, 3 ], 2))
        self.assertEqual(2, solve_iteratively([ 1, 2, 3 ], 3))

    def test_with_several_element_data_and_missing_key(self):
        self.assertEqual(-1, solve_iteratively([ 5, -7, 3, 0, 9, -1, 9 ], 4))

    def test_with_several_element_data_and_present_key(self):
        self.assertEqual(5, solve_iteratively([ 5, -7, 3, 0, 9, -1, 9 ], 9))

    def test_with_several_element_data_with_duplicates_and_missing_key(self):
        self.assertEqual(-1, solve_iteratively([ 5, -7, 3, 0, 9, -1, 9 ], 4))

    def test_with_several_element_data_with_duplicates_and_present_key(self):
        self.assertEqual(2, solve_iteratively([ 5, -7, 3, 0, 9, -1, 9 ], 0))

    def test_with_key_as_one_of_duplicates(self):
        self.assertEqual(4,
            solve_iteratively([ 0, 1, 2, 4, 4, 4, 4, 7, 8, 9 ], 4))

    def test_with_all_duplicate_elements_and_lesser_key(self):
        self.assertEqual(-1,
            solve_iteratively([ 3, 3, 3, 3, 3, 3, 3, 3, 3, 3 ], 1))

    def test_with_all_duplicate_elements_and_equal_key(self):
        self.assertEqual(4,
            solve_iteratively([ 3, 3, 3, 3, 3, 3, 3, 3, 3, 3 ], 3))

    def test_with_all_duplicate_elements_and_greater_key(self):
        self.assertEqual(-1,
            solve_iteratively([ 3, 3, 3, 3, 3, 3, 3, 3, 3, 3 ], 5))

if __name__ == '__main__':
    unittest.main()
