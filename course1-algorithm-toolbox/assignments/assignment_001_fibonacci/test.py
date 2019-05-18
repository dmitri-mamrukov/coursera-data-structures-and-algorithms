#!/usr/bin/python3

import unittest

from fib import calc_fibonacci

class CalcFibonacciTestCase(unittest.TestCase):

    @unittest.expectedFailure
    def test_with_preceeding_lower_bound(self):
        calc_fibonacci(-1)

    def test_with_n_as_0(self):
        self.assertEqual(0, calc_fibonacci(0))

    def test_with_n_as_1(self):
        self.assertEqual(1, calc_fibonacci(1))

    def test_with_n_as_2(self):
        self.assertEqual(1, calc_fibonacci(2))

    def test_with_n_as_3(self):
        self.assertEqual(2, calc_fibonacci(3))

    def test_with_n_as_4(self):
        self.assertEqual(3, calc_fibonacci(4))

    def test_with_n_as_5(self):
        self.assertEqual(5, calc_fibonacci(5))

    def test_with_n_as_6(self):
        self.assertEqual(8, calc_fibonacci(6))

    def test_with_n_as_7(self):
        self.assertEqual(13, calc_fibonacci(7))

    def test_with_n_as_8(self):
        self.assertEqual(21, calc_fibonacci(8))

    def test_with_n_as_9(self):
        self.assertEqual(34, calc_fibonacci(9))

    def test_with_n_as_10(self):
        self.assertEqual(55, calc_fibonacci(10))

    def test_with_n_as_20(self):
        self.assertEqual(6765, calc_fibonacci(20))

    def test_with_n_as_30(self):
        self.assertEqual(832040, calc_fibonacci(30))

    def test_with_n_as_40(self):
        self.assertEqual(102334155, calc_fibonacci(40))

    def test_with_n_as_45(self):
        self.assertEqual(1134903170, calc_fibonacci(45))

if __name__ == '__main__':
    unittest.main()
