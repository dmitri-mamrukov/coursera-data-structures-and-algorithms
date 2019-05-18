#!/usr/bin/python3

import unittest

from different_summands import optimal_summands

class OptimalSummandsProductTestCase(unittest.TestCase):

    @unittest.expectedFailure
    def test_with_preceeding_lower_bound_as_negative(self):
        optimal_summands(-1)

    @unittest.expectedFailure
    def test_with_preceeding_lower_bound_as_zero(self):
        optimal_summands(0)

    def test_with_1(self):
        n = 1
        result = optimal_summands(n)
        self.assertEqual(1, len(result))
        self.assertEqual(1, result[0])
        self.assertEqual(n, sum(result))

    def test_with_2(self):
        n = 2
        result = optimal_summands(n)
        self.assertEqual(1, len(result))
        self.assertEqual(2, result[0])
        self.assertEqual(n, sum(result))

    def test_with_3(self):
        n = 3
        result = optimal_summands(n)
        self.assertEqual(2, len(result))
        self.assertEqual(1, result[0])
        self.assertEqual(2, result[1])
        self.assertEqual(n, sum(result))

    def test_with_4(self):
        n = 4
        result = optimal_summands(n)
        self.assertEqual(2, len(result))
        self.assertEqual(1, result[0])
        self.assertEqual(3, result[1])
        self.assertEqual(n, sum(result))

    def test_with_5(self):
        n = 5
        result = optimal_summands(n)
        self.assertEqual(2, len(result))
        self.assertEqual(1, result[0])
        self.assertEqual(4, result[1])
        self.assertEqual(n, sum(result))

    def test_with_6(self):
        n = 6
        result = optimal_summands(n)
        self.assertEqual(3, len(result))
        self.assertEqual(1, result[0])
        self.assertEqual(2, result[1])
        self.assertEqual(3, result[2])
        self.assertEqual(n, sum(result))

    def test_with_7(self):
        n = 7
        result = optimal_summands(n)
        self.assertEqual(3, len(result))
        self.assertEqual(1, result[0])
        self.assertEqual(2, result[1])
        self.assertEqual(4, result[2])
        self.assertEqual(n, sum(result))

    def test_with_8(self):
        n = 8
        result = optimal_summands(n)
        self.assertEqual(3, len(result))
        self.assertEqual(1, result[0])
        self.assertEqual(2, result[1])
        self.assertEqual(5, result[2])
        self.assertEqual(n, sum(result))

    def test_with_9(self):
        n = 9
        result = optimal_summands(n)
        self.assertEqual(3, len(result))
        self.assertEqual(1, result[0])
        self.assertEqual(2, result[1])
        self.assertEqual(6, result[2])
        self.assertEqual(n, sum(result))

    def test_with_10(self):
        n = 10
        result = optimal_summands(n)
        self.assertEqual(4, len(result))
        self.assertEqual(1, result[0])
        self.assertEqual(2, result[1])
        self.assertEqual(3, result[2])
        self.assertEqual(4, result[3])
        self.assertEqual(n, sum(result))

    def test_with_1000(self):
        n = 1000
        result = optimal_summands(n)
        self.assertEqual(44, len(result))
        self.assertEqual(n, sum(result))

    def test_with_1000000(self):
        n = 1000000
        result = optimal_summands(n)
        self.assertEqual(1413, len(result))
        self.assertEqual(n, sum(result))

    def test_with_1000000000(self):
        n = 1000000000
        result = optimal_summands(n)
        self.assertEqual(44720, len(result))
        self.assertEqual(n, sum(result))

if __name__ == '__main__':
    unittest.main()
