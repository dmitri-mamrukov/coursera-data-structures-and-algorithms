#!/usr/bin/python3

import math
import unittest

from fibonacci_modulo import calc_fibonacci_modulo

class FibonacciModuloTestCase(unittest.TestCase):

    @unittest.expectedFailure
    def test_with_preceeding_lower_bound_of_n_as_negative(self):
        calc_fibonacci_modulo(-1, 2)

    @unittest.expectedFailure
    def test_with_preceeding_lower_bound_of_n_as_zero(self):
        calc_fibonacci_modulo(0, 2)

    @unittest.expectedFailure
    def test_with_preceeding_lower_bound_of_m_as_negative(self):
        calc_fibonacci_modulo(1, -1)

    @unittest.expectedFailure
    def test_with_preceeding_lower_bound_of_m_as_zero(self):
        calc_fibonacci_modulo(1, 0)

    @unittest.expectedFailure
    def test_with_preceeding_lower_bound_of_m_as_one(self):
        calc_fibonacci_modulo(1, 1)

    def test_with_15_and_2(self):
        self.assertEqual(0, calc_fibonacci_modulo(15, 2))

    def test_with_14_and_3(self):
        self.assertEqual(2, calc_fibonacci_modulo(14, 3))

    def test_with_2015_and_3(self):
        self.assertEqual(1, calc_fibonacci_modulo(2015, 3))

    def test_with_281621358815590_and_30524(self):
        self.assertEqual(11963, calc_fibonacci_modulo(281621358815590, 30524))

    def test_with_99999999999999999_and_100000(self):
        self.assertEqual(90626, calc_fibonacci_modulo(99999999999999999,
            int(math.pow(10, 5))))

    def test_with_1000000000000000000_and_100000(self):
        self.assertEqual(46875, calc_fibonacci_modulo(int(math.pow(10, 18)),
            int(math.pow(10, 5))))

if __name__ == '__main__':
    unittest.main()
