#!/usr/bin/python3

import unittest

from majority_element import solve

class GetMajorityElementTestCase(unittest.TestCase):

    def test_with_empty_data(self):
        self.assertEqual(None, solve([]))

    def test_with_one_element(self):
        self.assertEqual(3, solve([ 3 ]))

    def test_with_two_elements(self):
        self.assertEqual(3, solve([ 3, 3 ]))
        self.assertEqual(None, solve([ 2, 3 ]))

    def test_with_three_elements(self):
        self.assertEqual(3, solve([ 3, 3, 3 ]))
        self.assertEqual(3, solve([ 3, 3, 2 ]))

    def test_with_four_elements(self):
        self.assertEqual(3, solve([ 3, 3, 3, 3 ]))
        self.assertEqual(3, solve([ 3, 3, 3, 2 ]))
        self.assertEqual(None, solve([ 3, 3, 1, 2 ]))
        self.assertEqual(None, solve([ 1, 2, 3, 4 ]))

        self.assertEqual(None, solve([ 1, 2, 3, 4 ]))
        self.assertEqual(None, solve([ 1, 2, 3, 1 ]))

    def test_with_five_elements(self):
        self.assertEqual(3, solve([ 3, 3, 3, 3, 3 ]))
        self.assertEqual(3, solve([ 3, 3, 3, 3, 2 ]))
        self.assertEqual(3, solve([ 3, 3, 3, 1, 2 ]))
        self.assertEqual(None, solve([ 3, 3, 1, 2, 4 ]))
        self.assertEqual(None, solve([ 3, 1, 2, 4, 5 ]))

        self.assertEqual(2, solve([ 2, 3, 9, 2, 2 ]))

    def test_with_several_elements(self):
        self.assertEqual(2, solve([ 2, 124554847, 2, 941795895,
            2, 2, 2, 2, 792755190, 756617003 ]))

if __name__ == '__main__':
    unittest.main()
