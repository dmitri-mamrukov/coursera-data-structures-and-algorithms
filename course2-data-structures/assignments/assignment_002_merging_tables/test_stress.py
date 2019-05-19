#!/usr/bin/python3

import math
from random import randint

import unittest

from merging_tables import Solver

class StressTestCase(unittest.TestCase):

    N = 100000
    M = 100000
    ROWS = 10000

    def copy_nodes_as_tuples(self, solver, destination, source):
        # so that paths are appropriately compressed before we copy nodes
        solver.get_parent(solver._nodes[destination])
        solver.get_parent(solver._nodes[source])

        return [ (n._label, n._size, n._parent._label)
            for n in solver._nodes ]

    def get_parent(self, old_nodes, x):

        while x != old_nodes[x][2]:
            x = old_nodes[x][2]

        return x

    def assert_nodes(self, expected_nodes, nodes):
        for i, n in enumerate(nodes):
            label = expected_nodes[i][0]
            size = expected_nodes[i][1]
            parent = expected_nodes[i][2]
            self.assertEqual(label, n._label)
            self.assertEqual(size, n._size)
            self.assertEqual(parent, n._parent._label)

    def assert_result(self, old_nodes, solver, destination, source):
        real_destination = self.get_parent(old_nodes, destination)
        real_source = self.get_parent(old_nodes, source)

        if real_destination == real_source:
            self.assert_nodes(old_nodes, solver._nodes)
        else:
            self.assertEqual(
                old_nodes[real_destination][1] +
                old_nodes[real_source][1],
                solver._nodes[real_destination]._size)
            self.assertEqual(0, solver._nodes[real_source]._size)

            self.assertNotEqual(old_nodes[real_source][2],
                solver._nodes[real_source]._parent._label)
            self.assertEqual(real_destination,
                solver._nodes[real_source]._parent._label)

        self.assertEqual(solver.max_table_size,
            max(solver._nodes, key=lambda n: n._size)._size)

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

                old_nodes = self.copy_nodes_as_tuples(solver,
                    destination, source)
                solver.merge(destination, source)

                try:
                    self.assert_result(old_nodes, solver, destination, source)
                    print('.')
                except Exception as e:
                    f = open('stress-test-failure.txt', 'w')
                    f.write('max_table_size: %s\n' % solver.max_table_size)
                    f.write('source: %s\n' % source)
                    f.write('destination: %s\n' % destination)
                    f.write('old_nodes: %s\n' % old_nodes)
                    f.write('nodes: %s\n' % solver._nodes)
                    f.close()
                    raise e

def main():
    unittest.main()

if __name__ == '__main__':
    unittest.main()
