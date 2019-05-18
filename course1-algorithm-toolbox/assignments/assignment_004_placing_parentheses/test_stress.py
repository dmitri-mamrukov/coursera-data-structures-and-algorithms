#!/usr/bin/python3

import math
from random import randint

import unittest

from placing_parentheses import get_min_max

class StressTestCase(unittest.TestCase):

    DIGITS = '0123456789'
    OPERATORS = '+-*'
    N = 14

    def test(self):
        while True:
            text = ''
            for i in range(0, StressTestCase.N):
                digit = StressTestCase.DIGITS[randint(0, \
                    len(StressTestCase.DIGITS) - 1)]
                op = StressTestCase.OPERATORS[randint(0, \
                    len(StressTestCase.OPERATORS) - 1)]
                text = text + digit + op
            digit = StressTestCase.DIGITS[randint(0, \
                    len(StressTestCase.DIGITS) - 1)]
            text = text + digit

            min_val, max_val, min_solution, max_solution = get_min_max(text)
            print('text: %s: ' % text)
            print('min_val: %s' % min_val)
            print('max_val: %s' % max_val)
            print('min_solution: %s' % min_solution)
            print('max_solution: %s' % max_solution)
            print()
            self.assertEqual(min_val, eval(min_solution))
            self.assertEqual(max_val, eval(max_solution))

if __name__ == '__main__':
    class_names = \
    [
        StressTestCase
    ]

    suite = unittest.TestSuite()

    for c in class_names:
        suite.addTest(unittest.defaultTestLoader.loadTestsFromTestCase(c))

    unittest.TextTestRunner().run(suite)
