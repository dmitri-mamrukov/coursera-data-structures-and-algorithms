#!/usr/bin/python3

import unittest

from inversions import merge_sort

class MergeSortTestCase(unittest.TestCase):

    def assert_sorted(self, data):
        if len(data) >= 2:
            i = 0
            for j in range(1, len(data)):
                self.assertTrue(data[i] <= data[j])

    def assert_process(self, data, expected_number_of_inversions):
        self.assertEqual(expected_number_of_inversions, merge_sort(data))
        self.assert_sorted(data)

    def test_with_empty_data(self):
        self.assert_process([], 0)

    def test_with_one_element_data(self):
        self.assert_process([ 1 ], 0)

    def test_with_two_element_data(self):
        self.assert_process([ 1, 2 ], 0)
        self.assert_process([ 2, 1 ], 1)

        self.assert_process([ 3, 3 ], 0)

    def test_with_three_element_data(self):
        self.assert_process([ 1, 2, 3 ], 0)
        self.assert_process([ 1, 3, 2 ], 1)
        self.assert_process([ 2, 1, 3 ], 1)
        self.assert_process([ 2, 3, 1 ], 2)
        self.assert_process([ 3, 1, 2 ], 2)
        self.assert_process([ 3, 2, 1 ], 3)

        self.assert_process([ 3, 3, 3 ], 0)

    def test_with_four_element_data(self):
        self.assert_process([ 1, 2, 3, 4 ], 0)
        self.assert_process([ 1, 2, 4, 3 ], 1)
        self.assert_process([ 1, 3, 2, 4 ], 1)
        self.assert_process([ 1, 3, 4, 2 ], 2)
        self.assert_process([ 1, 4, 2, 3 ], 2)
        self.assert_process([ 1, 4, 3, 2 ], 3)
        self.assert_process([ 2, 1, 3, 4 ], 1)
        self.assert_process([ 2, 1, 4, 3 ], 2)
        self.assert_process([ 2, 3, 1, 4 ], 2)
        self.assert_process([ 2, 3, 4, 1 ], 3)
        self.assert_process([ 2, 4, 1, 3 ], 3)
        self.assert_process([ 2, 4, 3, 1 ], 4)
        self.assert_process([ 3, 1, 2, 4 ], 2)
        self.assert_process([ 3, 1, 4, 2 ], 3)
        self.assert_process([ 3, 2, 1, 4 ], 3)
        self.assert_process([ 3, 2, 4, 1 ], 4)
        self.assert_process([ 3, 4, 1, 2 ], 4)
        self.assert_process([ 3, 4, 2, 1 ], 5)
        self.assert_process([ 4, 1, 2, 3 ], 3)
        self.assert_process([ 4, 1, 3, 2 ], 4)
        self.assert_process([ 4, 2, 1, 3 ], 4)
        self.assert_process([ 4, 2, 3, 1 ], 5)
        self.assert_process([ 4, 3, 1, 2 ], 5)
        self.assert_process([ 4, 3, 2, 1 ], 6)

        self.assert_process([ 3, 3, 3, 3 ], 0)

    def test_with_several_element_data(self):
        self.assert_process([ 2, 3, 9, 2, 9 ], 2)

if __name__ == '__main__':
    unittest.main()
