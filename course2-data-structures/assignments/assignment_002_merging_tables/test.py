#!/usr/bin/python3

import sys
import threading
import unittest

from merging_tables import Node, Solver

class NodeTestCase(unittest.TestCase):

    def test_constructor_with_no_parent(self):
        label = 'abc'
        size = 123

        node = Node(label, size)

        self.assertEqual(label, node._label)
        self.assertEqual(size, node._size)
        self.assertEqual(node, node._parent)

    def test_constructor_with_parent(self):
        label1 = 'abc'
        size1 = 123
        label2 = 'xyz'
        size2 = 456

        node1 = Node(label1, size1)
        node2 = Node(label2, size2, node1)

        self.assertEqual(label1, node1._label)
        self.assertEqual(size1, node1._size)
        self.assertEqual(node1, node1._parent)

        self.assertEqual(label2, node2._label)
        self.assertEqual(size2, node2._size)
        self.assertEqual(node1, node2._parent)

    def test_str_with_no_parent(self):
        self.assertEqual('abc', str(Node('abc', 123)))

    def test_str_with_parent(self):
        node1 = Node('abc', 123)
        node2 = Node('xyz', 456, node1)
        self.assertEqual('abc', str(node1))
        self.assertEqual('xyz', str(node2))

    def test_repr_with_no_parent(self):
        self.assertEqual('[label=abc, size=123, parent=abc]',
            repr(Node('abc', 123)))

    def test_repr_with_parent(self):
        node1 = Node('abc', 123)
        node2 = Node('xyz', 456, node1)
        self.assertEqual('[label=abc, size=123, parent=abc]',
            repr(node1))
        self.assertEqual('[label=xyz, size=456, parent=abc]',
            repr(node2))

class SolverTestCase(unittest.TestCase):

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

        self.assertEqual(n, len(solver._nodes))
        self.assert_nodes([ (0, 2, 0) ], solver._nodes)
        self.assertEqual(2, solver.max_table_size)

    def test_constructor_with_n_as_two_and_two_element_list(self):
        n = 2
        solver = Solver(n, [ 1, 3 ])

        self.assertEqual(n, len(solver._nodes))
        self.assert_nodes([ (0, 1, 0), (1, 3, 1) ], solver._nodes)
        self.assertEqual(3, solver.max_table_size)

    def test_constructor_with_n_as_three_and_three_element_list(self):
        n = 3
        solver = Solver(n, [ 1, 3, 5 ])

        self.assertEqual(n, len(solver._nodes))
        self.assert_nodes([ (0, 1, 0), (1, 3, 1), (2, 5, 2) ],
            solver._nodes)
        self.assertEqual(5, solver.max_table_size)

    def test_merge_with_5_tables_and_5_operations(self):
        n = 5
        solver = Solver(n, [ 1, 1, 1, 1, 1 ])

        self.assertEqual(n, len(solver._nodes))
        self.assert_nodes([ (0, 1, 0), (1, 1, 1), (2, 1, 2),
            (3, 1, 3), (4, 1, 4) ], solver._nodes)
        self.assertEqual(1, solver.max_table_size)

        destination, source = 2, 4
        old_nodes = self.copy_nodes_as_tuples(solver, destination, source)
        solver.merge(destination, source)

        self.assertEqual(n, len(solver._nodes))
        self.assert_nodes([ (0, 1, 0), (1, 1, 1), (2, 2, 2),
            (3, 1, 3), (4, 0, 2) ], solver._nodes)
        self.assertEqual(2, solver.max_table_size)
        self.assert_result(old_nodes, solver, destination, source)

        destination, source = 1, 3
        old_nodes = self.copy_nodes_as_tuples(solver, destination, source)
        solver.merge(destination, source)

        self.assertEqual(n, len(solver._nodes))
        self.assert_nodes([ (0, 1, 0), (1, 2, 1), (2, 2, 2),
            (3, 0, 1), (4, 0, 2) ], solver._nodes)
        self.assertEqual(2, solver.max_table_size)
        self.assert_result(old_nodes, solver, destination, source)

        destination, source = 0, 3
        old_nodes = self.copy_nodes_as_tuples(solver, destination, source)
        solver.merge(destination, source)

        self.assertEqual(n, len(solver._nodes))
        self.assert_nodes([ (0, 3, 0), (1, 0, 0), (2, 2, 2),
            (3, 0, 1), (4, 0, 2) ], solver._nodes)
        self.assertEqual(3, solver.max_table_size)
        self.assert_result(old_nodes, solver, destination, source)

        destination, source = 4, 3
        old_nodes = self.copy_nodes_as_tuples(solver, destination, source)
        solver.merge(destination, source)

        self.assertEqual(n, len(solver._nodes))
        self.assert_nodes([ (0, 0, 2), (1, 0, 0), (2, 5, 2),
            (3, 0, 0), (4, 0, 2) ], solver._nodes)
        self.assertEqual(5, solver.max_table_size)
        self.assert_result(old_nodes, solver, destination, source)

        destination, source = 4, 2
        old_nodes = self.copy_nodes_as_tuples(solver, destination, source)
        solver.merge(destination, source)

        self.assertEqual(n, len(solver._nodes))
        self.assert_nodes([ (0, 0, 2), (1, 0, 0), (2, 5, 2),
            (3, 0, 0), (4, 0, 2) ], solver._nodes)
        self.assertEqual(5, solver.max_table_size)
        self.assert_result(old_nodes, solver, destination, source)

    def test_merge_with_6_tables_and_4_operations(self):
        n = 6
        solver = Solver(n, [ 10, 0, 5, 0, 3, 3 ])

        self.assertEqual(n, len(solver._nodes))
        self.assert_nodes([ (0, 10, 0), (1, 0, 1), (2, 5, 2),
            (3, 0, 3), (4, 3, 4), (5, 3, 5) ], solver._nodes)
        self.assertEqual(10, solver.max_table_size)

        destination, source = 5, 5
        old_nodes = self.copy_nodes_as_tuples(solver, destination, source)
        solver.merge(destination, source)

        self.assertEqual(n, len(solver._nodes))
        self.assert_nodes([ (0, 10, 0), (1, 0, 1), (2, 5, 2),
            (3, 0, 3), (4, 3, 4), (5, 3, 5) ], solver._nodes)
        self.assertEqual(10, solver.max_table_size)
        self.assert_result(old_nodes, solver, destination, source)

        destination, source = 5, 4
        old_nodes = self.copy_nodes_as_tuples(solver, destination, source)
        solver.merge(destination, source)

        self.assertEqual(n, len(solver._nodes))
        self.assert_nodes([ (0, 10, 0), (1, 0, 1), (2, 5, 2),
            (3, 0, 3), (4, 0, 5), (5, 6, 5) ], solver._nodes)
        self.assertEqual(10, solver.max_table_size)
        self.assert_result(old_nodes, solver, destination, source)

        destination, source = 4, 3
        old_nodes = self.copy_nodes_as_tuples(solver, destination, source)
        solver.merge(destination, source)

        self.assertEqual(n, len(solver._nodes))
        self.assert_nodes([ (0, 10, 0), (1, 0, 1), (2, 5, 2),
            (3, 0, 5), (4, 0, 5), (5, 6, 5) ], solver._nodes)
        self.assertEqual(10, solver.max_table_size)
        self.assert_result(old_nodes, solver, destination, source)

        destination, source = 3, 2
        old_nodes = self.copy_nodes_as_tuples(solver, destination, source)
        solver.merge(destination, source)

        self.assertEqual(n, len(solver._nodes))
        self.assert_nodes([ (0, 10, 0), (1, 0, 1), (2, 0, 5),
            (3, 0, 5), (4, 0, 5), (5, 11, 5) ], solver._nodes)
        self.assertEqual(11, solver.max_table_size)
        self.assert_result(old_nodes, solver, destination, source)

    def test_merge_with_6_tables_and_6_operations(self):
        n = 6
        solver = Solver(n, [ 10, 0, 5, 0, 3, 3 ])

        self.assertEqual(n, len(solver._nodes))
        self.assert_nodes([ (0, 10, 0), (1, 0, 1), (2, 5, 2),
            (3, 0, 3), (4, 3, 4), (5, 3, 5) ], solver._nodes)
        self.assertEqual(10, solver.max_table_size)

        destination, source = 5, 5
        old_nodes = self.copy_nodes_as_tuples(solver, destination, source)
        solver.merge(destination, source)

        self.assertEqual(n, len(solver._nodes))
        self.assert_nodes([ (0, 10, 0), (1, 0, 1), (2, 5, 2),
            (3, 0, 3), (4, 3, 4), (5, 3, 5) ], solver._nodes)
        self.assertEqual(10, solver.max_table_size)
        self.assert_result(old_nodes, solver, destination, source)

        destination, source = 5, 4
        old_nodes = self.copy_nodes_as_tuples(solver, destination, source)
        solver.merge(destination, source)

        self.assertEqual(n, len(solver._nodes))
        self.assert_nodes([ (0, 10, 0), (1, 0, 1), (2, 5, 2),
            (3, 0, 3), (4, 0, 5), (5, 6, 5) ], solver._nodes)
        self.assertEqual(10, solver.max_table_size)
        self.assert_result(old_nodes, solver, destination, source)

        destination, source = 4, 3
        old_nodes = self.copy_nodes_as_tuples(solver, destination, source)
        solver.merge(destination, source)

        self.assertEqual(n, len(solver._nodes))
        self.assert_nodes([ (0, 10, 0), (1, 0, 1), (2, 5, 2),
            (3, 0, 5), (4, 0, 5), (5, 6, 5) ], solver._nodes)
        self.assertEqual(10, solver.max_table_size)
        self.assert_result(old_nodes, solver, destination, source)

        destination, source = 3, 2
        old_nodes = self.copy_nodes_as_tuples(solver, destination, source)
        solver.merge(destination, source)

        self.assertEqual(n, len(solver._nodes))
        self.assert_nodes([ (0, 10, 0), (1, 0, 1), (2, 0, 5),
            (3, 0, 5), (4, 0, 5), (5, 11, 5) ], solver._nodes)
        self.assertEqual(11, solver.max_table_size)
        self.assert_result(old_nodes, solver, destination, source)

        destination, source = 2, 1
        old_nodes = self.copy_nodes_as_tuples(solver, destination, source)
        solver.merge(destination, source)

        self.assertEqual(n, len(solver._nodes))
        self.assert_nodes([ (0, 10, 0), (1, 0, 5), (2, 0, 5),
            (3, 0, 5), (4, 0, 5), (5, 11, 5) ], solver._nodes)
        self.assertEqual(11, solver.max_table_size)
        self.assert_result(old_nodes, solver, destination, source)

        destination, source = 1, 0
        old_nodes = self.copy_nodes_as_tuples(solver, destination, source)
        solver.merge(destination, source)

        self.assertEqual(n, len(solver._nodes))
        self.assert_nodes([ (0, 0, 5), (1, 0, 5), (2, 0, 5),
            (3, 0, 5), (4, 0, 5), (5, 21, 5) ], solver._nodes)
        self.assertEqual(21, solver.max_table_size)
        self.assert_result(old_nodes, solver, destination, source)

    def test_merge_with_2_empty_tables_and_merge_first_and_second(self):
        n = 2
        solver = Solver(n, [ 0, 0 ])

        self.assertEqual(n, len(solver._nodes))
        self.assert_nodes([ (0, 0, 0), (1, 0, 1) ], solver._nodes)
        self.assertEqual(0, solver.max_table_size)

        destination, source = 0, 1
        old_nodes = self.copy_nodes_as_tuples(solver, destination, source)
        solver.merge(destination, source)

        self.assertEqual(n, len(solver._nodes))
        self.assert_nodes([ (0, 0, 0), (1, 0, 0) ], solver._nodes)
        self.assertEqual(0, solver.max_table_size)
        self.assert_result(old_nodes, solver, destination, source)

    def test_merge_with_2_empty_tables_and_merge_second_and_first(self):
        n = 2
        solver = Solver(n, [ 0, 0 ])

        self.assertEqual(n, len(solver._nodes))
        self.assert_nodes([ (0, 0, 0), (1, 0, 1) ], solver._nodes)
        self.assertEqual(0, solver.max_table_size)

        destination, source = 1, 0
        old_nodes = self.copy_nodes_as_tuples(solver, destination, source)
        solver.merge(destination, source)

        self.assertEqual(n, len(solver._nodes))
        self.assert_nodes([ (0, 0, 1), (1, 0, 1) ], solver._nodes)
        self.assertEqual(0, solver.max_table_size)
        self.assert_result(old_nodes, solver, destination, source)

    def test_merge_with_2_tables_and_merge_first_and_second(self):
        n = 2
        solver = Solver(n, [ 1, 2 ])

        self.assertEqual(n, len(solver._nodes))
        self.assert_nodes([ (0, 1, 0), (1, 2, 1) ], solver._nodes)
        self.assertEqual(2, solver.max_table_size)

        destination, source = 0, 1
        old_nodes = self.copy_nodes_as_tuples(solver, destination, source)
        solver.merge(destination, source)

        self.assertEqual(n, len(solver._nodes))
        self.assert_nodes([ (0, 3, 0), (1, 0, 0) ], solver._nodes)
        self.assertEqual(3, solver.max_table_size)
        self.assert_result(old_nodes, solver, destination, source)

    def test_merge_with_2_tables_and_merge_second_and_first(self):
        n = 2
        solver = Solver(n, [ 1, 2 ])

        self.assertEqual(n, len(solver._nodes))
        self.assert_nodes([ (0, 1, 0), (1, 2, 1) ], solver._nodes)
        self.assertEqual(2, solver.max_table_size)

        destination, source = 1, 0
        old_nodes = self.copy_nodes_as_tuples(solver, destination, source)
        solver.merge(destination, source)

        self.assertEqual(n, len(solver._nodes))
        self.assert_nodes([ (0, 0, 1), (1, 3, 1) ], solver._nodes)
        self.assertEqual(3, solver.max_table_size)
        self.assert_result(old_nodes, solver, destination, source)

    def test_merge_with_3_tables_and_merge_from_right(self):
        n = 3
        solver = Solver(n, [ 1, 2, 3 ])

        self.assertEqual(n, len(solver._nodes))
        self.assert_nodes([ (0, 1, 0), (1, 2, 1), (2, 3, 2) ], solver._nodes)
        self.assertEqual(3, solver.max_table_size)

        destination, source = 0, 1
        old_nodes = self.copy_nodes_as_tuples(solver, destination, source)
        solver.merge(destination, source)

        self.assertEqual(n, len(solver._nodes))
        self.assert_nodes([ (0, 3, 0), (1, 0, 0), (2, 3, 2) ], solver._nodes)
        self.assertEqual(3, solver.max_table_size)
        self.assert_result(old_nodes, solver, destination, source)

        destination, source = 1, 2
        old_nodes = self.copy_nodes_as_tuples(solver, destination, source)
        solver.merge(destination, source)

        self.assertEqual(n, len(solver._nodes))
        self.assert_nodes([ (0, 6, 0), (1, 0, 0), (2, 0, 0) ], solver._nodes)
        self.assertEqual(6, solver.max_table_size)
        self.assert_result(old_nodes, solver, destination, source)

    def test_merge_with_3_tables_and_merge_from_left(self):
        n = 3
        solver = Solver(n, [ 1, 2, 3 ])

        self.assertEqual(n, len(solver._nodes))
        self.assert_nodes([ (0, 1, 0), (1, 2, 1), (2, 3, 2) ], solver._nodes)
        self.assertEqual(3, solver.max_table_size)

        destination, source = 1, 0
        old_nodes = self.copy_nodes_as_tuples(solver, destination, source)
        solver.merge(destination, source)

        self.assertEqual(n, len(solver._nodes))
        self.assert_nodes([ (0, 0, 1), (1, 3, 1), (2, 3, 2) ], solver._nodes)
        self.assertEqual(3, solver.max_table_size)
        self.assert_result(old_nodes, solver, destination, source)

        destination, source = 2, 0
        old_nodes = self.copy_nodes_as_tuples(solver, destination, source)
        solver.merge(destination, source)

        self.assertEqual(n, len(solver._nodes))
        self.assert_nodes([ (0, 0, 1), (1, 0, 2), (2, 6, 2) ], solver._nodes)
        self.assertEqual(6, solver.max_table_size)
        self.assert_result(old_nodes, solver, destination, source)

    def test_merge_with_4_tables(self):
        n = 4
        solver = Solver(n, [ 1, 2, 3, 4 ])

        self.assertEqual(n, len(solver._nodes))
        self.assert_nodes([ (0, 1, 0), (1, 2, 1), (2, 3, 2), (3, 4, 3) ],
            solver._nodes)
        self.assertEqual(4, solver.max_table_size)

        destination, source = 2, 3
        old_nodes = self.copy_nodes_as_tuples(solver, destination, source)
        solver.merge(destination, source)

        self.assertEqual(n, len(solver._nodes))
        self.assert_nodes([ (0, 1, 0), (1, 2, 1), (2, 7, 2), (3, 0, 2) ],
            solver._nodes)
        self.assertEqual(7, solver.max_table_size)
        self.assert_result(old_nodes, solver, destination, source)

        destination, source = 1, 2
        old_nodes = self.copy_nodes_as_tuples(solver, destination, source)
        solver.merge(destination, source)

        self.assertEqual(n, len(solver._nodes))
        self.assert_nodes([ (0, 1, 0), (1, 9, 1), (2, 0, 1), (3, 0, 2) ],
            solver._nodes)
        self.assertEqual(9, solver.max_table_size)
        self.assert_result(old_nodes, solver, destination, source)

        destination, source = 0, 3
        old_nodes = self.copy_nodes_as_tuples(solver, destination, source)
        solver.merge(destination, source)

        self.assertEqual(n, len(solver._nodes))
        self.assert_nodes([ (0, 10, 0), (1, 0, 0), (2, 0, 1), (3, 0, 1) ],
            solver._nodes)
        self.assertEqual(10, solver.max_table_size)
        self.assert_result(old_nodes, solver, destination, source)

    def test_merge_with_3_tables(self):
        n = 3
        solver = Solver(n, [ 2, 0, 0 ])

        self.assertEqual(n, len(solver._nodes))
        self.assert_nodes([ (0, 2, 0), (1, 0, 1), (2, 0, 2) ],
            solver._nodes)
        self.assertEqual(2, solver.max_table_size)

        destination, source = 1, 2
        old_nodes = self.copy_nodes_as_tuples(solver, destination, source)
        solver.merge(destination, source)

        self.assertEqual(n, len(solver._nodes))
        self.assert_nodes([ (0, 2, 0), (1, 0, 1), (2, 0, 1) ],
            solver._nodes)
        self.assertEqual(2, solver.max_table_size)
        self.assert_result(old_nodes, solver, destination, source)

        destination, source = 0, 2
        old_nodes = self.copy_nodes_as_tuples(solver, destination, source)
        solver.merge(destination, source)

        self.assertEqual(n, len(solver._nodes))
        self.assert_nodes([ (0, 2, 0), (1, 0, 0), (2, 0, 1) ],
            solver._nodes)
        self.assertEqual(2, solver.max_table_size)
        self.assert_result(old_nodes, solver, destination, source)

        destination, source = 1, 0
        old_nodes = self.copy_nodes_as_tuples(solver, destination, source)
        solver.merge(destination, source)

        self.assertEqual(n, len(solver._nodes))
        self.assert_nodes([ (0, 2, 0), (1, 0, 0), (2, 0, 1) ],
            solver._nodes)
        self.assertEqual(2, solver.max_table_size)
        self.assert_result(old_nodes, solver, destination, source)

        destination, source = 2, 0
        old_nodes = self.copy_nodes_as_tuples(solver, destination, source)
        solver.merge(destination, source)

        self.assertEqual(n, len(solver._nodes))
        self.assert_nodes([ (0, 2, 0), (1, 0, 0), (2, 0, 0) ],
            solver._nodes)
        self.assertEqual(2, solver.max_table_size)
        self.assert_result(old_nodes, solver, destination, source)

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
