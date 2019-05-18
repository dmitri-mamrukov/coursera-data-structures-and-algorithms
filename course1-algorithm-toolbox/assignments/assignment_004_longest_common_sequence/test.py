#!/usr/bin/python3

import unittest

from longest_common_sequence import longest_common_sequence, \
    longest_common_sequence_different_matrix

class LongestCommonSequenceTestCase(unittest.TestCase):

    def assert_solution(self, a, b, c, indices, expected_sequence):
        self.assertEqual(len(indices), len(expected_sequence))

        sequence = []
        for group in reversed(indices):
            i, j, k = group
            self.assertTrue(a[i] == b[j] == c[k])
            sequence.append(a[i])

        self.assertEqual(expected_sequence, sequence)

    def test_with_1_and_1_and_1(self):
        a = [ 1 ]
        b = [ 1 ]
        c = [ 1 ]
        value, indices = longest_common_sequence(a, b, c)
        self.assertEqual(1, value)
        self.assertEqual([ (0, 0, 0) ], indices)
        self.assert_solution(a, b, c, indices, [ 1 ])

    def test_with_1_and_2_and_1(self):
        a = [ 1 ]
        b = [ 2 ]
        c = [ 1 ]
        value, indices = longest_common_sequence(a, b, c)
        self.assertEqual(0, value)
        self.assertEqual([], indices)
        self.assert_solution(a, b, c, indices, [])

    def test_with_1_2_and_1_2_and_1_2(self):
        a = [ 1, 2 ]
        b = [ 1, 2 ]
        c = [ 1, 2 ]
        value, indices = longest_common_sequence(a, b, c)
        self.assertEqual(2, value)
        self.assertEqual([ (1, 1, 1), (0, 0, 0) ], indices)
        self.assert_solution(a, b, c, indices, [ 1, 2 ])

    def test_with_1_3_3_and_2_1_3_and_1_3_5(self):
        a = [ 1, 2, 3 ]
        b = [ 2, 1, 3 ]
        c = [ 1, 3, 5 ]
        value, indices = longest_common_sequence(a, b, c)
        self.assertEqual(2, value)
        self.assertEqual([ (2, 2, 1), (0, 1, 0) ], indices)
        self.assert_solution(a, b, c, indices, [ 1, 3 ])

    def test_with_8_3_2_1_7_and_8_2_1_3_8_10_7_and_6_8_3_1_4(self):
        a = [ 8, 3, 2, 1, 7 ]
        b = [ 8, 2, 1, 3, 8, 10, 7 ]
        c = [ 6, 8, 3, 1, 4, 7 ]
        value, indices = longest_common_sequence(a, b, c)
        self.assertEqual(3, value)
        self.assertEqual([ (4, 6, 5), (1, 3, 2), (0, 0, 1) ], indices)
        self.assert_solution(a, b, c, indices, [ 8, 3, 7 ])

    def test_with_large_inputs(self):
        a = [ 6, 6, 6, 2, 2, 2, 0, 5, 4, 2, 6, 3, 3, 1, 4, 4, 4, 3, 7, 1, 2]
        b = [ 5, 4, 3, 2, 1, 2, 7, 4, 1, 3, 5, 4, 2, 3, 7, 7, 7, 7, 7 ]
        c = [ 6, 6, 6, 4, 6, 6, 4, 5, 6, 5, 4, 6, 4, 0, 5, 7, 4, 2, 5 ]
        value, indices = longest_common_sequence(a, b, c)
        self.assertEqual(5, value)
        self.assertEqual([ (20, 12, 17), (16, 11, 16), (15, 7, 12),
            (14, 1, 10), (7, 0, 7) ], indices)
        self.assert_solution(a, b, c, indices, [ 5, 4, 4, 4, 2 ])

class LongestCommonSequenceDifferentMatrixTestCase(unittest.TestCase):

    def test_with_1_and_1_and_1(self):
        a = [ 1 ]
        b = [ 1 ]
        c = [ 1 ]
        value = longest_common_sequence_different_matrix(a, b, c)
        self.assertEqual(1, value)

    def test_with_1_and_2_and_1(self):
        a = [ 1 ]
        b = [ 2 ]
        c = [ 1 ]
        value = longest_common_sequence_different_matrix(a, b, c)
        self.assertEqual(0, value)

    def test_with_1_2_and_1_2_and_1_2(self):
        a = [ 1, 2 ]
        b = [ 1, 2 ]
        c = [ 1, 2 ]
        value = longest_common_sequence_different_matrix(a, b, c)
        self.assertEqual(2, value)

    def test_with_1_3_3_and_2_1_3_and_1_3_5(self):
        a = [ 1, 2, 3 ]
        b = [ 2, 1, 3 ]
        c = [ 1, 3, 5 ]
        value = longest_common_sequence_different_matrix(a, b, c)
        self.assertEqual(2, value)

    def test_with_8_3_2_1_7_and_8_2_1_3_8_10_7_and_6_8_3_1_4(self):
        a = [ 8, 3, 2, 1, 7 ]
        b = [ 8, 2, 1, 3, 8, 10, 7 ]
        c = [ 6, 8, 3, 1, 4, 7 ]
        value = longest_common_sequence_different_matrix(a, b, c)
        self.assertEqual(3, value)

    def test_with_large_inputs(self):
        a = [ 6, 6, 6, 2, 2, 2, 0, 5, 4, 2, 6, 3, 3, 1, 4, 4, 4, 3, 7, 1, 2]
        b = [ 5, 4, 3, 2, 1, 2, 7, 4, 1, 3, 5, 4, 2, 3, 7, 7, 7, 7, 7 ]
        c = [ 6, 6, 6, 4, 6, 6, 4, 5, 6, 5, 4, 6, 4, 0, 5, 7, 4, 2, 5 ]
        value = longest_common_sequence_different_matrix(a, b, c)
        self.assertEqual(5, value)

if __name__ == '__main__':
    unittest.main()
