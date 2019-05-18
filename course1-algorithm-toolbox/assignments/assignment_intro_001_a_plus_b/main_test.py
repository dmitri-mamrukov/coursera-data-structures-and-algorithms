#!/usr/bin/python3

import unittest

from util import Util

class UtilTestCase(unittest.TestCase):

    def test_with_zeros(self):
        self.assertEqual(0, Util.sum(0, 0))

    def test_with_number_and_zero(self):
        self.assertEqual(5, Util.sum(5, 0))

    def test_with_zero_and_number(self):
        self.assertEqual(5, Util.sum(0, 5))

    def test_with_mediums(self):
        self.assertEqual(11, Util.sum(5, 6))
        self.assertEqual(11, Util.sum(6, 5))

    def test_with_maximums(self):
        self.assertEqual(18, Util.sum(9, 9))

if __name__ == '__main__':
    unittest.main()
