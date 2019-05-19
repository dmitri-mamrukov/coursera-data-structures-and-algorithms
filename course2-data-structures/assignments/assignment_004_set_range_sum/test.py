#!/usr/bin/python3

import unittest

import set_range_sum

class VertexTestCase(unittest.TestCase):

    def test_constructor_with_parent_as_none(self):
        key = 1
        sum = 123
        left = None
        right = None
        parent = None

        vertex = set_range_sum.SumSplayTree.Vertex(key,
                                                   sum,
                                                   left,
                                                   right,
                                                   parent)

        self.assertEqual(key, vertex.key)
        self.assertEqual(sum, vertex.sum)
        self.assertEqual(left, vertex.left)
        self.assertEqual(right, vertex.right)
        self.assertEqual(parent, vertex.parent)

    def test_constructor_with_parent_as_another_vertex(self):
        key1 = 1
        sum1 = 123
        left1 = None
        right1 = None
        parent1 = None

        vertex1 = set_range_sum.SumSplayTree.Vertex(key1,
                                                    sum1,
                                                    left1,
                                                    right1,
                                                    parent1)

        self.assertEqual(key1, vertex1.key)
        self.assertEqual(sum1, vertex1.sum)
        self.assertEqual(left1, vertex1.left)
        self.assertEqual(right1, vertex1.right)
        self.assertEqual(parent1, vertex1.parent)

        key2 = 2
        sum2 = 456
        left2 = None
        right2 = None
        parent2 = vertex1

        vertex2 = set_range_sum.SumSplayTree.Vertex(key2,
                                                    sum2,
                                                    left2,
                                                    right2,
                                                    parent2)

        self.assertEqual(key1, vertex1.key)
        self.assertEqual(sum1, vertex1.sum)
        self.assertEqual(left1, vertex1.left)
        self.assertEqual(right1, vertex1.right)
        self.assertEqual(parent1, vertex1.parent)

        self.assertEqual(key2, vertex2.key)
        self.assertEqual(sum2, vertex2.sum)
        self.assertEqual(left2, vertex2.left)
        self.assertEqual(right2, vertex2.right)
        self.assertEqual(parent2, vertex2.parent)

    def test_str(self):
        vertex = set_range_sum.SumSplayTree.Vertex(1, 123, None, None, None)

        self.assertEqual('1', str(vertex))

    def test_str_on_three_node_tree(self):
        key1 = 1
        key2 = 2
        key3 = 3
        parent = set_range_sum.SumSplayTree.Vertex(key1, 11, None, None, None)
        left = set_range_sum.SumSplayTree.Vertex(key2, 22, None, None, None)
        right = set_range_sum.SumSplayTree.Vertex(key3, 33, None, None, None)
        parent.left = left
        parent.right = right
        left.parent = parent
        right.parent = parent

        self.assertEqual('1', str(parent))
        self.assertEqual('2', str(left))
        self.assertEqual('3', str(right))

    def test_repr_on_one_node(self):
        vertex = set_range_sum.SumSplayTree.Vertex(1, 123, None, None, None)

        self.assertEqual(
                    '[key: 1, sum: 123, left: None, right: None, parent: None]',
                    repr(vertex))

    def test_repr_on_three_node_tree(self):
        key1 = 1
        key2 = 2
        key3 = 3
        parent = set_range_sum.SumSplayTree.Vertex(key1, 11, None, None, None)
        left = set_range_sum.SumSplayTree.Vertex(key2, 22, None, None, None)
        right = set_range_sum.SumSplayTree.Vertex(key3, 33, None, None, None)
        parent.left = left
        parent.right = right
        left.parent = parent
        right.parent = parent

        self.assertEqual('[key: 1, sum: 11, left: 2, right: 3, parent: None]',
                         repr(parent))
        self.assertEqual(
                        '[key: 2, sum: 22, left: None, right: None, parent: 1]',
                        repr(left))
        self.assertEqual(
                        '[key: 3, sum: 33, left: None, right: None, parent: 1]',
                        repr(right))

class SumSplayTreeTestCase(unittest.TestCase):

    def setUp(self):
        self.tree = set_range_sum.SumSplayTree()

    def tearDown(self):
        pass

    def assert_binary_search_property(self, root):
        nodes = [ root ]

        while len(nodes) > 0:
            node = nodes.pop()
            if node.left is not None:
                self.assertTrue(node.left.key <= node.key)
            if node.right is not None:
                self.assertTrue(node.key <= node.right.key)

            if node.left is not None:
                nodes.append(node.left)
            if node.right is not None:
                nodes.append(node.right)

    def assert_augmented_property_as_sums(self, root):
        nodes = [ root ]

        while len(nodes) > 0:
            node = nodes.pop()
            left_sum = node.left.sum if node.left is not None else 0
            right_sum = node.right.sum if node.right is not None else 0
            self.assertEqual(left_sum + node.key + right_sum, node.sum)

            if node.left is not None:
                nodes.append(node.left)
            if node.right is not None:
                nodes.append(node.right)

    def assert_binary_search_properties(self, root):
        self.assert_binary_search_property(root)
        self.assert_augmented_property_as_sums(root)

    def assert_left_tree_less_than_right_tree(self, left, right):
        left_rightmost_node = left
        while left_rightmost_node.right is not None:
            left_rightmost_node = left_rightmost_node.right
        right_leftmost_node = right
        while right_leftmost_node.left is not None:
            right_leftmost_node = right_leftmost_node.left

        self.assertTrue(left_rightmost_node.key < right_leftmost_node.key)

    def create_one_node_tree(self):
        key = 1
        sum = key
        v = set_range_sum.SumSplayTree.Vertex(key, sum, None, None, None)

        self.assertEqual(key, v.key)
        self.assertEqual(None, v.left)
        self.assertEqual(None, v.right)
        self.assertEqual(None, v.parent)

        self.assert_binary_search_properties(v)

        return (key, v)

    def create_two_node_tree_as_left_root(self):
        key1 = 2
        key2 = 1
        sum2 = key2
        sum1 = sum2 + key1
        parent = set_range_sum.SumSplayTree.Vertex(key1,
                                                   sum1,
                                                   None,
                                                   None,
                                                   None)
        left = set_range_sum.SumSplayTree.Vertex(key2,
                                                 sum2,
                                                 None,
                                                 None,
                                                 None)
        parent.left = left
        left.parent = parent

        self.assertEqual(key1, parent.key)
        self.assertEqual(left, parent.left)
        self.assertEqual(None, parent.right)
        self.assertEqual(None, parent.parent)

        self.assertEqual(key2, left.key)
        self.assertEqual(None, left.left)
        self.assertEqual(None, left.right)
        self.assertEqual(parent, left.parent)

        self.assert_binary_search_properties(parent)

        return (key1, key2, parent, left)

    def create_two_node_tree_as_root_right(self):
        key1 = 1
        key2 = 2
        sum2 = key2
        sum1 = key1 + sum2
        parent = set_range_sum.SumSplayTree.Vertex(key1,
                                                   sum1,
                                                   None,
                                                   None,
                                                   None)
        right = set_range_sum.SumSplayTree.Vertex(key2,
                                                  sum2,
                                                  None,
                                                  None,
                                                  None)
        parent.right = right
        right.parent = parent

        self.assertEqual(key1, parent.key)
        self.assertEqual(None, parent.left)
        self.assertEqual(right, parent.right)
        self.assertEqual(None, parent.parent)

        self.assertEqual(key2, right.key)
        self.assertEqual(None, right.left)
        self.assertEqual(None, right.right)
        self.assertEqual(parent, right.parent)

        self.assert_binary_search_properties(parent)

        return (key1, key2, parent, right)

    def create_three_node_tree_as_left_root_right(self):
        key1 = 2
        key2 = 1
        key3 = 3
        sum3 = key3
        sum2 = key2
        sum1 = sum2 + key1 + sum3
        parent = set_range_sum.SumSplayTree.Vertex(key1,
                                                   sum1,
                                                   None,
                                                   None,
                                                   None)
        left = set_range_sum.SumSplayTree.Vertex(key2,
                                                 sum2,
                                                 None,
                                                 None,
                                                 None)
        right = set_range_sum.SumSplayTree.Vertex(key3,
                                                  sum3,
                                                  None,
                                                  None,
                                                  None)
        parent.left = left
        parent.right = right
        left.parent = parent
        right.parent = parent

        self.assertEqual(key1, parent.key)
        self.assertEqual(left, parent.left)
        self.assertEqual(right, parent.right)
        self.assertEqual(None, parent.parent)

        self.assertEqual(key2, left.key)
        self.assertEqual(None, left.left)
        self.assertEqual(None, left.right)
        self.assertEqual(parent, left.parent)

        self.assertEqual(key3, right.key)
        self.assertEqual(None, right.left)
        self.assertEqual(None, right.right)
        self.assertEqual(parent, right.parent)

        self.assert_binary_search_properties(parent)

        return (key1, key2, key3, parent, left, right)

    def create_nine_node_tree_with_left_subtree(self):
        key1 = 8
        key2 = 4
        key3 = 9
        key4 = 2
        key5 = 6
        key6 = 1
        key7 = 3
        key8 = 5
        key9 = 7
        sum9 = key9
        sum8 = key8
        sum7 = key7
        sum6 = key6
        sum5 = sum8 + key5 + sum9
        sum4 = sum6 + key4 + sum7
        sum3 = key3
        sum2 = sum4 + key2 + sum5
        sum1 = sum2 + key1 + sum3
        grandparent = set_range_sum.SumSplayTree.Vertex(key1,
                                                        sum1,
                                                        None,
                                                        None,
                                                        None)
        grandparent_left = set_range_sum.SumSplayTree.Vertex(key2,
                                                             sum2,
                                                             None,
                                                             None,
                                                             None)
        grandparent_right = set_range_sum.SumSplayTree.Vertex(key3,
                                                              sum3,
                                                              None,
                                                              None,
                                                              None)
        grandparent.left = grandparent_left
        grandparent.right = grandparent_right
        grandparent_left.parent = grandparent
        grandparent_right.parent = grandparent
        left = set_range_sum.SumSplayTree.Vertex(key4,
                                                 sum4,
                                                 None,
                                                 None,
                                                 None)
        right = set_range_sum.SumSplayTree.Vertex(key5,
                                                  sum5,
                                                  None,
                                                  None,
                                                  None)
        grandparent_left.left = left
        grandparent_left.right = right
        left.parent = grandparent_left
        right.parent = grandparent_left
        left_left = set_range_sum.SumSplayTree.Vertex(key6,
                                                      sum6,
                                                      None,
                                                      None,
                                                      None)
        left_right = set_range_sum.SumSplayTree.Vertex(key7,
                                                       sum7,
                                                       None,
                                                       None,
                                                       None)
        left.left = left_left
        left.right = left_right
        left_left.parent = left
        left_right.parent = left
        right_left = set_range_sum.SumSplayTree.Vertex(key8,
                                                       sum8,
                                                       None,
                                                       None,
                                                       None)
        right_right = set_range_sum.SumSplayTree.Vertex(key9,
                                                        sum9,
                                                        None,
                                                        None,
                                                        None)
        right.left = right_left
        right.right = right_right
        right_left.parent = right
        right_right.parent = right

        self.assertEqual(key1, grandparent.key)
        self.assertEqual(grandparent_left, grandparent.left)
        self.assertEqual(grandparent_right, grandparent.right)
        self.assertEqual(None, grandparent.parent)

        self.assertEqual(key2, grandparent_left.key)
        self.assertEqual(left, grandparent_left.left)
        self.assertEqual(right, grandparent_left.right)
        self.assertEqual(grandparent, grandparent_left.parent)

        self.assertEqual(key3, grandparent_right.key)
        self.assertEqual(None, grandparent_right.left)
        self.assertEqual(None, grandparent_right.right)
        self.assertEqual(grandparent, grandparent_right.parent)

        self.assertEqual(key4, left.key)
        self.assertEqual(left_left, left.left)
        self.assertEqual(left_right, left.right)
        self.assertEqual(grandparent_left, left.parent)

        self.assertEqual(key5, right.key)
        self.assertEqual(right_left, right.left)
        self.assertEqual(right_right, right.right)
        self.assertEqual(grandparent_left, right.parent)

        self.assertEqual(key6, left_left.key)
        self.assertEqual(None, left_left.left)
        self.assertEqual(None, left_left.right)
        self.assertEqual(left, left_left.parent)

        self.assertEqual(key7, left_right.key)
        self.assertEqual(None, left_right.left)
        self.assertEqual(None, left_right.right)
        self.assertEqual(left, left_right.parent)

        self.assertEqual(key8, right_left.key)
        self.assertEqual(None, right_left.left)
        self.assertEqual(None, right_left.right)
        self.assertEqual(right, right_left.parent)

        self.assertEqual(key9, right_right.key)
        self.assertEqual(None, right_right.left)
        self.assertEqual(None, right_right.right)
        self.assertEqual(right, right_right.parent)

        self.assert_binary_search_properties(grandparent)

        return (key1, key2, key3, key4, key5, key6, key7, key8, key9,
                grandparent, grandparent_left, grandparent_right, left, right,
                left_left, left_right, right_left, right_right)

    def create_nine_node_tree_with_right_subtree(self):
        key1 = 2
        key2 = 1
        key3 = 6
        key4 = 4
        key5 = 8
        key6 = 3
        key7 = 5
        key8 = 7
        key9 = 9
        sum9 = key9
        sum8 = key8
        sum7 = key7
        sum6 = key6
        sum5 = sum8 + key5 + sum9
        sum4 = sum6 + key4 + sum7
        sum3 = sum4 + key3 + sum5
        sum2 = key2
        sum1 = sum2 + key1 + sum3
        grandparent = set_range_sum.SumSplayTree.Vertex(key1,
                                                        sum1,
                                                        None,
                                                        None,
                                                        None)
        grandparent_left = set_range_sum.SumSplayTree.Vertex(key2,
                                                             sum2,
                                                             None,
                                                             None,
                                                             None)
        grandparent_right = set_range_sum.SumSplayTree.Vertex(key3,
                                                              sum3,
                                                              None,
                                                              None,
                                                              None)
        grandparent.left = grandparent_left
        grandparent.right = grandparent_right
        grandparent_left.parent = grandparent
        grandparent_right.parent = grandparent
        left = set_range_sum.SumSplayTree.Vertex(key4,
                                                 sum4,
                                                 None,
                                                 None,
                                                 None)
        right = set_range_sum.SumSplayTree.Vertex(key5,
                                                  sum5,
                                                  None,
                                                  None,
                                                  None)
        grandparent_right.left = left
        grandparent_right.right = right
        left.parent = grandparent_right
        right.parent = grandparent_right
        left_left = set_range_sum.SumSplayTree.Vertex(key6,
                                                      sum6,
                                                      None,
                                                      None,
                                                      None)
        left_right = set_range_sum.SumSplayTree.Vertex(key7,
                                                       sum7,
                                                       None,
                                                       None,
                                                       None)
        left.left = left_left
        left.right = left_right
        left_left.parent = left
        left_right.parent = left
        right_left = set_range_sum.SumSplayTree.Vertex(key8,
                                                       sum8,
                                                       None,
                                                       None,
                                                       None)
        right_right = set_range_sum.SumSplayTree.Vertex(key9,
                                                        sum9,
                                                        None,
                                                        None,
                                                        None)
        right.left = right_left
        right.right = right_right
        right_left.parent = right
        right_right.parent = right

        self.assertEqual(key1, grandparent.key)
        self.assertEqual(grandparent_left, grandparent.left)
        self.assertEqual(grandparent_right, grandparent.right)
        self.assertEqual(None, grandparent.parent)

        self.assertEqual(key2, grandparent_left.key)
        self.assertEqual(None, grandparent_left.left)
        self.assertEqual(None, grandparent_left.right)
        self.assertEqual(grandparent, grandparent_left.parent)

        self.assertEqual(key3, grandparent_right.key)
        self.assertEqual(left, grandparent_right.left)
        self.assertEqual(right, grandparent_right.right)
        self.assertEqual(grandparent, grandparent_right.parent)

        self.assertEqual(key4, left.key)
        self.assertEqual(left_left, left.left)
        self.assertEqual(left_right, left.right)
        self.assertEqual(grandparent_right, left.parent)

        self.assertEqual(key5, right.key)
        self.assertEqual(right_left, right.left)
        self.assertEqual(right_right, right.right)
        self.assertEqual(grandparent_right, right.parent)

        self.assertEqual(key6, left_left.key)
        self.assertEqual(None, left_left.left)
        self.assertEqual(None, left_left.right)
        self.assertEqual(left, left_left.parent)

        self.assertEqual(key7, left_right.key)
        self.assertEqual(None, left_right.left)
        self.assertEqual(None, left_right.right)
        self.assertEqual(left, left_right.parent)

        self.assertEqual(key8, right_left.key)
        self.assertEqual(None, right_left.left)
        self.assertEqual(None, right_left.right)
        self.assertEqual(right, right_left.parent)

        self.assertEqual(key9, right_right.key)
        self.assertEqual(None, right_right.left)
        self.assertEqual(None, right_right.right)
        self.assertEqual(right, right_right.parent)

        self.assert_binary_search_properties(grandparent)

        return (key1, key2, key3, key4, key5, key6, key7, key8, key9,
                grandparent, grandparent_left, grandparent_right, left, right,
                left_left, left_right, right_left, right_right)

    def assert_original_complete_fifteen_node_tree(self, key1, key2, key3, key4,
                                                   key5, key6, key7, key8, key9,
                                                   key10, key11, key12, key13,
                                                   key14, key15, node1, node2,
                                                   node3, node4, node5, node6,
                                                   node7, node8, node9, node10,
                                                   node11, node12, node13,
                                                   node14, node15):
        self.assertEqual(key1, node1.key)
        self.assertEqual(node2, node1.left)
        self.assertEqual(node3, node1.right)
        self.assertEqual(None, node1.parent)

        self.assertEqual(key2, node2.key)
        self.assertEqual(node4, node2.left)
        self.assertEqual(node5, node2.right)
        self.assertEqual(node1, node2.parent)

        self.assertEqual(key3, node3.key)
        self.assertEqual(node6, node3.left)
        self.assertEqual(node7, node3.right)
        self.assertEqual(node1, node3.parent)

        self.assertEqual(key4, node4.key)
        self.assertEqual(node8, node4.left)
        self.assertEqual(node9, node4.right)
        self.assertEqual(node2, node4.parent)

        self.assertEqual(key5, node5.key)
        self.assertEqual(node10, node5.left)
        self.assertEqual(node11, node5.right)
        self.assertEqual(node2, node5.parent)

        self.assertEqual(key6, node6.key)
        self.assertEqual(node12, node6.left)
        self.assertEqual(node13, node6.right)
        self.assertEqual(node3, node6.parent)

        self.assertEqual(key7, node7.key)
        self.assertEqual(node14, node7.left)
        self.assertEqual(node15, node7.right)
        self.assertEqual(node3, node7.parent)

        self.assertEqual(key8, node8.key)
        self.assertEqual(None, node8.left)
        self.assertEqual(None, node8.right)
        self.assertEqual(node4, node8.parent)

        self.assertEqual(key9, node9.key)
        self.assertEqual(None, node9.left)
        self.assertEqual(None, node9.right)
        self.assertEqual(node4, node9.parent)

        self.assertEqual(key10, node10.key)
        self.assertEqual(None, node10.left)
        self.assertEqual(None, node10.right)
        self.assertEqual(node5, node10.parent)

        self.assertEqual(key11, node11.key)
        self.assertEqual(None, node11.left)
        self.assertEqual(None, node11.right)
        self.assertEqual(node5, node11.parent)

        self.assertEqual(key12, node12.key)
        self.assertEqual(None, node12.left)
        self.assertEqual(None, node12.right)
        self.assertEqual(node6, node12.parent)

        self.assertEqual(key13, node13.key)
        self.assertEqual(None, node13.left)
        self.assertEqual(None, node13.right)
        self.assertEqual(node6, node13.parent)

        self.assertEqual(key14, node14.key)
        self.assertEqual(None, node14.left)
        self.assertEqual(None, node14.right)
        self.assertEqual(node7, node14.parent)

        self.assertEqual(key15, node15.key)
        self.assertEqual(None, node15.left)
        self.assertEqual(None, node15.right)
        self.assertEqual(node7, node15.parent)

        self.assert_binary_search_properties(node1)

    def create_complete_fifteen_node_tree(self):
        key1 = 15
        key2 = 7
        key3 = 23
        key4 = 3
        key5 = 11
        key6 = 19
        key7 = 27
        key8 = 1
        key9 = 5
        key10 = 9
        key11 = 13
        key12 = 17
        key13 = 21
        key14 = 25
        key15 = 29
        sum15 = key15
        sum14 = key14
        sum13 = key13
        sum12 = key12
        sum11 = key11
        sum10 = key10
        sum9 = key9
        sum8 = key8
        sum7 = sum14 + key7 + sum15
        sum6 = sum12 + key6 + sum13
        sum5 = sum10 + key5 + sum11
        sum4 = sum8 + key4 + sum9
        sum3 = sum6 + key3 + sum7
        sum2 = sum4 + key2 + sum5
        sum1 = sum2 + key1 + sum3
        node1 = set_range_sum.SumSplayTree.Vertex(key1,
                                                  sum1,
                                                  None,
                                                  None,
                                                  None)
        node2 = set_range_sum.SumSplayTree.Vertex(key2,
                                                  sum2,
                                                  None,
                                                  None,
                                                  node1)
        node3 = set_range_sum.SumSplayTree.Vertex(key3,
                                                  sum3,
                                                  None,
                                                  None,
                                                  node1)
        node1.left = node2
        node1.right = node3
        node4 = set_range_sum.SumSplayTree.Vertex(key4,
                                                  sum4,
                                                  None,
                                                  None,
                                                  node2)
        node5 = set_range_sum.SumSplayTree.Vertex(key5,
                                                  sum5,
                                                  None,
                                                  None,
                                                  node2)
        node2.left = node4
        node2.right = node5
        node6 = set_range_sum.SumSplayTree.Vertex(key6,
                                                  sum6,
                                                  None,
                                                  None,
                                                  node3)
        node7 = set_range_sum.SumSplayTree.Vertex(key7,
                                                  sum7,
                                                  None,
                                                  None,
                                                  node3)
        node3.left = node6
        node3.right = node7
        node8 = set_range_sum.SumSplayTree.Vertex(key8,
                                                  sum8,
                                                  None,
                                                  None,
                                                  node4)
        node9 = set_range_sum.SumSplayTree.Vertex(key9,
                                                  sum9,
                                                  None,
                                                  None,
                                                  node4)
        node4.left = node8
        node4.right = node9
        node10 = set_range_sum.SumSplayTree.Vertex(key10,
                                                   sum10,
                                                   None,
                                                   None,
                                                   node5)
        node11 = set_range_sum.SumSplayTree.Vertex(key11,
                                                   sum11,
                                                   None,
                                                   None,
                                                   node5)
        node5.left = node10
        node5.right = node11
        node12 = set_range_sum.SumSplayTree.Vertex(key12,
                                                   sum12,
                                                   None,
                                                   None,
                                                   node6)
        node13 = set_range_sum.SumSplayTree.Vertex(key13,
                                                   sum13,
                                                   None,
                                                   None,
                                                   node6)
        node6.left = node12
        node6.right = node13
        node14 = set_range_sum.SumSplayTree.Vertex(key14,
                                                   sum14,
                                                   None,
                                                   None,
                                                   node7)
        node15 = set_range_sum.SumSplayTree.Vertex(key15,
                                                   sum15,
                                                   None,
                                                   None,
                                                   node7)
        node7.left = node14
        node7.right = node15

        self.assert_original_complete_fifteen_node_tree(key1, key2, key3, key4,
                                                        key5, key6, key7, key8,
                                                        key9, key10, key11,
                                                        key12, key13, key14,
                                                        key15, node1, node2,
                                                        node3, node4, node5,
                                                        node6, node7, node8,
                                                        node9, node10, node11,
                                                        node12, node13, node14,
                                                        node15)

        self.assert_binary_search_properties(node1)

        return (key1, key2, key3, key4, key5, key6, key7, key8, key9,
                key10, key11, key12, key13, key14, key15,
                node1, node2, node3, node4, node5, node6, node7, node8, node9,
                node10, node11, node12, node13, node14, node15)

    def assert_update_root_on_one_node_tree(self, key, v):
        self.assertEqual(key, v.key)
        self.assertEqual(None, v.left)
        self.assertEqual(None, v.right)
        self.assertEqual(None, v.parent)

        self.assert_binary_search_properties(v)

    def assert_update_root_on_two_node_tree_as_left_root(self, key1, key2,
                                                         parent, left):
        self.assertEqual(key1, parent.key)
        self.assertEqual(left, parent.left)
        self.assertEqual(None, parent.right)
        self.assertEqual(None, parent.parent)

        self.assertEqual(key2, left.key)
        self.assertEqual(None, left.left)
        self.assertEqual(None, left.right)
        self.assertEqual(parent, left.parent)

        self.assert_binary_search_properties(parent)

    def assert_update_root_on_two_node_tree_as_root_right(self, key1, key2,
                                                          parent, right):
        self.assertEqual(key1, parent.key)
        self.assertEqual(None, parent.left)
        self.assertEqual(right, parent.right)
        self.assertEqual(None, parent.parent)

        self.assertEqual(key2, right.key)
        self.assertEqual(None, right.left)
        self.assertEqual(None, right.right)
        self.assertEqual(parent, right.parent)

        self.assert_binary_search_properties(parent)

    def assert_update_root_on_three_node_tree_as_left_root_right(self, key1,
                                                                 key2, key3,
                                                                 parent, left,
                                                                 right):
        self.assertEqual(key1, parent.key)
        self.assertEqual(left, parent.left)
        self.assertEqual(right, parent.right)
        self.assertEqual(None, parent.parent)

        self.assertEqual(key2, left.key)
        self.assertEqual(None, left.left)
        self.assertEqual(None, left.right)
        self.assertEqual(parent, left.parent)

        self.assertEqual(key3, right.key)
        self.assertEqual(None, right.left)
        self.assertEqual(None, right.right)
        self.assertEqual(parent, right.parent)

        self.assert_binary_search_properties(parent)

    def assert_small_rotation_on_parentless_node(self, key, v):
        self.assertEqual(key, v.key)
        self.assertEqual(None, v.left)
        self.assertEqual(None, v.right)
        self.assertEqual(None, v.parent)

        self.assert_binary_search_properties(v)

    def assert_small_rotation_on_parent_of_tree_as_left_root(self, key1, key2,
                                                             parent, left):
        self.assertEqual(key1, parent.key)
        self.assertEqual(left, parent.left)
        self.assertEqual(None, parent.right)
        self.assertEqual(None, parent.parent)

        self.assertEqual(key2, left.key)
        self.assertEqual(None, left.left)
        self.assertEqual(None, left.right)
        self.assertEqual(parent, left.parent)

        self.assert_binary_search_properties(parent)

    def asseret_small_rotation_on_left_of_tree_as_left_root(self, key1, key2,
                                                            parent, left):
        self.assertEqual(key2, left.key)
        self.assertEqual(None, left.left)
        self.assertEqual(parent, left.right)
        self.assertEqual(None, left.parent)

        self.assertEqual(key1, parent.key)
        self.assertEqual(None, parent.left)
        self.assertEqual(None, parent.right)
        self.assertEqual(left, parent.parent)

        self.assert_binary_search_properties(parent)

    def assert_small_rotation_on_parent_of_tree_as_root_right(self, key1, key2,
                                                              parent, right):
        self.assertEqual(key1, parent.key)
        self.assertEqual(None, parent.left)
        self.assertEqual(right, parent.right)
        self.assertEqual(None, parent.parent)

        self.assertEqual(key2, right.key)
        self.assertEqual(None, right.left)
        self.assertEqual(None, right.right)
        self.assertEqual(parent, right.parent)

        self.assert_binary_search_properties(parent)

    def assert_small_rotation_on_right_of_tree_as_root_right(self, key1, key2,
                                                             parent, right):
        self.assertEqual(key2, right.key)
        self.assertEqual(parent, right.left)
        self.assertEqual(None, right.right)
        self.assertEqual(None, right.parent)

        self.assertEqual(key1, parent.key)
        self.assertEqual(None, parent.left)
        self.assertEqual(None, parent.right)
        self.assertEqual(right, parent.parent)

        self.assert_binary_search_properties(parent)

    def assert_small_rotation_on_parent_of_tree_as_left_root_right(self, key1,
                                                                   key2, key3,
                                                                   parent,
                                                                   left,
                                                                   right):
        self.assertEqual(key1, parent.key)
        self.assertEqual(left, parent.left)
        self.assertEqual(right, parent.right)
        self.assertEqual(None, parent.parent)

        self.assertEqual(key2, left.key)
        self.assertEqual(None, left.left)
        self.assertEqual(None, left.right)
        self.assertEqual(parent, left.parent)

        self.assertEqual(key3, right.key)
        self.assertEqual(None, right.left)
        self.assertEqual(None, right.right)
        self.assertEqual(parent, right.parent)

        self.assert_binary_search_properties(parent)

    def assert_small_rotation_on_left_of_tree_as_left_root_right(self, key1,
                                                                 key2, key3,
                                                                 parent, left,
                                                                 right):
        self.assertEqual(key2, left.key)
        self.assertEqual(None, left.left)
        self.assertEqual(parent, left.right)
        self.assertEqual(None, left.parent)

        self.assertEqual(key1, parent.key)
        self.assertEqual(None, parent.left)
        self.assertEqual(right, parent.right)
        self.assertEqual(left, parent.parent)

        self.assertEqual(key3, right.key)
        self.assertEqual(None, right.left)
        self.assertEqual(None, right.right)
        self.assertEqual(parent, right.parent)

        self.assert_binary_search_properties(parent)

    def assert_small_rotation_on_right_of_tree_as_left_root_right(self, key1,
                                                                  key2, key3,
                                                                  parent, left,
                                                                  right):
        self.assertEqual(key3, right.key)
        self.assertEqual(parent, right.left)
        self.assertEqual(None, right.right)
        self.assertEqual(None, right.parent)

        self.assertEqual(key1, parent.key)
        self.assertEqual(left, parent.left)
        self.assertEqual(None, parent.right)
        self.assertEqual(right, parent.parent)

        self.assertEqual(key2, left.key)
        self.assertEqual(None, left.left)
        self.assertEqual(None, left.right)
        self.assertEqual(parent, left.parent)

        self.assert_binary_search_properties(parent)

    def assert_small_rotation_on_left_of_leftward_tree(self, key1, key2, key3,
                                                       key4, key5, key6, key7,
                                                       key8, key9,
                                                       grandparent,
                                                       grandparent_left,
                                                       grandparent_right, left,
                                                       right, left_left,
                                                       left_right, right_left,
                                                       right_right):
        self.assertEqual(key1, grandparent.key)
        self.assertEqual(left, grandparent.left)
        self.assertEqual(grandparent_right, grandparent.right)
        self.assertEqual(None, grandparent.parent)

        self.assertEqual(key3, grandparent_right.key)
        self.assertEqual(None, grandparent_right.left)
        self.assertEqual(None, grandparent_right.right)
        self.assertEqual(grandparent, grandparent_right.parent)

        self.assertEqual(key4, left.key)
        self.assertEqual(left_left, left.left)
        self.assertEqual(grandparent_left, left.right)
        self.assertEqual(grandparent, left.parent)

        self.assertEqual(key2, grandparent_left.key)
        self.assertEqual(left_right, grandparent_left.left)
        self.assertEqual(right, grandparent_left.right)
        self.assertEqual(left, grandparent_left.parent)

        self.assertEqual(key5, right.key)
        self.assertEqual(right_left, right.left)
        self.assertEqual(right_right, right.right)
        self.assertEqual(grandparent_left, right.parent)

        self.assertEqual(key6, left_left.key)
        self.assertEqual(None, left_left.left)
        self.assertEqual(None, left_left.right)
        self.assertEqual(left, left_left.parent)

        self.assertEqual(key7, left_right.key)
        self.assertEqual(None, left_right.left)
        self.assertEqual(None, left_right.right)
        self.assertEqual(grandparent_left, left_right.parent)

        self.assertEqual(key8, right_left.key)
        self.assertEqual(None, right_left.left)
        self.assertEqual(None, right_left.right)
        self.assertEqual(right, right_left.parent)

        self.assertEqual(key9, right_right.key)
        self.assertEqual(None, right_right.left)
        self.assertEqual(None, right_right.right)
        self.assertEqual(right, right_right.parent)

        self.assert_binary_search_properties(grandparent)

    def assert_small_rotation_on_right_of_leftward_tree(self, key1, key2, key3,
                                                        key4, key5, key6, key7,
                                                        key8, key9,
                                                        grandparent,
                                                        grandparent_left,
                                                        grandparent_right,
                                                        left, right, left_left,
                                                        left_right, right_left,
                                                        right_right):
        self.assertEqual(key1, grandparent.key)
        self.assertEqual(right, grandparent.left)
        self.assertEqual(grandparent_right, grandparent.right)
        self.assertEqual(None, grandparent.parent)

        self.assertEqual(key3, grandparent_right.key)
        self.assertEqual(None, grandparent_right.left)
        self.assertEqual(None, grandparent_right.right)
        self.assertEqual(grandparent, grandparent_right.parent)

        self.assertEqual(key5, right.key)
        self.assertEqual(grandparent_left, right.left)
        self.assertEqual(right_right, right.right)
        self.assertEqual(grandparent, right.parent)

        self.assertEqual(key2, grandparent_left.key)
        self.assertEqual(left, grandparent_left.left)
        self.assertEqual(right_left, grandparent_left.right)
        self.assertEqual(right, grandparent_left.parent)

        self.assertEqual(key4, left.key)
        self.assertEqual(left_left, left.left)
        self.assertEqual(left_right, left.right)
        self.assertEqual(grandparent_left, left.parent)

        self.assertEqual(key6, left_left.key)
        self.assertEqual(None, left_left.left)
        self.assertEqual(None, left_left.right)
        self.assertEqual(left, left_left.parent)

        self.assertEqual(key7, left_right.key)
        self.assertEqual(None, left_right.left)
        self.assertEqual(None, left_right.right)
        self.assertEqual(left, left_right.parent)

        self.assertEqual(key8, right_left.key)
        self.assertEqual(None, right_left.left)
        self.assertEqual(None, right_left.right)
        self.assertEqual(grandparent_left, right_left.parent)

        self.assertEqual(key9, right_right.key)
        self.assertEqual(None, right_right.left)
        self.assertEqual(None, right_right.right)
        self.assertEqual(right, right_right.parent)

        self.assert_binary_search_properties(grandparent)

    def assert_small_rotation_on_left_of_rightward_tree(self, key1, key2, key3,
                                                        key4, key5, key6, key7,
                                                        key8, key9,
                                                        grandparent,
                                                        grandparent_left,
                                                        grandparent_right,
                                                        left, right, left_left,
                                                        left_right, right_left,
                                                        right_right):
        self.assertEqual(key1, grandparent.key)
        self.assertEqual(grandparent_left, grandparent.left)
        self.assertEqual(left, grandparent.right)
        self.assertEqual(None, grandparent.parent)

        self.assertEqual(key2, grandparent_left.key)
        self.assertEqual(None, grandparent_left.left)
        self.assertEqual(None, grandparent_left.right)
        self.assertEqual(grandparent, grandparent_left.parent)

        self.assertEqual(key4, left.key)
        self.assertEqual(left_left, left.left)
        self.assertEqual(grandparent_right, left.right)
        self.assertEqual(grandparent, left.parent)

        self.assertEqual(key3, grandparent_right.key)
        self.assertEqual(left_right, grandparent_right.left)
        self.assertEqual(right, grandparent_right.right)
        self.assertEqual(left, grandparent_right.parent)

        self.assertEqual(key5, right.key)
        self.assertEqual(right_left, right.left)
        self.assertEqual(right_right, right.right)
        self.assertEqual(grandparent_right, right.parent)

        self.assertEqual(key6, left_left.key)
        self.assertEqual(None, left_left.left)
        self.assertEqual(None, left_left.right)
        self.assertEqual(left, left_left.parent)

        self.assertEqual(key7, left_right.key)
        self.assertEqual(None, left_right.left)
        self.assertEqual(None, left_right.right)
        self.assertEqual(grandparent_right, left_right.parent)

        self.assertEqual(key8, right_left.key)
        self.assertEqual(None, right_left.left)
        self.assertEqual(None, right_left.right)
        self.assertEqual(right, right_left.parent)

        self.assertEqual(key9, right_right.key)
        self.assertEqual(None, right_right.left)
        self.assertEqual(None, right_right.right)
        self.assertEqual(right, right_right.parent)

        self.assert_binary_search_properties(grandparent)

    def assert_small_rotation_on_right_of_rightward_tree(self, key1, key2,
                                                         key3, key4, key5,
                                                         key6, key7, key8,
                                                         key9, grandparent,
                                                         grandparent_left,
                                                         grandparent_right,
                                                         left, right,
                                                         left_left, left_right,
                                                         right_left,
                                                         right_right):
        self.assertEqual(key1, grandparent.key)
        self.assertEqual(grandparent_left, grandparent.left)
        self.assertEqual(right, grandparent.right)
        self.assertEqual(None, grandparent.parent)

        self.assertEqual(key2, grandparent_left.key)
        self.assertEqual(None, grandparent_left.left)
        self.assertEqual(None, grandparent_left.right)
        self.assertEqual(grandparent, grandparent_left.parent)

        self.assertEqual(key5, right.key)
        self.assertEqual(grandparent_right, right.left)
        self.assertEqual(right_right, right.right)
        self.assertEqual(grandparent, right.parent)

        self.assertEqual(key3, grandparent_right.key)
        self.assertEqual(left, grandparent_right.left)
        self.assertEqual(right_left, grandparent_right.right)
        self.assertEqual(right, grandparent_right.parent)

        self.assertEqual(key4, left.key)
        self.assertEqual(left_left, left.left)
        self.assertEqual(left_right, left.right)
        self.assertEqual(grandparent_right, left.parent)

        self.assertEqual(key6, left_left.key)
        self.assertEqual(None, left_left.left)
        self.assertEqual(None, left_left.right)
        self.assertEqual(left, left_left.parent)

        self.assertEqual(key7, left_right.key)
        self.assertEqual(None, left_right.left)
        self.assertEqual(None, left_right.right)
        self.assertEqual(left, left_right.parent)

        self.assertEqual(key8, right_left.key)
        self.assertEqual(None, right_left.left)
        self.assertEqual(None, right_left.right)
        self.assertEqual(grandparent_right, right_left.parent)

        self.assertEqual(key9, right_right.key)
        self.assertEqual(None, right_right.left)
        self.assertEqual(None, right_right.right)
        self.assertEqual(right, right_right.parent)

        self.assert_binary_search_properties(grandparent)

    def assert_big_rotation_on_left_of_leftward_tree(self, key1, key2, key3,
                                                     key4, key5, key6, key7,
                                                     key8, key9, grandparent,
                                                     grandparent_left,
                                                     grandparent_right, left,
                                                     right, left_left,
                                                     left_right, right_left,
                                                     right_right):
        self.assertEqual(key4, left.key)
        self.assertEqual(left_left, left.left)
        self.assertEqual(grandparent_left, left.right)
        self.assertEqual(None, left.parent)

        self.assertEqual(key2, grandparent_left.key)
        self.assertEqual(left_right, grandparent_left.left)
        self.assertEqual(grandparent, grandparent_left.right)
        self.assertEqual(left, grandparent_left.parent)

        self.assertEqual(key1, grandparent.key)
        self.assertEqual(right, grandparent.left)
        self.assertEqual(grandparent_right, grandparent.right)
        self.assertEqual(grandparent_left, grandparent.parent)

        self.assertEqual(key5, right.key)
        self.assertEqual(right_left, right.left)
        self.assertEqual(right_right, right.right)
        self.assertEqual(grandparent, right.parent)

        self.assertEqual(key3, grandparent_right.key)
        self.assertEqual(None, grandparent_right.left)
        self.assertEqual(None, grandparent_right.right)
        self.assertEqual(grandparent, grandparent_right.parent)

        self.assertEqual(key6, left_left.key)
        self.assertEqual(None, left_left.left)
        self.assertEqual(None, left_left.right)
        self.assertEqual(left, left_left.parent)

        self.assertEqual(key7, left_right.key)
        self.assertEqual(None, left_right.left)
        self.assertEqual(None, left_right.right)
        self.assertEqual(grandparent_left, left_right.parent)

        self.assertEqual(key8, right_left.key)
        self.assertEqual(None, right_left.left)
        self.assertEqual(None, right_left.right)
        self.assertEqual(right, right_left.parent)

        self.assertEqual(key9, right_right.key)
        self.assertEqual(None, right_right.left)
        self.assertEqual(None, right_right.right)
        self.assertEqual(right, right_right.parent)

        self.assert_binary_search_properties(grandparent)

    def assert_big_rotation_on_right_of_leftward_tree(self, key1, key2, key3,
                                                      key4, key5, key6, key7,
                                                      key8, key9, grandparent,
                                                      grandparent_left,
                                                      grandparent_right, left,
                                                      right, left_left,
                                                      left_right, right_left,
                                                      right_right):
        self.assertEqual(key5, right.key)
        self.assertEqual(grandparent_left, right.left)
        self.assertEqual(grandparent, right.right)
        self.assertEqual(None, right.parent)

        self.assertEqual(key2, grandparent_left.key)
        self.assertEqual(left, grandparent_left.left)
        self.assertEqual(right_left, grandparent_left.right)
        self.assertEqual(right, grandparent_left.parent)

        self.assertEqual(key1, grandparent.key)
        self.assertEqual(right_right, grandparent.left)
        self.assertEqual(grandparent_right, grandparent.right)
        self.assertEqual(right, grandparent.parent)

        self.assertEqual(key3, grandparent_right.key)
        self.assertEqual(None, grandparent_right.left)
        self.assertEqual(None, grandparent_right.right)
        self.assertEqual(grandparent, grandparent_right.parent)

        self.assertEqual(key4, left.key)
        self.assertEqual(left_left, left.left)
        self.assertEqual(left_right, left.right)
        self.assertEqual(grandparent_left, left.parent)

        self.assertEqual(key6, left_left.key)
        self.assertEqual(None, left_left.left)
        self.assertEqual(None, left_left.right)
        self.assertEqual(left, left_left.parent)

        self.assertEqual(key7, left_right.key)
        self.assertEqual(None, left_right.left)
        self.assertEqual(None, left_right.right)
        self.assertEqual(left, left_right.parent)

        self.assertEqual(key8, right_left.key)
        self.assertEqual(None, right_left.left)
        self.assertEqual(None, right_left.right)
        self.assertEqual(grandparent_left, right_left.parent)

        self.assertEqual(key9, right_right.key)
        self.assertEqual(None, right_right.left)
        self.assertEqual(None, right_right.right)
        self.assertEqual(grandparent, right_right.parent)

        self.assert_binary_search_properties(grandparent)

    def assert_big_rotation_on_left_of_rightward_tree(self, key1, key2, key3,
                                                      key4, key5, key6, key7,
                                                      key8, key9, grandparent,
                                                      grandparent_left,
                                                      grandparent_right, left,
                                                      right, left_left,
                                                      left_right, right_left,
                                                      right_right):
        self.assertEqual(key4, left.key)
        self.assertEqual(grandparent, left.left)
        self.assertEqual(grandparent_right, left.right)
        self.assertEqual(None, left.parent)

        self.assertEqual(key1, grandparent.key)
        self.assertEqual(grandparent_left, grandparent.left)
        self.assertEqual(left_left, grandparent.right)
        self.assertEqual(left, grandparent.parent)

        self.assertEqual(key2, grandparent_left.key)
        self.assertEqual(None, grandparent_left.left)
        self.assertEqual(None, grandparent_left.right)
        self.assertEqual(grandparent, grandparent_left.parent)

        self.assertEqual(key3, grandparent_right.key)
        self.assertEqual(left_right, grandparent_right.left)
        self.assertEqual(right, grandparent_right.right)
        self.assertEqual(left, grandparent_right.parent)

        self.assertEqual(key5, right.key)
        self.assertEqual(right_left, right.left)
        self.assertEqual(right_right, right.right)
        self.assertEqual(grandparent_right, right.parent)

        self.assertEqual(key6, left_left.key)
        self.assertEqual(None, left_left.left)
        self.assertEqual(None, left_left.right)
        self.assertEqual(grandparent, left_left.parent)

        self.assertEqual(key7, left_right.key)
        self.assertEqual(None, left_right.left)
        self.assertEqual(None, left_right.right)
        self.assertEqual(grandparent_right, left_right.parent)

        self.assertEqual(key8, right_left.key)
        self.assertEqual(None, right_left.left)
        self.assertEqual(None, right_left.right)
        self.assertEqual(right, right_left.parent)

        self.assertEqual(key9, right_right.key)
        self.assertEqual(None, right_right.left)
        self.assertEqual(None, right_right.right)
        self.assertEqual(right, right_right.parent)

        self.assert_binary_search_properties(grandparent)

    def assert_big_rotation_on_right_of_rightward_tree(self, key1, key2, key3,
                                                       key4, key5, key6, key7,
                                                       key8, key9, grandparent,
                                                       grandparent_left,
                                                       grandparent_right, left,
                                                       right, left_left,
                                                       left_right, right_left,
                                                       right_right):
        self.assertEqual(key5, right.key)
        self.assertEqual(grandparent_right, right.left)
        self.assertEqual(right_right, right.right)
        self.assertEqual(None, right.parent)

        self.assertEqual(key3, grandparent_right.key)
        self.assertEqual(grandparent, grandparent_right.left)
        self.assertEqual(right_left, grandparent_right.right)
        self.assertEqual(right, grandparent_right.parent)

        self.assertEqual(key1, grandparent.key)
        self.assertEqual(grandparent_left, grandparent.left)
        self.assertEqual(left, grandparent.right)
        self.assertEqual(grandparent_right, grandparent.parent)

        self.assertEqual(key2, grandparent_left.key)
        self.assertEqual(None, grandparent_left.left)
        self.assertEqual(None, grandparent_left.right)
        self.assertEqual(grandparent, grandparent_left.parent)

        self.assertEqual(key4, left.key)
        self.assertEqual(left_left, left.left)
        self.assertEqual(left_right, left.right)
        self.assertEqual(grandparent, left.parent)

        self.assertEqual(key6, left_left.key)
        self.assertEqual(None, left_left.left)
        self.assertEqual(None, left_left.right)
        self.assertEqual(left, left_left.parent)

        self.assertEqual(key7, left_right.key)
        self.assertEqual(None, left_right.left)
        self.assertEqual(None, left_right.right)
        self.assertEqual(left, left_right.parent)

        self.assertEqual(key8, right_left.key)
        self.assertEqual(None, right_left.left)
        self.assertEqual(None, right_left.right)
        self.assertEqual(grandparent_right, right_left.parent)

        self.assertEqual(key9, right_right.key)
        self.assertEqual(None, right_right.left)
        self.assertEqual(None, right_right.right)
        self.assertEqual(right, right_right.parent)

        self.assert_binary_search_properties(grandparent)

    def test_update_none(self):
        self.tree._update(None)

    def test_update_root_on_one_node_tree(self):
        key, v = self.create_one_node_tree()

        self.tree._update(v)

        self.assert_update_root_on_one_node_tree(key, v)

    def test_update_root_on_two_node_tree_as_left_root(self):
        key1, key2, parent, left = self.create_two_node_tree_as_left_root()

        self.tree._update(parent)

        self.assert_update_root_on_two_node_tree_as_left_root(key1, key2,
                                                              parent, left)

    def test_update_root_on_two_node_tree_as_parentless_left_root(self):
        key1, key2, parent, left = self.create_two_node_tree_as_left_root()
        left.parent = None

        self.tree._update(parent)

        self.assert_update_root_on_two_node_tree_as_left_root(key1, key2,
                                                              parent, left)

    def test_update_root_on_two_node_tree_as_root_right(self):
        key1, key2, parent, right = self.create_two_node_tree_as_root_right()

        self.tree._update(parent)

        self.assert_update_root_on_two_node_tree_as_root_right(key1, key2,
                                                               parent, right)

    def test_update_root_on_two_node_tree_as_parentless_root_right(self):
        key1, key2, parent, right = self.create_two_node_tree_as_root_right()
        right.parent = None

        self.tree._update(parent)

        self.assert_update_root_on_two_node_tree_as_root_right(
            key1, key2, parent, right)

    def test_update_root_on_three_node_tree_as_left_root_right(self):
        key1, key2, key3, parent, left, right = \
                                self.create_three_node_tree_as_left_root_right()

        self.tree._update(parent)

        self.assert_update_root_on_three_node_tree_as_left_root_right(key1,
                                                                      key2,
                                                                      key3,
                                                                      parent,
                                                                      left,
                                                                      right)

    def test_update_root_on_three_node_tree_as_root_parentless_children(self):
        key1, key2, key3, parent, left, right = \
                                self.create_three_node_tree_as_left_root_right()
        left.parent = None
        right.parent = None

        self.tree._update(parent)

        self.assert_update_root_on_three_node_tree_as_left_root_right(key1,
                                                                      key2,
                                                                      key3,
                                                                      parent,
                                                                      left,
                                                                      right)

    def test_small_rotation_on_parentless_node(self):
        key, v = self.create_one_node_tree()

        self.tree._small_rotation(v)

        self.assert_small_rotation_on_parentless_node(key, v)

    def test_small_rotation_on_parent_of_tree_as_left_root(self):
        key1, key2, parent, left = self.create_two_node_tree_as_left_root()

        self.tree._small_rotation(parent)

        self.assert_small_rotation_on_parent_of_tree_as_left_root(key1, key2,
                                                                  parent, left)

    def test_small_rotation_on_left_of_tree_as_left_root(self):
        key1, key2, parent, left = self.create_two_node_tree_as_left_root()

        self.tree._small_rotation(left)

        self.asseret_small_rotation_on_left_of_tree_as_left_root(key1, key2,
                                                                 parent, left)

    def test_small_rotation_on_parent_of_tree_as_root_right(self):
        key1, key2, parent, right = self.create_two_node_tree_as_root_right()

        self.tree._small_rotation(parent)

        self.assert_small_rotation_on_parent_of_tree_as_root_right(key1, key2,
                                                                   parent,
                                                                   right)

    def test_small_rotation_on_right_of_tree_as_root_right(self):
        key1, key2, parent, right = self.create_two_node_tree_as_root_right()

        self.tree._small_rotation(right)

        self.assert_small_rotation_on_right_of_tree_as_root_right(key1, key2,
                                                                  parent,
                                                                  right)

    def test_small_rotation_on_parent_of_tree_as_left_root_right(self):
        key1, key2, key3, parent, left, right = \
                                self.create_three_node_tree_as_left_root_right()

        self.tree._small_rotation(parent)

        self.assert_small_rotation_on_parent_of_tree_as_left_root_right(key1,
                                                                        key2,
                                                                        key3,
                                                                        parent,
                                                                        left,
                                                                        right)

    def test_small_rotation_on_left_of_tree_as_left_root_right(self):
        key1, key2, key3, parent, left, right = \
                                self.create_three_node_tree_as_left_root_right()

        self.tree._small_rotation(left)

        self.assert_small_rotation_on_left_of_tree_as_left_root_right(key1,
                                                                      key2,
                                                                      key3,
                                                                      parent,
                                                                      left,
                                                                      right)

    def test_small_rotation_on_right_of_tree_as_left_root_right(self):
        key1, key2, key3, parent, left, right = \
                                self.create_three_node_tree_as_left_root_right()

        self.tree._small_rotation(right)

        self.assert_small_rotation_on_right_of_tree_as_left_root_right(key1,
                                                                       key2,
                                                                       key3,
                                                                       parent,
                                                                       left,
                                                                       right)

    def test_small_rotation_on_left_of_leftward_tree(self):
        (key1, key2, key3, key4, key5, key6, key7, key8, key9,
         grandparent, grandparent_left, grandparent_right, left, right,
         left_left, left_right, right_left, right_right) = \
                                  self.create_nine_node_tree_with_left_subtree()

        self.tree._small_rotation(left)

        self.assert_small_rotation_on_left_of_leftward_tree(key1, key2, key3,
                                                            key4, key5, key6,
                                                            key7, key8, key9,
                                                            grandparent,
                                                            grandparent_left,
                                                            grandparent_right,
                                                            left, right,
                                                            left_left,
                                                            left_right,
                                                            right_left,
                                                            right_right)

    def test_small_rotation_on_right_of_leftward_tree(self):
        (key1, key2, key3, key4, key5, key6, key7, key8, key9,
         grandparent, grandparent_left, grandparent_right, left, right,
         left_left, left_right, right_left, right_right) = \
                                  self.create_nine_node_tree_with_left_subtree()

        self.tree._small_rotation(right)

        self.assert_small_rotation_on_right_of_leftward_tree(key1, key2, key3,
                                                             key4, key5, key6,
                                                             key7, key8, key9,
                                                             grandparent,
                                                             grandparent_left,
                                                             grandparent_right,
                                                             left, right,
                                                             left_left,
                                                             left_right,
                                                             right_left,
                                                             right_right)

    def test_small_rotation_on_left_of_rightward_tree(self):
        (key1, key2, key3, key4, key5, key6, key7, key8, key9,
         grandparent, grandparent_left, grandparent_right, left, right,
         left_left, left_right, right_left, right_right) = \
                                 self.create_nine_node_tree_with_right_subtree()

        self.tree._small_rotation(left)

        self.assert_small_rotation_on_left_of_rightward_tree(key1, key2, key3,
                                                             key4, key5, key6,
                                                             key7, key8, key9,
                                                             grandparent,
                                                             grandparent_left,
                                                             grandparent_right,
                                                             left, right,
                                                             left_left,
                                                             left_right,
                                                             right_left,
                                                             right_right)

    def test_small_rotation_on_right_of_rightward_tree(self):
        (key1, key2, key3, key4, key5, key6, key7, key8, key9,
         grandparent, grandparent_left, grandparent_right, left, right,
         left_left, left_right, right_left, right_right) = \
                                 self.create_nine_node_tree_with_right_subtree()

        self.tree._small_rotation(right)

        self.assert_small_rotation_on_right_of_rightward_tree(
                           key1, key2, key3, key4, key5, key6, key7, key8, key9,
                           grandparent, grandparent_left, grandparent_right,
                           left, right,  left_left, left_right, right_left,
                           right_right)

    def test_big_rotation_on_left_of_leftward_tree(self):
        (key1, key2, key3, key4, key5, key6, key7, key8, key9,
         grandparent, grandparent_left, grandparent_right, left, right,
         left_left, left_right, right_left, right_right) = \
                                  self.create_nine_node_tree_with_left_subtree()

        self.tree._big_rotation(left)

        self.assert_big_rotation_on_left_of_leftward_tree(key1, key2, key3,
                                                          key4, key5, key6,
                                                          key7, key8, key9,
                                                          grandparent,
                                                          grandparent_left,
                                                          grandparent_right,
                                                          left, right,
                                                          left_left,
                                                          left_right,
                                                          right_left,
                                                          right_right)

    def test_big_rotation_on_right_of_leftward_tree(self):
        (key1, key2, key3, key4, key5, key6, key7, key8, key9,
         grandparent, grandparent_left, grandparent_right, left, right,
         left_left, left_right, right_left, right_right) = \
                                  self.create_nine_node_tree_with_left_subtree()

        self.tree._big_rotation(right)

        self.assert_big_rotation_on_right_of_leftward_tree(key1, key2, key3,
                                                           key4, key5, key6,
                                                           key7, key8, key9,
                                                           grandparent,
                                                           grandparent_left,
                                                           grandparent_right,
                                                           left, right,
                                                           left_left,
                                                           left_right,
                                                           right_left,
                                                           right_right)

    def test_big_rotation_on_left_of_rightward_tree(self):
        (key1, key2, key3, key4, key5, key6, key7, key8, key9,
         grandparent, grandparent_left, grandparent_right, left, right,
         left_left, left_right, right_left, right_right) = \
                                 self.create_nine_node_tree_with_right_subtree()

        self.tree._big_rotation(left)

        self.assert_big_rotation_on_left_of_rightward_tree(key1, key2, key3,
                                                           key4, key5, key6,
                                                           key7, key8, key9,
                                                           grandparent,
                                                           grandparent_left,
                                                           grandparent_right,
                                                           left, right,
                                                           left_left,
                                                           left_right,
                                                           right_left,
                                                           right_right)

    def test_big_rotation_on_right_of_rightward_tree(self):
        (key1, key2, key3, key4, key5, key6, key7, key8, key9,
         grandparent, grandparent_left, grandparent_right, left, right,
         left_left, left_right, right_left, right_right) = \
                                 self.create_nine_node_tree_with_right_subtree()

        self.tree._big_rotation(right)

        self.assert_big_rotation_on_right_of_rightward_tree(key1, key2, key3,
                                                            key4, key5, key6,
                                                            key7, key8, key9,
                                                            grandparent,
                                                            grandparent_left,
                                                            grandparent_right,
                                                            left, right,
                                                            left_left,
                                                            left_right,
                                                            right_left,
                                                            right_right)

    def test_splay_none(self):
        v = self.tree.splay(None)

        self.assertEqual(None, v)

    def test_splay_on_parentless_node(self):
        key, v = self.create_one_node_tree()

        result = self.tree.splay(v)

        self.assertEqual(v, result)
        self.assert_small_rotation_on_parentless_node(key, v)

    def test_splay_on_parent_of_tree_as_left_root(self):
        key1, key2, parent, left = self.create_two_node_tree_as_left_root()

        result = self.tree.splay(parent)

        self.assertEqual(parent, result)
        self.assert_small_rotation_on_parent_of_tree_as_left_root(key1, key2,
                                                                  parent, left)

    def test_splay_on_left_of_tree_as_left_root(self):
        key1, key2, parent, left = self.create_two_node_tree_as_left_root()

        result = self.tree.splay(left)

        self.assertEqual(left, result)
        self.asseret_small_rotation_on_left_of_tree_as_left_root(key1, key2,
                                                                 parent, left)

    def test_splay_on_parent_of_tree_as_root_right(self):
        key1, key2, parent, right = self.create_two_node_tree_as_root_right()

        result = self.tree.splay(parent)

        self.assertEqual(parent, result)
        self.assert_small_rotation_on_parent_of_tree_as_root_right(key1, key2,
                                                                   parent,
                                                                   right)

    def test_splay_on_right_of_tree_as_root_right(self):
        key1, key2, parent, right = self.create_two_node_tree_as_root_right()

        result = self.tree.splay(right)

        self.assertEqual(right, result)
        self.assert_small_rotation_on_right_of_tree_as_root_right(key1, key2,
                                                                  parent,
                                                                  right)

    def test_splay_on_parent_of_tree_as_left_root_right(self):
        key1, key2, key3, parent, left, right = \
                                self.create_three_node_tree_as_left_root_right()

        result = self.tree.splay(parent)

        self.assertEqual(parent, result)
        self.assert_small_rotation_on_parent_of_tree_as_left_root_right(key1,
                                                                        key2,
                                                                        key3,
                                                                        parent,
                                                                        left,
                                                                        right)

    def test_splay_on_left_of_tree_as_left_root_right(self):
        key1, key2, key3, parent, left, right = \
                                self.create_three_node_tree_as_left_root_right()

        result = self.tree.splay(left)

        self.assertEqual(left, result)
        self.assert_small_rotation_on_left_of_tree_as_left_root_right(key1,
                                                                      key2,
                                                                      key3,
                                                                      parent,
                                                                      left,
                                                                      right)

    def test_splay_on_right_of_tree_as_left_root_right(self):
        key1, key2, key3, parent, left, right = \
                                self.create_three_node_tree_as_left_root_right()

        result = self.tree.splay(right)

        self.assertEqual(right, result)
        self.assert_small_rotation_on_right_of_tree_as_left_root_right(key1,
                                                                       key2,
                                                                       key3,
                                                                       parent,
                                                                       left,
                                                                       right)

    def test_splay_on_left_of_leftward_tree(self):
        (key1, key2, key3, key4, key5, key6, key7, key8, key9,
         grandparent, grandparent_left, grandparent_right, left, right,
         left_left, left_right, right_left, right_right) = \
                                  self.create_nine_node_tree_with_left_subtree()

        result = self.tree.splay(left)

        self.assertEqual(left, result)
        self.assert_small_rotation_on_left_of_leftward_tree(key1, key2, key3,
                                                            key4, key5, key6,
                                                            key7, key8, key9,
                                                            grandparent,
                                                            grandparent_left,
                                                            grandparent_right,
                                                            left, right,
                                                            left_left,
                                                            left_right,
                                                            right_left,
                                                            right_right)

    def test_splay_on_right_of_leftward_tree(self):
        (key1, key2, key3, key4, key5, key6, key7, key8, key9,
         grandparent, grandparent_left, grandparent_right, left, right,
         left_left, left_right, right_left, right_right) = \
                                  self.create_nine_node_tree_with_left_subtree()

        result = self.tree.splay(right)

        self.assertEqual(right, result)
        self.assert_small_rotation_on_right_of_leftward_tree(key1, key2, key3,
                                                             key4, key5, key6,
                                                             key7, key8, key9,
                                                             grandparent,
                                                             grandparent_left,
                                                             grandparent_right,
                                                             left, right,
                                                             left_left,
                                                             left_right,
                                                             right_left,
                                                             right_right)

    def test_splay_on_left_of_rightward_tree(self):
        (key1, key2, key3, key4, key5, key6, key7, key8, key9,
         grandparent, grandparent_left, grandparent_right, left, right,
         left_left, left_right, right_left, right_right) = \
                                 self.create_nine_node_tree_with_right_subtree()

        result = self.tree.splay(left)

        self.assertEqual(left, result)
        self.assert_small_rotation_on_left_of_rightward_tree(key1, key2, key3,
                                                             key4, key5, key6,
                                                             key7, key8, key9,
                                                             grandparent,
                                                             grandparent_left,
                                                             grandparent_right,
                                                             left, right,
                                                             left_left,
                                                             left_right,
                                                             right_left,
                                                             right_right)

    def test_splay_on_right_of_rightward_tree(self):
        (key1, key2, key3, key4, key5, key6, key7, key8, key9,
         grandparent, grandparent_left, grandparent_right, left, right,
         left_left, left_right, right_left, right_right) = \
                                 self.create_nine_node_tree_with_right_subtree()

        result = self.tree.splay(right)

        self.assertEqual(right, result)
        self.assert_small_rotation_on_right_of_rightward_tree(
                          key1, key2, key3, key4, key5, key6, key7, key8, key9,
                          grandparent, grandparent_left, grandparent_right,
                          left, right, left_left, left_right, right_left,
                          right_right)

    def test_splay_on_left_of_leftward_tree(self):
        (key1, key2, key3, key4, key5, key6, key7, key8, key9,
         grandparent, grandparent_left, grandparent_right, left, right,
         left_left, left_right, right_left, right_right) = \
                                  self.create_nine_node_tree_with_left_subtree()

        result = self.tree.splay(left)

        self.assertEqual(left, result)
        self.assert_big_rotation_on_left_of_leftward_tree(key1, key2, key3,
                                                          key4, key5, key6,
                                                          key7, key8, key9,
                                                          grandparent,
                                                          grandparent_left,
                                                          grandparent_right,
                                                          left, right,
                                                          left_left,
                                                          left_right,
                                                          right_left,
                                                          right_right)

    def test_splay_on_right_of_leftward_tree(self):
        (key1, key2, key3, key4, key5, key6, key7, key8, key9,
         grandparent, grandparent_left, grandparent_right, left, right,
         left_left, left_right, right_left, right_right) = \
                                  self.create_nine_node_tree_with_left_subtree()

        result = self.tree.splay(right)

        self.assertEqual(right, result)
        self.assert_big_rotation_on_right_of_leftward_tree(key1, key2, key3,
                                                           key4, key5, key6,
                                                           key7, key8, key9,
                                                           grandparent,
                                                           grandparent_left,
                                                           grandparent_right,
                                                           left, right,
                                                           left_left,
                                                           left_right,
                                                           right_left,
                                                           right_right)

    def test_splay_on_left_of_rightward_tree(self):
        (key1, key2, key3, key4, key5, key6, key7, key8, key9,
         grandparent, grandparent_left, grandparent_right, left, right,
         left_left, left_right, right_left, right_right) = \
                                 self.create_nine_node_tree_with_right_subtree()

        result = self.tree.splay(left)

        self.assertEqual(left, result)
        self.assert_big_rotation_on_left_of_rightward_tree(
                        key1, key2, key3, key4, key5, key6, key7, key8, key9,
                        grandparent, grandparent_left, grandparent_right, left,
                        right, left_left, left_right, right_left, right_right)

    def test_splay_on_right_of_rightward_tree(self):
        (key1, key2, key3, key4, key5, key6, key7, key8, key9,
         grandparent, grandparent_left, grandparent_right, left, right,
         left_left, left_right, right_left, right_right) = \
                                 self.create_nine_node_tree_with_right_subtree()

        result = self.tree.splay(right)

        self.assertEqual(right, result)
        self.assert_big_rotation_on_right_of_rightward_tree(
                 key1, key2, key3, key4, key5, key6, key7, key8, key9,
                 grandparent, grandparent_left, grandparent_right, left, right,
                 left_left, left_right, right_left, right_right)

    def test_find_with_none_and_key(self):
        root = None
        search_key = 1

        node, root = self.tree.find(root, search_key)

        self.assertEqual(None, node)
        self.assertEqual(None, root)

    def test_find_on_parentless_node_with_existing_key(self):
        key, v = self.create_one_node_tree()

        root = v
        search_key = key

        node, root = self.tree.find(root, search_key)

        self.assertEqual(v, node)
        self.assertEqual(v, root)
        self.assertEqual(search_key, node.key)

        self.assertEqual(key, v.key)
        self.assertEqual(None, v.left)
        self.assertEqual(None, v.right)
        self.assertEqual(None, v.parent)

        self.assert_binary_search_properties(root)

    def test_find_on_parentless_node_with_missing_key_as_lesser(self):
        key, v = self.create_one_node_tree()

        root = v
        search_key = key - 1

        node, root = self.tree.find(root, search_key)

        self.assertEqual(v, node)
        self.assertEqual(v, root)
        self.assertTrue(search_key < node.key)

        self.assertEqual(key, v.key)
        self.assertEqual(None, v.left)
        self.assertEqual(None, v.right)
        self.assertEqual(None, v.parent)

        self.assert_binary_search_properties(root)

    def test_find_on_parentless_node_with_missing_key_as_larger(self):
        key, v = self.create_one_node_tree()

        root = v
        search_key = key + 1

        node, root = self.tree.find(root, search_key)

        self.assertEqual(None, node)
        self.assertEqual(v, root)

        self.assertEqual(key, v.key)
        self.assertEqual(None, v.left)
        self.assertEqual(None, v.right)
        self.assertEqual(None, v.parent)

        self.assert_binary_search_properties(root)

    def test_find_on_fifteen_node_tree_with_greater_than_key15(self):
        (key1, key2, key3, key4, key5, key6, key7, key8, key9,
         key10, key11, key12, key13, key14, key15,
         node1, node2, node3, node4, node5, node6, node7, node8, node9,
         node10, node11, node12, node13, node14, node15) = \
                                        self.create_complete_fifteen_node_tree()

        root = node1
        search_key = key15 + 1

        node, root = self.tree.find(root, search_key)

        self.assertEqual(None, node)
        self.assertEqual(node15, root)

        self.assertEqual(key15, node15.key)
        self.assertEqual(node1, node15.left)
        self.assertEqual(None, node15.right)
        self.assertEqual(None, node15.parent)

        self.assertEqual(key1, node1.key)
        self.assertEqual(node2, node1.left)
        self.assertEqual(node7, node1.right)
        self.assertEqual(None, node15.parent)

        self.assertEqual(key2, node2.key)
        self.assertEqual(node4, node2.left)
        self.assertEqual(node5, node2.right)
        self.assertEqual(node1, node2.parent)

        self.assertEqual(key7, node7.key)
        self.assertEqual(node3, node7.left)
        self.assertEqual(None, node7.right)
        self.assertEqual(node1, node7.parent)

        self.assertEqual(key4, node4.key)
        self.assertEqual(node8, node4.left)
        self.assertEqual(node9, node4.right)
        self.assertEqual(node2, node4.parent)

        self.assertEqual(key5, node5.key)
        self.assertEqual(node10, node5.left)
        self.assertEqual(node11, node5.right)
        self.assertEqual(node2, node5.parent)

        self.assertEqual(key3, node3.key)
        self.assertEqual(node6, node3.left)
        self.assertEqual(node14, node3.right)
        self.assertEqual(node7, node3.parent)

        self.assertEqual(key8, node8.key)
        self.assertEqual(None, node8.left)
        self.assertEqual(None, node8.right)
        self.assertEqual(node4, node8.parent)

        self.assertEqual(key9, node9.key)
        self.assertEqual(None, node9.left)
        self.assertEqual(None, node9.right)
        self.assertEqual(node4, node9.parent)

        self.assertEqual(key10, node10.key)
        self.assertEqual(None, node10.left)
        self.assertEqual(None, node10.right)
        self.assertEqual(node5, node10.parent)

        self.assertEqual(key11, node11.key)
        self.assertEqual(None, node11.left)
        self.assertEqual(None, node11.right)
        self.assertEqual(node5, node11.parent)

        self.assertEqual(key6, node6.key)
        self.assertEqual(node12, node6.left)
        self.assertEqual(node13, node6.right)
        self.assertEqual(node3, node6.parent)

        self.assertEqual(key14, node14.key)
        self.assertEqual(None, node14.left)
        self.assertEqual(None, node14.right)
        self.assertEqual(node3, node14.parent)

        self.assertEqual(key12, node12.key)
        self.assertEqual(None, node12.left)
        self.assertEqual(None, node12.right)
        self.assertEqual(node6, node12.parent)

        self.assertEqual(key13, node13.key)
        self.assertEqual(None, node13.left)
        self.assertEqual(None, node13.right)
        self.assertEqual(node6, node13.parent)

        self.assert_binary_search_properties(root)

    def test_find_on_fifteen_node_tree_with_key15(self):
        (key1, key2, key3, key4, key5, key6, key7, key8, key9,
         key10, key11, key12, key13, key14, key15,
         node1, node2, node3, node4, node5, node6, node7, node8, node9,
         node10, node11, node12, node13, node14, node15) = \
                                        self.create_complete_fifteen_node_tree()

        root = node1
        search_key = key15

        node, root = self.tree.find(root, search_key)

        self.assertEqual(node15, node)
        self.assertEqual(node15, root)
        self.assertEqual(search_key, node.key)

        self.assertEqual(key15, node15.key)
        self.assertEqual(node1, node15.left)
        self.assertEqual(None, node15.right)
        self.assertEqual(None, node15.parent)

        self.assertEqual(key1, node1.key)
        self.assertEqual(node2, node1.left)
        self.assertEqual(node7, node1.right)
        self.assertEqual(None, node15.parent)

        self.assertEqual(key2, node2.key)
        self.assertEqual(node4, node2.left)
        self.assertEqual(node5, node2.right)
        self.assertEqual(node1, node2.parent)

        self.assertEqual(key7, node7.key)
        self.assertEqual(node3, node7.left)
        self.assertEqual(None, node7.right)
        self.assertEqual(node1, node7.parent)

        self.assertEqual(key4, node4.key)
        self.assertEqual(node8, node4.left)
        self.assertEqual(node9, node4.right)
        self.assertEqual(node2, node4.parent)

        self.assertEqual(key5, node5.key)
        self.assertEqual(node10, node5.left)
        self.assertEqual(node11, node5.right)
        self.assertEqual(node2, node5.parent)

        self.assertEqual(key3, node3.key)
        self.assertEqual(node6, node3.left)
        self.assertEqual(node14, node3.right)
        self.assertEqual(node7, node3.parent)

        self.assertEqual(key8, node8.key)
        self.assertEqual(None, node8.left)
        self.assertEqual(None, node8.right)
        self.assertEqual(node4, node8.parent)

        self.assertEqual(key9, node9.key)
        self.assertEqual(None, node9.left)
        self.assertEqual(None, node9.right)
        self.assertEqual(node4, node9.parent)

        self.assertEqual(key10, node10.key)
        self.assertEqual(None, node10.left)
        self.assertEqual(None, node10.right)
        self.assertEqual(node5, node10.parent)

        self.assertEqual(key11, node11.key)
        self.assertEqual(None, node11.left)
        self.assertEqual(None, node11.right)
        self.assertEqual(node5, node11.parent)

        self.assertEqual(key6, node6.key)
        self.assertEqual(node12, node6.left)
        self.assertEqual(node13, node6.right)
        self.assertEqual(node3, node6.parent)

        self.assertEqual(key14, node14.key)
        self.assertEqual(None, node14.left)
        self.assertEqual(None, node14.right)
        self.assertEqual(node3, node14.parent)

        self.assertEqual(key12, node12.key)
        self.assertEqual(None, node12.left)
        self.assertEqual(None, node12.right)
        self.assertEqual(node6, node12.parent)

        self.assertEqual(key13, node13.key)
        self.assertEqual(None, node13.left)
        self.assertEqual(None, node13.right)
        self.assertEqual(node6, node13.parent)

        self.assert_binary_search_properties(root)

    def test_find_on_fifteen_node_tree_with_between_key14_and_key15(self):
        (key1, key2, key3, key4, key5, key6, key7, key8, key9,
         key10, key11, key12, key13, key14, key15,
         node1, node2, node3, node4, node5, node6, node7, node8, node9,
         node10, node11, node12, node13, node14, node15) = \
                                        self.create_complete_fifteen_node_tree()

        root = node1
        search_key = key15 - 1

        node, root = self.tree.find(root, search_key)

        self.assertEqual(node15, node)
        self.assertEqual(node15, root)
        self.assertTrue(search_key < node.key)

        self.assertEqual(key15, node15.key)
        self.assertEqual(node1, node15.left)
        self.assertEqual(None, node15.right)
        self.assertEqual(None, node15.parent)

        self.assertEqual(key1, node1.key)
        self.assertEqual(node2, node1.left)
        self.assertEqual(node7, node1.right)
        self.assertEqual(None, node15.parent)

        self.assertEqual(key2, node2.key)
        self.assertEqual(node4, node2.left)
        self.assertEqual(node5, node2.right)
        self.assertEqual(node1, node2.parent)

        self.assertEqual(key7, node7.key)
        self.assertEqual(node3, node7.left)
        self.assertEqual(None, node7.right)
        self.assertEqual(node1, node7.parent)

        self.assertEqual(key4, node4.key)
        self.assertEqual(node8, node4.left)
        self.assertEqual(node9, node4.right)
        self.assertEqual(node2, node4.parent)

        self.assertEqual(key5, node5.key)
        self.assertEqual(node10, node5.left)
        self.assertEqual(node11, node5.right)
        self.assertEqual(node2, node5.parent)

        self.assertEqual(key3, node3.key)
        self.assertEqual(node6, node3.left)
        self.assertEqual(node14, node3.right)
        self.assertEqual(node7, node3.parent)

        self.assertEqual(key8, node8.key)
        self.assertEqual(None, node8.left)
        self.assertEqual(None, node8.right)
        self.assertEqual(node4, node8.parent)

        self.assertEqual(key9, node9.key)
        self.assertEqual(None, node9.left)
        self.assertEqual(None, node9.right)
        self.assertEqual(node4, node9.parent)

        self.assertEqual(key10, node10.key)
        self.assertEqual(None, node10.left)
        self.assertEqual(None, node10.right)
        self.assertEqual(node5, node10.parent)

        self.assertEqual(key11, node11.key)
        self.assertEqual(None, node11.left)
        self.assertEqual(None, node11.right)
        self.assertEqual(node5, node11.parent)

        self.assertEqual(key6, node6.key)
        self.assertEqual(node12, node6.left)
        self.assertEqual(node13, node6.right)
        self.assertEqual(node3, node6.parent)

        self.assertEqual(key14, node14.key)
        self.assertEqual(None, node14.left)
        self.assertEqual(None, node14.right)
        self.assertEqual(node3, node14.parent)

        self.assertEqual(key12, node12.key)
        self.assertEqual(None, node12.left)
        self.assertEqual(None, node12.right)
        self.assertEqual(node6, node12.parent)

        self.assertEqual(key13, node13.key)
        self.assertEqual(None, node13.left)
        self.assertEqual(None, node13.right)
        self.assertEqual(node6, node13.parent)

        self.assert_binary_search_properties(root)

    def test_find_on_fifteen_node_tree_with_key14(self):
        (key1, key2, key3, key4, key5, key6, key7, key8, key9,
         key10, key11, key12, key13, key14, key15,
         node1, node2, node3, node4, node5, node6, node7, node8, node9,
         node10, node11, node12, node13, node14, node15) = \
                                        self.create_complete_fifteen_node_tree()

        root = node1
        search_key = key14

        node, root = self.tree.find(root, search_key)

        self.assertEqual(node14, node)
        self.assertEqual(node14, root)
        self.assertEqual(search_key, node.key)

        self.assertEqual(key15, node15.key)
        self.assertEqual(None, node15.left)
        self.assertEqual(None, node15.right)
        self.assertEqual(node7, node15.parent)

        self.assertEqual(key1, node1.key)
        self.assertEqual(node2, node1.left)
        self.assertEqual(node3, node1.right)
        self.assertEqual(node7, node15.parent)

        self.assertEqual(key2, node2.key)
        self.assertEqual(node4, node2.left)
        self.assertEqual(node5, node2.right)
        self.assertEqual(node1, node2.parent)

        self.assertEqual(key7, node7.key)
        self.assertEqual(None, node7.left)
        self.assertEqual(node15, node7.right)
        self.assertEqual(node14, node7.parent)

        self.assertEqual(key4, node4.key)
        self.assertEqual(node8, node4.left)
        self.assertEqual(node9, node4.right)
        self.assertEqual(node2, node4.parent)

        self.assertEqual(key5, node5.key)
        self.assertEqual(node10, node5.left)
        self.assertEqual(node11, node5.right)
        self.assertEqual(node2, node5.parent)

        self.assertEqual(key3, node3.key)
        self.assertEqual(node6, node3.left)
        self.assertEqual(None, node3.right)
        self.assertEqual(node1, node3.parent)

        self.assertEqual(key8, node8.key)
        self.assertEqual(None, node8.left)
        self.assertEqual(None, node8.right)
        self.assertEqual(node4, node8.parent)

        self.assertEqual(key9, node9.key)
        self.assertEqual(None, node9.left)
        self.assertEqual(None, node9.right)
        self.assertEqual(node4, node9.parent)

        self.assertEqual(key10, node10.key)
        self.assertEqual(None, node10.left)
        self.assertEqual(None, node10.right)
        self.assertEqual(node5, node10.parent)

        self.assertEqual(key11, node11.key)
        self.assertEqual(None, node11.left)
        self.assertEqual(None, node11.right)
        self.assertEqual(node5, node11.parent)

        self.assertEqual(key6, node6.key)
        self.assertEqual(node12, node6.left)
        self.assertEqual(node13, node6.right)
        self.assertEqual(node3, node6.parent)

        self.assertEqual(key14, node14.key)
        self.assertEqual(node1, node14.left)
        self.assertEqual(node7, node14.right)
        self.assertEqual(None, node14.parent)

        self.assertEqual(key12, node12.key)
        self.assertEqual(None, node12.left)
        self.assertEqual(None, node12.right)
        self.assertEqual(node6, node12.parent)

        self.assertEqual(key13, node13.key)
        self.assertEqual(None, node13.left)
        self.assertEqual(None, node13.right)
        self.assertEqual(node6, node13.parent)

        self.assert_binary_search_properties(root)

    def test_find_on_fifteen_node_tree_with_between_key13_and_key14(self):
        (key1, key2, key3, key4, key5, key6, key7, key8, key9,
         key10, key11, key12, key13, key14, key15,
         node1, node2, node3, node4, node5, node6, node7, node8, node9,
         node10, node11, node12, node13, node14, node15) = \
                                        self.create_complete_fifteen_node_tree()

        root = node1
        search_key = key14 - 1

        node, root = self.tree.find(root, search_key)

        self.assertEqual(node14, node)
        self.assertEqual(node14, root)
        self.assertTrue(search_key < node.key)

        self.assertEqual(key15, node15.key)
        self.assertEqual(None, node15.left)
        self.assertEqual(None, node15.right)
        self.assertEqual(node7, node15.parent)

        self.assertEqual(key1, node1.key)
        self.assertEqual(node2, node1.left)
        self.assertEqual(node3, node1.right)
        self.assertEqual(node7, node15.parent)

        self.assertEqual(key2, node2.key)
        self.assertEqual(node4, node2.left)
        self.assertEqual(node5, node2.right)
        self.assertEqual(node1, node2.parent)

        self.assertEqual(key7, node7.key)
        self.assertEqual(None, node7.left)
        self.assertEqual(node15, node7.right)
        self.assertEqual(node14, node7.parent)

        self.assertEqual(key4, node4.key)
        self.assertEqual(node8, node4.left)
        self.assertEqual(node9, node4.right)
        self.assertEqual(node2, node4.parent)

        self.assertEqual(key5, node5.key)
        self.assertEqual(node10, node5.left)
        self.assertEqual(node11, node5.right)
        self.assertEqual(node2, node5.parent)

        self.assertEqual(key3, node3.key)
        self.assertEqual(node6, node3.left)
        self.assertEqual(None, node3.right)
        self.assertEqual(node1, node3.parent)

        self.assertEqual(key8, node8.key)
        self.assertEqual(None, node8.left)
        self.assertEqual(None, node8.right)
        self.assertEqual(node4, node8.parent)

        self.assertEqual(key9, node9.key)
        self.assertEqual(None, node9.left)
        self.assertEqual(None, node9.right)
        self.assertEqual(node4, node9.parent)

        self.assertEqual(key10, node10.key)
        self.assertEqual(None, node10.left)
        self.assertEqual(None, node10.right)
        self.assertEqual(node5, node10.parent)

        self.assertEqual(key11, node11.key)
        self.assertEqual(None, node11.left)
        self.assertEqual(None, node11.right)
        self.assertEqual(node5, node11.parent)

        self.assertEqual(key6, node6.key)
        self.assertEqual(node12, node6.left)
        self.assertEqual(node13, node6.right)
        self.assertEqual(node3, node6.parent)

        self.assertEqual(key14, node14.key)
        self.assertEqual(node1, node14.left)
        self.assertEqual(node7, node14.right)
        self.assertEqual(None, node14.parent)

        self.assertEqual(key12, node12.key)
        self.assertEqual(None, node12.left)
        self.assertEqual(None, node12.right)
        self.assertEqual(node6, node12.parent)

        self.assertEqual(key13, node13.key)
        self.assertEqual(None, node13.left)
        self.assertEqual(None, node13.right)
        self.assertEqual(node6, node13.parent)

        self.assert_binary_search_properties(root)

    def test_find_on_fifteen_node_tree_with_key13(self):
        (key1, key2, key3, key4, key5, key6, key7, key8, key9,
         key10, key11, key12, key13, key14, key15,
         node1, node2, node3, node4, node5, node6, node7, node8, node9,
         node10, node11, node12, node13, node14, node15) = \
                                        self.create_complete_fifteen_node_tree()

        root = node1
        search_key = key13

        node, root = self.tree.find(root, search_key)

        self.assertEqual(node13, node)
        self.assertEqual(node13, root)
        self.assertEqual(search_key, node.key)

        self.assertEqual(key15, node15.key)
        self.assertEqual(None, node15.left)
        self.assertEqual(None, node15.right)
        self.assertEqual(node7, node15.parent)

        self.assertEqual(key1, node1.key)
        self.assertEqual(node2, node1.left)
        self.assertEqual(node6, node1.right)
        self.assertEqual(node7, node15.parent)

        self.assertEqual(key2, node2.key)
        self.assertEqual(node4, node2.left)
        self.assertEqual(node5, node2.right)
        self.assertEqual(node1, node2.parent)

        self.assertEqual(key7, node7.key)
        self.assertEqual(node14, node7.left)
        self.assertEqual(node15, node7.right)
        self.assertEqual(node3, node7.parent)

        self.assertEqual(key4, node4.key)
        self.assertEqual(node8, node4.left)
        self.assertEqual(node9, node4.right)
        self.assertEqual(node2, node4.parent)

        self.assertEqual(key5, node5.key)
        self.assertEqual(node10, node5.left)
        self.assertEqual(node11, node5.right)
        self.assertEqual(node2, node5.parent)

        self.assertEqual(key3, node3.key)
        self.assertEqual(None, node3.left)
        self.assertEqual(node7, node3.right)
        self.assertEqual(node13, node3.parent)

        self.assertEqual(key8, node8.key)
        self.assertEqual(None, node8.left)
        self.assertEqual(None, node8.right)
        self.assertEqual(node4, node8.parent)

        self.assertEqual(key9, node9.key)
        self.assertEqual(None, node9.left)
        self.assertEqual(None, node9.right)
        self.assertEqual(node4, node9.parent)

        self.assertEqual(key10, node10.key)
        self.assertEqual(None, node10.left)
        self.assertEqual(None, node10.right)
        self.assertEqual(node5, node10.parent)

        self.assertEqual(key11, node11.key)
        self.assertEqual(None, node11.left)
        self.assertEqual(None, node11.right)
        self.assertEqual(node5, node11.parent)

        self.assertEqual(key6, node6.key)
        self.assertEqual(node12, node6.left)
        self.assertEqual(None, node6.right)
        self.assertEqual(node1, node6.parent)

        self.assertEqual(key14, node14.key)
        self.assertEqual(None, node14.left)
        self.assertEqual(None, node14.right)
        self.assertEqual(node7, node14.parent)

        self.assertEqual(key12, node12.key)
        self.assertEqual(None, node12.left)
        self.assertEqual(None, node12.right)
        self.assertEqual(node6, node12.parent)

        self.assertEqual(key13, node13.key)
        self.assertEqual(node1, node13.left)
        self.assertEqual(node3, node13.right)
        self.assertEqual(None, node13.parent)

        self.assert_binary_search_properties(root)

    def test_find_on_fifteen_node_tree_with_between_key12_and_key13(self):
        (key1, key2, key3, key4, key5, key6, key7, key8, key9,
         key10, key11, key12, key13, key14, key15,
         node1, node2, node3, node4, node5, node6, node7, node8, node9,
         node10, node11, node12, node13, node14, node15) = \
                                        self.create_complete_fifteen_node_tree()

        root = node1
        search_key = key13 - 1

        node, root = self.tree.find(root, search_key)

        self.assertEqual(node13, node)
        self.assertEqual(node13, root)
        self.assertTrue(search_key < node.key)

        self.assertEqual(key15, node15.key)
        self.assertEqual(None, node15.left)
        self.assertEqual(None, node15.right)
        self.assertEqual(node7, node15.parent)

        self.assertEqual(key1, node1.key)
        self.assertEqual(node2, node1.left)
        self.assertEqual(node6, node1.right)
        self.assertEqual(node7, node15.parent)

        self.assertEqual(key2, node2.key)
        self.assertEqual(node4, node2.left)
        self.assertEqual(node5, node2.right)
        self.assertEqual(node1, node2.parent)

        self.assertEqual(key7, node7.key)
        self.assertEqual(node14, node7.left)
        self.assertEqual(node15, node7.right)
        self.assertEqual(node3, node7.parent)

        self.assertEqual(key4, node4.key)
        self.assertEqual(node8, node4.left)
        self.assertEqual(node9, node4.right)
        self.assertEqual(node2, node4.parent)

        self.assertEqual(key5, node5.key)
        self.assertEqual(node10, node5.left)
        self.assertEqual(node11, node5.right)
        self.assertEqual(node2, node5.parent)

        self.assertEqual(key3, node3.key)
        self.assertEqual(None, node3.left)
        self.assertEqual(node7, node3.right)
        self.assertEqual(node13, node3.parent)

        self.assertEqual(key8, node8.key)
        self.assertEqual(None, node8.left)
        self.assertEqual(None, node8.right)
        self.assertEqual(node4, node8.parent)

        self.assertEqual(key9, node9.key)
        self.assertEqual(None, node9.left)
        self.assertEqual(None, node9.right)
        self.assertEqual(node4, node9.parent)

        self.assertEqual(key10, node10.key)
        self.assertEqual(None, node10.left)
        self.assertEqual(None, node10.right)
        self.assertEqual(node5, node10.parent)

        self.assertEqual(key11, node11.key)
        self.assertEqual(None, node11.left)
        self.assertEqual(None, node11.right)
        self.assertEqual(node5, node11.parent)

        self.assertEqual(key6, node6.key)
        self.assertEqual(node12, node6.left)
        self.assertEqual(None, node6.right)
        self.assertEqual(node1, node6.parent)

        self.assertEqual(key14, node14.key)
        self.assertEqual(None, node14.left)
        self.assertEqual(None, node14.right)
        self.assertEqual(node7, node14.parent)

        self.assertEqual(key12, node12.key)
        self.assertEqual(None, node12.left)
        self.assertEqual(None, node12.right)
        self.assertEqual(node6, node12.parent)

        self.assertEqual(key13, node13.key)
        self.assertEqual(node1, node13.left)
        self.assertEqual(node3, node13.right)
        self.assertEqual(None, node13.parent)

        self.assert_binary_search_properties(root)

    def test_find_on_fifteen_node_tree_with_key12(self):
        (key1, key2, key3, key4, key5, key6, key7, key8, key9,
         key10, key11, key12, key13, key14, key15,
         node1, node2, node3, node4, node5, node6, node7, node8, node9,
         node10, node11, node12, node13, node14, node15) = \
                                        self.create_complete_fifteen_node_tree()

        root = node1
        search_key = key12

        node, root = self.tree.find(root, search_key)

        self.assertEqual(node12, node)
        self.assertEqual(node12, root)
        self.assertEqual(search_key, node.key)

        self.assertEqual(key15, node15.key)
        self.assertEqual(None, node15.left)
        self.assertEqual(None, node15.right)
        self.assertEqual(node7, node15.parent)

        self.assertEqual(key1, node1.key)
        self.assertEqual(node2, node1.left)
        self.assertEqual(None, node1.right)
        self.assertEqual(node7, node15.parent)

        self.assertEqual(key2, node2.key)
        self.assertEqual(node4, node2.left)
        self.assertEqual(node5, node2.right)
        self.assertEqual(node1, node2.parent)

        self.assertEqual(key7, node7.key)
        self.assertEqual(node14, node7.left)
        self.assertEqual(node15, node7.right)
        self.assertEqual(node3, node7.parent)

        self.assertEqual(key4, node4.key)
        self.assertEqual(node8, node4.left)
        self.assertEqual(node9, node4.right)
        self.assertEqual(node2, node4.parent)

        self.assertEqual(key5, node5.key)
        self.assertEqual(node10, node5.left)
        self.assertEqual(node11, node5.right)
        self.assertEqual(node2, node5.parent)

        self.assertEqual(key3, node3.key)
        self.assertEqual(node13, node3.left)
        self.assertEqual(node7, node3.right)
        self.assertEqual(node6, node3.parent)

        self.assertEqual(key8, node8.key)
        self.assertEqual(None, node8.left)
        self.assertEqual(None, node8.right)
        self.assertEqual(node4, node8.parent)

        self.assertEqual(key9, node9.key)
        self.assertEqual(None, node9.left)
        self.assertEqual(None, node9.right)
        self.assertEqual(node4, node9.parent)

        self.assertEqual(key10, node10.key)
        self.assertEqual(None, node10.left)
        self.assertEqual(None, node10.right)
        self.assertEqual(node5, node10.parent)

        self.assertEqual(key11, node11.key)
        self.assertEqual(None, node11.left)
        self.assertEqual(None, node11.right)
        self.assertEqual(node5, node11.parent)

        self.assertEqual(key6, node6.key)
        self.assertEqual(None, node6.left)
        self.assertEqual(node3, node6.right)
        self.assertEqual(node12, node6.parent)

        self.assertEqual(key14, node14.key)
        self.assertEqual(None, node14.left)
        self.assertEqual(None, node14.right)
        self.assertEqual(node7, node14.parent)

        self.assertEqual(key12, node12.key)
        self.assertEqual(node1, node12.left)
        self.assertEqual(node6, node12.right)
        self.assertEqual(None, node12.parent)

        self.assertEqual(key13, node13.key)
        self.assertEqual(None, node13.left)
        self.assertEqual(None, node13.right)
        self.assertEqual(node3, node13.parent)

        self.assert_binary_search_properties(root)

    def test_find_on_fifteen_node_tree_with_between_key11_and_key12(self):
        (key1, key2, key3, key4, key5, key6, key7, key8, key9,
         key10, key11, key12, key13, key14, key15,
         node1, node2, node3, node4, node5, node6, node7, node8, node9,
         node10, node11, node12, node13, node14, node15) = \
                                        self.create_complete_fifteen_node_tree()

        root = node1
        search_key = key12 - 1

        node, root = self.tree.find(root, search_key)

        self.assertEqual(node12, node)
        self.assertEqual(node12, root)
        self.assertTrue(search_key < node.key)

        self.assertEqual(key15, node15.key)
        self.assertEqual(None, node15.left)
        self.assertEqual(None, node15.right)
        self.assertEqual(node7, node15.parent)

        self.assertEqual(key1, node1.key)
        self.assertEqual(node2, node1.left)
        self.assertEqual(None, node1.right)
        self.assertEqual(node7, node15.parent)

        self.assertEqual(key2, node2.key)
        self.assertEqual(node4, node2.left)
        self.assertEqual(node5, node2.right)
        self.assertEqual(node1, node2.parent)

        self.assertEqual(key7, node7.key)
        self.assertEqual(node14, node7.left)
        self.assertEqual(node15, node7.right)
        self.assertEqual(node3, node7.parent)

        self.assertEqual(key4, node4.key)
        self.assertEqual(node8, node4.left)
        self.assertEqual(node9, node4.right)
        self.assertEqual(node2, node4.parent)

        self.assertEqual(key5, node5.key)
        self.assertEqual(node10, node5.left)
        self.assertEqual(node11, node5.right)
        self.assertEqual(node2, node5.parent)

        self.assertEqual(key3, node3.key)
        self.assertEqual(node13, node3.left)
        self.assertEqual(node7, node3.right)
        self.assertEqual(node6, node3.parent)

        self.assertEqual(key8, node8.key)
        self.assertEqual(None, node8.left)
        self.assertEqual(None, node8.right)
        self.assertEqual(node4, node8.parent)

        self.assertEqual(key9, node9.key)
        self.assertEqual(None, node9.left)
        self.assertEqual(None, node9.right)
        self.assertEqual(node4, node9.parent)

        self.assertEqual(key10, node10.key)
        self.assertEqual(None, node10.left)
        self.assertEqual(None, node10.right)
        self.assertEqual(node5, node10.parent)

        self.assertEqual(key11, node11.key)
        self.assertEqual(None, node11.left)
        self.assertEqual(None, node11.right)
        self.assertEqual(node5, node11.parent)

        self.assertEqual(key6, node6.key)
        self.assertEqual(None, node6.left)
        self.assertEqual(node3, node6.right)
        self.assertEqual(node12, node6.parent)

        self.assertEqual(key14, node14.key)
        self.assertEqual(None, node14.left)
        self.assertEqual(None, node14.right)
        self.assertEqual(node7, node14.parent)

        self.assertEqual(key12, node12.key)
        self.assertEqual(node1, node12.left)
        self.assertEqual(node6, node12.right)
        self.assertEqual(None, node12.parent)

        self.assertEqual(key13, node13.key)
        self.assertEqual(None, node13.left)
        self.assertEqual(None, node13.right)
        self.assertEqual(node3, node13.parent)

        self.assert_binary_search_properties(root)

    def test_find_on_fifteen_node_tree_with_key11(self):
        (key1, key2, key3, key4, key5, key6, key7, key8, key9,
         key10, key11, key12, key13, key14, key15,
         node1, node2, node3, node4, node5, node6, node7, node8, node9,
         node10, node11, node12, node13, node14, node15) = \
                                        self.create_complete_fifteen_node_tree()

        root = node1
        search_key = key11

        node, root = self.tree.find(root, search_key)

        self.assertEqual(node11, node)
        self.assertEqual(node11, root)
        self.assertEqual(search_key, node.key)

        self.assertEqual(key15, node15.key)
        self.assertEqual(None, node15.left)
        self.assertEqual(None, node15.right)
        self.assertEqual(node7, node15.parent)

        self.assertEqual(key1, node1.key)
        self.assertEqual(None, node1.left)
        self.assertEqual(node3, node1.right)
        self.assertEqual(node7, node15.parent)

        self.assertEqual(key2, node2.key)
        self.assertEqual(node4, node2.left)
        self.assertEqual(node10, node2.right)
        self.assertEqual(node5, node2.parent)

        self.assertEqual(key7, node7.key)
        self.assertEqual(node14, node7.left)
        self.assertEqual(node15, node7.right)
        self.assertEqual(node3, node7.parent)

        self.assertEqual(key4, node4.key)
        self.assertEqual(node8, node4.left)
        self.assertEqual(node9, node4.right)
        self.assertEqual(node2, node4.parent)

        self.assertEqual(key5, node5.key)
        self.assertEqual(node2, node5.left)
        self.assertEqual(None, node5.right)
        self.assertEqual(node11, node5.parent)

        self.assertEqual(key3, node3.key)
        self.assertEqual(node6, node3.left)
        self.assertEqual(node7, node3.right)
        self.assertEqual(node1, node3.parent)

        self.assertEqual(key8, node8.key)
        self.assertEqual(None, node8.left)
        self.assertEqual(None, node8.right)
        self.assertEqual(node4, node8.parent)

        self.assertEqual(key9, node9.key)
        self.assertEqual(None, node9.left)
        self.assertEqual(None, node9.right)
        self.assertEqual(node4, node9.parent)

        self.assertEqual(key10, node10.key)
        self.assertEqual(None, node10.left)
        self.assertEqual(None, node10.right)
        self.assertEqual(node2, node10.parent)

        self.assertEqual(key11, node11.key)
        self.assertEqual(node5, node11.left)
        self.assertEqual(node1, node11.right)
        self.assertEqual(None, node11.parent)

        self.assertEqual(key6, node6.key)
        self.assertEqual(node12, node6.left)
        self.assertEqual(node13, node6.right)
        self.assertEqual(node3, node6.parent)

        self.assertEqual(key14, node14.key)
        self.assertEqual(None, node14.left)
        self.assertEqual(None, node14.right)
        self.assertEqual(node7, node14.parent)

        self.assertEqual(key12, node12.key)
        self.assertEqual(None, node12.left)
        self.assertEqual(None, node12.right)
        self.assertEqual(node6, node12.parent)

        self.assertEqual(key13, node13.key)
        self.assertEqual(None, node13.left)
        self.assertEqual(None, node13.right)
        self.assertEqual(node6, node13.parent)

        self.assert_binary_search_properties(root)

    def test_find_on_fifteen_node_tree_with_between_key10_and_key11(self):
        (key1, key2, key3, key4, key5, key6, key7, key8, key9,
         key10, key11, key12, key13, key14, key15,
         node1, node2, node3, node4, node5, node6, node7, node8, node9,
         node10, node11, node12, node13, node14, node15) = \
                                        self.create_complete_fifteen_node_tree()

        root = node1
        search_key = key11 - 1

        node, root = self.tree.find(root, search_key)

        self.assertEqual(node11, node)
        self.assertEqual(node11, root)
        self.assertTrue(search_key < node.key)

        self.assertEqual(key15, node15.key)
        self.assertEqual(None, node15.left)
        self.assertEqual(None, node15.right)
        self.assertEqual(node7, node15.parent)

        self.assertEqual(key1, node1.key)
        self.assertEqual(None, node1.left)
        self.assertEqual(node3, node1.right)
        self.assertEqual(node7, node15.parent)

        self.assertEqual(key2, node2.key)
        self.assertEqual(node4, node2.left)
        self.assertEqual(node10, node2.right)
        self.assertEqual(node5, node2.parent)

        self.assertEqual(key7, node7.key)
        self.assertEqual(node14, node7.left)
        self.assertEqual(node15, node7.right)
        self.assertEqual(node3, node7.parent)

        self.assertEqual(key4, node4.key)
        self.assertEqual(node8, node4.left)
        self.assertEqual(node9, node4.right)
        self.assertEqual(node2, node4.parent)

        self.assertEqual(key5, node5.key)
        self.assertEqual(node2, node5.left)
        self.assertEqual(None, node5.right)
        self.assertEqual(node11, node5.parent)

        self.assertEqual(key3, node3.key)
        self.assertEqual(node6, node3.left)
        self.assertEqual(node7, node3.right)
        self.assertEqual(node1, node3.parent)

        self.assertEqual(key8, node8.key)
        self.assertEqual(None, node8.left)
        self.assertEqual(None, node8.right)
        self.assertEqual(node4, node8.parent)

        self.assertEqual(key9, node9.key)
        self.assertEqual(None, node9.left)
        self.assertEqual(None, node9.right)
        self.assertEqual(node4, node9.parent)

        self.assertEqual(key10, node10.key)
        self.assertEqual(None, node10.left)
        self.assertEqual(None, node10.right)
        self.assertEqual(node2, node10.parent)

        self.assertEqual(key11, node11.key)
        self.assertEqual(node5, node11.left)
        self.assertEqual(node1, node11.right)
        self.assertEqual(None, node11.parent)

        self.assertEqual(key6, node6.key)
        self.assertEqual(node12, node6.left)
        self.assertEqual(node13, node6.right)
        self.assertEqual(node3, node6.parent)

        self.assertEqual(key14, node14.key)
        self.assertEqual(None, node14.left)
        self.assertEqual(None, node14.right)
        self.assertEqual(node7, node14.parent)

        self.assertEqual(key12, node12.key)
        self.assertEqual(None, node12.left)
        self.assertEqual(None, node12.right)
        self.assertEqual(node6, node12.parent)

        self.assertEqual(key13, node13.key)
        self.assertEqual(None, node13.left)
        self.assertEqual(None, node13.right)
        self.assertEqual(node6, node13.parent)

        self.assert_binary_search_properties(root)

    def test_find_on_fifteen_node_tree_with_key10(self):
        (key1, key2, key3, key4, key5, key6, key7, key8, key9,
         key10, key11, key12, key13, key14, key15,
         node1, node2, node3, node4, node5, node6, node7, node8, node9,
         node10, node11, node12, node13, node14, node15) = \
                                        self.create_complete_fifteen_node_tree()

        root = node1
        search_key = key10

        node, root = self.tree.find(root, search_key)

        self.assertEqual(node10, node)
        self.assertEqual(node10, root)
        self.assertEqual(search_key, node.key)

        self.assertEqual(key15, node15.key)
        self.assertEqual(None, node15.left)
        self.assertEqual(None, node15.right)
        self.assertEqual(node7, node15.parent)

        self.assertEqual(key1, node1.key)
        self.assertEqual(node5, node1.left)
        self.assertEqual(node3, node1.right)
        self.assertEqual(node7, node15.parent)

        self.assertEqual(key2, node2.key)
        self.assertEqual(node4, node2.left)
        self.assertEqual(None, node2.right)
        self.assertEqual(node10, node2.parent)

        self.assertEqual(key7, node7.key)
        self.assertEqual(node14, node7.left)
        self.assertEqual(node15, node7.right)
        self.assertEqual(node3, node7.parent)

        self.assertEqual(key4, node4.key)
        self.assertEqual(node8, node4.left)
        self.assertEqual(node9, node4.right)
        self.assertEqual(node2, node4.parent)

        self.assertEqual(key5, node5.key)
        self.assertEqual(None, node5.left)
        self.assertEqual(node11, node5.right)
        self.assertEqual(node1, node5.parent)

        self.assertEqual(key3, node3.key)
        self.assertEqual(node6, node3.left)
        self.assertEqual(node7, node3.right)
        self.assertEqual(node1, node3.parent)

        self.assertEqual(key8, node8.key)
        self.assertEqual(None, node8.left)
        self.assertEqual(None, node8.right)
        self.assertEqual(node4, node8.parent)

        self.assertEqual(key9, node9.key)
        self.assertEqual(None, node9.left)
        self.assertEqual(None, node9.right)
        self.assertEqual(node4, node9.parent)

        self.assertEqual(key10, node10.key)
        self.assertEqual(node2, node10.left)
        self.assertEqual(node1, node10.right)
        self.assertEqual(None, node10.parent)

        self.assertEqual(key11, node11.key)
        self.assertEqual(None, node11.left)
        self.assertEqual(None, node11.right)
        self.assertEqual(node5, node11.parent)

        self.assertEqual(key6, node6.key)
        self.assertEqual(node12, node6.left)
        self.assertEqual(node13, node6.right)
        self.assertEqual(node3, node6.parent)

        self.assertEqual(key14, node14.key)
        self.assertEqual(None, node14.left)
        self.assertEqual(None, node14.right)
        self.assertEqual(node7, node14.parent)

        self.assertEqual(key12, node12.key)
        self.assertEqual(None, node12.left)
        self.assertEqual(None, node12.right)
        self.assertEqual(node6, node12.parent)

        self.assertEqual(key13, node13.key)
        self.assertEqual(None, node13.left)
        self.assertEqual(None, node13.right)
        self.assertEqual(node6, node13.parent)

        self.assert_binary_search_properties(root)

    def test_find_on_fifteen_node_tree_with_between_key9_and_key10(self):
        (key1, key2, key3, key4, key5, key6, key7, key8, key9,
         key10, key11, key12, key13, key14, key15,
         node1, node2, node3, node4, node5, node6, node7, node8, node9,
         node10, node11, node12, node13, node14, node15) = \
                                        self.create_complete_fifteen_node_tree()

        root = node1
        search_key = key10 - 1

        node, root = self.tree.find(root, search_key)

        self.assertEqual(node10, node)
        self.assertEqual(node10, root)
        self.assertTrue(search_key < node.key)

        self.assertEqual(key15, node15.key)
        self.assertEqual(None, node15.left)
        self.assertEqual(None, node15.right)
        self.assertEqual(node7, node15.parent)

        self.assertEqual(key1, node1.key)
        self.assertEqual(node5, node1.left)
        self.assertEqual(node3, node1.right)
        self.assertEqual(node7, node15.parent)

        self.assertEqual(key2, node2.key)
        self.assertEqual(node4, node2.left)
        self.assertEqual(None, node2.right)
        self.assertEqual(node10, node2.parent)

        self.assertEqual(key7, node7.key)
        self.assertEqual(node14, node7.left)
        self.assertEqual(node15, node7.right)
        self.assertEqual(node3, node7.parent)

        self.assertEqual(key4, node4.key)
        self.assertEqual(node8, node4.left)
        self.assertEqual(node9, node4.right)
        self.assertEqual(node2, node4.parent)

        self.assertEqual(key5, node5.key)
        self.assertEqual(None, node5.left)
        self.assertEqual(node11, node5.right)
        self.assertEqual(node1, node5.parent)

        self.assertEqual(key3, node3.key)
        self.assertEqual(node6, node3.left)
        self.assertEqual(node7, node3.right)
        self.assertEqual(node1, node3.parent)

        self.assertEqual(key8, node8.key)
        self.assertEqual(None, node8.left)
        self.assertEqual(None, node8.right)
        self.assertEqual(node4, node8.parent)

        self.assertEqual(key9, node9.key)
        self.assertEqual(None, node9.left)
        self.assertEqual(None, node9.right)
        self.assertEqual(node4, node9.parent)

        self.assertEqual(key10, node10.key)
        self.assertEqual(node2, node10.left)
        self.assertEqual(node1, node10.right)
        self.assertEqual(None, node10.parent)

        self.assertEqual(key11, node11.key)
        self.assertEqual(None, node11.left)
        self.assertEqual(None, node11.right)
        self.assertEqual(node5, node11.parent)

        self.assertEqual(key6, node6.key)
        self.assertEqual(node12, node6.left)
        self.assertEqual(node13, node6.right)
        self.assertEqual(node3, node6.parent)

        self.assertEqual(key14, node14.key)
        self.assertEqual(None, node14.left)
        self.assertEqual(None, node14.right)
        self.assertEqual(node7, node14.parent)

        self.assertEqual(key12, node12.key)
        self.assertEqual(None, node12.left)
        self.assertEqual(None, node12.right)
        self.assertEqual(node6, node12.parent)

        self.assertEqual(key13, node13.key)
        self.assertEqual(None, node13.left)
        self.assertEqual(None, node13.right)
        self.assertEqual(node6, node13.parent)

        self.assert_binary_search_properties(root)

    def test_find_on_fifteen_node_tree_with_key9(self):
        (key1, key2, key3, key4, key5, key6, key7, key8, key9,
         key10, key11, key12, key13, key14, key15,
         node1, node2, node3, node4, node5, node6, node7, node8, node9,
         node10, node11, node12, node13, node14, node15) = \
                                        self.create_complete_fifteen_node_tree()

        root = node1
        search_key = key9

        node, root = self.tree.find(root, search_key)

        self.assertEqual(node9, node)
        self.assertEqual(node9, root)
        self.assertEqual(search_key, node.key)

        self.assertEqual(key15, node15.key)
        self.assertEqual(None, node15.left)
        self.assertEqual(None, node15.right)
        self.assertEqual(node7, node15.parent)

        self.assertEqual(key1, node1.key)
        self.assertEqual(node2, node1.left)
        self.assertEqual(node3, node1.right)
        self.assertEqual(node7, node15.parent)

        self.assertEqual(key2, node2.key)
        self.assertEqual(None, node2.left)
        self.assertEqual(node5, node2.right)
        self.assertEqual(node1, node2.parent)

        self.assertEqual(key7, node7.key)
        self.assertEqual(node14, node7.left)
        self.assertEqual(node15, node7.right)
        self.assertEqual(node3, node7.parent)

        self.assertEqual(key4, node4.key)
        self.assertEqual(node8, node4.left)
        self.assertEqual(None, node4.right)
        self.assertEqual(node9, node4.parent)

        self.assertEqual(key5, node5.key)
        self.assertEqual(node10, node5.left)
        self.assertEqual(node11, node5.right)
        self.assertEqual(node2, node5.parent)

        self.assertEqual(key3, node3.key)
        self.assertEqual(node6, node3.left)
        self.assertEqual(node7, node3.right)
        self.assertEqual(node1, node3.parent)

        self.assertEqual(key8, node8.key)
        self.assertEqual(None, node8.left)
        self.assertEqual(None, node8.right)
        self.assertEqual(node4, node8.parent)

        self.assertEqual(key9, node9.key)
        self.assertEqual(node4, node9.left)
        self.assertEqual(node1, node9.right)
        self.assertEqual(None, node9.parent)

        self.assertEqual(key10, node10.key)
        self.assertEqual(None, node10.left)
        self.assertEqual(None, node10.right)
        self.assertEqual(node5, node10.parent)

        self.assertEqual(key11, node11.key)
        self.assertEqual(None, node11.left)
        self.assertEqual(None, node11.right)
        self.assertEqual(node5, node11.parent)

        self.assertEqual(key6, node6.key)
        self.assertEqual(node12, node6.left)
        self.assertEqual(node13, node6.right)
        self.assertEqual(node3, node6.parent)

        self.assertEqual(key14, node14.key)
        self.assertEqual(None, node14.left)
        self.assertEqual(None, node14.right)
        self.assertEqual(node7, node14.parent)

        self.assertEqual(key12, node12.key)
        self.assertEqual(None, node12.left)
        self.assertEqual(None, node12.right)
        self.assertEqual(node6, node12.parent)

        self.assertEqual(key13, node13.key)
        self.assertEqual(None, node13.left)
        self.assertEqual(None, node13.right)
        self.assertEqual(node6, node13.parent)

        self.assert_binary_search_properties(root)

    def test_find_on_fifteen_node_tree_with_between_key8_and_key9(self):
        (key1, key2, key3, key4, key5, key6, key7, key8, key9,
         key10, key11, key12, key13, key14, key15,
         node1, node2, node3, node4, node5, node6, node7, node8, node9,
         node10, node11, node12, node13, node14, node15) = \
                                        self.create_complete_fifteen_node_tree()

        root = node1
        search_key = key9 - 1

        node, root = self.tree.find(root, search_key)

        self.assertEqual(node9, node)
        self.assertEqual(node9, root)
        self.assertTrue(search_key < node.key)

        self.assertEqual(key15, node15.key)
        self.assertEqual(None, node15.left)
        self.assertEqual(None, node15.right)
        self.assertEqual(node7, node15.parent)

        self.assertEqual(key1, node1.key)
        self.assertEqual(node2, node1.left)
        self.assertEqual(node3, node1.right)
        self.assertEqual(node7, node15.parent)

        self.assertEqual(key2, node2.key)
        self.assertEqual(None, node2.left)
        self.assertEqual(node5, node2.right)
        self.assertEqual(node1, node2.parent)

        self.assertEqual(key7, node7.key)
        self.assertEqual(node14, node7.left)
        self.assertEqual(node15, node7.right)
        self.assertEqual(node3, node7.parent)

        self.assertEqual(key4, node4.key)
        self.assertEqual(node8, node4.left)
        self.assertEqual(None, node4.right)
        self.assertEqual(node9, node4.parent)

        self.assertEqual(key5, node5.key)
        self.assertEqual(node10, node5.left)
        self.assertEqual(node11, node5.right)
        self.assertEqual(node2, node5.parent)

        self.assertEqual(key3, node3.key)
        self.assertEqual(node6, node3.left)
        self.assertEqual(node7, node3.right)
        self.assertEqual(node1, node3.parent)

        self.assertEqual(key8, node8.key)
        self.assertEqual(None, node8.left)
        self.assertEqual(None, node8.right)
        self.assertEqual(node4, node8.parent)

        self.assertEqual(key9, node9.key)
        self.assertEqual(node4, node9.left)
        self.assertEqual(node1, node9.right)
        self.assertEqual(None, node9.parent)

        self.assertEqual(key10, node10.key)
        self.assertEqual(None, node10.left)
        self.assertEqual(None, node10.right)
        self.assertEqual(node5, node10.parent)

        self.assertEqual(key11, node11.key)
        self.assertEqual(None, node11.left)
        self.assertEqual(None, node11.right)
        self.assertEqual(node5, node11.parent)

        self.assertEqual(key6, node6.key)
        self.assertEqual(node12, node6.left)
        self.assertEqual(node13, node6.right)
        self.assertEqual(node3, node6.parent)

        self.assertEqual(key14, node14.key)
        self.assertEqual(None, node14.left)
        self.assertEqual(None, node14.right)
        self.assertEqual(node7, node14.parent)

        self.assertEqual(key12, node12.key)
        self.assertEqual(None, node12.left)
        self.assertEqual(None, node12.right)
        self.assertEqual(node6, node12.parent)

        self.assertEqual(key13, node13.key)
        self.assertEqual(None, node13.left)
        self.assertEqual(None, node13.right)
        self.assertEqual(node6, node13.parent)

        self.assert_binary_search_properties(root)

    def test_find_on_fifteen_node_tree_with_key8(self):
        (key1, key2, key3, key4, key5, key6, key7, key8, key9,
         key10, key11, key12, key13, key14, key15,
         node1, node2, node3, node4, node5, node6, node7, node8, node9,
         node10, node11, node12, node13, node14, node15) = \
                                        self.create_complete_fifteen_node_tree()

        root = node1
        search_key = key8

        node, root = self.tree.find(root, search_key)

        self.assertEqual(node8, node)
        self.assertEqual(node8, root)
        self.assertEqual(search_key, node.key)

        self.assertEqual(key15, node15.key)
        self.assertEqual(None, node15.left)
        self.assertEqual(None, node15.right)
        self.assertEqual(node7, node15.parent)

        self.assertEqual(key1, node1.key)
        self.assertEqual(node4, node1.left)
        self.assertEqual(node3, node1.right)
        self.assertEqual(node7, node15.parent)

        self.assertEqual(key2, node2.key)
        self.assertEqual(node9, node2.left)
        self.assertEqual(node5, node2.right)
        self.assertEqual(node4, node2.parent)

        self.assertEqual(key7, node7.key)
        self.assertEqual(node14, node7.left)
        self.assertEqual(node15, node7.right)
        self.assertEqual(node3, node7.parent)

        self.assertEqual(key4, node4.key)
        self.assertEqual(None, node4.left)
        self.assertEqual(node2, node4.right)
        self.assertEqual(node1, node4.parent)

        self.assertEqual(key5, node5.key)
        self.assertEqual(node10, node5.left)
        self.assertEqual(node11, node5.right)
        self.assertEqual(node2, node5.parent)

        self.assertEqual(key3, node3.key)
        self.assertEqual(node6, node3.left)
        self.assertEqual(node7, node3.right)
        self.assertEqual(node1, node3.parent)

        self.assertEqual(key8, node8.key)
        self.assertEqual(None, node8.left)
        self.assertEqual(node1, node8.right)
        self.assertEqual(None, node8.parent)

        self.assertEqual(key9, node9.key)
        self.assertEqual(None, node9.left)
        self.assertEqual(None, node9.right)
        self.assertEqual(node2, node9.parent)

        self.assertEqual(key10, node10.key)
        self.assertEqual(None, node10.left)
        self.assertEqual(None, node10.right)
        self.assertEqual(node5, node10.parent)

        self.assertEqual(key11, node11.key)
        self.assertEqual(None, node11.left)
        self.assertEqual(None, node11.right)
        self.assertEqual(node5, node11.parent)

        self.assertEqual(key6, node6.key)
        self.assertEqual(node12, node6.left)
        self.assertEqual(node13, node6.right)
        self.assertEqual(node3, node6.parent)

        self.assertEqual(key14, node14.key)
        self.assertEqual(None, node14.left)
        self.assertEqual(None, node14.right)
        self.assertEqual(node7, node14.parent)

        self.assertEqual(key12, node12.key)
        self.assertEqual(None, node12.left)
        self.assertEqual(None, node12.right)
        self.assertEqual(node6, node12.parent)

        self.assertEqual(key13, node13.key)
        self.assertEqual(None, node13.left)
        self.assertEqual(None, node13.right)
        self.assertEqual(node6, node13.parent)

        self.assert_binary_search_properties(root)

    def test_find_on_fifteen_node_tree_with_between_key7_and_key8(self):
        (key1, key2, key3, key4, key5, key6, key7, key8, key9,
         key10, key11, key12, key13, key14, key15,
         node1, node2, node3, node4, node5, node6, node7, node8, node9,
         node10, node11, node12, node13, node14, node15) = \
                                        self.create_complete_fifteen_node_tree()

        root = node1
        search_key = key8 - 1

        node, root = self.tree.find(root, search_key)

        self.assertEqual(node8, node)
        self.assertEqual(node8, root)
        self.assertTrue(search_key < node.key)

        self.assertEqual(key15, node15.key)
        self.assertEqual(None, node15.left)
        self.assertEqual(None, node15.right)
        self.assertEqual(node7, node15.parent)

        self.assertEqual(key1, node1.key)
        self.assertEqual(node4, node1.left)
        self.assertEqual(node3, node1.right)
        self.assertEqual(node7, node15.parent)

        self.assertEqual(key2, node2.key)
        self.assertEqual(node9, node2.left)
        self.assertEqual(node5, node2.right)
        self.assertEqual(node4, node2.parent)

        self.assertEqual(key7, node7.key)
        self.assertEqual(node14, node7.left)
        self.assertEqual(node15, node7.right)
        self.assertEqual(node3, node7.parent)

        self.assertEqual(key4, node4.key)
        self.assertEqual(None, node4.left)
        self.assertEqual(node2, node4.right)
        self.assertEqual(node1, node4.parent)

        self.assertEqual(key5, node5.key)
        self.assertEqual(node10, node5.left)
        self.assertEqual(node11, node5.right)
        self.assertEqual(node2, node5.parent)

        self.assertEqual(key3, node3.key)
        self.assertEqual(node6, node3.left)
        self.assertEqual(node7, node3.right)
        self.assertEqual(node1, node3.parent)

        self.assertEqual(key8, node8.key)
        self.assertEqual(None, node8.left)
        self.assertEqual(node1, node8.right)
        self.assertEqual(None, node8.parent)

        self.assertEqual(key9, node9.key)
        self.assertEqual(None, node9.left)
        self.assertEqual(None, node9.right)
        self.assertEqual(node2, node9.parent)

        self.assertEqual(key10, node10.key)
        self.assertEqual(None, node10.left)
        self.assertEqual(None, node10.right)
        self.assertEqual(node5, node10.parent)

        self.assertEqual(key11, node11.key)
        self.assertEqual(None, node11.left)
        self.assertEqual(None, node11.right)
        self.assertEqual(node5, node11.parent)

        self.assertEqual(key6, node6.key)
        self.assertEqual(node12, node6.left)
        self.assertEqual(node13, node6.right)
        self.assertEqual(node3, node6.parent)

        self.assertEqual(key14, node14.key)
        self.assertEqual(None, node14.left)
        self.assertEqual(None, node14.right)
        self.assertEqual(node7, node14.parent)

        self.assertEqual(key12, node12.key)
        self.assertEqual(None, node12.left)
        self.assertEqual(None, node12.right)
        self.assertEqual(node6, node12.parent)

        self.assertEqual(key13, node13.key)
        self.assertEqual(None, node13.left)
        self.assertEqual(None, node13.right)
        self.assertEqual(node6, node13.parent)

        self.assert_binary_search_properties(root)

    def test_find_on_fifteen_node_tree_with_key7(self):
        (key1, key2, key3, key4, key5, key6, key7, key8, key9,
         key10, key11, key12, key13, key14, key15,
         node1, node2, node3, node4, node5, node6, node7, node8, node9,
         node10, node11, node12, node13, node14, node15) = \
                                        self.create_complete_fifteen_node_tree()

        root = node1
        search_key = key7

        node, root = self.tree.find(root, search_key)

        self.assertEqual(node7, node)
        self.assertEqual(node7, root)
        self.assertEqual(search_key, node.key)

        self.assertEqual(key7, node7.key)
        self.assertEqual(node3, node7.left)
        self.assertEqual(node15, node7.right)
        self.assertEqual(None, node7.parent)

        self.assertEqual(key15, node15.key)
        self.assertEqual(None, node15.left)
        self.assertEqual(None, node15.right)
        self.assertEqual(node7, node15.parent)

        self.assertEqual(key2, node2.key)
        self.assertEqual(node4, node2.left)
        self.assertEqual(node5, node2.right)
        self.assertEqual(node1, node2.parent)

        self.assertEqual(key4, node4.key)
        self.assertEqual(node8, node4.left)
        self.assertEqual(node9, node4.right)
        self.assertEqual(node2, node4.parent)

        self.assertEqual(key5, node5.key)
        self.assertEqual(node10, node5.left)
        self.assertEqual(node11, node5.right)
        self.assertEqual(node2, node5.parent)

        self.assertEqual(key3, node3.key)
        self.assertEqual(node1, node3.left)
        self.assertEqual(node14, node3.right)
        self.assertEqual(node7, node3.parent)

        self.assertEqual(key1, node1.key)
        self.assertEqual(node2, node1.left)
        self.assertEqual(node6, node1.right)
        self.assertEqual(node7, node15.parent)

        self.assertEqual(key8, node8.key)
        self.assertEqual(None, node8.left)
        self.assertEqual(None, node8.right)
        self.assertEqual(node4, node8.parent)

        self.assertEqual(key9, node9.key)
        self.assertEqual(None, node9.left)
        self.assertEqual(None, node9.right)
        self.assertEqual(node4, node9.parent)

        self.assertEqual(key10, node10.key)
        self.assertEqual(None, node10.left)
        self.assertEqual(None, node10.right)
        self.assertEqual(node5, node10.parent)

        self.assertEqual(key11, node11.key)
        self.assertEqual(None, node11.left)
        self.assertEqual(None, node11.right)
        self.assertEqual(node5, node11.parent)

        self.assertEqual(key6, node6.key)
        self.assertEqual(node12, node6.left)
        self.assertEqual(node13, node6.right)
        self.assertEqual(node1, node6.parent)

        self.assertEqual(key14, node14.key)
        self.assertEqual(None, node14.left)
        self.assertEqual(None, node14.right)
        self.assertEqual(node3, node14.parent)

        self.assertEqual(key12, node12.key)
        self.assertEqual(None, node12.left)
        self.assertEqual(None, node12.right)
        self.assertEqual(node6, node12.parent)

        self.assertEqual(key13, node13.key)
        self.assertEqual(None, node13.left)
        self.assertEqual(None, node13.right)
        self.assertEqual(node6, node13.parent)

        self.assert_binary_search_properties(root)

    def test_find_on_fifteen_node_tree_with_between_key6_and_key7(self):
        (key1, key2, key3, key4, key5, key6, key7, key8, key9,
         key10, key11, key12, key13, key14, key15,
         node1, node2, node3, node4, node5, node6, node7, node8, node9,
         node10, node11, node12, node13, node14, node15) = \
                                        self.create_complete_fifteen_node_tree()

        root = node1
        search_key = key7 - 1

        node, root = self.tree.find(root, search_key)

        self.assertEqual(node7, node)
        self.assertEqual(node14, root)
        self.assertTrue(search_key < node.key)

        self.assertEqual(key7, node7.key)
        self.assertEqual(None, node7.left)
        self.assertEqual(node15, node7.right)
        self.assertEqual(node14, node7.parent)

        self.assertEqual(key15, node15.key)
        self.assertEqual(None, node15.left)
        self.assertEqual(None, node15.right)
        self.assertEqual(node7, node15.parent)

        self.assertEqual(key2, node2.key)
        self.assertEqual(node4, node2.left)
        self.assertEqual(node5, node2.right)
        self.assertEqual(node1, node2.parent)

        self.assertEqual(key4, node4.key)
        self.assertEqual(node8, node4.left)
        self.assertEqual(node9, node4.right)
        self.assertEqual(node2, node4.parent)

        self.assertEqual(key5, node5.key)
        self.assertEqual(node10, node5.left)
        self.assertEqual(node11, node5.right)
        self.assertEqual(node2, node5.parent)

        self.assertEqual(key3, node3.key)
        self.assertEqual(node6, node3.left)
        self.assertEqual(None, node3.right)
        self.assertEqual(node1, node3.parent)

        self.assertEqual(key1, node1.key)
        self.assertEqual(node2, node1.left)
        self.assertEqual(node3, node1.right)
        self.assertEqual(node7, node15.parent)

        self.assertEqual(key8, node8.key)
        self.assertEqual(None, node8.left)
        self.assertEqual(None, node8.right)
        self.assertEqual(node4, node8.parent)

        self.assertEqual(key9, node9.key)
        self.assertEqual(None, node9.left)
        self.assertEqual(None, node9.right)
        self.assertEqual(node4, node9.parent)

        self.assertEqual(key10, node10.key)
        self.assertEqual(None, node10.left)
        self.assertEqual(None, node10.right)
        self.assertEqual(node5, node10.parent)

        self.assertEqual(key11, node11.key)
        self.assertEqual(None, node11.left)
        self.assertEqual(None, node11.right)
        self.assertEqual(node5, node11.parent)

        self.assertEqual(key6, node6.key)
        self.assertEqual(node12, node6.left)
        self.assertEqual(node13, node6.right)
        self.assertEqual(node3, node6.parent)

        self.assertEqual(key14, node14.key)
        self.assertEqual(node1, node14.left)
        self.assertEqual(node7, node14.right)
        self.assertEqual(None, node14.parent)

        self.assertEqual(key12, node12.key)
        self.assertEqual(None, node12.left)
        self.assertEqual(None, node12.right)
        self.assertEqual(node6, node12.parent)

        self.assertEqual(key13, node13.key)
        self.assertEqual(None, node13.left)
        self.assertEqual(None, node13.right)
        self.assertEqual(node6, node13.parent)

        self.assert_binary_search_properties(root)

    def test_find_on_fifteen_node_tree_with_key6(self):
        (key1, key2, key3, key4, key5, key6, key7, key8, key9,
         key10, key11, key12, key13, key14, key15,
         node1, node2, node3, node4, node5, node6, node7, node8, node9,
         node10, node11, node12, node13, node14, node15) = \
                                        self.create_complete_fifteen_node_tree()

        root = node1
        search_key = key6

        node, root = self.tree.find(root, search_key)

        self.assertEqual(node6, node)
        self.assertEqual(node6, root)
        self.assertEqual(search_key, node.key)

        self.assertEqual(key7, node7.key)
        self.assertEqual(node14, node7.left)
        self.assertEqual(node15, node7.right)
        self.assertEqual(node3, node7.parent)

        self.assertEqual(key15, node15.key)
        self.assertEqual(None, node15.left)
        self.assertEqual(None, node15.right)
        self.assertEqual(node7, node15.parent)

        self.assertEqual(key2, node2.key)
        self.assertEqual(node4, node2.left)
        self.assertEqual(node5, node2.right)
        self.assertEqual(node1, node2.parent)

        self.assertEqual(key4, node4.key)
        self.assertEqual(node8, node4.left)
        self.assertEqual(node9, node4.right)
        self.assertEqual(node2, node4.parent)

        self.assertEqual(key5, node5.key)
        self.assertEqual(node10, node5.left)
        self.assertEqual(node11, node5.right)
        self.assertEqual(node2, node5.parent)

        self.assertEqual(key3, node3.key)
        self.assertEqual(node13, node3.left)
        self.assertEqual(node7, node3.right)
        self.assertEqual(node6, node3.parent)

        self.assertEqual(key1, node1.key)
        self.assertEqual(node2, node1.left)
        self.assertEqual(node12, node1.right)
        self.assertEqual(node7, node15.parent)

        self.assertEqual(key8, node8.key)
        self.assertEqual(None, node8.left)
        self.assertEqual(None, node8.right)
        self.assertEqual(node4, node8.parent)

        self.assertEqual(key9, node9.key)
        self.assertEqual(None, node9.left)
        self.assertEqual(None, node9.right)
        self.assertEqual(node4, node9.parent)

        self.assertEqual(key10, node10.key)
        self.assertEqual(None, node10.left)
        self.assertEqual(None, node10.right)
        self.assertEqual(node5, node10.parent)

        self.assertEqual(key11, node11.key)
        self.assertEqual(None, node11.left)
        self.assertEqual(None, node11.right)
        self.assertEqual(node5, node11.parent)

        self.assertEqual(key6, node6.key)
        self.assertEqual(node1, node6.left)
        self.assertEqual(node3, node6.right)
        self.assertEqual(None, node6.parent)

        self.assertEqual(key14, node14.key)
        self.assertEqual(None, node14.left)
        self.assertEqual(None, node14.right)
        self.assertEqual(node7, node14.parent)

        self.assertEqual(key12, node12.key)
        self.assertEqual(None, node12.left)
        self.assertEqual(None, node12.right)
        self.assertEqual(node1, node12.parent)

        self.assertEqual(key13, node13.key)
        self.assertEqual(None, node13.left)
        self.assertEqual(None, node13.right)
        self.assertEqual(node3, node13.parent)

        self.assert_binary_search_properties(root)

    def test_find_on_fifteen_node_tree_with_between_key5_and_key6(self):
        (key1, key2, key3, key4, key5, key6, key7, key8, key9,
         key10, key11, key12, key13, key14, key15,
         node1, node2, node3, node4, node5, node6, node7, node8, node9,
         node10, node11, node12, node13, node14, node15) = \
                                        self.create_complete_fifteen_node_tree()

        root = node1
        search_key = key6 - 1

        node, root = self.tree.find(root, search_key)

        self.assertEqual(node6, node)
        self.assertEqual(node12, root)
        self.assertTrue(search_key < node.key)

        self.assertEqual(key7, node7.key)
        self.assertEqual(node14, node7.left)
        self.assertEqual(node15, node7.right)
        self.assertEqual(node3, node7.parent)

        self.assertEqual(key15, node15.key)
        self.assertEqual(None, node15.left)
        self.assertEqual(None, node15.right)
        self.assertEqual(node7, node15.parent)

        self.assertEqual(key2, node2.key)
        self.assertEqual(node4, node2.left)
        self.assertEqual(node5, node2.right)
        self.assertEqual(node1, node2.parent)

        self.assertEqual(key4, node4.key)
        self.assertEqual(node8, node4.left)
        self.assertEqual(node9, node4.right)
        self.assertEqual(node2, node4.parent)

        self.assertEqual(key5, node5.key)
        self.assertEqual(node10, node5.left)
        self.assertEqual(node11, node5.right)
        self.assertEqual(node2, node5.parent)

        self.assertEqual(key3, node3.key)
        self.assertEqual(node13, node3.left)
        self.assertEqual(node7, node3.right)
        self.assertEqual(node6, node3.parent)

        self.assertEqual(key1, node1.key)
        self.assertEqual(node2, node1.left)
        self.assertEqual(None, node1.right)
        self.assertEqual(node7, node15.parent)

        self.assertEqual(key8, node8.key)
        self.assertEqual(None, node8.left)
        self.assertEqual(None, node8.right)
        self.assertEqual(node4, node8.parent)

        self.assertEqual(key9, node9.key)
        self.assertEqual(None, node9.left)
        self.assertEqual(None, node9.right)
        self.assertEqual(node4, node9.parent)

        self.assertEqual(key10, node10.key)
        self.assertEqual(None, node10.left)
        self.assertEqual(None, node10.right)
        self.assertEqual(node5, node10.parent)

        self.assertEqual(key11, node11.key)
        self.assertEqual(None, node11.left)
        self.assertEqual(None, node11.right)
        self.assertEqual(node5, node11.parent)

        self.assertEqual(key6, node6.key)
        self.assertEqual(None, node6.left)
        self.assertEqual(node3, node6.right)
        self.assertEqual(node12, node6.parent)

        self.assertEqual(key14, node14.key)
        self.assertEqual(None, node14.left)
        self.assertEqual(None, node14.right)
        self.assertEqual(node7, node14.parent)

        self.assertEqual(key12, node12.key)
        self.assertEqual(node1, node12.left)
        self.assertEqual(node6, node12.right)
        self.assertEqual(None, node12.parent)

        self.assertEqual(key13, node13.key)
        self.assertEqual(None, node13.left)
        self.assertEqual(None, node13.right)
        self.assertEqual(node3, node13.parent)

        self.assert_binary_search_properties(root)

    def test_find_on_fifteen_node_tree_with_key5(self):
        (key1, key2, key3, key4, key5, key6, key7, key8, key9,
         key10, key11, key12, key13, key14, key15,
         node1, node2, node3, node4, node5, node6, node7, node8, node9,
         node10, node11, node12, node13, node14, node15) = \
                                        self.create_complete_fifteen_node_tree()

        root = node1
        search_key = key5

        node, root = self.tree.find(root, search_key)

        self.assertEqual(node5, node)
        self.assertEqual(node5, root)
        self.assertEqual(search_key, node.key)

        self.assertEqual(key7, node7.key)
        self.assertEqual(node14, node7.left)
        self.assertEqual(node15, node7.right)
        self.assertEqual(node3, node7.parent)

        self.assertEqual(key15, node15.key)
        self.assertEqual(None, node15.left)
        self.assertEqual(None, node15.right)
        self.assertEqual(node7, node15.parent)

        self.assertEqual(key2, node2.key)
        self.assertEqual(node4, node2.left)
        self.assertEqual(node10, node2.right)
        self.assertEqual(node5, node2.parent)

        self.assertEqual(key4, node4.key)
        self.assertEqual(node8, node4.left)
        self.assertEqual(node9, node4.right)
        self.assertEqual(node2, node4.parent)

        self.assertEqual(key5, node5.key)
        self.assertEqual(node2, node5.left)
        self.assertEqual(node1, node5.right)
        self.assertEqual(None, node5.parent)

        self.assertEqual(key3, node3.key)
        self.assertEqual(node6, node3.left)
        self.assertEqual(node7, node3.right)
        self.assertEqual(node1, node3.parent)

        self.assertEqual(key1, node1.key)
        self.assertEqual(node11, node1.left)
        self.assertEqual(node3, node1.right)
        self.assertEqual(node7, node15.parent)

        self.assertEqual(key8, node8.key)
        self.assertEqual(None, node8.left)
        self.assertEqual(None, node8.right)
        self.assertEqual(node4, node8.parent)

        self.assertEqual(key9, node9.key)
        self.assertEqual(None, node9.left)
        self.assertEqual(None, node9.right)
        self.assertEqual(node4, node9.parent)

        self.assertEqual(key10, node10.key)
        self.assertEqual(None, node10.left)
        self.assertEqual(None, node10.right)
        self.assertEqual(node2, node10.parent)

        self.assertEqual(key11, node11.key)
        self.assertEqual(None, node11.left)
        self.assertEqual(None, node11.right)
        self.assertEqual(node1, node11.parent)

        self.assertEqual(key6, node6.key)
        self.assertEqual(node12, node6.left)
        self.assertEqual(node13, node6.right)
        self.assertEqual(node3, node6.parent)

        self.assertEqual(key14, node14.key)
        self.assertEqual(None, node14.left)
        self.assertEqual(None, node14.right)
        self.assertEqual(node7, node14.parent)

        self.assertEqual(key12, node12.key)
        self.assertEqual(None, node12.left)
        self.assertEqual(None, node12.right)
        self.assertEqual(node6, node12.parent)

        self.assertEqual(key13, node13.key)
        self.assertEqual(None, node13.left)
        self.assertEqual(None, node13.right)
        self.assertEqual(node6, node13.parent)

        self.assert_binary_search_properties(root)

    def test_find_on_fifteen_node_tree_with_between_key4_and_key5(self):
        (key1, key2, key3, key4, key5, key6, key7, key8, key9,
         key10, key11, key12, key13, key14, key15,
         node1, node2, node3, node4, node5, node6, node7, node8, node9,
         node10, node11, node12, node13, node14, node15) = \
                                        self.create_complete_fifteen_node_tree()

        root = node1
        search_key = key5 - 1

        node, root = self.tree.find(root, search_key)

        self.assertEqual(node5, node)
        self.assertEqual(node10, root)
        self.assertTrue(search_key < node.key)

        self.assertEqual(key7, node7.key)
        self.assertEqual(node14, node7.left)
        self.assertEqual(node15, node7.right)
        self.assertEqual(node3, node7.parent)

        self.assertEqual(key15, node15.key)
        self.assertEqual(None, node15.left)
        self.assertEqual(None, node15.right)
        self.assertEqual(node7, node15.parent)

        self.assertEqual(key2, node2.key)
        self.assertEqual(node4, node2.left)
        self.assertEqual(None, node2.right)
        self.assertEqual(node10, node2.parent)

        self.assertEqual(key4, node4.key)
        self.assertEqual(node8, node4.left)
        self.assertEqual(node9, node4.right)
        self.assertEqual(node2, node4.parent)

        self.assertEqual(key5, node5.key)
        self.assertEqual(None, node5.left)
        self.assertEqual(node11, node5.right)
        self.assertEqual(node1, node5.parent)

        self.assertEqual(key3, node3.key)
        self.assertEqual(node6, node3.left)
        self.assertEqual(node7, node3.right)
        self.assertEqual(node1, node3.parent)

        self.assertEqual(key1, node1.key)
        self.assertEqual(node5, node1.left)
        self.assertEqual(node3, node1.right)
        self.assertEqual(node7, node15.parent)

        self.assertEqual(key8, node8.key)
        self.assertEqual(None, node8.left)
        self.assertEqual(None, node8.right)
        self.assertEqual(node4, node8.parent)

        self.assertEqual(key9, node9.key)
        self.assertEqual(None, node9.left)
        self.assertEqual(None, node9.right)
        self.assertEqual(node4, node9.parent)

        self.assertEqual(key10, node10.key)
        self.assertEqual(node2, node10.left)
        self.assertEqual(node1, node10.right)
        self.assertEqual(None, node10.parent)

        self.assertEqual(key11, node11.key)
        self.assertEqual(None, node11.left)
        self.assertEqual(None, node11.right)
        self.assertEqual(node5, node11.parent)

        self.assertEqual(key6, node6.key)
        self.assertEqual(node12, node6.left)
        self.assertEqual(node13, node6.right)
        self.assertEqual(node3, node6.parent)

        self.assertEqual(key14, node14.key)
        self.assertEqual(None, node14.left)
        self.assertEqual(None, node14.right)
        self.assertEqual(node7, node14.parent)

        self.assertEqual(key12, node12.key)
        self.assertEqual(None, node12.left)
        self.assertEqual(None, node12.right)
        self.assertEqual(node6, node12.parent)

        self.assertEqual(key13, node13.key)
        self.assertEqual(None, node13.left)
        self.assertEqual(None, node13.right)
        self.assertEqual(node6, node13.parent)

        self.assert_binary_search_properties(root)

    def test_find_on_fifteen_node_tree_with_key4(self):
        (key1, key2, key3, key4, key5, key6, key7, key8, key9,
         key10, key11, key12, key13, key14, key15,
         node1, node2, node3, node4, node5, node6, node7, node8, node9,
         node10, node11, node12, node13, node14, node15) = \
                                        self.create_complete_fifteen_node_tree()

        root = node1
        search_key = key4

        node, root = self.tree.find(root, search_key)

        self.assertEqual(node4, node)
        self.assertEqual(node4, root)
        self.assertEqual(search_key, node.key)

        self.assertEqual(key7, node7.key)
        self.assertEqual(node14, node7.left)
        self.assertEqual(node15, node7.right)
        self.assertEqual(node3, node7.parent)

        self.assertEqual(key15, node15.key)
        self.assertEqual(None, node15.left)
        self.assertEqual(None, node15.right)
        self.assertEqual(node7, node15.parent)

        self.assertEqual(key2, node2.key)
        self.assertEqual(node9, node2.left)
        self.assertEqual(node1, node2.right)
        self.assertEqual(node4, node2.parent)

        self.assertEqual(key4, node4.key)
        self.assertEqual(node8, node4.left)
        self.assertEqual(node2, node4.right)
        self.assertEqual(None, node4.parent)

        self.assertEqual(key5, node5.key)
        self.assertEqual(node10, node5.left)
        self.assertEqual(node11, node5.right)
        self.assertEqual(node1, node5.parent)

        self.assertEqual(key3, node3.key)
        self.assertEqual(node6, node3.left)
        self.assertEqual(node7, node3.right)
        self.assertEqual(node1, node3.parent)

        self.assertEqual(key1, node1.key)
        self.assertEqual(node5, node1.left)
        self.assertEqual(node3, node1.right)
        self.assertEqual(node7, node15.parent)

        self.assertEqual(key8, node8.key)
        self.assertEqual(None, node8.left)
        self.assertEqual(None, node8.right)
        self.assertEqual(node4, node8.parent)

        self.assertEqual(key9, node9.key)
        self.assertEqual(None, node9.left)
        self.assertEqual(None, node9.right)
        self.assertEqual(node2, node9.parent)

        self.assertEqual(key10, node10.key)
        self.assertEqual(None, node10.left)
        self.assertEqual(None, node10.right)
        self.assertEqual(node5, node10.parent)

        self.assertEqual(key11, node11.key)
        self.assertEqual(None, node11.left)
        self.assertEqual(None, node11.right)
        self.assertEqual(node5, node11.parent)

        self.assertEqual(key6, node6.key)
        self.assertEqual(node12, node6.left)
        self.assertEqual(node13, node6.right)
        self.assertEqual(node3, node6.parent)

        self.assertEqual(key14, node14.key)
        self.assertEqual(None, node14.left)
        self.assertEqual(None, node14.right)
        self.assertEqual(node7, node14.parent)

        self.assertEqual(key12, node12.key)
        self.assertEqual(None, node12.left)
        self.assertEqual(None, node12.right)
        self.assertEqual(node6, node12.parent)

        self.assertEqual(key13, node13.key)
        self.assertEqual(None, node13.left)
        self.assertEqual(None, node13.right)
        self.assertEqual(node6, node13.parent)

        self.assert_binary_search_properties(root)

    def test_find_on_fifteen_node_tree_with_between_key3_and_key4(self):
        (key1, key2, key3, key4, key5, key6, key7, key8, key9,
         key10, key11, key12, key13, key14, key15,
         node1, node2, node3, node4, node5, node6, node7, node8, node9,
         node10, node11, node12, node13, node14, node15) = \
                                        self.create_complete_fifteen_node_tree()

        root = node1
        search_key = key4 - 1

        node, root = self.tree.find(root, search_key)

        self.assertEqual(node4, node)
        self.assertEqual(node8, root)
        self.assertTrue(search_key < node.key)

        self.assertEqual(key7, node7.key)
        self.assertEqual(node14, node7.left)
        self.assertEqual(node15, node7.right)
        self.assertEqual(node3, node7.parent)

        self.assertEqual(key15, node15.key)
        self.assertEqual(None, node15.left)
        self.assertEqual(None, node15.right)
        self.assertEqual(node7, node15.parent)

        self.assertEqual(key2, node2.key)
        self.assertEqual(node9, node2.left)
        self.assertEqual(node5, node2.right)
        self.assertEqual(node4, node2.parent)

        self.assertEqual(key4, node4.key)
        self.assertEqual(None, node4.left)
        self.assertEqual(node2, node4.right)
        self.assertEqual(node1, node4.parent)

        self.assertEqual(key5, node5.key)
        self.assertEqual(node10, node5.left)
        self.assertEqual(node11, node5.right)
        self.assertEqual(node2, node5.parent)

        self.assertEqual(key3, node3.key)
        self.assertEqual(node6, node3.left)
        self.assertEqual(node7, node3.right)
        self.assertEqual(node1, node3.parent)

        self.assertEqual(key1, node1.key)
        self.assertEqual(node4, node1.left)
        self.assertEqual(node3, node1.right)
        self.assertEqual(node7, node15.parent)

        self.assertEqual(key8, node8.key)
        self.assertEqual(None, node8.left)
        self.assertEqual(node1, node8.right)
        self.assertEqual(None, node8.parent)

        self.assertEqual(key9, node9.key)
        self.assertEqual(None, node9.left)
        self.assertEqual(None, node9.right)
        self.assertEqual(node2, node9.parent)

        self.assertEqual(key10, node10.key)
        self.assertEqual(None, node10.left)
        self.assertEqual(None, node10.right)
        self.assertEqual(node5, node10.parent)

        self.assertEqual(key11, node11.key)
        self.assertEqual(None, node11.left)
        self.assertEqual(None, node11.right)
        self.assertEqual(node5, node11.parent)

        self.assertEqual(key6, node6.key)
        self.assertEqual(node12, node6.left)
        self.assertEqual(node13, node6.right)
        self.assertEqual(node3, node6.parent)

        self.assertEqual(key14, node14.key)
        self.assertEqual(None, node14.left)
        self.assertEqual(None, node14.right)
        self.assertEqual(node7, node14.parent)

        self.assertEqual(key12, node12.key)
        self.assertEqual(None, node12.left)
        self.assertEqual(None, node12.right)
        self.assertEqual(node6, node12.parent)

        self.assertEqual(key13, node13.key)
        self.assertEqual(None, node13.left)
        self.assertEqual(None, node13.right)
        self.assertEqual(node6, node13.parent)

        self.assert_binary_search_properties(root)

    def test_find_on_fifteen_node_tree_with_key3(self):
        (key1, key2, key3, key4, key5, key6, key7, key8, key9,
         key10, key11, key12, key13, key14, key15,
         node1, node2, node3, node4, node5, node6, node7, node8, node9,
         node10, node11, node12, node13, node14, node15) = \
                                        self.create_complete_fifteen_node_tree()

        root = node1
        search_key = key3

        node, root = self.tree.find(root, search_key)

        self.assertEqual(node3, node)
        self.assertEqual(node3, root)
        self.assertEqual(search_key, node.key)

        self.assertEqual(key7, node7.key)
        self.assertEqual(node14, node7.left)
        self.assertEqual(node15, node7.right)
        self.assertEqual(node3, node7.parent)

        self.assertEqual(key15, node15.key)
        self.assertEqual(None, node15.left)
        self.assertEqual(None, node15.right)
        self.assertEqual(node7, node15.parent)

        self.assertEqual(key2, node2.key)
        self.assertEqual(node4, node2.left)
        self.assertEqual(node5, node2.right)
        self.assertEqual(node1, node2.parent)

        self.assertEqual(key4, node4.key)
        self.assertEqual(node8, node4.left)
        self.assertEqual(node9, node4.right)
        self.assertEqual(node2, node4.parent)

        self.assertEqual(key5, node5.key)
        self.assertEqual(node10, node5.left)
        self.assertEqual(node11, node5.right)
        self.assertEqual(node2, node5.parent)

        self.assertEqual(key3, node3.key)
        self.assertEqual(node1, node3.left)
        self.assertEqual(node7, node3.right)
        self.assertEqual(None, node3.parent)

        self.assertEqual(key1, node1.key)
        self.assertEqual(node2, node1.left)
        self.assertEqual(node6, node1.right)
        self.assertEqual(node7, node15.parent)

        self.assertEqual(key8, node8.key)
        self.assertEqual(None, node8.left)
        self.assertEqual(None, node8.right)
        self.assertEqual(node4, node8.parent)

        self.assertEqual(key9, node9.key)
        self.assertEqual(None, node9.left)
        self.assertEqual(None, node9.right)
        self.assertEqual(node4, node9.parent)

        self.assertEqual(key10, node10.key)
        self.assertEqual(None, node10.left)
        self.assertEqual(None, node10.right)
        self.assertEqual(node5, node10.parent)

        self.assertEqual(key11, node11.key)
        self.assertEqual(None, node11.left)
        self.assertEqual(None, node11.right)
        self.assertEqual(node5, node11.parent)

        self.assertEqual(key6, node6.key)
        self.assertEqual(node12, node6.left)
        self.assertEqual(node13, node6.right)
        self.assertEqual(node1, node6.parent)

        self.assertEqual(key14, node14.key)
        self.assertEqual(None, node14.left)
        self.assertEqual(None, node14.right)
        self.assertEqual(node7, node14.parent)

        self.assertEqual(key12, node12.key)
        self.assertEqual(None, node12.left)
        self.assertEqual(None, node12.right)
        self.assertEqual(node6, node12.parent)

        self.assertEqual(key13, node13.key)
        self.assertEqual(None, node13.left)
        self.assertEqual(None, node13.right)
        self.assertEqual(node6, node13.parent)

        self.assert_binary_search_properties(root)

    def test_find_on_fifteen_node_tree_with_between_key2_and_key3(self):
        (key1, key2, key3, key4, key5, key6, key7, key8, key9,
         key10, key11, key12, key13, key14, key15,
         node1, node2, node3, node4, node5, node6, node7, node8, node9,
         node10, node11, node12, node13, node14, node15) = \
                                        self.create_complete_fifteen_node_tree()

        root = node1
        search_key = key3 - 1

        node, root = self.tree.find(root, search_key)

        self.assertEqual(node3, node)
        self.assertEqual(node13, root)
        self.assertTrue(search_key < node.key)

        self.assertEqual(key7, node7.key)
        self.assertEqual(node14, node7.left)
        self.assertEqual(node15, node7.right)
        self.assertEqual(node3, node7.parent)

        self.assertEqual(key15, node15.key)
        self.assertEqual(None, node15.left)
        self.assertEqual(None, node15.right)
        self.assertEqual(node7, node15.parent)

        self.assertEqual(key2, node2.key)
        self.assertEqual(node4, node2.left)
        self.assertEqual(node5, node2.right)
        self.assertEqual(node1, node2.parent)

        self.assertEqual(key4, node4.key)
        self.assertEqual(node8, node4.left)
        self.assertEqual(node9, node4.right)
        self.assertEqual(node2, node4.parent)

        self.assertEqual(key5, node5.key)
        self.assertEqual(node10, node5.left)
        self.assertEqual(node11, node5.right)
        self.assertEqual(node2, node5.parent)

        self.assertEqual(key3, node3.key)
        self.assertEqual(None, node3.left)
        self.assertEqual(node7, node3.right)
        self.assertEqual(node13, node3.parent)

        self.assertEqual(key1, node1.key)
        self.assertEqual(node2, node1.left)
        self.assertEqual(node6, node1.right)
        self.assertEqual(node7, node15.parent)

        self.assertEqual(key8, node8.key)
        self.assertEqual(None, node8.left)
        self.assertEqual(None, node8.right)
        self.assertEqual(node4, node8.parent)

        self.assertEqual(key9, node9.key)
        self.assertEqual(None, node9.left)
        self.assertEqual(None, node9.right)
        self.assertEqual(node4, node9.parent)

        self.assertEqual(key10, node10.key)
        self.assertEqual(None, node10.left)
        self.assertEqual(None, node10.right)
        self.assertEqual(node5, node10.parent)

        self.assertEqual(key11, node11.key)
        self.assertEqual(None, node11.left)
        self.assertEqual(None, node11.right)
        self.assertEqual(node5, node11.parent)

        self.assertEqual(key6, node6.key)
        self.assertEqual(node12, node6.left)
        self.assertEqual(None, node6.right)
        self.assertEqual(node1, node6.parent)

        self.assertEqual(key14, node14.key)
        self.assertEqual(None, node14.left)
        self.assertEqual(None, node14.right)
        self.assertEqual(node7, node14.parent)

        self.assertEqual(key12, node12.key)
        self.assertEqual(None, node12.left)
        self.assertEqual(None, node12.right)
        self.assertEqual(node6, node12.parent)

        self.assertEqual(key13, node13.key)
        self.assertEqual(node1, node13.left)
        self.assertEqual(node3, node13.right)

        self.assert_binary_search_properties(root)

    def test_find_on_fifteen_node_tree_with_key2(self):
        (key1, key2, key3, key4, key5, key6, key7, key8, key9,
         key10, key11, key12, key13, key14, key15,
         node1, node2, node3, node4, node5, node6, node7, node8, node9,
         node10, node11, node12, node13, node14, node15) = \
                                        self.create_complete_fifteen_node_tree()

        root = node1
        search_key = key2

        node, root = self.tree.find(root, search_key)

        self.assertEqual(node2, node)
        self.assertEqual(node2, root)
        self.assertEqual(search_key, node.key)

        self.assertEqual(key7, node7.key)
        self.assertEqual(node14, node7.left)
        self.assertEqual(node15, node7.right)
        self.assertEqual(node3, node7.parent)

        self.assertEqual(key15, node15.key)
        self.assertEqual(None, node15.left)
        self.assertEqual(None, node15.right)
        self.assertEqual(node7, node15.parent)

        self.assertEqual(key2, node2.key)
        self.assertEqual(node4, node2.left)
        self.assertEqual(node1, node2.right)
        self.assertEqual(None, node2.parent)

        self.assertEqual(key4, node4.key)
        self.assertEqual(node8, node4.left)
        self.assertEqual(node9, node4.right)
        self.assertEqual(node2, node4.parent)

        self.assertEqual(key5, node5.key)
        self.assertEqual(node10, node5.left)
        self.assertEqual(node11, node5.right)
        self.assertEqual(node1, node5.parent)

        self.assertEqual(key3, node3.key)
        self.assertEqual(node6, node3.left)
        self.assertEqual(node7, node3.right)
        self.assertEqual(node1, node3.parent)

        self.assertEqual(key1, node1.key)
        self.assertEqual(node5, node1.left)
        self.assertEqual(node3, node1.right)
        self.assertEqual(node7, node15.parent)

        self.assertEqual(key8, node8.key)
        self.assertEqual(None, node8.left)
        self.assertEqual(None, node8.right)
        self.assertEqual(node4, node8.parent)

        self.assertEqual(key9, node9.key)
        self.assertEqual(None, node9.left)
        self.assertEqual(None, node9.right)
        self.assertEqual(node4, node9.parent)

        self.assertEqual(key10, node10.key)
        self.assertEqual(None, node10.left)
        self.assertEqual(None, node10.right)
        self.assertEqual(node5, node10.parent)

        self.assertEqual(key11, node11.key)
        self.assertEqual(None, node11.left)
        self.assertEqual(None, node11.right)
        self.assertEqual(node5, node11.parent)

        self.assertEqual(key6, node6.key)
        self.assertEqual(node12, node6.left)
        self.assertEqual(node13, node6.right)
        self.assertEqual(node3, node6.parent)

        self.assertEqual(key14, node14.key)
        self.assertEqual(None, node14.left)
        self.assertEqual(None, node14.right)
        self.assertEqual(node7, node14.parent)

        self.assertEqual(key12, node12.key)
        self.assertEqual(None, node12.left)
        self.assertEqual(None, node12.right)
        self.assertEqual(node6, node12.parent)

        self.assertEqual(key13, node13.key)
        self.assertEqual(None, node13.left)
        self.assertEqual(None, node13.right)

        self.assert_binary_search_properties(root)

    def test_find_on_fifteen_node_tree_with_between_key1_and_key2(self):
        (key1, key2, key3, key4, key5, key6, key7, key8, key9,
         key10, key11, key12, key13, key14, key15,
         node1, node2, node3, node4, node5, node6, node7, node8, node9,
         node10, node11, node12, node13, node14, node15) = \
                                        self.create_complete_fifteen_node_tree()

        root = node1
        search_key = key2 - 1

        node, root = self.tree.find(root, search_key)

        self.assertEqual(node2, node)
        self.assertEqual(node9, root)
        self.assertTrue(search_key < node.key)

        self.assertEqual(key7, node7.key)
        self.assertEqual(node14, node7.left)
        self.assertEqual(node15, node7.right)
        self.assertEqual(node3, node7.parent)

        self.assertEqual(key15, node15.key)
        self.assertEqual(None, node15.left)
        self.assertEqual(None, node15.right)
        self.assertEqual(node7, node15.parent)

        self.assertEqual(key2, node2.key)
        self.assertEqual(None, node2.left)
        self.assertEqual(node5, node2.right)
        self.assertEqual(node1, node2.parent)

        self.assertEqual(key4, node4.key)
        self.assertEqual(node8, node4.left)
        self.assertEqual(None, node4.right)
        self.assertEqual(node9, node4.parent)

        self.assertEqual(key5, node5.key)
        self.assertEqual(node10, node5.left)
        self.assertEqual(node11, node5.right)
        self.assertEqual(node2, node5.parent)

        self.assertEqual(key3, node3.key)
        self.assertEqual(node6, node3.left)
        self.assertEqual(node7, node3.right)
        self.assertEqual(node1, node3.parent)

        self.assertEqual(key1, node1.key)
        self.assertEqual(node2, node1.left)
        self.assertEqual(node3, node1.right)
        self.assertEqual(node7, node15.parent)

        self.assertEqual(key8, node8.key)
        self.assertEqual(None, node8.left)
        self.assertEqual(None, node8.right)
        self.assertEqual(node4, node8.parent)

        self.assertEqual(key9, node9.key)
        self.assertEqual(node4, node9.left)
        self.assertEqual(node1, node9.right)
        self.assertEqual(None, node9.parent)

        self.assertEqual(key10, node10.key)
        self.assertEqual(None, node10.left)
        self.assertEqual(None, node10.right)
        self.assertEqual(node5, node10.parent)

        self.assertEqual(key11, node11.key)
        self.assertEqual(None, node11.left)
        self.assertEqual(None, node11.right)
        self.assertEqual(node5, node11.parent)

        self.assertEqual(key6, node6.key)
        self.assertEqual(node12, node6.left)
        self.assertEqual(node13, node6.right)
        self.assertEqual(node3, node6.parent)

        self.assertEqual(key14, node14.key)
        self.assertEqual(None, node14.left)
        self.assertEqual(None, node14.right)
        self.assertEqual(node7, node14.parent)

        self.assertEqual(key12, node12.key)
        self.assertEqual(None, node12.left)
        self.assertEqual(None, node12.right)
        self.assertEqual(node6, node12.parent)

        self.assertEqual(key13, node13.key)
        self.assertEqual(None, node13.left)
        self.assertEqual(None, node13.right)

        self.assert_binary_search_properties(root)

    def test_find_on_fifteen_node_tree_with_key1(self):
        (key1, key2, key3, key4, key5, key6, key7, key8, key9,
         key10, key11, key12, key13, key14, key15,
         node1, node2, node3, node4, node5, node6, node7, node8, node9,
         node10, node11, node12, node13, node14, node15) = \
                                        self.create_complete_fifteen_node_tree()

        root = node1
        search_key = key1

        node, root = self.tree.find(root, search_key)

        self.assertEqual(node1, node)
        self.assertEqual(node1, root)
        self.assertEqual(search_key, node.key)

        self.assertEqual(key7, node7.key)
        self.assertEqual(node14, node7.left)
        self.assertEqual(node15, node7.right)
        self.assertEqual(node3, node7.parent)

        self.assertEqual(key15, node15.key)
        self.assertEqual(None, node15.left)
        self.assertEqual(None, node15.right)
        self.assertEqual(node7, node15.parent)

        self.assertEqual(key2, node2.key)
        self.assertEqual(node4, node2.left)
        self.assertEqual(node5, node2.right)
        self.assertEqual(node1, node2.parent)

        self.assertEqual(key4, node4.key)
        self.assertEqual(node8, node4.left)
        self.assertEqual(node9, node4.right)
        self.assertEqual(node2, node4.parent)

        self.assertEqual(key5, node5.key)
        self.assertEqual(node10, node5.left)
        self.assertEqual(node11, node5.right)
        self.assertEqual(node2, node5.parent)

        self.assertEqual(key3, node3.key)
        self.assertEqual(node6, node3.left)
        self.assertEqual(node7, node3.right)
        self.assertEqual(node1, node3.parent)

        self.assertEqual(key1, node1.key)
        self.assertEqual(node2, node1.left)
        self.assertEqual(node3, node1.right)
        self.assertEqual(node7, node15.parent)

        self.assertEqual(key8, node8.key)
        self.assertEqual(None, node8.left)
        self.assertEqual(None, node8.right)
        self.assertEqual(node4, node8.parent)

        self.assertEqual(key9, node9.key)
        self.assertEqual(None, node9.left)
        self.assertEqual(None, node9.right)
        self.assertEqual(node4, node9.parent)

        self.assertEqual(key10, node10.key)
        self.assertEqual(None, node10.left)
        self.assertEqual(None, node10.right)
        self.assertEqual(node5, node10.parent)

        self.assertEqual(key11, node11.key)
        self.assertEqual(None, node11.left)
        self.assertEqual(None, node11.right)
        self.assertEqual(node5, node11.parent)

        self.assertEqual(key6, node6.key)
        self.assertEqual(node12, node6.left)
        self.assertEqual(node13, node6.right)
        self.assertEqual(node3, node6.parent)

        self.assertEqual(key14, node14.key)
        self.assertEqual(None, node14.left)
        self.assertEqual(None, node14.right)
        self.assertEqual(node7, node14.parent)

        self.assertEqual(key12, node12.key)
        self.assertEqual(None, node12.left)
        self.assertEqual(None, node12.right)
        self.assertEqual(node6, node12.parent)

        self.assertEqual(key13, node13.key)
        self.assertEqual(None, node13.left)
        self.assertEqual(None, node13.right)

        self.assert_binary_search_properties(root)

    def test_split_with_none_and_key(self):
        root, search_key = None, 1

        left, right = self.tree.split(root, search_key)

        self.assertEqual(None, left)
        self.assertEqual(None, right)

    def test_split_on_parentless_node_with_existing_key(self):
        key, root = self.create_one_node_tree()

        search_key = key

        left, right = self.tree.split(root, search_key)

        self.assertEqual(None, left)
        self.assertEqual(root, right)

        self.assertEqual(key, root.key)
        self.assertEqual(None, root.left)
        self.assertEqual(None, root.right)
        self.assertEqual(None, root.parent)

        self.assert_binary_search_properties(right)

    def test_split_on_parentless_node_with_missing_key_as_lesser(self):
        key, root = self.create_one_node_tree()

        search_key = key - 1

        left, right = self.tree.split(root, search_key)

        self.assertEqual(None, left)
        self.assertEqual(root, right)

        self.assertEqual(key, root.key)
        self.assertEqual(None, root.left)
        self.assertEqual(None, root.right)
        self.assertEqual(None, root.parent)

        self.assert_binary_search_properties(right)

    def test_split_on_parentless_node_with_missing_key_as_larger(self):
        key, root = self.create_one_node_tree()

        search_key = key + 1

        left, right = self.tree.split(root, search_key)

        self.assertEqual(root, left)
        self.assertEqual(None, right)

        self.assertEqual(key, root.key)
        self.assertEqual(None, root.left)
        self.assertEqual(None, root.right)
        self.assertEqual(None, root.parent)

        self.assert_binary_search_properties(left)

    def test_split_on_fifteen_node_tree_with_root_key(self):
        (key1, key2, key3, key4, key5, key6, key7, key8, key9,
         key10, key11, key12, key13, key14, key15,
         node1, node2, node3, node4, node5, node6, node7, node8, node9,
         node10, node11, node12, node13, node14, node15) = \
                                        self.create_complete_fifteen_node_tree()

        root = node1
        search_key = key1

        left, right = self.tree.split(root, search_key)

        self.assertEqual(node2, left)
        self.assertEqual(node1, right)

        self.assertEqual(key1, node1.key)
        self.assertEqual(None, node1.left)
        self.assertEqual(node3, node1.right)
        self.assertEqual(None, node1.parent)

        self.assertEqual(key2, node2.key)
        self.assertEqual(node4, node2.left)
        self.assertEqual(node5, node2.right)
        self.assertEqual(None, node2.parent)

        self.assertEqual(key3, node3.key)
        self.assertEqual(node6, node3.left)
        self.assertEqual(node7, node3.right)
        self.assertEqual(node1, node3.parent)

        self.assertEqual(key4, node4.key)
        self.assertEqual(node8, node4.left)
        self.assertEqual(node9, node4.right)
        self.assertEqual(node2, node4.parent)

        self.assertEqual(key5, node5.key)
        self.assertEqual(node10, node5.left)
        self.assertEqual(node11, node5.right)
        self.assertEqual(node2, node5.parent)

        self.assertEqual(key6, node6.key)
        self.assertEqual(node12, node6.left)
        self.assertEqual(node13, node6.right)
        self.assertEqual(node3, node6.parent)

        self.assertEqual(key7, node7.key)
        self.assertEqual(node14, node7.left)
        self.assertEqual(node15, node7.right)
        self.assertEqual(node3, node7.parent)

        self.assertEqual(key8, node8.key)
        self.assertEqual(None, node8.left)
        self.assertEqual(None, node8.right)
        self.assertEqual(node4, node8.parent)

        self.assertEqual(key9, node9.key)
        self.assertEqual(None, node9.left)
        self.assertEqual(None, node9.right)
        self.assertEqual(node4, node9.parent)

        self.assertEqual(key10, node10.key)
        self.assertEqual(None, node10.left)
        self.assertEqual(None, node10.right)
        self.assertEqual(node5, node10.parent)

        self.assertEqual(key11, node11.key)
        self.assertEqual(None, node11.left)
        self.assertEqual(None, node11.right)
        self.assertEqual(node5, node11.parent)

        self.assertEqual(key12, node12.key)
        self.assertEqual(None, node12.left)
        self.assertEqual(None, node12.right)
        self.assertEqual(node6, node12.parent)

        self.assertEqual(key13, node13.key)
        self.assertEqual(None, node13.left)
        self.assertEqual(None, node13.right)
        self.assertEqual(node6, node13.parent)

        self.assertEqual(key14, node14.key)
        self.assertEqual(None, node14.left)
        self.assertEqual(None, node14.right)
        self.assertEqual(node7, node14.parent)

        self.assertEqual(key15, node15.key)
        self.assertEqual(None, node15.left)
        self.assertEqual(None, node15.right)
        self.assertEqual(node7, node15.parent)

        self.assert_binary_search_properties(left)
        self.assert_binary_search_properties(right)

        self.assert_left_tree_less_than_right_tree(left, right)

    def test_split_on_fifteen_node_tree_with_key_less_than_least(self):
        (key1, key2, key3, key4, key5, key6, key7, key8, key9,
         key10, key11, key12, key13, key14, key15,
         node1, node2, node3, node4, node5, node6, node7, node8, node9,
         node10, node11, node12, node13, node14, node15) = \
                                        self.create_complete_fifteen_node_tree()

        root = node1
        search_key = key8 - 1

        left, right = self.tree.split(root, search_key)

        self.assertEqual(None, left)
        self.assertEqual(node8, right)

        self.assertEqual(key1, node1.key)
        self.assertEqual(node4, node1.left)
        self.assertEqual(node3, node1.right)
        self.assertEqual(node8, node1.parent)

        self.assertEqual(key2, node2.key)
        self.assertEqual(node9, node2.left)
        self.assertEqual(node5, node2.right)
        self.assertEqual(node4, node2.parent)

        self.assertEqual(key3, node3.key)
        self.assertEqual(node6, node3.left)
        self.assertEqual(node7, node3.right)
        self.assertEqual(node1, node3.parent)

        self.assertEqual(key4, node4.key)
        self.assertEqual(None, node4.left)
        self.assertEqual(node2, node4.right)
        self.assertEqual(node1, node4.parent)

        self.assertEqual(key5, node5.key)
        self.assertEqual(node10, node5.left)
        self.assertEqual(node11, node5.right)
        self.assertEqual(node2, node5.parent)

        self.assertEqual(key6, node6.key)
        self.assertEqual(node12, node6.left)
        self.assertEqual(node13, node6.right)
        self.assertEqual(node3, node6.parent)

        self.assertEqual(key7, node7.key)
        self.assertEqual(node14, node7.left)
        self.assertEqual(node15, node7.right)
        self.assertEqual(node3, node7.parent)

        self.assertEqual(key8, node8.key)
        self.assertEqual(None, node8.left)
        self.assertEqual(node1, node8.right)
        self.assertEqual(None, node8.parent)

        self.assertEqual(key9, node9.key)
        self.assertEqual(None, node9.left)
        self.assertEqual(None, node9.right)
        self.assertEqual(node2, node9.parent)

        self.assertEqual(key10, node10.key)
        self.assertEqual(None, node10.left)
        self.assertEqual(None, node10.right)
        self.assertEqual(node5, node10.parent)

        self.assertEqual(key11, node11.key)
        self.assertEqual(None, node11.left)
        self.assertEqual(None, node11.right)
        self.assertEqual(node5, node11.parent)

        self.assertEqual(key12, node12.key)
        self.assertEqual(None, node12.left)
        self.assertEqual(None, node12.right)
        self.assertEqual(node6, node12.parent)

        self.assertEqual(key13, node13.key)
        self.assertEqual(None, node13.left)
        self.assertEqual(None, node13.right)
        self.assertEqual(node6, node13.parent)

        self.assertEqual(key14, node14.key)
        self.assertEqual(None, node14.left)
        self.assertEqual(None, node14.right)
        self.assertEqual(node7, node14.parent)

        self.assertEqual(key15, node15.key)
        self.assertEqual(None, node15.left)
        self.assertEqual(None, node15.right)
        self.assertEqual(node7, node15.parent)

        self.assert_binary_search_properties(right)

    def test_split_on_fifteen_node_tree_with_key_larger_than_largest(self):
        (key1, key2, key3, key4, key5, key6, key7, key8, key9,
         key10, key11, key12, key13, key14, key15,
         node1, node2, node3, node4, node5, node6, node7, node8, node9,
         node10, node11, node12, node13, node14, node15) = \
                                        self.create_complete_fifteen_node_tree()

        root = node1
        search_key = key15 + 1

        left, right = self.tree.split(root, search_key)

        self.assertEqual(node15, left)
        self.assertEqual(None, right)

        self.assertEqual(key1, node1.key)
        self.assertEqual(node2, node1.left)
        self.assertEqual(node7, node1.right)
        self.assertEqual(node15, node1.parent)

        self.assertEqual(key2, node2.key)
        self.assertEqual(node4, node2.left)
        self.assertEqual(node5, node2.right)
        self.assertEqual(node1, node2.parent)

        self.assertEqual(key3, node3.key)
        self.assertEqual(node6, node3.left)
        self.assertEqual(node14, node3.right)
        self.assertEqual(node7, node3.parent)

        self.assertEqual(key4, node4.key)
        self.assertEqual(node8, node4.left)
        self.assertEqual(node9, node4.right)
        self.assertEqual(node2, node4.parent)

        self.assertEqual(key5, node5.key)
        self.assertEqual(node10, node5.left)
        self.assertEqual(node11, node5.right)
        self.assertEqual(node2, node5.parent)

        self.assertEqual(key6, node6.key)
        self.assertEqual(node12, node6.left)
        self.assertEqual(node13, node6.right)
        self.assertEqual(node3, node6.parent)

        self.assertEqual(key7, node7.key)
        self.assertEqual(node3, node7.left)
        self.assertEqual(None, node7.right)
        self.assertEqual(node1, node7.parent)

        self.assertEqual(key8, node8.key)
        self.assertEqual(None, node8.left)
        self.assertEqual(None, node8.right)
        self.assertEqual(node4, node8.parent)

        self.assertEqual(key9, node9.key)
        self.assertEqual(None, node9.left)
        self.assertEqual(None, node9.right)
        self.assertEqual(node4, node9.parent)

        self.assertEqual(key10, node10.key)
        self.assertEqual(None, node10.left)
        self.assertEqual(None, node10.right)
        self.assertEqual(node5, node10.parent)

        self.assertEqual(key11, node11.key)
        self.assertEqual(None, node11.left)
        self.assertEqual(None, node11.right)
        self.assertEqual(node5, node11.parent)

        self.assertEqual(key12, node12.key)
        self.assertEqual(None, node12.left)
        self.assertEqual(None, node12.right)
        self.assertEqual(node6, node12.parent)

        self.assertEqual(key13, node13.key)
        self.assertEqual(None, node13.left)
        self.assertEqual(None, node13.right)
        self.assertEqual(node6, node13.parent)

        self.assertEqual(key14, node14.key)
        self.assertEqual(None, node14.left)
        self.assertEqual(None, node14.right)
        self.assertEqual(node3, node14.parent)

        self.assertEqual(key15, node15.key)
        self.assertEqual(node1, node15.left)
        self.assertEqual(None, node15.right)
        self.assertEqual(None, node15.parent)

        self.assert_binary_search_properties(left)

    def test_split_and_merge_back_fifteen_node_tree(self):
        (key1, key2, key3, key4, key5, key6, key7, key8, key9,
         key10, key11, key12, key13, key14, key15,
         node1, node2, node3, node4, node5, node6, node7, node8, node9,
         node10, node11, node12, node13, node14, node15) = \
                                        self.create_complete_fifteen_node_tree()

        root = node1
        search_key = key1

        left, right = self.tree.split(root, search_key)

        self.assertEqual(node2, left)
        self.assertEqual(node1, right)

        self.assert_binary_search_properties(left)
        self.assert_binary_search_properties(right)

        self.assert_left_tree_less_than_right_tree(left, right)

        merged = self.tree.merge(left, right)

        self.assertEqual(root, merged)

        self.assert_original_complete_fifteen_node_tree(key1, key2, key3, key4,
                                                        key5, key6, key7, key8,
                                                        key9, key10, key11,
                                                        key12, key13, key14,
                                                        key15, node1, node2,
                                                        node3, node4, node5,
                                                        node6, node7, node8,
                                                        node9, node10, node11,
                                                        node12, node13, node14,
                                                        node15)

        self.assert_binary_search_properties(merged)

    def test_merge_none_and_left(self):
        (key1, key2, key3, key4, key5, key6, key7, key8, key9,
         key10, key11, key12, key13, key14, key15,
         node1, node2, node3, node4, node5, node6, node7, node8, node9,
         node10, node11, node12, node13, node14, node15) = \
                                        self.create_complete_fifteen_node_tree()

        root = node1
        left, right = root, None

        merged = self.tree.merge(left, right)

        self.assertEqual(left, merged)

        self.assert_original_complete_fifteen_node_tree(key1, key2, key3, key4,
                                                        key5, key6, key7, key8,
                                                        key9, key10, key11,
                                                        key12, key13, key14,
                                                        key15, node1, node2,
                                                        node3, node4, node5,
                                                        node6, node7, node8,
                                                        node9, node10, node11,
                                                        node12, node13, node14,
                                                        node15)

        self.assert_binary_search_properties(merged)

    def test_merge_left_and_none(self):
        (key1, key2, key3, key4, key5, key6, key7, key8, key9,
         key10, key11, key12, key13, key14, key15,
         node1, node2, node3, node4, node5, node6, node7, node8, node9,
         node10, node11, node12, node13, node14, node15) = \
                                        self.create_complete_fifteen_node_tree()

        root = node1
        left, right = None, root

        merged = self.tree.merge(left, right)

        self.assertEqual(right, merged)

        self.assert_original_complete_fifteen_node_tree(key1, key2, key3, key4,
                                                        key5, key6, key7, key8,
                                                        key9, key10, key11,
                                                        key12, key13, key14,
                                                        key15, node1, node2,
                                                        node3, node4, node5,
                                                        node6, node7, node8,
                                                        node9, node10, node11,
                                                        node12, node13, node14,
                                                        node15)

        self.assert_binary_search_properties(merged)

class SetTestCase(unittest.TestCase):

    def setUp(self):
        self.set = set_range_sum.Set()

    def tearDown(self):
        pass

    def test_find_on_empty_set(self):
        element = 1

        self.assertFalse(self.set.search(element))

    def test_find_missing(self):
        element = 1

        self.set.insert(element)

        self.assertTrue(self.set.search(element))

        self.assertFalse(self.set.search(5))

    def test_insert(self):
        element = 1

        self.set.insert(element)

        self.assertTrue(self.set.search(element))

    def test_insert_twice(self):
        element = 1

        self.set.insert(element)

        self.assertTrue(self.set.search(element))

        self.set.insert(element)

        self.assertTrue(self.set.search(element))

    def test_insert_on_non_empty_set(self):
        element1 = 1
        element2 = 2
        element3 = 3

        self.set.insert(element1)
        self.set.insert(element2)
        self.set.insert(element3)

        new_element = 5

        self.set.insert(new_element)

        self.assertTrue(self.set.search(element1))
        self.assertTrue(self.set.search(element2))
        self.assertTrue(self.set.search(element3))
        self.assertTrue(self.set.search(new_element))

    def test_insert_twice_on_non_empty_set(self):
        element1 = 1
        element2 = 2
        element3 = 3

        self.set.insert(element1)
        self.set.insert(element2)
        self.set.insert(element3)

        new_element = 5

        self.set.insert(new_element)

        self.assertTrue(self.set.search(element1))
        self.assertTrue(self.set.search(element2))
        self.assertTrue(self.set.search(element3))
        self.assertTrue(self.set.search(new_element))

        self.set.insert(new_element)

        self.assertTrue(self.set.search(element1))
        self.assertTrue(self.set.search(element2))
        self.assertTrue(self.set.search(element3))
        self.assertTrue(self.set.search(new_element))

    def test_erase(self):
        element = 1

        self.set.insert(element)

        self.assertTrue(self.set.search(element))

        self.set.erase(element)

        self.assertFalse(self.set.search(element))

    def test_erase_twice(self):
        element = 1

        self.set.insert(element)

        self.assertTrue(self.set.search(element))

        self.set.erase(element)

        self.assertFalse(self.set.search(element))

        self.set.erase(element)

        self.assertFalse(self.set.search(element))

    def test_erase_on_non_empty_set(self):
        element1 = 1
        element2 = 2
        element3 = 3

        self.set.insert(element1)
        self.set.insert(element2)
        self.set.insert(element3)

        self.set.erase(element3)

        self.assertTrue(self.set.search(element1))
        self.assertTrue(self.set.search(element2))
        self.assertFalse(self.set.search(element3))

    def test_erase_on_non_empty_set_twice(self):
        element1 = 1
        element2 = 2
        element3 = 3

        self.set.insert(element1)
        self.set.insert(element2)
        self.set.insert(element3)

        self.set.erase(element3)

        self.assertTrue(self.set.search(element1))
        self.assertTrue(self.set.search(element2))
        self.assertFalse(self.set.search(element3))

        self.set.erase(element3)

        self.assertTrue(self.set.search(element1))
        self.assertTrue(self.set.search(element2))
        self.assertFalse(self.set.search(element3))

    def test_erase_all(self):
        element1 = 1
        element2 = 2
        element3 = 3

        self.set.insert(element1)
        self.set.insert(element2)
        self.set.insert(element3)

        self.set.erase(element3)

        self.assertTrue(self.set.search(element1))
        self.assertTrue(self.set.search(element2))
        self.assertFalse(self.set.search(element3))

        self.set.erase(element2)

        self.assertTrue(self.set.search(element1))
        self.assertFalse(self.set.search(element2))
        self.assertFalse(self.set.search(element3))

        self.set.erase(element1)

        self.assertFalse(self.set.search(element1))
        self.assertFalse(self.set.search(element2))
        self.assertFalse(self.set.search(element3))

    def test_sum_on_empty_set(self):
        self.assertEquals(0, self.set.sum(-10, -10))
        self.assertEquals(0, self.set.sum(-10, 10))
        self.assertEquals(0, self.set.sum(10, 10))

    def test_sum_on_one_element_set(self):
        self.set.insert(1)

        self.assertEquals(0, self.set.sum(-1, -1))
        self.assertEquals(0, self.set.sum(-1, 0))
        self.assertEquals(0, self.set.sum(0, 0))
        self.assertEquals(1, self.set.sum(0, 1))
        self.assertEquals(1, self.set.sum(1, 1))
        self.assertEquals(1, self.set.sum(1, 2))
        self.assertEquals(0, self.set.sum(2, 2))
        self.assertEquals(0, self.set.sum(2, 3))
        self.assertEquals(0, self.set.sum(3, 3))

    def test_sum_on_two_element_set(self):
        self.set.insert(1)
        self.set.insert(5)

        self.assertEquals(0, self.set.sum(-1, -1))
        self.assertEquals(0, self.set.sum(-1, 0))
        self.assertEquals(0, self.set.sum(0, 0))
        self.assertEquals(1, self.set.sum(0, 1))
        self.assertEquals(1, self.set.sum(1, 1))
        self.assertEquals(1, self.set.sum(1, 2))
        self.assertEquals(0, self.set.sum(2, 2))
        self.assertEquals(0, self.set.sum(2, 3))
        self.assertEquals(0, self.set.sum(3, 3))
        self.assertEquals(0, self.set.sum(3, 4))
        self.assertEquals(0, self.set.sum(4, 4))
        self.assertEquals(5, self.set.sum(4, 5))
        self.assertEquals(5, self.set.sum(5, 5))
        self.assertEquals(1, self.set.sum(0, 3))
        self.assertEquals(6, self.set.sum(0, 6))
        self.assertEquals(5, self.set.sum(3, 6))

    def test_sum_on_three_element_set(self):
        self.set.insert(1)
        self.set.insert(3)
        self.set.insert(5)

        self.assertEquals(0, self.set.sum(-1, -1))
        self.assertEquals(0, self.set.sum(-1, 0))
        self.assertEquals(0, self.set.sum(0, 0))
        self.assertEquals(1, self.set.sum(0, 1))
        self.assertEquals(1, self.set.sum(1, 1))
        self.assertEquals(1, self.set.sum(1, 2))
        self.assertEquals(0, self.set.sum(2, 2))
        self.assertEquals(3, self.set.sum(2, 3))
        self.assertEquals(3, self.set.sum(3, 3))
        self.assertEquals(3, self.set.sum(3, 4))
        self.assertEquals(0, self.set.sum(4, 4))
        self.assertEquals(5, self.set.sum(4, 5))
        self.assertEquals(5, self.set.sum(5, 5))
        self.assertEquals(4, self.set.sum(0, 3))
        self.assertEquals(9, self.set.sum(0, 6))
        self.assertEquals(8, self.set.sum(3, 6))

    def test_erase_and_sum_all(self):
        element1 = 1
        element2 = 2
        element3 = 3

        self.set.insert(element1)
        self.set.insert(element2)
        self.set.insert(element3)

        self.assertEquals(6, self.set.sum(0, 4))

        self.set.erase(element3)

        self.assertTrue(self.set.search(element1))
        self.assertTrue(self.set.search(element2))
        self.assertFalse(self.set.search(element3))
        self.assertEquals(3, self.set.sum(0, 4))

        self.set.erase(element2)

        self.assertTrue(self.set.search(element1))
        self.assertFalse(self.set.search(element2))
        self.assertFalse(self.set.search(element3))
        self.assertEquals(1, self.set.sum(0, 4))

        self.set.erase(element1)

        self.assertFalse(self.set.search(element1))
        self.assertFalse(self.set.search(element2))
        self.assertFalse(self.set.search(element3))
        self.assertEquals(0, self.set.sum(0, 4))

class SolverSolveTestCase(unittest.TestCase):

    def setUp(self):
        self.solver = set_range_sum.Solver()
        self.solver._input = self.generate_input
        self.solver._output = self.accumulate_output
        self.output_list = []
        self.index = 0

    def tearDown(self):
        pass

    def generate_input(self):
        line = self.input_list[self.index]
        self.index += 1

        return line

    def accumulate_output(self, text):
        return self.output_list.append(text)

    def test_case1(self):
        self.input_list = [
                              '15',
                              '? 1',
                              '+ 1',
                              '? 1',
                              '+ 2',
                              's 1 2',
                              '+ 1000000000',
                              '? 1000000000',
                              '- 1000000000',
                              '? 1000000000',
                              's 999999999 1000000000',
                              '- 2',
                              '? 2',
                              '- 0',
                              '+ 9',
                              's 0 9',
                          ]
        expected_result = [
                              'Not found',
                              'Found',
                              '3',
                              'Found',
                              'Not found',
                              '1',
                              'Not found',
                              '10',
                          ]

        self.solver.solve()

        self.assertEqual(expected_result, self.output_list)

    def test_case2(self):
        self.input_list = [
                              '5',
                              '? 0',
                              '+ 0',
                              '? 0',
                              '- 0',
                              '? 0',
                          ]
        expected_result = [
                              'Not found',
                              'Found',
                              'Not found',
                          ]

        self.solver.solve()

        self.assertEqual(expected_result, self.output_list)

    def test_case3(self):
        self.input_list = [
                              '5',
                              '+ 491572259',
                              '? 491572259',
                              '? 899375874',
                              's 310971296 877523306',
                              '+ 352411209',
                          ]
        expected_result = [
                              'Found',
                              'Not found',
                              '491572259',
                          ]

        self.solver.solve()

        self.assertEqual(expected_result, self.output_list)

if __name__ == '__main__':
    class_names = [
                       VertexTestCase,
                       SumSplayTreeTestCase,
                       SetTestCase,
                       SolverSolveTestCase,
                  ]

    suite = unittest.TestSuite()

    for c in class_names:
        suite.addTest(unittest.defaultTestLoader.loadTestsFromTestCase(c))

    unittest.TextTestRunner().run(suite)
