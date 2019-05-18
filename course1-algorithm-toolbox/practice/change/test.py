#!/usr/bin/python3

import unittest

from change import change

class SolveTestCase(unittest.TestCase):

    def test_with_zero_money_and_empty_coins(self):
        self.assertEqual([], change(0, []))

    def test_with_zero_money_and_one_coin(self):
        self.assertEqual([], change(0, [ 1 ]))

    def test_with_zero_money_and_two_coins(self):
        self.assertEqual([], change(0, [ 1, 2 ]))

    def test_with_zero_money_and_several_coins(self):
        self.assertEqual([], change(0, [ 1, 2, 3 ]))

    def test_with_money_as_1_and_coins_as_1(self):
        self.assertEqual([ 1 ], change(1, [ 1 ]))

    def test_with_money_as_1_and_coins_as_2(self):
        self.assertEqual([], change(1, [ 2 ]))

    def test_with_money_as_1_and_coins_as_3(self):
        self.assertEqual([], change(1, [ 3 ]))

    def test_with_money_as_2_and_coins_as_1(self):
        self.assertEqual([ 1, 1 ], change(2, [ 1 ]))

    def test_with_money_as_2_and_coins_as_2(self):
        self.assertEqual([ 2 ], change(2, [ 2 ]))

    def test_with_money_as_2_and_coins_as_3(self):
        self.assertEqual([], change(2, [ 3 ]))

    def test_with_money_as_3_and_coins_as_1(self):
        self.assertEqual([ 1, 1, 1 ], change(3, [ 1 ]))

    def test_with_money_as_3_and_coins_as_2(self):
        self.assertEqual([], change(3, [ 2 ]))

    def test_with_money_as_3_and_coins_as_3(self):
        self.assertEqual([ 3 ], change(3, [ 3 ]))

    def test_with_money_as_1_and_coins_as_1_2(self):
        self.assertEqual([ 1 ], change(1, [ 1, 2 ]))

    def test_with_money_as_1_and_coins_as_2_1(self):
        self.assertEqual([ 1 ], change(1, [ 2, 1 ]))

    def test_with_money_as_2_and_coins_as_1_2(self):
        self.assertEqual([ 2 ], change(2, [ 1, 2 ]))

    def test_with_money_as_2_and_coins_as_2_1(self):
        self.assertEqual([ 2 ], change(2, [ 2, 1 ]))

    def test_with_money_as_3_and_coins_as_1_2(self):
        self.assertEqual([ 1, 2 ], change(3, [ 1, 2 ]))

    def test_with_money_as_3_and_coins_as_2_1(self):
        self.assertEqual([ 2, 1 ], change(3, [ 2, 1 ]))

    def test_with_money_as_0_and_coins_as_1_5_6(self):
        self.assertEqual([], change(0, [ 1, 5, 6 ]))

    def test_with_money_as_0_and_coins_as_1_6_5(self):
        self.assertEqual([], change(0, [ 1, 6, 5 ]))

    def test_with_money_as_0_and_coins_as_5_1_6(self):
        self.assertEqual([], change(0, [ 5, 1, 6 ]))

    def test_with_money_as_0_and_coins_as_5_6_1(self):
        self.assertEqual([], change(0, [ 5, 6, 1 ]))

    def test_with_money_as_0_and_coins_as_6_1_5(self):
        self.assertEqual([], change(0, [ 6, 1, 5 ]))

    def test_with_money_as_0_and_coins_as_6_5_1(self):
        self.assertEqual([], change(0, [ 6, 5, 1 ]))

    def test_with_money_as_1_and_coins_as_1_5_6(self):
        self.assertEqual([ 1 ], change(1, [ 1, 5, 6 ]))

    def test_with_money_as_1_and_coins_as_1_6_5(self):
        self.assertEqual([ 1 ], change(1, [ 1, 6, 5 ]))

    def test_with_money_as_1_and_coins_as_5_1_6(self):
        self.assertEqual([ 1 ], change(1, [ 5, 1, 6 ]))

    def test_with_money_as_1_and_coins_as_5_6_1(self):
        self.assertEqual([ 1 ], change(1, [ 5, 6, 1 ]))

    def test_with_money_as_1_and_coins_as_6_1_5(self):
        self.assertEqual([ 1 ], change(1, [ 6, 1, 5 ]))

    def test_with_money_as_1_and_coins_as_6_5_1(self):
        self.assertEqual([ 1 ], change(1, [ 6, 5, 1 ]))

    def test_with_money_as_2_and_coins_as_1_5_6(self):
        self.assertEqual([ 1, 1 ], change(2, [ 1, 5, 6 ]))

    def test_with_money_as_2_and_coins_as_1_6_5(self):
        self.assertEqual([ 1, 1 ], change(2, [ 1, 6, 5 ]))

    def test_with_money_as_2_and_coins_as_5_1_6(self):
        self.assertEqual([ 1, 1 ], change(2, [ 5, 1, 6 ]))

    def test_with_money_as_2_and_coins_as_5_6_1(self):
        self.assertEqual([ 1, 1 ], change(2, [ 5, 6, 1 ]))

    def test_with_money_as_2_and_coins_as_6_1_5(self):
        self.assertEqual([ 1, 1 ], change(2, [ 6, 1, 5 ]))

    def test_with_money_as_2_and_coins_as_6_5_1(self):
        self.assertEqual([ 1, 1 ], change(2, [ 6, 5, 1 ]))

    def test_with_money_as_3_and_coins_as_1_5_6(self):
        self.assertEqual([ 1, 1, 1 ], change(3, [ 1, 5, 6 ]))

    def test_with_money_as_3_and_coins_as_1_6_5(self):
        self.assertEqual([ 1, 1, 1 ], change(3, [ 1, 6, 5 ]))

    def test_with_money_as_3_and_coins_as_5_1_6(self):
        self.assertEqual([ 1, 1, 1 ], change(3, [ 5, 1, 6 ]))

    def test_with_money_as_3_and_coins_as_5_6_1(self):
        self.assertEqual([ 1, 1, 1 ], change(3, [ 5, 6, 1 ]))

    def test_with_money_as_3_and_coins_as_6_1_5(self):
        self.assertEqual([ 1, 1, 1 ], change(3, [ 6, 1, 5 ]))

    def test_with_money_as_3_and_coins_as_6_5_1(self):
        self.assertEqual([ 1, 1, 1 ], change(3, [ 6, 5, 1 ]))

    def test_with_money_as_4_and_coins_as_1_5_6(self):
        self.assertEqual([ 1, 1, 1, 1 ], change(4, [ 1, 5, 6 ]))

    def test_with_money_as_4_and_coins_as_1_6_5(self):
        self.assertEqual([ 1, 1, 1, 1 ], change(4, [ 1, 6, 5 ]))

    def test_with_money_as_4_and_coins_as_5_1_6(self):
        self.assertEqual([ 1, 1, 1, 1 ], change(4, [ 5, 1, 6 ]))

    def test_with_money_as_4_and_coins_as_5_6_1(self):
        self.assertEqual([ 1, 1, 1, 1 ], change(4, [ 5, 6, 1 ]))

    def test_with_money_as_4_and_coins_as_6_1_5(self):
        self.assertEqual([ 1, 1, 1, 1 ], change(4, [ 6, 1, 5 ]))

    def test_with_money_as_4_and_coins_as_6_5_1(self):
        self.assertEqual([ 1, 1, 1, 1 ], change(4, [ 6, 5, 1 ]))

    def test_with_money_as_5_and_coins_as_1_5_6(self):
        self.assertEqual([ 5 ], change(5, [ 1, 5, 6 ]))

    def test_with_money_as_5_and_coins_as_1_6_5(self):
        self.assertEqual([ 5 ], change(5, [ 1, 6, 5 ]))

    def test_with_money_as_5_and_coins_as_5_1_6(self):
        self.assertEqual([ 5 ], change(5, [ 5, 1, 6 ]))

    def test_with_money_as_5_and_coins_as_5_6_1(self):
        self.assertEqual([ 5 ], change(5, [ 5, 6, 1 ]))

    def test_with_money_as_5_and_coins_as_6_1_5(self):
        self.assertEqual([ 5 ], change(5, [ 6, 1, 5 ]))

    def test_with_money_as_5_and_coins_as_6_5_1(self):
        self.assertEqual([ 5 ], change(5, [ 6, 5, 1 ]))

    def test_with_money_as_6_and_coins_as_1_5_6(self):
        self.assertEqual([ 6 ], change(6, [ 1, 5, 6 ]))

    def test_with_money_as_6_and_coins_as_1_6_5(self):
        self.assertEqual([ 6 ], change(6, [ 1, 6, 5 ]))

    def test_with_money_as_6_and_coins_as_5_1_6(self):
        self.assertEqual([ 6 ], change(6, [ 5, 1, 6 ]))

    def test_with_money_as_6_and_coins_as_5_6_1(self):
        self.assertEqual([ 6 ], change(6, [ 5, 6, 1 ]))

    def test_with_money_as_6_and_coins_as_6_1_5(self):
        self.assertEqual([ 6 ], change(6, [ 6, 1, 5 ]))

    def test_with_money_as_6_and_coins_as_6_5_1(self):
        self.assertEqual([ 6 ], change(6, [ 6, 5, 1 ]))

    def test_with_money_as_7_and_coins_as_1_5_6(self):
        self.assertEqual([ 1, 6 ], change(7, [ 1, 5, 6 ]))

    def test_with_money_as_7_and_coins_as_1_6_5(self):
        self.assertEqual([ 1, 6 ], change(7, [ 1, 6, 5 ]))

    def test_with_money_as_7_and_coins_as_5_1_6(self):
        self.assertEqual([ 1, 6 ], change(7, [ 5, 1, 6 ]))

    def test_with_money_as_7_and_coins_as_5_6_1(self):
        self.assertEqual([ 6, 1 ], change(7, [ 5, 6, 1 ]))

    def test_with_money_as_7_and_coins_as_6_1_5(self):
        self.assertEqual([ 6, 1 ], change(7, [ 6, 1, 5 ]))

    def test_with_money_as_7_and_coins_as_6_5_1(self):
        self.assertEqual([ 6, 1 ], change(7, [ 6, 5, 1 ]))

    def test_with_money_as_8_and_coins_as_1_5_6(self):
        self.assertEqual([ 1, 1, 6 ], change(8, [ 1, 5, 6 ]))

    def test_with_money_as_8_and_coins_as_1_6_5(self):
        self.assertEqual([ 1, 1, 6 ], change(8, [ 1, 6, 5 ]))

    def test_with_money_as_8_and_coins_as_5_1_6(self):
        self.assertEqual([ 1, 1, 6 ], change(8, [ 5, 1, 6 ]))

    def test_with_money_as_8_and_coins_as_5_6_1(self):
        self.assertEqual([ 6, 1, 1 ], change(8, [ 5, 6, 1 ]))

    def test_with_money_as_8_and_coins_as_6_1_5(self):
        self.assertEqual([ 6, 1, 1 ], change(8, [ 6, 1, 5 ]))

    def test_with_money_as_8_and_coins_as_6_5_1(self):
        self.assertEqual([ 6, 1, 1 ], change(8, [ 6, 5, 1 ]))

    def test_with_money_as_9_and_coins_as_1_5_6(self):
        self.assertEqual([ 1, 1, 1, 6 ], change(9, [ 1, 5, 6 ]))

    def test_with_money_as_9_and_coins_as_1_6_5(self):
        self.assertEqual([ 1, 1, 1, 6 ], change(9, [ 1, 6, 5 ]))

    def test_with_money_as_9_and_coins_as_5_1_6(self):
        self.assertEqual([ 1, 1, 1, 6 ], change(9, [ 5, 1, 6 ]))

    def test_with_money_as_9_and_coins_as_5_6_1(self):
        self.assertEqual([ 6, 1, 1, 1 ], change(9, [ 5, 6, 1 ]))

    def test_with_money_as_9_and_coins_as_6_1_5(self):
        self.assertEqual([ 6, 1, 1, 1 ], change(9, [ 6, 1, 5 ]))

    def test_with_money_as_9_and_coins_as_6_5_1(self):
        self.assertEqual([ 6, 1, 1, 1 ], change(9, [ 6, 5, 1 ]))

    def test_with_money_as_0_and_coins_as_2_5_6(self):
        self.assertEqual([], change(0, [ 2, 5, 6 ]))

    def test_with_money_as_0_and_coins_as_2_6_5(self):
        self.assertEqual([], change(0, [ 2, 6, 5 ]))

    def test_with_money_as_0_and_coins_as_5_2_6(self):
        self.assertEqual([], change(0, [ 5, 2, 6 ]))

    def test_with_money_as_0_and_coins_as_5_6_2(self):
        self.assertEqual([], change(0, [ 5, 6, 2 ]))

    def test_with_money_as_0_and_coins_as_6_2_5(self):
        self.assertEqual([], change(0, [ 6, 2, 5 ]))

    def test_with_money_as_0_and_coins_as_6_5_2(self):
        self.assertEqual([], change(0, [ 6, 5, 2 ]))

    def test_with_money_as_1_and_coins_as_2_5_6(self):
        self.assertEqual([], change(1, [ 2, 5, 6 ]))

    def test_with_money_as_1_and_coins_as_2_6_5(self):
        self.assertEqual([], change(1, [ 2, 6, 5 ]))

    def test_with_money_as_1_and_coins_as_5_2_6(self):
        self.assertEqual([], change(1, [ 5, 2, 6 ]))

    def test_with_money_as_1_and_coins_as_5_6_2(self):
        self.assertEqual([], change(1, [ 5, 6, 2 ]))

    def test_with_money_as_1_and_coins_as_6_2_5(self):
        self.assertEqual([], change(1, [ 6, 2, 5 ]))

    def test_with_money_as_1_and_coins_as_6_5_2(self):
        self.assertEqual([], change(1, [ 6, 5, 2 ]))

    def test_with_money_as_2_and_coins_as_2_5_6(self):
        self.assertEqual([ 2 ], change(2, [ 2, 5, 6 ]))

    def test_with_money_as_2_and_coins_as_2_6_5(self):
        self.assertEqual([ 2 ], change(2, [ 2, 6, 5 ]))

    def test_with_money_as_2_and_coins_as_5_2_6(self):
        self.assertEqual([ 2 ], change(2, [ 5, 2, 6 ]))

    def test_with_money_as_2_and_coins_as_5_6_2(self):
        self.assertEqual([ 2 ], change(2, [ 5, 6, 2 ]))

    def test_with_money_as_2_and_coins_as_6_2_5(self):
        self.assertEqual([ 2 ], change(2, [ 6, 2, 5 ]))

    def test_with_money_as_2_and_coins_as_6_5_2(self):
        self.assertEqual([ 2 ], change(2, [ 6, 5, 2 ]))

    def test_with_money_as_3_and_coins_as_2_5_6(self):
        self.assertEqual([], change(3, [ 2, 5, 6 ]))

    def test_with_money_as_3_and_coins_as_2_6_5(self):
        self.assertEqual([], change(3, [ 2, 6, 5 ]))

    def test_with_money_as_3_and_coins_as_5_2_6(self):
        self.assertEqual([], change(3, [ 5, 2, 6 ]))

    def test_with_money_as_3_and_coins_as_5_6_2(self):
        self.assertEqual([], change(3, [ 5, 6, 2 ]))

    def test_with_money_as_3_and_coins_as_6_2_5(self):
        self.assertEqual([], change(3, [ 6, 2, 5 ]))

    def test_with_money_as_3_and_coins_as_6_5_2(self):
        self.assertEqual([], change(3, [ 6, 5, 2 ]))

    def test_with_money_as_4_and_coins_as_2_5_6(self):
        self.assertEqual([ 2, 2 ], change(4, [ 2, 5, 6 ]))

    def test_with_money_as_4_and_coins_as_2_6_5(self):
        self.assertEqual([ 2, 2 ], change(4, [ 2, 6, 5 ]))

    def test_with_money_as_4_and_coins_as_5_2_6(self):
        self.assertEqual([ 2, 2 ], change(4, [ 5, 2, 6 ]))

    def test_with_money_as_4_and_coins_as_5_6_2(self):
        self.assertEqual([ 2, 2 ], change(4, [ 5, 6, 2 ]))

    def test_with_money_as_4_and_coins_as_6_2_5(self):
        self.assertEqual([ 2, 2 ], change(4, [ 6, 2, 5 ]))

    def test_with_money_as_4_and_coins_as_6_5_2(self):
        self.assertEqual([ 2, 2 ], change(4, [ 6, 5, 2 ]))

    def test_with_money_as_5_and_coins_as_2_5_6(self):
        self.assertEqual([ 5 ], change(5, [ 2, 5, 6 ]))

    def test_with_money_as_5_and_coins_as_2_6_5(self):
        self.assertEqual([ 5 ], change(5, [ 2, 6, 5 ]))

    def test_with_money_as_5_and_coins_as_5_2_6(self):
        self.assertEqual([ 5 ], change(5, [ 5, 2, 6 ]))

    def test_with_money_as_5_and_coins_as_5_6_2(self):
        self.assertEqual([ 5 ], change(5, [ 5, 6, 2 ]))

    def test_with_money_as_5_and_coins_as_6_2_5(self):
        self.assertEqual([ 5 ], change(5, [ 6, 2, 5 ]))

    def test_with_money_as_5_and_coins_as_6_5_2(self):
        self.assertEqual([ 5 ], change(5, [ 6, 5, 2 ]))

    def test_with_money_as_6_and_coins_as_2_5_6(self):
        self.assertEqual([ 6 ], change(6, [ 2, 5, 6 ]))

    def test_with_money_as_6_and_coins_as_2_6_5(self):
        self.assertEqual([ 6 ], change(6, [ 2, 6, 5 ]))

    def test_with_money_as_6_and_coins_as_5_2_6(self):
        self.assertEqual([ 6 ], change(6, [ 5, 2, 6 ]))

    def test_with_money_as_6_and_coins_as_5_6_2(self):
        self.assertEqual([ 6 ], change(6, [ 5, 6, 2 ]))

    def test_with_money_as_6_and_coins_as_6_2_5(self):
        self.assertEqual([ 6 ], change(6, [ 6, 2, 5 ]))

    def test_with_money_as_6_and_coins_as_6_5_2(self):
        self.assertEqual([ 6 ], change(6, [ 6, 5, 2 ]))

    def test_with_money_as_7_and_coins_as_2_5_6(self):
        self.assertEqual([ 2, 5 ], change(7, [ 2, 5, 6 ]))

    def test_with_money_as_7_and_coins_as_2_6_5(self):
        self.assertEqual([ 2, 5 ], change(7, [ 2, 6, 5 ]))

    def test_with_money_as_7_and_coins_as_5_2_6(self):
        self.assertEqual([ 5, 2 ], change(7, [ 5, 2, 6 ]))

    def test_with_money_as_7_and_coins_as_5_6_2(self):
        self.assertEqual([ 5, 2 ], change(7, [ 5, 6, 2 ]))

    def test_with_money_as_7_and_coins_as_6_2_5(self):
        self.assertEqual([ 2, 5 ], change(7, [ 6, 2, 5 ]))

    def test_with_money_as_7_and_coins_as_6_5_2(self):
        self.assertEqual([ 5, 2 ], change(7, [ 6, 5, 2 ]))

    def test_with_money_as_8_and_coins_as_2_5_6(self):
        self.assertEqual([ 2, 6 ], change(8, [ 2, 5, 6 ]))

    def test_with_money_as_8_and_coins_as_2_6_5(self):
        self.assertEqual([ 2, 6 ], change(8, [ 2, 6, 5 ]))

    def test_with_money_as_8_and_coins_as_5_2_6(self):
        self.assertEqual([ 2, 6 ], change(8, [ 5, 2, 6 ]))

    def test_with_money_as_8_and_coins_as_5_6_2(self):
        self.assertEqual([ 6, 2 ], change(8, [ 5, 6, 2 ]))

    def test_with_money_as_8_and_coins_as_6_2_5(self):
        self.assertEqual([ 6, 2 ], change(8, [ 6, 2, 5 ]))

    def test_with_money_as_8_and_coins_as_6_5_2(self):
        self.assertEqual([ 6, 2 ], change(8, [ 6, 5, 2 ]))

    def test_with_money_as_9_and_coins_as_2_5_6(self):
        self.assertEqual([ 2, 2, 5 ], change(9, [ 2, 5, 6 ]))

    def test_with_money_as_9_and_coins_as_2_6_5(self):
        self.assertEqual([ 2, 2, 5 ], change(9, [ 2, 6, 5 ]))

    def test_with_money_as_9_and_coins_as_5_2_6(self):
        self.assertEqual([ 5, 2, 2 ], change(9, [ 5, 2, 6 ]))

    def test_with_money_as_9_and_coins_as_5_6_2(self):
        self.assertEqual([ 5, 2, 2 ], change(9, [ 5, 6, 2 ]))

    def test_with_money_as_9_and_coins_as_6_2_5(self):
        self.assertEqual([ 2, 2, 5 ], change(9, [ 6, 2, 5 ]))

    def test_with_money_as_9_and_coins_as_6_5_2(self):
        self.assertEqual([ 5, 2, 2 ], change(9, [ 6, 5, 2 ]))

if __name__ == '__main__':
    unittest.main()
