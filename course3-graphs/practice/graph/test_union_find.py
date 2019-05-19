#!/usr/bin/python3

import unittest

import union_find

class NodeTestCase(unittest.TestCase):

    def test_constructor(self):
        value = 1

        node = union_find.Node(value)

        self.assertEqual(value, node.value)
        self.assertEqual(None, node.parent)
        self.assertEqual(None, node.rank)

    def test_str(self):
        node = union_find.Node(1)

        self.assertEqual('1', str(node))

    def test_repr(self):
        node = union_find.Node(1)

        self.assertEqual('[1, parent=None, rank=None]', repr(node))

    def test_repr_with_parent_and_rank(self):
        parent = union_find.Node(1)
        node = union_find.Node(2)
        node.parent = parent
        node.rank = 123

        self.assertEqual('[2, parent=1, rank=123]', repr(node))

    def test_lt_on_self(self):
        node = union_find.Node(1)

        self.assertEqual(False, node < node)

    def test_eq_on_self(self):
        node = union_find.Node(1)

        self.assertEqual(True, node == node)

    def test_gt_on_self(self):
        node = union_find.Node(1)

        self.assertEqual(False, node > node)

    def test_lt_on_none(self):
        node = union_find.Node(1)

        self.assertEqual(False, None < node)
        self.assertEqual(False, node < None)

    def test_eq_on_none(self):
        node = union_find.Node(1)

        self.assertEqual(False, None == node)
        self.assertEqual(False, node == None)

    def test_gt_on_none(self):
        node = union_find.Node(1)

        self.assertEqual(False, None > node)
        self.assertEqual(False, node > None)

    def test_lt_on_diff_type(self):
        node = union_find.Node(1)

        self.assertEqual(False, 'diff-type' < node)
        self.assertEqual(False, node < 'diff-type')

    def test_eq_on_diff_type(self):
        node = union_find.Node(1)

        self.assertEqual(False, 'diff-type' == node)
        self.assertEqual(False, node == 'diff-type')

    def test_gt_on_diff_type(self):
        node = union_find.Node(1)

        self.assertEqual(False, 'diff-type' > node)
        self.assertEqual(False, node > 'diff-type')

    def test_lt(self):
        node1 = union_find.Node(1)
        node2 = union_find.Node(2)

        self.assertEqual(True, node1 < node2)
        self.assertEqual(False, node2 < node1)

    def test_eq(self):
        node1 = union_find.Node(1)
        node2 = union_find.Node(2)

        self.assertEqual(False, node1 == node2)
        self.assertEqual(False, node2 == node1)

    def test_gt(self):
        node1 = union_find.Node(1)
        node2 = union_find.Node(2)

        self.assertEqual(False, node1 > node2)
        self.assertEqual(True, node2 > node1)

class UnionFindTestCase(unittest.TestCase):

    def setUp(self):
        self.structure = union_find.UnionFind()

    def tearDown(self):
        pass

    def assert_node(self, node, value, parent, rank):
        self.assertEqual(value, node.value)
        self.assertEqual(parent, node.parent)
        self.assertEqual(rank, node.rank)

    def test_make_set_on_one_node(self):
        value = 1
        node = union_find.Node(value)

        self.structure.make_set(node)

        self.assert_node(node, value, node, 0)

    def test_make_set_on_two_nodes(self):
        value1 = 1
        value2 = 2
        node1 = union_find.Node(value1)
        node2 = union_find.Node(value2)

        self.structure.make_set(node1)

        self.assert_node(node1, value1, node1, 0)
        self.assert_node(node2, value2, None, None)

        self.structure.make_set(node2)

        self.assert_node(node1, value1, node1, 0)
        self.assert_node(node2, value2, node2, 0)

    def test_make_set_on_three_nodes(self):
        value1 = 1
        value2 = 2
        value3 = 3
        node1 = union_find.Node(value1)
        node2 = union_find.Node(value2)
        node3 = union_find.Node(value3)

        self.structure.make_set(node1)

        self.assert_node(node1, value1, node1, 0)
        self.assert_node(node2, value2, None, None)
        self.assert_node(node3, value3, None, None)

        self.structure.make_set(node2)

        self.assert_node(node1, value1, node1, 0)
        self.assert_node(node2, value2, node2, 0)
        self.assert_node(node3, value3, None, None)

        self.structure.make_set(node3)

        self.assert_node(node1, value1, node1, 0)
        self.assert_node(node2, value2, node2, 0)
        self.assert_node(node3, value3, node3, 0)

    def test_union_on_one_node_before_make_set(self):
        node = union_find.Node(1)

        with self.assertRaisesRegex(ValueError,
            '1 not in the set.'):
            self.structure.union(node, node)

    def test_union_on_two_nodes_before_make_set(self):
        value1 = 1
        value2 = 2
        node1 = union_find.Node(value1)
        node2 = union_find.Node(value2)

        with self.assertRaisesRegex(ValueError,
            '1 not in the set.'):
            self.structure.union(node1, node2)

        with self.assertRaisesRegex(ValueError,
            '2 not in the set.'):
            self.structure.union(node2, node1)

    def test_union_on_one_node(self):
        value = 1
        node = union_find.Node(value)

        self.structure.make_set(node)

        self.assert_node(node, value, node, 0)

        self.structure.union(node, node)

        self.assert_node(node, value, node, 0)

    def test_union_on_two_nodes(self):
        value1 = 1
        value2 = 2
        node1 = union_find.Node(value1)
        node2 = union_find.Node(value2)

        self.structure.make_set(node1)
        self.structure.make_set(node2)

        self.assert_node(node1, value1, node1, 0)
        self.assert_node(node2, value2, node2, 0)

        self.structure.union(node1, node2)

        self.assert_node(node1, value1, node1, 1)
        self.assert_node(node2, value2, node1, 0)

    def test_union_on_three_nodes_as_1_2_and_2_3(self):
        value1 = 1
        value2 = 2
        value3 = 3
        node1 = union_find.Node(value1)
        node2 = union_find.Node(value2)
        node3 = union_find.Node(value3)

        self.structure.make_set(node1)
        self.structure.make_set(node2)
        self.structure.make_set(node3)

        self.assert_node(node1, value1, node1, 0)
        self.assert_node(node2, value2, node2, 0)
        self.assert_node(node3, value3, node3, 0)

        self.structure.union(node1, node2)

        self.assert_node(node1, value1, node1, 1)
        self.assert_node(node2, value2, node1, 0)
        self.assert_node(node3, value3, node3, 0)

        self.structure.union(node2, node3)

        self.assert_node(node1, value1, node1, 1)
        self.assert_node(node2, value2, node1, 0)
        self.assert_node(node3, value3, node1, 0)

    def test_union_on_three_nodes_as_1_2_and_1_3(self):
        value1 = 1
        value2 = 2
        value3 = 3
        node1 = union_find.Node(value1)
        node2 = union_find.Node(value2)
        node3 = union_find.Node(value3)

        self.structure.make_set(node1)
        self.structure.make_set(node2)
        self.structure.make_set(node3)

        self.assert_node(node1, value1, node1, 0)
        self.assert_node(node2, value2, node2, 0)
        self.assert_node(node3, value3, node3, 0)

        self.structure.union(node1, node2)

        self.assert_node(node1, value1, node1, 1)
        self.assert_node(node2, value2, node1, 0)
        self.assert_node(node3, value3, node3, 0)

        self.structure.union(node1, node3)

        self.assert_node(node1, value1, node1, 1)
        self.assert_node(node2, value2, node1, 0)
        self.assert_node(node3, value3, node1, 0)

    def test_union_on_four_nodes_as_1_2_and_3_4_and_1_3(self):
        value1 = 1
        value2 = 2
        value3 = 3
        value4 = 4
        node1 = union_find.Node(value1)
        node2 = union_find.Node(value2)
        node3 = union_find.Node(value3)
        node4 = union_find.Node(value4)

        self.structure.make_set(node1)
        self.structure.make_set(node2)
        self.structure.make_set(node3)
        self.structure.make_set(node4)

        self.assert_node(node1, value1, node1, 0)
        self.assert_node(node2, value2, node2, 0)
        self.assert_node(node3, value3, node3, 0)
        self.assert_node(node4, value4, node4, 0)

        self.structure.union(node1, node2)

        self.assert_node(node1, value1, node1, 1)
        self.assert_node(node2, value2, node1, 0)
        self.assert_node(node3, value3, node3, 0)
        self.assert_node(node4, value4, node4, 0)

        self.structure.union(node3, node4)

        self.assert_node(node1, value1, node1, 1)
        self.assert_node(node2, value2, node1, 0)
        self.assert_node(node3, value3, node3, 1)
        self.assert_node(node4, value4, node3, 0)

        self.structure.union(node1, node3)

        self.assert_node(node1, value1, node1, 2)
        self.assert_node(node2, value2, node1, 0)
        self.assert_node(node3, value3, node1, 1)
        self.assert_node(node4, value4, node3, 0)

    def test_find_before_make_set(self):
        node = union_find.Node(1)

        with self.assertRaisesRegex(ValueError,
            '1 not in the set.'):
            self.structure.find(node)

    def test_find_on_one_node(self):
        value = 1
        node = union_find.Node(value)

        self.structure.make_set(node)

        result = self.structure.find(node)

        self.assertEqual(node, result)
        self.assert_node(node, value, node, 0)

    def test_find_on_two_nodes(self):
        value1 = 1
        value2 = 2
        node1 = union_find.Node(value1)
        node2 = union_find.Node(value2)

        self.structure.make_set(node1)
        self.structure.make_set(node2)

        result = self.structure.find(node1)

        self.assertEqual(node1, result)
        self.assert_node(node1, value1, node1, 0)
        self.assert_node(node2, value2, node2, 0)

        result = self.structure.find(node2)

        self.assertEqual(node2, result)
        self.assert_node(node1, value1, node1, 0)
        self.assert_node(node2, value2, node2, 0)

    def test_find_on_on_three_nodes(self):
        value1 = 1
        value2 = 2
        value3 = 3
        node1 = union_find.Node(value1)
        node2 = union_find.Node(value2)
        node3 = union_find.Node(value3)

        self.structure.make_set(node1)
        self.structure.make_set(node2)
        self.structure.make_set(node3)

        result = self.structure.find(node1)

        self.assertEqual(node1, result)
        self.assert_node(node1, value1, node1, 0)
        self.assert_node(node2, value2, node2, 0)
        self.assert_node(node3, value3, node3, 0)

        result = self.structure.find(node2)

        self.assertEqual(node2, result)
        self.assert_node(node1, value1, node1, 0)
        self.assert_node(node2, value2, node2, 0)
        self.assert_node(node3, value3, node3, 0)

        result = self.structure.find(node3)

        self.assertEqual(node3, result)
        self.assert_node(node1, value1, node1, 0)
        self.assert_node(node2, value2, node2, 0)
        self.assert_node(node3, value3, node3, 0)

    def test_find_on_four_node_set_of_two_ranks(self):
        value1 = 1
        value2 = 2
        value3 = 3
        value4 = 4
        node1 = union_find.Node(value1)
        node2 = union_find.Node(value2)
        node3 = union_find.Node(value3)
        node4 = union_find.Node(value4)

        self.structure.make_set(node1)
        self.structure.make_set(node2)
        self.structure.make_set(node3)
        self.structure.make_set(node4)
        self.structure.union(node1, node2)
        self.structure.union(node3, node4)
        self.structure.union(node1, node3)

        result = self.structure.find(node1)

        self.assertEqual(node1, result)
        self.assert_node(node1, value1, node1, 2)
        self.assert_node(node2, value2, node1, 0)
        self.assert_node(node3, value3, node1, 1)
        self.assert_node(node4, value4, node3, 0)

        result = self.structure.find(node2)

        self.assertEqual(node1, result)
        self.assert_node(node1, value1, node1, 2)
        self.assert_node(node2, value2, node1, 0)
        self.assert_node(node3, value3, node1, 1)
        self.assert_node(node4, value4, node3, 0)

        result = self.structure.find(node3)

        self.assertEqual(node1, result)
        self.assert_node(node1, value1, node1, 2)
        self.assert_node(node2, value2, node1, 0)
        self.assert_node(node3, value3, node1, 1)
        self.assert_node(node4, value4, node3, 0)

        result = self.structure.find(node4)

        self.assertEqual(node1, result)
        self.assert_node(node1, value1, node1, 2)
        self.assert_node(node2, value2, node1, 0)
        self.assert_node(node3, value3, node1, 1)
        self.assert_node(node4, value4, node1, 0)

    def test_find_on_seven_node_set_of_two_ranks(self):
        value1 = 1
        value2 = 2
        value3 = 3
        value4 = 4
        value5 = 5
        value6 = 6
        value7 = 7
        node1 = union_find.Node(value1)
        node2 = union_find.Node(value2)
        node3 = union_find.Node(value3)
        node4 = union_find.Node(value4)
        node5 = union_find.Node(value5)
        node6 = union_find.Node(value6)
        node7 = union_find.Node(value7)

        self.structure.make_set(node1)
        self.structure.make_set(node2)
        self.structure.make_set(node3)
        self.structure.make_set(node4)
        self.structure.make_set(node5)
        self.structure.make_set(node6)
        self.structure.make_set(node7)
        self.structure.union(node1, node2)
        self.structure.union(node3, node4)
        self.structure.union(node5, node6)
        self.structure.union(node1, node3)
        self.structure.union(node5, node7)
        self.structure.union(node1, node5)

        self.assert_node(node1, value1, node1, 2)
        self.assert_node(node2, value2, node1, 0)
        self.assert_node(node3, value3, node1, 1)
        self.assert_node(node4, value4, node3, 0)
        self.assert_node(node5, value5, node1, 1)
        self.assert_node(node6, value6, node5, 0)
        self.assert_node(node7, value7, node5, 0)

        result = self.structure.find(node1)

        self.assertEqual(node1, result)
        self.assert_node(node1, value1, node1, 2)
        self.assert_node(node2, value2, node1, 0)
        self.assert_node(node3, value3, node1, 1)
        self.assert_node(node4, value4, node3, 0)
        self.assert_node(node5, value5, node1, 1)
        self.assert_node(node6, value6, node5, 0)
        self.assert_node(node7, value7, node5, 0)

        result = self.structure.find(node2)

        self.assertEqual(node1, result)
        self.assert_node(node1, value1, node1, 2)
        self.assert_node(node2, value2, node1, 0)
        self.assert_node(node3, value3, node1, 1)
        self.assert_node(node4, value4, node3, 0)
        self.assert_node(node5, value5, node1, 1)
        self.assert_node(node6, value6, node5, 0)
        self.assert_node(node7, value7, node5, 0)

        result = self.structure.find(node3)

        self.assertEqual(node1, result)
        self.assert_node(node1, value1, node1, 2)
        self.assert_node(node2, value2, node1, 0)
        self.assert_node(node3, value3, node1, 1)
        self.assert_node(node4, value4, node3, 0)
        self.assert_node(node5, value5, node1, 1)
        self.assert_node(node6, value6, node5, 0)
        self.assert_node(node7, value7, node5, 0)

        result = self.structure.find(node4)

        self.assertEqual(node1, result)
        self.assert_node(node1, value1, node1, 2)
        self.assert_node(node2, value2, node1, 0)
        self.assert_node(node3, value3, node1, 1)
        self.assert_node(node4, value4, node1, 0)
        self.assert_node(node5, value5, node1, 1)
        self.assert_node(node6, value6, node5, 0)
        self.assert_node(node7, value7, node5, 0)

        result = self.structure.find(node5)

        self.assertEqual(node1, result)
        self.assert_node(node1, value1, node1, 2)
        self.assert_node(node2, value2, node1, 0)
        self.assert_node(node3, value3, node1, 1)
        self.assert_node(node4, value4, node1, 0)
        self.assert_node(node5, value5, node1, 1)
        self.assert_node(node6, value6, node5, 0)
        self.assert_node(node7, value7, node5, 0)

        result = self.structure.find(node6)

        self.assertEqual(node1, result)
        self.assert_node(node1, value1, node1, 2)
        self.assert_node(node2, value2, node1, 0)
        self.assert_node(node3, value3, node1, 1)
        self.assert_node(node4, value4, node1, 0)
        self.assert_node(node5, value5, node1, 1)
        self.assert_node(node6, value6, node1, 0)
        self.assert_node(node7, value7, node5, 0)

        result = self.structure.find(node7)

        self.assertEqual(node1, result)
        self.assert_node(node1, value1, node1, 2)
        self.assert_node(node2, value2, node1, 0)
        self.assert_node(node3, value3, node1, 1)
        self.assert_node(node4, value4, node1, 0)
        self.assert_node(node5, value5, node1, 1)
        self.assert_node(node6, value6, node1, 0)
        self.assert_node(node7, value7, node1, 0)

    def test_find_on_eight_node_set_of_three_ranks(self):
        value1 = 1
        value2 = 2
        value3 = 3
        value4 = 4
        value5 = 5
        value6 = 6
        value7 = 7
        value8 = 8
        node1 = union_find.Node(value1)
        node2 = union_find.Node(value2)
        node3 = union_find.Node(value3)
        node4 = union_find.Node(value4)
        node5 = union_find.Node(value5)
        node6 = union_find.Node(value6)
        node7 = union_find.Node(value7)
        node8 = union_find.Node(value8)

        self.structure.make_set(node1)
        self.structure.make_set(node2)
        self.structure.make_set(node3)
        self.structure.make_set(node4)
        self.structure.make_set(node5)
        self.structure.make_set(node6)
        self.structure.make_set(node7)
        self.structure.make_set(node8)
        self.structure.union(node1, node2)
        self.structure.union(node3, node4)
        self.structure.union(node1, node3)
        self.structure.union(node5, node6)
        self.structure.union(node7, node8)
        self.structure.union(node5, node7)
        self.structure.union(node1, node5)

        self.assert_node(node1, value1, node1, 3)
        self.assert_node(node2, value2, node1, 0)
        self.assert_node(node3, value3, node1, 1)
        self.assert_node(node4, value4, node3, 0)
        self.assert_node(node5, value5, node1, 2)
        self.assert_node(node6, value6, node5, 0)
        self.assert_node(node7, value7, node5, 1)
        self.assert_node(node8, value8, node7, 0)

        result = self.structure.find(node1)

        self.assertEqual(node1, result)
        self.assert_node(node1, value1, node1, 3)
        self.assert_node(node2, value2, node1, 0)
        self.assert_node(node3, value3, node1, 1)
        self.assert_node(node4, value4, node3, 0)
        self.assert_node(node5, value5, node1, 2)
        self.assert_node(node6, value6, node5, 0)
        self.assert_node(node7, value7, node5, 1)
        self.assert_node(node8, value8, node7, 0)

        result = self.structure.find(node2)

        self.assertEqual(node1, result)
        self.assert_node(node1, value1, node1, 3)
        self.assert_node(node2, value2, node1, 0)
        self.assert_node(node3, value3, node1, 1)
        self.assert_node(node4, value4, node3, 0)
        self.assert_node(node5, value5, node1, 2)
        self.assert_node(node6, value6, node5, 0)
        self.assert_node(node7, value7, node5, 1)
        self.assert_node(node8, value8, node7, 0)

        result = self.structure.find(node3)

        self.assertEqual(node1, result)
        self.assert_node(node1, value1, node1, 3)
        self.assert_node(node2, value2, node1, 0)
        self.assert_node(node3, value3, node1, 1)
        self.assert_node(node4, value4, node3, 0)
        self.assert_node(node5, value5, node1, 2)
        self.assert_node(node6, value6, node5, 0)
        self.assert_node(node7, value7, node5, 1)
        self.assert_node(node8, value8, node7, 0)

        result = self.structure.find(node4)

        self.assertEqual(node1, result)
        self.assert_node(node1, value1, node1, 3)
        self.assert_node(node2, value2, node1, 0)
        self.assert_node(node3, value3, node1, 1)
        self.assert_node(node4, value4, node1, 0)
        self.assert_node(node5, value5, node1, 2)
        self.assert_node(node6, value6, node5, 0)
        self.assert_node(node7, value7, node5, 1)
        self.assert_node(node8, value8, node7, 0)

        result = self.structure.find(node5)

        self.assertEqual(node1, result)
        self.assert_node(node1, value1, node1, 3)
        self.assert_node(node2, value2, node1, 0)
        self.assert_node(node3, value3, node1, 1)
        self.assert_node(node4, value4, node1, 0)
        self.assert_node(node5, value5, node1, 2)
        self.assert_node(node6, value6, node5, 0)
        self.assert_node(node7, value7, node5, 1)
        self.assert_node(node8, value8, node7, 0)

        result = self.structure.find(node6)

        self.assertEqual(node1, result)
        self.assert_node(node1, value1, node1, 3)
        self.assert_node(node2, value2, node1, 0)
        self.assert_node(node3, value3, node1, 1)
        self.assert_node(node4, value4, node1, 0)
        self.assert_node(node5, value5, node1, 2)
        self.assert_node(node6, value6, node1, 0)
        self.assert_node(node7, value7, node5, 1)
        self.assert_node(node8, value8, node7, 0)

        result = self.structure.find(node7)

        self.assertEqual(node1, result)
        self.assert_node(node1, value1, node1, 3)
        self.assert_node(node2, value2, node1, 0)
        self.assert_node(node3, value3, node1, 1)
        self.assert_node(node4, value4, node1, 0)
        self.assert_node(node5, value5, node1, 2)
        self.assert_node(node6, value6, node1, 0)
        self.assert_node(node7, value7, node1, 1)
        self.assert_node(node8, value8, node7, 0)

        result = self.structure.find(node8)

        self.assertEqual(node1, result)
        self.assert_node(node1, value1, node1, 3)
        self.assert_node(node2, value2, node1, 0)
        self.assert_node(node3, value3, node1, 1)
        self.assert_node(node4, value4, node1, 0)
        self.assert_node(node5, value5, node1, 2)
        self.assert_node(node6, value6, node1, 0)
        self.assert_node(node7, value7, node1, 1)
        self.assert_node(node8, value8, node1, 0)

if __name__ == '__main__':
    class_names = \
    [
        NodeTestCase,
        UnionFindTestCase,
    ]

    suite = unittest.TestSuite()

    for c in class_names:
        suite.addTest(unittest.defaultTestLoader.loadTestsFromTestCase(c))

    unittest.TextTestRunner().run(suite)
