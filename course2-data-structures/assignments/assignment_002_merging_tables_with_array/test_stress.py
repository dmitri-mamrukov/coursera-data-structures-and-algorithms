#!/usr/bin/python3

import math
from random import randint

import unittest

from merging_tables import Solver

class StressTestCase(unittest.TestCase):

    N = 100000
    M = 100000
    ROWS = 10000

    def get_parent(self, old_parent, table):

        while table != old_parent[table]:
            table = old_parent[table]

        return table

    def assert_result(self, old_rank, old_parent, solver,
        destination, source):
        real_destination = self.get_parent(old_parent, destination)
        real_source = self.get_parent(old_parent, source)

        if real_destination == real_source:
            self.assertEqual(old_rank, solver._rank)
        else:
            self.assertEqual(
                old_rank[real_destination] + old_rank[real_source],
                solver._rank[real_destination])
            self.assertEqual(0, solver._rank[real_source])

            self.assertNotEqual(old_parent[real_source],
                solver._parent[real_source])
            self.assertEqual(real_destination,
                solver._parent[real_source])

        self.assertEqual(solver.max_table_size, max(solver._rank))

    def test(self):
        while True:
            print('n: %s' % StressTestCase.N)
            print('m: %s' % StressTestCase.M)

            table_sizes = \
            [ randint(0, StressTestCase.ROWS)
                for i in range(StressTestCase.N) ]
            solver = Solver(StressTestCase.N, table_sizes)

            for i in range(0, StressTestCase.M):
                destination = randint(0, StressTestCase.N - 1)
                source = randint(0, StressTestCase.N - 1)

                old_rank = [ x for x in solver._rank ]
                old_parent = [ x for x in solver._parent ]
                solver.merge(destination, source)

                try:
                    self.assert_result(old_rank, old_parent, solver,
                        destination, source)
                    print('.')
                except Exception as e:
                    f = open('stress-test-failure.txt', 'w')
                    f.write('old_parent: %s' % old_parent)
                    f.write('old_rank: %s' % old_rank)
                    f.write('destination: %s' % destination)
                    f.write('source: %s' % source)
                    f.write('parent: %s' % solver._parent)
                    f.write('rank: %s' % solver._rank)
                    f.close()
                    raise e

if __name__ == '__main__':
    class_names = \
    [
        StressTestCase
    ]

    suite = unittest.TestSuite()

    for c in class_names:
        suite.addTest(unittest.defaultTestLoader.loadTestsFromTestCase(c))

    unittest.TextTestRunner().run(suite)
