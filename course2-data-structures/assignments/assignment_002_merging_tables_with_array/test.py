#!/usr/bin/python3

import sys
import threading
import unittest

from merging_tables import Solver

class SolverTestCase(unittest.TestCase):

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

    def test_constructor_with_negative_n(self):
        with self.assertRaisesRegex(ValueError, 'n must be > 0.'):
            Solver(-1, [])

    def test_constructor_with_n_as_one_and_empty_list(self):
        with self.assertRaisesRegex(ValueError,
            'n must equal to the length of the list of tables.'):
            Solver(1, [])

    def test_constructor_with_n_as_zero_and_one_element_list(self):
        with self.assertRaisesRegex(ValueError,
            'n must equal to the length of the list of tables.'):
            Solver(1, [ 1, 2 ])

    def test_constructor_with_n_as_one_and_one_element_list(self):
        n = 1
        solver = Solver(n, [ 2 ])

        self.assertEqual(n, len(solver._parent))
        self.assertEqual([ 0 ], solver._parent)
        self.assertEqual(n, len(solver._rank))
        self.assertEqual([ 2 ], solver._rank)
        self.assertEqual(2, solver.max_table_size)

    def test_constructor_with_n_as_two_and_two_element_list(self):
        n = 2
        solver = Solver(n, [ 1, 3 ])

        self.assertEqual(n, len(solver._parent))
        self.assertEqual([ 0, 1 ], solver._parent)
        self.assertEqual(n, len(solver._rank))
        self.assertEqual([ 1, 3 ], solver._rank)
        self.assertEqual(3, solver.max_table_size)

    def test_constructor_with_n_as_three_and_three_element_list(self):
        n = 3
        solver = Solver(n, [ 1, 3, 5 ])

        self.assertEqual(n, len(solver._parent))
        self.assertEqual([ 0, 1, 2 ], solver._parent)
        self.assertEqual(n, len(solver._rank))
        self.assertEqual([ 1, 3, 5 ], solver._rank)
        self.assertEqual(5, solver.max_table_size)

    def test_merge_with_5_tables_and_5_operations(self):
        n = 5
        solver = Solver(n, [ 1, 1, 1, 1, 1 ])

        self.assertEqual(n, len(solver._parent))
        self.assertEqual([ 0, 1, 2, 3, 4 ], solver._parent)
        self.assertEqual(n, len(solver._rank))
        self.assertEqual([ 1, 1, 1, 1, 1 ], solver._rank)
        self.assertEqual(1, solver.max_table_size)

        old_rank = [ x for x in solver._rank ]
        old_parent = [ x for x in solver._parent ]
        destination, source = 2, 4
        solver.merge(destination, source)

        self.assertEqual(n, len(solver._parent))
        self.assertEqual([ 0, 1, 2, 3, 2 ], solver._parent)
        self.assertEqual(n, len(solver._rank))
        self.assertEqual([ 1, 1, 2, 1, 0 ], solver._rank)
        self.assertEqual(2, solver.max_table_size)
        self.assert_result(old_rank, old_parent, solver, destination, source)

        old_rank = [ x for x in solver._rank ]
        old_parent = [ x for x in solver._parent ]
        destination, source = 1, 3
        solver.merge(destination, source)

        self.assertEqual(n, len(solver._parent))
        self.assertEqual([ 0, 1, 2, 1, 2 ], solver._parent)
        self.assertEqual(n, len(solver._rank))
        self.assertEqual([ 1, 2, 2, 0, 0 ], solver._rank)
        self.assertEqual(2, solver.max_table_size)
        self.assert_result(old_rank, old_parent, solver, destination, source)

        old_rank = [ x for x in solver._rank ]
        old_parent = [ x for x in solver._parent ]
        destination, source = 0, 3
        solver.merge(destination, source)

        self.assertEqual(n, len(solver._parent))
        self.assertEqual([ 0, 0, 2, 1, 2 ], solver._parent)
        self.assertEqual(n, len(solver._rank))
        self.assertEqual([ 3, 0, 2, 0, 0 ], solver._rank)
        self.assertEqual(3, solver.max_table_size)
        self.assert_result(old_rank, old_parent, solver, destination, source)

        old_rank = [ x for x in solver._rank ]
        old_parent = [ x for x in solver._parent ]
        destination, source = 4, 3
        solver.merge(destination, source)

        self.assertEqual(n, len(solver._parent))
        self.assertEqual([ 2, 0, 2, 0, 2 ], solver._parent)
        self.assertEqual(n, len(solver._rank))
        self.assertEqual([ 0, 0, 5, 0, 0 ], solver._rank)
        self.assertEqual(5, solver.max_table_size)
        self.assert_result(old_rank, old_parent, solver, destination, source)

        old_rank = [ x for x in solver._rank ]
        old_parent = [ x for x in solver._parent ]
        destination, source = 4, 2
        solver.merge(destination, source)

        self.assertEqual(n, len(solver._parent))
        self.assertEqual([ 2, 0, 2, 0, 2 ], solver._parent)
        self.assertEqual(n, len(solver._rank))
        self.assertEqual([ 0, 0, 5, 0, 0 ], solver._rank)
        self.assertEqual(5, solver.max_table_size)
        self.assert_result(old_rank, old_parent, solver, destination, source)

    def test_merge_with_6_tables_and_4_operations(self):
        n = 6
        solver = Solver(n, [ 10, 0, 5, 0, 3, 3 ])

        self.assertEqual(n, len(solver._parent))
        self.assertEqual([ 0, 1, 2, 3, 4, 5 ], solver._parent)
        self.assertEqual(n, len(solver._rank))
        self.assertEqual([ 10, 0, 5, 0, 3, 3 ], solver._rank)
        self.assertEqual(10, solver.max_table_size)

        old_rank = [ x for x in solver._rank ]
        old_parent = [ x for x in solver._parent ]
        destination, source = 5, 5
        solver.merge(destination, source)

        self.assertEqual(n, len(solver._parent))
        self.assertEqual([ 0, 1, 2, 3, 4, 5 ], solver._parent)
        self.assertEqual(n, len(solver._rank))
        self.assertEqual([ 10, 0, 5, 0, 3, 3 ], solver._rank)
        self.assertEqual(10, solver.max_table_size)
        self.assert_result(old_rank, old_parent, solver, destination, source)

        old_rank = [ x for x in solver._rank ]
        old_parent = [ x for x in solver._parent ]
        destination, source = 5, 4
        solver.merge(destination, source)

        self.assertEqual(n, len(solver._parent))
        self.assertEqual([ 0, 1, 2, 3, 5, 5 ], solver._parent)
        self.assertEqual(n, len(solver._rank))
        self.assertEqual([ 10, 0, 5, 0, 0, 6 ], solver._rank)
        self.assertEqual(10, solver.max_table_size)
        self.assert_result(old_rank, old_parent, solver, destination, source)

        old_rank = [ x for x in solver._rank ]
        old_parent = [ x for x in solver._parent ]
        destination, source = 4, 3
        solver.merge(destination, source)

        self.assertEqual(n, len(solver._parent))
        self.assertEqual([ 0, 1, 2, 5, 5, 5 ], solver._parent)
        self.assertEqual(n, len(solver._rank))
        self.assertEqual([ 10, 0, 5, 0, 0, 6 ], solver._rank)
        self.assertEqual(10, solver.max_table_size)
        self.assert_result(old_rank, old_parent, solver, destination, source)

        old_rank = [ x for x in solver._rank ]
        old_parent = [ x for x in solver._parent ]
        destination, source = 3, 2
        solver.merge(destination, source)

        self.assertEqual(n, len(solver._parent))
        self.assertEqual([ 0, 1, 5, 5, 5, 5 ], solver._parent)
        self.assertEqual(n, len(solver._rank))
        self.assertEqual([ 10, 0, 0, 0, 0, 11 ], solver._rank)
        self.assertEqual(11, solver.max_table_size)
        self.assert_result(old_rank, old_parent, solver, destination, source)

    def test_merge_with_6_tables_and_6_operations(self):
        n = 6
        solver = Solver(n, [ 10, 0, 5, 0, 3, 3 ])

        self.assertEqual(n, len(solver._parent))
        self.assertEqual([ 0, 1, 2, 3, 4, 5 ], solver._parent)
        self.assertEqual(n, len(solver._rank))
        self.assertEqual([ 10, 0, 5, 0, 3, 3 ], solver._rank)
        self.assertEqual(10, solver.max_table_size)

        old_rank = [ x for x in solver._rank ]
        old_parent = [ x for x in solver._parent ]
        destination, source = 5, 5
        solver.merge(destination, source)

        self.assertEqual(n, len(solver._parent))
        self.assertEqual([ 0, 1, 2, 3, 4, 5 ], solver._parent)
        self.assertEqual(n, len(solver._rank))
        self.assertEqual([ 10, 0, 5, 0, 3, 3 ], solver._rank)
        self.assertEqual(10, solver.max_table_size)
        self.assert_result(old_rank, old_parent, solver, destination, source)

        old_rank = [ x for x in solver._rank ]
        old_parent = [ x for x in solver._parent ]
        destination, source = 5, 4
        solver.merge(destination, source)

        self.assertEqual(n, len(solver._parent))
        self.assertEqual([ 0, 1, 2, 3, 5, 5 ], solver._parent)
        self.assertEqual(n, len(solver._rank))
        self.assertEqual([ 10, 0, 5, 0, 0, 6 ], solver._rank)
        self.assertEqual(10, solver.max_table_size)
        self.assert_result(old_rank, old_parent, solver, destination, source)

        old_rank = [ x for x in solver._rank ]
        old_parent = [ x for x in solver._parent ]
        destination, source = 4, 3
        solver.merge(destination, source)

        self.assertEqual(n, len(solver._parent))
        self.assertEqual([ 0, 1, 2, 5, 5, 5 ], solver._parent)
        self.assertEqual(n, len(solver._rank))
        self.assertEqual([ 10, 0, 5, 0, 0, 6 ], solver._rank)
        self.assertEqual(10, solver.max_table_size)
        self.assert_result(old_rank, old_parent, solver, destination, source)

        old_rank = [ x for x in solver._rank ]
        old_parent = [ x for x in solver._parent ]
        destination, source = 3, 2
        solver.merge(destination, source)

        self.assertEqual(n, len(solver._parent))
        self.assertEqual([ 0, 1, 5, 5, 5, 5 ], solver._parent)
        self.assertEqual(n, len(solver._rank))
        self.assertEqual([ 10, 0, 0, 0, 0, 11 ], solver._rank)
        self.assertEqual(11, solver.max_table_size)
        self.assert_result(old_rank, old_parent, solver, destination, source)

        old_rank = [ x for x in solver._rank ]
        old_parent = [ x for x in solver._parent ]
        destination, source = 2, 1
        solver.merge(destination, source)

        self.assertEqual(n, len(solver._parent))
        self.assertEqual([ 0, 5, 5, 5, 5, 5 ], solver._parent)
        self.assertEqual(n, len(solver._rank))
        self.assertEqual([ 10, 0, 0, 0, 0, 11 ], solver._rank)
        self.assertEqual(11, solver.max_table_size)
        self.assert_result(old_rank, old_parent, solver, destination, source)

        old_rank = [ x for x in solver._rank ]
        old_parent = [ x for x in solver._parent ]
        destination, source = 1, 0
        solver.merge(destination, source)

        self.assertEqual(n, len(solver._parent))
        self.assertEqual([ 5, 5, 5, 5, 5, 5 ], solver._parent)
        self.assertEqual(n, len(solver._rank))
        self.assertEqual([ 0, 0, 0, 0, 0, 21 ], solver._rank)
        self.assertEqual(21, solver.max_table_size)
        self.assert_result(old_rank, old_parent, solver, destination, source)

    def test_merge_with_2_empty_tables_and_merge_first_and_second(self):
        n = 2
        solver = Solver(n, [ 0, 0 ])

        self.assertEqual(n, len(solver._parent))
        self.assertEqual([ 0, 1 ], solver._parent)
        self.assertEqual(n, len(solver._rank))
        self.assertEqual([ 0, 0 ], solver._rank)
        self.assertEqual(0, solver.max_table_size)

        old_rank = [ x for x in solver._rank ]
        old_parent = [ x for x in solver._parent ]
        destination, source = 0, 1
        solver.merge(destination, source)

        self.assertEqual(n, len(solver._parent))
        self.assertEqual([ 0, 0 ], solver._parent)
        self.assertEqual(n, len(solver._rank))
        self.assertEqual([ 0, 0 ], solver._rank)
        self.assertEqual(0, solver.max_table_size)
        self.assert_result(old_rank, old_parent, solver, destination, source)

    def test_merge_with_2_empty_tables_and_merge_second_and_first(self):
        n = 2
        solver = Solver(n, [ 0, 0 ])

        self.assertEqual(n, len(solver._parent))
        self.assertEqual([ 0, 1 ], solver._parent)
        self.assertEqual(n, len(solver._rank))
        self.assertEqual([ 0, 0 ], solver._rank)
        self.assertEqual(0, solver.max_table_size)

        old_rank = [ x for x in solver._rank ]
        old_parent = [ x for x in solver._parent ]
        destination, source = 1, 0
        solver.merge(destination, source)

        self.assertEqual(n, len(solver._parent))
        self.assertEqual([ 1, 1 ], solver._parent)
        self.assertEqual(n, len(solver._rank))
        self.assertEqual([ 0, 0 ], solver._rank)
        self.assertEqual(0, solver.max_table_size)
        self.assert_result(old_rank, old_parent, solver, destination, source)

    def test_merge_with_2_tables_and_merge_first_and_second(self):
        n = 2
        solver = Solver(n, [ 1, 2 ])

        self.assertEqual(n, len(solver._parent))
        self.assertEqual([ 0, 1 ], solver._parent)
        self.assertEqual(n, len(solver._rank))
        self.assertEqual([ 1, 2 ], solver._rank)
        self.assertEqual(2, solver.max_table_size)

        old_rank = [ x for x in solver._rank ]
        old_parent = [ x for x in solver._parent ]
        destination, source = 0, 1
        solver.merge(destination, source)

        self.assertEqual(n, len(solver._parent))
        self.assertEqual([ 0, 0 ], solver._parent)
        self.assertEqual(n, len(solver._rank))
        self.assertEqual([ 3, 0 ], solver._rank)
        self.assertEqual(3, solver.max_table_size)
        self.assert_result(old_rank, old_parent, solver, destination, source)

    def test_merge_with_2_tables_and_merge_second_and_first(self):
        n = 2
        solver = Solver(n, [ 1, 2 ])

        self.assertEqual(n, len(solver._parent))
        self.assertEqual([ 0, 1 ], solver._parent)
        self.assertEqual(n, len(solver._rank))
        self.assertEqual([ 1, 2 ], solver._rank)
        self.assertEqual(2, solver.max_table_size)

        old_rank = [ x for x in solver._rank ]
        old_parent = [ x for x in solver._parent ]
        destination, source = 1, 0
        solver.merge(destination, source)

        self.assertEqual(n, len(solver._parent))
        self.assertEqual([ 1, 1 ], solver._parent)
        self.assertEqual(n, len(solver._rank))
        self.assertEqual([ 0, 3 ], solver._rank)
        self.assertEqual(3, solver.max_table_size)
        self.assert_result(old_rank, old_parent, solver, destination, source)

    def test_merge_with_3_tables_and_merge_from_right(self):
        n = 3
        solver = Solver(n, [ 1, 2, 3 ])

        self.assertEqual(n, len(solver._parent))
        self.assertEqual([ 0, 1, 2 ], solver._parent)
        self.assertEqual(n, len(solver._rank))
        self.assertEqual([ 1, 2, 3 ], solver._rank)
        self.assertEqual(3, solver.max_table_size)

        old_rank = [ x for x in solver._rank ]
        old_parent = [ x for x in solver._parent ]
        destination, source = 0, 1
        solver.merge(destination, source)

        self.assertEqual(n, len(solver._parent))
        self.assertEqual([ 0, 0, 2 ], solver._parent)
        self.assertEqual(n, len(solver._rank))
        self.assertEqual([ 3, 0, 3 ], solver._rank)
        self.assertEqual(3, solver.max_table_size)
        self.assert_result(old_rank, old_parent, solver, destination, source)

        old_rank = [ x for x in solver._rank ]
        old_parent = [ x for x in solver._parent ]
        destination, source = 1, 2
        solver.merge(destination, source)

        self.assertEqual(n, len(solver._parent))
        self.assertEqual([ 0, 0, 0 ], solver._parent)
        self.assertEqual(n, len(solver._rank))
        self.assertEqual([ 6, 0, 0 ], solver._rank)
        self.assertEqual(6, solver.max_table_size)
        self.assert_result(old_rank, old_parent, solver, destination, source)

    def test_merge_with_3_tables_and_merge_from_left(self):
        n = 3
        solver = Solver(n, [ 1, 2, 3 ])

        self.assertEqual(n, len(solver._parent))
        self.assertEqual([ 0, 1, 2 ], solver._parent)
        self.assertEqual(n, len(solver._rank))
        self.assertEqual([ 1, 2, 3 ], solver._rank)
        self.assertEqual(3, solver.max_table_size)

        old_rank = [ x for x in solver._rank ]
        old_parent = [ x for x in solver._parent ]
        destination, source = 1, 0
        solver.merge(destination, source)

        self.assertEqual(n, len(solver._parent))
        self.assertEqual([ 1, 1, 2 ], solver._parent)
        self.assertEqual(n, len(solver._rank))
        self.assertEqual([ 0, 3, 3 ], solver._rank)
        self.assertEqual(3, solver.max_table_size)
        self.assert_result(old_rank, old_parent, solver, destination, source)

        old_rank = [ x for x in solver._rank ]
        old_parent = [ x for x in solver._parent ]
        destination, source = 2, 0
        solver.merge(destination, source)

        self.assertEqual(n, len(solver._parent))
        self.assertEqual([ 1, 2, 2 ], solver._parent)
        self.assertEqual(n, len(solver._rank))
        self.assertEqual([ 0, 0, 6 ], solver._rank)
        self.assertEqual(6, solver.max_table_size)
        self.assert_result(old_rank, old_parent, solver, destination, source)

    def test_merge_with_4_tables(self):
        n = 4
        solver = Solver(n, [ 1, 2, 3, 4 ])

        self.assertEqual(n, len(solver._parent))
        self.assertEqual([ 0, 1, 2, 3 ], solver._parent)
        self.assertEqual(n, len(solver._rank))
        self.assertEqual([ 1, 2, 3, 4 ], solver._rank)
        self.assertEqual(4, solver.max_table_size)

        old_rank = [ x for x in solver._rank ]
        old_parent = [ x for x in solver._parent ]
        destination, source = 2, 3
        solver.merge(destination, source)

        self.assertEqual(n, len(solver._parent))
        self.assertEqual([ 0, 1, 2, 2 ], solver._parent)
        self.assertEqual(n, len(solver._rank))
        self.assertEqual([ 1, 2, 7, 0 ], solver._rank)
        self.assertEqual(7, solver.max_table_size)
        self.assert_result(old_rank, old_parent, solver, destination, source)

        old_rank = [ x for x in solver._rank ]
        old_parent = [ x for x in solver._parent ]
        destination, source = 1, 2
        solver.merge(destination, source)

        self.assertEqual(n, len(solver._parent))
        self.assertEqual([ 0, 1, 1, 2 ], solver._parent)
        self.assertEqual(n, len(solver._rank))
        self.assertEqual([ 1, 9, 0, 0 ], solver._rank)
        self.assertEqual(9, solver.max_table_size)
        self.assert_result(old_rank, old_parent, solver, destination, source)

        old_rank = [ x for x in solver._rank ]
        old_parent = [ x for x in solver._parent ]
        destination, source = 0, 3
        solver.merge(destination, source)

        self.assertEqual(n, len(solver._parent))
        self.assertEqual([ 0, 0, 1, 1 ], solver._parent)
        self.assertEqual([ 10, 0, 0, 0 ], solver._rank)
        self.assertEqual(10, solver.max_table_size)
        self.assert_result(old_rank, old_parent, solver, destination, source)

    def test_merge_with_huge_tables(self):
        """
        This test reproduces a stack overflow due to the recursive nature of
        Solver.get_parent().
        """
        n = 100000
        solver = Solver(n, [ i for i in range(n) ])

        m = n
        for i in range(m):
            solver.merge(m - 2 - i, m - 1 - i)

        sum = (n - 1) * n // 2
        self.assertEqual(sum, solver.max_table_size)

    def test_merge_with_huge_tables(self):
        """
        This test reproduces a stack overflow due to the recursive nature of
        Solver.get_parent().
        """
        n = 100000
        solver = Solver(n, [ i for i in range(n) ])

        m = n
        for i in range(m):
            solver.merge(m - 2 - i, m - 1 - i)

        sum = (n - 1) * n // 2
        self.assertEqual(sum, solver.max_table_size)

def main():
    unittest.main()

if __name__ == '__main__':
    """Instructor Michael Levin: Not only those three lines are critical for
    everything to work correctly, but also creating and starting a Thread
    object and calling your solution function inside it, because you set the
    stack size for threading, not for the whole program.
    """
    sys.setrecursionlimit(10**7) # max depth of recursion
    threading.stack_size(2**25)  # a new thread will get a stack of such a size
    threading.Thread(target = main).start()
