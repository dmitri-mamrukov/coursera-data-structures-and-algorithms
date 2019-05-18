#!/usr/bin/python3

import math
from random import randint

import unittest

from points_and_segments import naive_count_segments, fast_count_segments

class StressTestCase(unittest.TestCase):

    MAX_SEGMENTS = 5 * int(math.pow(10, 3))
    MAX_POINTS = 5 * int(math.pow(10, 3))
    MAX_A = int(math.pow(10, 1))
    MAX_B = int(math.pow(10, 1))

    def test(self):
        while True:
            equal_segments = randint(0, 1)
            s, p = randint(0, StressTestCase.MAX_SEGMENTS), \
                randint(0, StressTestCase.MAX_POINTS)

            starts = []
            ends = []
            points = []

            if equal_segments == 0:
                a = randint(-1 * StressTestCase.MAX_A, StressTestCase.MAX_A)
                b = randint(a, StressTestCase.MAX_B)
                for i in range(0, s):
                    starts.append(a)
                    ends.append(b)
            else:
                for i in range(0, s):
                    a = randint(-1 * StressTestCase.MAX_A, StressTestCase.MAX_A)
                    b = randint(a, StressTestCase.MAX_B)
                    starts.append(a)
                    ends.append(b)

            for i in range(0, p):
                p = randint(-1 * StressTestCase.MAX_A, StressTestCase.MAX_B)
                points.append(p)

            naive_count_answer = naive_count_segments(starts, ends, points);
            fast_count_answer = fast_count_segments(starts, ends, points);
            print('starts: %s: ' % starts)
            print('ends: %s' % ends)
            print('points: %s' % points)
            print('counts: %s' % fast_count_answer)
            print()
            self.assertEqual(naive_count_answer, fast_count_answer)

if __name__ == '__main__':
    class_names = \
    [
        StressTestCase
    ]

    suite = unittest.TestSuite()

    for c in class_names:
        suite.addTest(unittest.defaultTestLoader.loadTestsFromTestCase(c))

    unittest.TextTestRunner().run(suite)
