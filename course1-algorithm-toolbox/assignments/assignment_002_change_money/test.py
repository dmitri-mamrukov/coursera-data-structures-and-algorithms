#!/usr/bin/python3

import math
import unittest

from change import get_change

class GetChangeTestCase(unittest.TestCase):

    @unittest.expectedFailure
    def test_with_preceeding_lower_bound_as_negative(self):
        get_change(-1)

    @unittest.expectedFailure
    def test_with_preceeding_lower_bound_as_zero(self):
        get_change(0)

    def test_with_1(self):
        self.assertEqual(1, get_change(1))

    def test_with_2(self):
        self.assertEqual(2, get_change(2))

    def test_with_3(self):
        self.assertEqual(3, get_change(3))

    def test_with_4(self):
        self.assertEqual(4, get_change(4))

    def test_with_5(self):
        self.assertEqual(1, get_change(5))

    def test_with_6(self):
        self.assertEqual(2, get_change(6))

    def test_with_7(self):
        self.assertEqual(3, get_change(7))

    def test_with_8(self):
        self.assertEqual(4, get_change(8))

    def test_with_9(self):
        self.assertEqual(5, get_change(9))

    def test_with_10(self):
        self.assertEqual(1, get_change(10))

    def test_with_11(self):
        self.assertEqual(2, get_change(11))

    def test_with_12(self):
        self.assertEqual(3, get_change(12))

    def test_with_13(self):
        self.assertEqual(4, get_change(13))

    def test_with_14(self):
        self.assertEqual(5, get_change(14))

    def test_with_15(self):
        self.assertEqual(2, get_change(15))

    def test_with_16(self):
        self.assertEqual(3, get_change(16))

    def test_with_17(self):
        self.assertEqual(4, get_change(17))

    def test_with_18(self):
        self.assertEqual(5, get_change(18))

    def test_with_19(self):
        self.assertEqual(6, get_change(19))

    def test_with_20(self):
        self.assertEqual(2, get_change(20))

    def test_with_28(self):
        self.assertEqual(6, get_change(28))

    def test_with_999(self):
        self.assertEqual(104, get_change(999))

    def test_with_1000(self):
        self.assertEqual(100, get_change(int(math.pow(10, 3))))

if __name__ == '__main__':
    unittest.main()
