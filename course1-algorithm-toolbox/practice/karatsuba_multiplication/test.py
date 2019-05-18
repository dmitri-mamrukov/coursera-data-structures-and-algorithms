#!/usr/bin/python3

import random

import unittest

from karatsuba_multiplication import karatsuba

class karatsubaTestCase(unittest.TestCase):

    def assert_karatsuba_multiplication(self, x, y):
        expected = x * y
        result = karatsuba(x, y)
        self.assertEqual(expected, result,
            ("Failed with x: %s and y: %s. "
            "Expected: %s but got %s") % (x, y, expected, result))
        result = karatsuba(y, x)
        self.assertEqual(expected, result,
            ("Failed with x: %s and y: %s. "
            "Expected: %s but got %s") % (y, x, expected, result))

    def test_same_numbers(self):
        self.assertEqual(25, karatsuba(5, 5))
        self.assertEqual(2500, karatsuba(50, 50))
        self.assertEqual(250000, karatsuba(500, 500))
        self.assertEqual(25000000, karatsuba(5000, 5000))
        self.assertEqual(2500000000, karatsuba(50000, 50000))
        self.assertEqual(250000000000, karatsuba(500000, 500000))
        self.assertEqual(25000000000000, karatsuba(5000000, 5000000))

    def test_one_digit_numbers(self):
        self.assert_karatsuba_multiplication(4, 3)

    def test_two_digit_numbers(self):
        self.assert_karatsuba_multiplication(19, 21)

    def test_three_digit_numbers(self):
        self.assert_karatsuba_multiplication(223, 321)

    def test_four_digit_numbers(self):
        self.assert_karatsuba_multiplication(1234, 4321)

    def test_five_digit_numbers(self):
        self.assert_karatsuba_multiplication(12345, 54321)

    def test_six_digit_numbers(self):
        self.assert_karatsuba_multiplication(123456, 654321)

    def test_seven_digit_numbers(self):
        self.assert_karatsuba_multiplication(1234567, 7654321)

    def test_eight_digit_numbers(self):
        self.assert_karatsuba_multiplication(12345678, 87654321)

    def test_nine_digit_numbers(self):
        self.assert_karatsuba_multiplication(123456789, 987654321)

    def test_different_sizes(self):
        self.assert_karatsuba_multiplication(2, 21)
        self.assert_karatsuba_multiplication(103, 3097)
        self.assert_karatsuba_multiplication(3097, 103)

    def test_random_cases(self):
        for i in range(1000):
            x = random.randint(1, 100000)
            y = random.randint(1, 100000)
            self.assert_karatsuba_multiplication(x, y)

if __name__ == '__main__':
    unittest.main()
