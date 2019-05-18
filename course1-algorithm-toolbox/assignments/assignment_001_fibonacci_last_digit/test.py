#!/usr/bin/python3

import unittest

from fibonacci_last_digit import get_fibonacci_last_digit

class GetFibonacciLastDigitTestCase(unittest.TestCase):

    @unittest.expectedFailure
    def test_with_preceeding_lower_bound(self):
        get_fibonacci_last_digit(-1)

    def test_with_n_as_0(self):
        self.assertEqual(0, get_fibonacci_last_digit(0))

    def test_with_n_as_1(self):
        self.assertEqual(1, get_fibonacci_last_digit(1))

    def test_with_n_as_2(self):
        self.assertEqual(1, get_fibonacci_last_digit(2))

    def test_with_n_as_3(self):
        self.assertEqual(2, get_fibonacci_last_digit(3))

    def test_with_n_as_4(self):
        self.assertEqual(3, get_fibonacci_last_digit(4))

    def test_with_n_as_5(self):
        self.assertEqual(5, get_fibonacci_last_digit(5))

    def test_with_n_as_6(self):
        self.assertEqual(8, get_fibonacci_last_digit(6))

    def test_with_n_as_7(self):
        self.assertEqual(3, get_fibonacci_last_digit(7))

    def test_with_n_as_8(self):
        self.assertEqual(1, get_fibonacci_last_digit(8))

    def test_with_n_as_9(self):
        self.assertEqual(4, get_fibonacci_last_digit(9))

    def test_with_n_as_10(self):
        self.assertEqual(5, get_fibonacci_last_digit(10))

    def test_with_n_as_20(self):
        self.assertEqual(5, get_fibonacci_last_digit(20))

    def test_with_n_as_30(self):
        self.assertEqual(0, get_fibonacci_last_digit(30))

    def test_with_n_as_40(self):
        self.assertEqual(5, get_fibonacci_last_digit(40))

    def test_with_n_as_327305(self):
        self.assertEqual(5, get_fibonacci_last_digit(327305))

    def test_with_n_as_10000000(self):
        self.assertEqual(5, get_fibonacci_last_digit(10000000))

if __name__ == '__main__':
    unittest.main()
