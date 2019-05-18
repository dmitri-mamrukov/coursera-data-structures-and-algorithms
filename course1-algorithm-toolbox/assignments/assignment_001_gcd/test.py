#!/usr/bin/python3

import math
import unittest

from gcd import gcd

class GcdTestCase(unittest.TestCase):

    @unittest.expectedFailure
    def test_with_preceeding_lower_bound_of_a_as_negative(self):
        gcd(-1, 1)

    @unittest.expectedFailure
    def test_with_preceeding_lower_bound_of_a_as_zero(self):
        gcd(0, 1)

    @unittest.expectedFailure
    def test_with_preceeding_lower_bound_of_b_as_negative(self):
        gcd(1, -1)

    @unittest.expectedFailure
    def test_with_preceeding_lower_bound_of_b_as_zero(self):
        gcd(1, 0)

    def test_with_1_and_1(self):
        self.assertEqual(1, gcd(1, 1))

    def test_with_2_and_1(self):
        self.assertEqual(1, gcd(2, 1))

    def test_with_1_and_2(self):
        self.assertEqual(1, gcd(1, 2))

    def test_with_10_and_1(self):
        self.assertEqual(1, gcd(10, 1))

    def test_with_1_and_10(self):
        self.assertEqual(1, gcd(1, 10))

    def test_with_1_and_2000000000(self):
        self.assertEqual(1, gcd(1, 2 * int(math.pow(10, 9))))

    def test_with_2000000000_and_1(self):
        self.assertEqual(1, gcd(2 * int(math.pow(10, 9)), 1))

    def test_with_3_and_2(self):
        self.assertEqual(1, gcd(3, 2))

    def test_with_2_and_3(self):
        self.assertEqual(1, gcd(2, 3))

    def test_with_4_and_2(self):
        self.assertEqual(2, gcd(4, 2))

    def test_with_2_and_4(self):
        self.assertEqual(2, gcd(2, 4))

    def test_with_10_and_4(self):
        self.assertEqual(2, gcd(10, 4))

    def test_with_4_and_10(self):
        self.assertEqual(2, gcd(4, 10))

    def test_with_18_and_35(self):
        self.assertEqual(1, gcd(18, 35))

    def test_with_35_and_18(self):
        self.assertEqual(1, gcd(35, 18))

    def test_with_85_and_30(self):
        self.assertEqual(5, gcd(85, 30))

    def test_with_30_and_85(self):
        self.assertEqual(5, gcd(30, 85))

    def test_with_180_and_126(self):
        self.assertEqual(18, gcd(180, 126))

    def test_with_126_and_180(self):
        self.assertEqual(18, gcd(126, 180))

    def test_with_391_and_299(self):
        self.assertEqual(23, gcd(391, 299))

    def test_with_299_and_391(self):
        self.assertEqual(23, gcd(299, 391))

    def test_with_9000_and_1350(self):
        self.assertEqual(450, gcd(9000, 1350))

    def test_with_1350_and_9000(self):
        self.assertEqual(450, gcd(1350, 9000))

    def test_with_28851538_and_1183019(self):
        self.assertEqual(17657, gcd(28851538, 1183019))

    def test_with_1183019_and_28851538(self):
        self.assertEqual(17657, gcd(1183019, 28851538))

    def test_with_2000000000_and_20000(self):
        self.assertEqual(2 * int(math.pow(10, 4)),
            gcd(2 * int(math.pow(10, 9)), 2 * int(math.pow(10, 4))))

    def test_with_20000_and_2000000000(self):
        self.assertEqual(2 * int(math.pow(10, 4)),
            gcd(2 * int(math.pow(10, 4)), 2 * int(math.pow(10, 9))))

    def test_with_2000000000_and_2000000000(self):
        self.assertEqual(2 * int(math.pow(10, 9)),
            gcd(2 * int(math.pow(10, 9)), 2 * int(math.pow(10, 9))))

if __name__ == '__main__':
    unittest.main()
