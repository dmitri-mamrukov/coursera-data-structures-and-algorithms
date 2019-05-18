#!/usr/bin/python3

import unittest

from merge_sort import solve

class SolveTestCase(unittest.TestCase):

    def test_with_empty_data(self):
        self.assertEqual([], solve([]))

    def test_with_one_element(self):
        self.assertEqual([ 3 ], solve([ 3 ]))

    def test_with_two_elements(self):
        self.assertEqual([ 1, 2 ], solve([ 1, 2 ]))
        self.assertEqual([ 1, 2 ], solve([ 2, 1 ]))
        self.assertEqual([ 3, 3 ], solve([ 3, 3 ]))

    def test_with_three_elements(self):
        self.assertEqual([ 1, 2, 3 ], solve([ 1, 2, 3 ]))
        self.assertEqual([ 1, 2, 3 ], solve([ 2, 1, 3 ]))
        self.assertEqual([ 3, 3, 3 ], solve([ 3, 3, 3 ]))

    def test_with_several_elements(self):
        self.assertEqual([ -7, -1, 0, 3, 5, 9, 9 ],
            solve([ 5, -7, 3, 0, 9, -1, 9 ]))
        self.assertEqual([ 1, 2, 3, 5, 6, 7, 7, 13 ],
            solve([ 7, 2, 5, 3, 7, 13, 1, 6 ]))
        self.assertEqual([ 17, 20, 26, 31, 44, 54, 55, 77, 93 ],
            solve([ 54, 26, 93, 17, 77, 31, 44, 55, 20 ]))

if __name__ == '__main__':
    unittest.main()
