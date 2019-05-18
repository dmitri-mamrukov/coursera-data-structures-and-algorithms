#!/usr/bin/python3

import unittest

from sorting import solve

class SolveTestCase(unittest.TestCase):

    def test_with_empty_data(self):
        data = []
        solve(data)
        self.assertEqual([], data)

    def test_with_one_element(self):
        data = [ 3 ]
        solve(data)
        self.assertEqual([ 3 ], data)

    def test_with_two_elements(self):
        data = [ 1, 2 ]
        solve(data)
        self.assertEqual([ 1, 2 ], data)

        data = [ 2, 1 ]
        solve(data)
        self.assertEqual([ 1, 2 ], data)

        data = [ 3, 3 ]
        solve(data)
        self.assertEqual([ 3, 3 ], data)

    def test_with_three_elements(self):
        data = [ 1, 2, 3 ]
        solve(data)
        self.assertEqual([ 1, 2, 3 ], data)

        data = [ 2, 1, 3 ]
        solve(data)
        self.assertEqual([ 1, 2, 3 ], data)

        data = [ 3, 3, 3 ]
        solve(data)
        self.assertEqual([ 3, 3, 3 ], data)

    def test_with_several_elements(self):
        data = [ 5, -7, 3, 0, 9, -1, 9 ]
        solve(data)
        self.assertEqual([ -7, -1, 0, 3, 5, 9, 9 ], data)

        data = [ 7, 2, 5, 3, 7, 13, 1, 6 ]
        solve(data)
        self.assertEqual([ 1, 2, 3, 5, 6, 7, 7, 13 ], data)

        data = [ 54, 26, 93, 17, 77, 31, 44, 55, 20 ]
        solve(data)
        self.assertEqual([ 17, 20, 26, 31, 44, 54, 55, 77, 93 ], data)

if __name__ == '__main__':
    unittest.main()
