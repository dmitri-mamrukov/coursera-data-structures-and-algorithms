#!/usr/bin/python3

import math
from random import randint

import unittest

from longest_common_sequence import longest_common_sequence

class LongestCommonSequenceTestCase(unittest.TestCase):

    LENGTH = int(math.pow(10, 2))
    LOW = int(math.pow(10, 1))
    HIGH = int(math.pow(10, 1))

    def assert_solution(self, a, b, c, value, indices):
        self.assertEqual(value, len(indices))

        for group in reversed(indices):
            i, j, k = group
            self.assertTrue(a[i] == b[j] == c[k])

    def test(self):
        while True:
            a, b, c = [], [], []
            for _ in range(LongestCommonSequenceTestCase.LENGTH):
                ai = randint(-1 * LongestCommonSequenceTestCase.LOW,
                    LongestCommonSequenceTestCase.HIGH)
                bi = randint(-1 * LongestCommonSequenceTestCase.LOW,
                    LongestCommonSequenceTestCase.HIGH)
                ci = randint(-1 * LongestCommonSequenceTestCase.LOW,
                    LongestCommonSequenceTestCase.HIGH)
                a.append(ai)
                b.append(bi)
                c.append(ci)

            value, indices = longest_common_sequence(a, b, c)

            print('a: %s' % a)
            print('b: %s' % b)
            print('c: %s' % c)
            print('value: %s' % value)
            print('indices: %s' % indices)
            print()
            self.assert_solution(a, b, c, value, indices)

if __name__ == '__main__':
    class_names = \
    [
        LongestCommonSequenceTestCase
    ]

    suite = unittest.TestSuite()

    for c in class_names:
        suite.addTest(unittest.defaultTestLoader.loadTestsFromTestCase(c))

    unittest.TextTestRunner().run(suite)
