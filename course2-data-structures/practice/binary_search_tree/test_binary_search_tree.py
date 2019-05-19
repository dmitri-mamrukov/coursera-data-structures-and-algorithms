#!/usr/bin/python3

import random
import unittest

import binary_search_tree

class TreeNodeTestCase(unittest.TestCase):

    def setUp(self):
        self.node_type = binary_search_tree.TreeNode
        pass

    def tearDown(self):
        pass

    def assert_binary_search_property(self, root):
        if root is None:
            return

        nodes = [ root ]

        while len(nodes) > 0:
            node = nodes.pop()

            if node.left_child is not None:
                self.assertTrue(node.left_child.key < node.key)
            if node.right_child is not None:
                self.assertTrue(node.key < node.right_child.key)

            if node.left_child is not None:
                nodes.append(node.left_child)
            if node.right_child is not None:
                nodes.append(node.right_child)

    def assert_height_property(self, root):
        if root is None:
            return

        nodes = [ root ]

        while len(nodes) > 0:
            node = nodes.pop()

            expected_height = 0
            if node.has_any_children():
                expected_height = (1 + max((node.left_child.height
                                            if node.left_child is not None
                                            else 0),
                                           (node.right_child.height
                                            if node.right_child is not None
                                            else 0)))
            self.assertEqual(expected_height, node.height)

            if node.left_child is not None:
                nodes.append(node.left_child)
            if node.right_child is not None:
                nodes.append(node.right_child)

    def assert_properties(self, root):
        self.assert_binary_search_property(root)
        self.assert_height_property(root)

    def create_four_node_tree(self, is_left=True):
        parent = self.node_type('z' if is_left else 'a', 'parent-value')
        left = self.node_type('m', 'm-value')
        right = self.node_type('o', 'o-value')
        node = self.node_type('n', 'n-value', left, right, parent)

        left.height = 0
        right.height = 0
        node.height = 1
        parent.height = 2

        if is_left:
            parent.left_child = node
        else:
            parent.right_child = node

        self.assert_properties(parent)

        return (node, left, right, parent)

    def create_seven_node_tree(self):
        node_d = self.node_type('d', 'd-value')
        node_b = self.node_type('b', 'b-value', parent=node_d)
        node_f = self.node_type('f', 'f-value', parent=node_d)
        node_d.left_child = node_b
        node_d.right_child = node_f
        node_a = self.node_type('a', 'a-value', parent=node_b)
        node_c = self.node_type('c', 'c-value', parent=node_b)
        node_b.left_child = node_a
        node_b.right_child = node_c
        node_e = self.node_type('e', 'e-value', parent=node_f)
        node_g = self.node_type('g', 'g-value', parent=node_f)
        node_f.left_child = node_e
        node_f.right_child = node_g

        node_a.height = 0
        node_b.height = 1
        node_c.height = 0
        node_d.height = 2
        node_e.height = 0
        node_f.height = 1
        node_g.height = 0

        self.assert_properties(node_d)

        return (node_a, node_b, node_c, node_d, node_e, node_f, node_g)

    def test_constructor_with_key_value(self):
        key = 'a'
        value = 'a-value'

        node = self.node_type(key, value)

        self.assertEqual(key, node.key)
        self.assertEqual(value, node.value)
        self.assertEqual(None, node.left_child)
        self.assertEqual(None, node.right_child)
        self.assertEqual(None, node.parent)
        self.assertEqual(0, node.height)

        self.assert_properties(node)

    def test_constructor_with_key_value_left(self):
        key = 'b'
        value = 'b-value'

        left = self.node_type('a', 'a-left')
        node = self.node_type(key, value, left)

        self.assertEqual(key, node.key)
        self.assertEqual(value, node.value)
        self.assertEqual(left, node.left_child)
        self.assertEqual(None, node.right_child)
        self.assertEqual(None, node.parent)
        self.assertEqual(1, node.height)

        self.assert_properties(node)

    def test_constructor_with_key_value_left_right(self):
        key = 'b'
        value = 'b-value'

        left = self.node_type('a', 'a-value')
        right = self.node_type('c', 'c-value')
        node = self.node_type(key, value, left, right)

        self.assertEqual(key, node.key)
        self.assertEqual(value, node.value)
        self.assertEqual(left, node.left_child)
        self.assertEqual(right, node.right_child)
        self.assertEqual(None, node.parent)
        self.assertEqual(1, node.height)

        self.assert_properties(node)

    def test_constructor_with_key_value_left_right_parent(self):
        key = 'b'
        value = 'b-value'

        left = self.node_type('a', 'a-value')
        right = self.node_type('c', 'c-value')
        parent = self.node_type('d', 'd-value')
        node = self.node_type(key, value, left, right, parent)

        self.assertEqual(key, node.key)
        self.assertEqual(value, node.value)
        self.assertEqual(left, node.left_child)
        self.assertEqual(right, node.right_child)
        self.assertEqual(parent, node.parent)
        self.assertEqual(1, node.height)

        self.assert_properties(parent)

    def test_str(self):
        node = self.node_type('a', 'a-value')

        self.assertEquals('key: a, value: a-value', str(node))

    def test_repr(self):
        node, left, right, parent = self.create_four_node_tree(is_left=True)

        self.assertEquals('key: n, value: n-value, parent: ' +
                          '[key: z, value: parent-value], ' +
                          'left: [key: m, value: m-value], ' +
                          'right: [key: o, value: o-value], height: 1',
                          repr(node))

    def test_iter_on_seven_node_tree(self):
        node_a, node_b, node_c, node_d, node_e, node_f, node_g = \
                                                   self.create_seven_node_tree()

        for actual_key in node_a:
            self.assertTrue(actual_key in [ 'a', ])

        for actual_key in node_b:
            self.assertTrue(actual_key in [ 'a', 'b', 'c', ])

        for actual_key in node_c:
            self.assertTrue(actual_key in [ 'c', ])

        for actual_key in node_d:
            self.assertTrue(actual_key in [ 'a', 'b', 'c', 'd', 'e', 'f',
                                           'g',  ])

        for actual_key in node_e:
            self.assertTrue(actual_key in [ 'e', ])

        for actual_key in node_f:
            self.assertTrue(actual_key in [ 'e', 'f', 'g', ])

        for actual_key in node_g:
            self.assertTrue(actual_key in [ 'g', ])

    def test_has_left_child(self):
        node, left, right, parent = self.create_four_node_tree(is_left=True)

        self.assertTrue(parent.has_left_child())
        self.assertTrue(node.has_left_child())
        self.assertFalse(left.has_left_child())
        self.assertFalse(right.has_left_child())

    def test_has_right_child(self):
        node, left, right, parent = self.create_four_node_tree(is_left=True)

        self.assertFalse(parent.has_right_child())
        self.assertTrue(node.has_right_child())
        self.assertFalse(left.has_right_child())
        self.assertFalse(right.has_right_child())

    def test_is_left_child(self):
        node, left, right, parent = self.create_four_node_tree(is_left=True)

        self.assertFalse(parent.is_left_child())
        self.assertTrue(node.is_left_child())
        self.assertTrue(left.is_left_child())
        self.assertFalse(right.is_left_child())

    def test_is_right_child(self):
        node, left, right, parent = self.create_four_node_tree(is_left=True)

        self.assertFalse(parent.is_right_child())
        self.assertFalse(node.is_right_child())
        self.assertFalse(left.is_right_child())
        self.assertTrue(right.is_right_child())

    def test_is_root(self):
        node, left, right, parent = self.create_four_node_tree()

        self.assertTrue(parent.is_root())
        self.assertFalse(node.is_root())
        self.assertFalse(left.is_root())
        self.assertFalse(right.is_root())

    def test_is_leaf(self):
        node, left, right, parent = self.create_four_node_tree()

        self.assertFalse(parent.is_leaf())
        self.assertFalse(node.is_leaf())
        self.assertTrue(left.is_leaf())
        self.assertTrue(right.is_leaf())

    def test_has_any_children(self):
        node, left, right, parent = self.create_four_node_tree()

        self.assertTrue(parent.has_any_children())
        self.assertTrue(node.has_any_children())
        self.assertFalse(left.has_any_children())
        self.assertFalse(right.has_any_children())

    def test_has_both_children(self):
        node, left, right, parent = self.create_four_node_tree()

        self.assertFalse(parent.has_both_children())
        self.assertTrue(node.has_both_children())
        self.assertFalse(left.has_both_children())
        self.assertFalse(right.has_both_children())

    def test_replace_node_data_with_none_left_and_none_right(self):
        node, left, right, parent = self.create_four_node_tree()

        new_key = 'nn'
        new_value = 'nn-value'

        node.replace_node_data(new_key, new_value, None, None)

        self.assertEqual(new_key, node.key)
        self.assertEqual(new_value, node.value)
        self.assertEqual(None, node.left_child)
        self.assertEqual(None, node.right_child)
        self.assertEqual(parent, node.parent)
        self.assertEqual(0, node.height)

        self.assert_properties(parent)

    def test_replace_node_data_with_left_and_none_right(self):
        node, left, right, parent = self.create_four_node_tree()

        new_key = 'nn'
        new_value = 'nn-value'
        new_left = self.node_type('mm', 'mm-value')

        node.replace_node_data(new_key, new_value, new_left, None)

        self.assertEqual(new_key, node.key)
        self.assertEqual(new_value, node.value)
        self.assertEqual(new_left, node.left_child)
        self.assertEqual(None, node.right_child)
        self.assertEqual(parent, node.parent)
        self.assertEqual(node, new_left.parent)
        self.assertEqual(1, node.height)

        self.assert_properties(parent)

    def test_replace_node_data_with_none_left_and_right(self):
        node, left, right, parent = self.create_four_node_tree()

        new_key = 'nn'
        new_value = 'nn-value'
        new_right = self.node_type('oo', 'oo-value')

        node.replace_node_data(new_key, new_value, None, new_right)

        self.assertEqual(new_key, node.key)
        self.assertEqual(new_value, node.value)
        self.assertEqual(None, node.left_child)
        self.assertEqual(new_right, node.right_child)
        self.assertEqual(parent, node.parent)
        self.assertEqual(node, new_right.parent)
        self.assertEqual(1, node.height)

        self.assert_properties(parent)

    def test_replace_node_data_with_left_and_right(self):
        node, left, right, parent = self.create_four_node_tree()

        new_key = 'nn'
        new_value = 'nn-value'
        new_left = self.node_type('mm', 'mm-value')
        new_right = self.node_type('oo', 'oo-value')

        node.replace_node_data(new_key, new_value, new_left, new_right)

        self.assertEqual(new_key, node.key)
        self.assertEqual(new_value, node.value)
        self.assertEqual(new_left, node.left_child)
        self.assertEqual(new_right, node.right_child)
        self.assertEqual(parent, node.parent)
        self.assertEqual(node, new_right.parent)
        self.assertEqual(1, node.height)

        self.assert_properties(parent)

    def test_find_min_and_find_successor(self):
        node_a, node_b, node_c, node_d, node_e, node_f, node_g = \
                                                   self.create_seven_node_tree()

        self.assertEqual(node_a, node_a.find_min())
        self.assertEqual(node_b, node_a.find_successor())

        self.assertEqual(node_a, node_b.find_min())
        self.assertEqual(node_c, node_b.find_successor())

        self.assertEqual(node_c, node_c.find_min())
        self.assertEqual(node_d, node_c.find_successor())

        self.assertEqual(node_a, node_d.find_min())
        self.assertEqual(node_e, node_d.find_successor())

        self.assertEqual(node_e, node_f.find_min())
        self.assertEqual(node_g, node_f.find_successor())

        self.assertEqual(node_e, node_e.find_min())
        self.assertEqual(node_f, node_e.find_successor())

        self.assertEqual(node_g, node_g.find_min())
        self.assertEqual(None, node_g.find_successor())

    def test_splice_out_on_node_d(self):
        node_a, node_b, node_c, node_d, node_e, node_f, node_g = \
                                                   self.create_seven_node_tree()

        self.assertTrue(node_d.is_root())

        node_d.splice_out()

        self.assertEqual(None, node_d.parent)
        self.assertEqual(node_b, node_d.left_child)
        self.assertEqual(node_f, node_d.right_child)

        self.assertEqual(node_d, node_b.parent)
        self.assertEqual(node_a, node_b.left_child)
        self.assertEqual(node_c, node_b.right_child)

        self.assertEqual(node_d, node_f.parent)
        self.assertEqual(node_e, node_f.left_child)
        self.assertEqual(node_g, node_f.right_child)

        self.assertEqual(node_b, node_a.parent)
        self.assertEqual(None, node_a.left_child)
        self.assertEqual(None, node_a.right_child)

        self.assertEqual(node_b, node_c.parent)
        self.assertEqual(None, node_c.left_child)
        self.assertEqual(None, node_c.right_child)

        self.assertEqual(node_f, node_e.parent)
        self.assertEqual(None, node_e.left_child)
        self.assertEqual(None, node_e.right_child)

        self.assertEqual(node_f, node_g.parent)
        self.assertEqual(None, node_g.left_child)
        self.assertEqual(None, node_g.right_child)

        self.assert_properties(node_d)

    def test_splice_out_both_leaf_children_on_left(self):
        node_a, node_b, node_c, node_d, node_e, node_f, node_g = \
                                                   self.create_seven_node_tree()

        self.assertTrue(node_a.is_leaf())

        node_a.splice_out()

        self.assertEqual(None, node_d.parent)
        self.assertEqual(node_b, node_d.left_child)
        self.assertEqual(node_f, node_d.right_child)

        self.assertEqual(node_d, node_b.parent)
        self.assertEqual(None, node_b.left_child)
        self.assertEqual(node_c, node_b.right_child)

        self.assertEqual(node_d, node_f.parent)
        self.assertEqual(node_e, node_f.left_child)
        self.assertEqual(node_g, node_f.right_child)

        self.assertEqual(node_b, node_c.parent)
        self.assertEqual(None, node_c.left_child)
        self.assertEqual(None, node_c.right_child)

        self.assertEqual(node_f, node_e.parent)
        self.assertEqual(None, node_e.left_child)
        self.assertEqual(None, node_e.right_child)

        self.assertEqual(node_f, node_g.parent)
        self.assertEqual(None, node_g.left_child)
        self.assertEqual(None, node_g.right_child)

        self.assert_properties(node_d)

        self.assertTrue(node_c.is_leaf())

        node_c.splice_out()

        self.assertEqual(None, node_d.parent)
        self.assertEqual(node_b, node_d.left_child)
        self.assertEqual(node_f, node_d.right_child)

        self.assertEqual(node_d, node_b.parent)
        self.assertEqual(None, node_b.left_child)
        self.assertEqual(None, node_b.right_child)

        self.assertEqual(node_d, node_f.parent)
        self.assertEqual(node_e, node_f.left_child)
        self.assertEqual(node_g, node_f.right_child)

        self.assertEqual(node_f, node_e.parent)
        self.assertEqual(None, node_e.left_child)
        self.assertEqual(None, node_e.right_child)

        self.assertEqual(node_f, node_g.parent)
        self.assertEqual(None, node_g.left_child)
        self.assertEqual(None, node_g.right_child)

        self.assert_properties(node_d)

    def test_splice_out_both_leaf_children_on_right(self):
        node_a, node_b, node_c, node_d, node_e, node_f, node_g = \
                                                   self.create_seven_node_tree()

        self.assertTrue(node_e.is_leaf())

        node_e.splice_out()

        self.assertEqual(None, node_d.parent)
        self.assertEqual(node_b, node_d.left_child)
        self.assertEqual(node_f, node_d.right_child)

        self.assertEqual(node_d, node_b.parent)
        self.assertEqual(node_a, node_b.left_child)
        self.assertEqual(node_c, node_b.right_child)

        self.assertEqual(node_d, node_f.parent)
        self.assertEqual(None, node_f.left_child)
        self.assertEqual(node_g, node_f.right_child)

        self.assertEqual(node_b, node_a.parent)
        self.assertEqual(None, node_a.left_child)
        self.assertEqual(None, node_a.right_child)

        self.assertEqual(node_b, node_c.parent)
        self.assertEqual(None, node_c.left_child)
        self.assertEqual(None, node_c.right_child)

        self.assertEqual(node_f, node_g.parent)
        self.assertEqual(None, node_g.left_child)
        self.assertEqual(None, node_g.right_child)

        self.assert_properties(node_d)

        self.assertTrue(node_g.is_leaf())

        node_g.splice_out()

        self.assertEqual(None, node_d.parent)
        self.assertEqual(node_b, node_d.left_child)
        self.assertEqual(node_f, node_d.right_child)

        self.assertEqual(node_d, node_b.parent)
        self.assertEqual(node_a, node_b.left_child)
        self.assertEqual(node_c, node_b.right_child)

        self.assertEqual(node_d, node_f.parent)
        self.assertEqual(None, node_f.left_child)
        self.assertEqual(None, node_f.right_child)

        self.assertEqual(node_b, node_a.parent)
        self.assertEqual(None, node_a.left_child)
        self.assertEqual(None, node_a.right_child)

        self.assertEqual(node_b, node_c.parent)
        self.assertEqual(None, node_c.left_child)
        self.assertEqual(None, node_c.right_child)

        self.assert_properties(node_d)

    def test_splice_out_on_leaf_a_and_parent(self):
        node_a, node_b, node_c, node_d, node_e, node_f, node_g = \
                                                   self.create_seven_node_tree()

        self.assertTrue(node_a.is_leaf())

        node_a.splice_out()

        self.assertEqual(None, node_d.parent)
        self.assertEqual(node_b, node_d.left_child)
        self.assertEqual(node_f, node_d.right_child)

        self.assertEqual(node_d, node_b.parent)
        self.assertEqual(None, node_b.left_child)
        self.assertEqual(node_c, node_b.right_child)

        self.assertEqual(node_d, node_f.parent)
        self.assertEqual(node_e, node_f.left_child)
        self.assertEqual(node_g, node_f.right_child)

        self.assertEqual(node_b, node_c.parent)
        self.assertEqual(None, node_c.left_child)
        self.assertEqual(None, node_c.right_child)

        self.assertEqual(node_f, node_e.parent)
        self.assertEqual(None, node_e.left_child)
        self.assertEqual(None, node_e.right_child)

        self.assertEqual(node_f, node_g.parent)
        self.assertEqual(None, node_g.left_child)
        self.assertEqual(None, node_g.right_child)

        self.assert_properties(node_d)

        self.assertFalse(node_b.has_left_child())
        self.assertTrue(node_b.has_right_child())
        self.assertTrue(node_b.has_any_children())

        node_b.splice_out()

        self.assertEqual(None, node_d.parent)
        self.assertEqual(node_c, node_d.left_child)
        self.assertEqual(node_f, node_d.right_child)

        self.assertEqual(node_d, node_f.parent)
        self.assertEqual(node_e, node_f.left_child)
        self.assertEqual(node_g, node_f.right_child)

        self.assertEqual(node_f, node_e.parent)
        self.assertEqual(None, node_e.left_child)
        self.assertEqual(None, node_e.right_child)

        self.assertEqual(node_f, node_g.parent)
        self.assertEqual(None, node_g.left_child)
        self.assertEqual(None, node_g.right_child)

        self.assert_properties(node_d)

    def test_splice_out_on_leaf_c_and_parent(self):
        node_a, node_b, node_c, node_d, node_e, node_f, node_g = \
                                                   self.create_seven_node_tree()

        self.assertTrue(node_c.is_leaf())

        node_c.splice_out()

        self.assertEqual(None, node_d.parent)
        self.assertEqual(node_b, node_d.left_child)
        self.assertEqual(node_f, node_d.right_child)

        self.assertEqual(node_d, node_b.parent)
        self.assertEqual(node_a, node_b.left_child)
        self.assertEqual(None, node_b.right_child)

        self.assertEqual(node_d, node_f.parent)
        self.assertEqual(node_e, node_f.left_child)
        self.assertEqual(node_g, node_f.right_child)

        self.assertEqual(node_b, node_a.parent)
        self.assertEqual(None, node_a.left_child)
        self.assertEqual(None, node_a.right_child)

        self.assertEqual(node_f, node_e.parent)
        self.assertEqual(None, node_e.left_child)
        self.assertEqual(None, node_e.right_child)

        self.assertEqual(node_f, node_g.parent)
        self.assertEqual(None, node_g.left_child)
        self.assertEqual(None, node_g.right_child)

        node_b.splice_out()

        self.assertEqual(None, node_d.parent)
        self.assertEqual(node_a, node_d.left_child)
        self.assertEqual(node_f, node_d.right_child)

        self.assertEqual(node_d, node_a.parent)
        self.assertEqual(None, node_a.left_child)
        self.assertEqual(None, node_a.right_child)

        self.assertEqual(node_d, node_f.parent)
        self.assertEqual(node_e, node_f.left_child)
        self.assertEqual(node_g, node_f.right_child)

        self.assertEqual(node_f, node_e.parent)
        self.assertEqual(None, node_e.left_child)
        self.assertEqual(None, node_e.right_child)

        self.assertEqual(node_f, node_g.parent)
        self.assertEqual(None, node_g.left_child)
        self.assertEqual(None, node_g.right_child)

    def test_splice_out_on_leaf_e_and_parent(self):
        node_a, node_b, node_c, node_d, node_e, node_f, node_g = \
                                                   self.create_seven_node_tree()

        self.assertTrue(node_e.is_leaf())

        node_e.splice_out()

        self.assertEqual(None, node_d.parent)
        self.assertEqual(node_b, node_d.left_child)
        self.assertEqual(node_f, node_d.right_child)

        self.assertEqual(node_d, node_b.parent)
        self.assertEqual(node_a, node_b.left_child)
        self.assertEqual(node_c, node_b.right_child)

        self.assertEqual(node_d, node_f.parent)
        self.assertEqual(None, node_f.left_child)
        self.assertEqual(node_g, node_f.right_child)

        self.assertEqual(node_b, node_a.parent)
        self.assertEqual(None, node_a.left_child)
        self.assertEqual(None, node_a.right_child)

        self.assertEqual(node_b, node_c.parent)
        self.assertEqual(None, node_c.left_child)
        self.assertEqual(None, node_c.right_child)

        self.assertEqual(node_f, node_g.parent)
        self.assertEqual(None, node_g.left_child)
        self.assertEqual(None, node_g.right_child)

        node_f.splice_out()

        self.assertEqual(None, node_d.parent)
        self.assertEqual(node_b, node_d.left_child)
        self.assertEqual(node_g, node_d.right_child)

        self.assertEqual(node_d, node_b.parent)
        self.assertEqual(node_a, node_b.left_child)
        self.assertEqual(node_c, node_b.right_child)

        self.assertEqual(node_b, node_a.parent)
        self.assertEqual(None, node_a.left_child)
        self.assertEqual(None, node_a.right_child)

        self.assertEqual(node_b, node_c.parent)
        self.assertEqual(None, node_c.left_child)
        self.assertEqual(None, node_c.right_child)

        self.assertEqual(node_d, node_g.parent)
        self.assertEqual(None, node_g.left_child)
        self.assertEqual(None, node_g.right_child)

    def test_splice_out_on_leaf_g_and_parent(self):
        node_a, node_b, node_c, node_d, node_e, node_f, node_g = \
                                                   self.create_seven_node_tree()

        self.assertTrue(node_g.is_leaf())

        node_g.splice_out()

        self.assertEqual(None, node_d.parent)
        self.assertEqual(node_b, node_d.left_child)
        self.assertEqual(node_f, node_d.right_child)

        self.assertEqual(node_d, node_b.parent)
        self.assertEqual(node_a, node_b.left_child)
        self.assertEqual(node_c, node_b.right_child)

        self.assertEqual(node_b, node_a.parent)
        self.assertEqual(None, node_a.left_child)
        self.assertEqual(None, node_a.right_child)

        self.assertEqual(node_b, node_c.parent)
        self.assertEqual(None, node_c.left_child)
        self.assertEqual(None, node_c.right_child)

        self.assertEqual(node_d, node_f.parent)
        self.assertEqual(node_e, node_f.left_child)
        self.assertEqual(None, node_f.right_child)

        self.assertEqual(node_f, node_e.parent)
        self.assertEqual(None, node_e.left_child)
        self.assertEqual(None, node_e.right_child)

        node_f.splice_out()

        self.assertEqual(None, node_d.parent)
        self.assertEqual(node_b, node_d.left_child)
        self.assertEqual(node_e, node_d.right_child)

        self.assertEqual(node_d, node_b.parent)
        self.assertEqual(node_a, node_b.left_child)
        self.assertEqual(node_c, node_b.right_child)

        self.assertEqual(node_b, node_a.parent)
        self.assertEqual(None, node_a.left_child)
        self.assertEqual(None, node_a.right_child)

        self.assertEqual(node_b, node_c.parent)
        self.assertEqual(None, node_c.left_child)
        self.assertEqual(None, node_c.right_child)

        self.assertEqual(node_d, node_e.parent)
        self.assertEqual(None, node_e.left_child)
        self.assertEqual(None, node_e.right_child)

    def test_splice_out_on_c_e_g_and_b(self):
        node_a, node_b, node_c, node_d, node_e, node_f, node_g = \
                                                   self.create_seven_node_tree()

        self.assertTrue(node_c.is_leaf())

        node_c.splice_out()

        self.assertEqual(None, node_d.parent)
        self.assertEqual(node_b, node_d.left_child)
        self.assertEqual(node_f, node_d.right_child)

        self.assertEqual(node_d, node_b.parent)
        self.assertEqual(node_a, node_b.left_child)
        self.assertEqual(None, node_b.right_child)

        self.assertEqual(node_d, node_f.parent)
        self.assertEqual(node_e, node_f.left_child)
        self.assertEqual(node_g, node_f.right_child)

        self.assertEqual(node_b, node_a.parent)
        self.assertEqual(None, node_a.left_child)
        self.assertEqual(None, node_a.right_child)

        self.assertEqual(node_f, node_e.parent)
        self.assertEqual(None, node_e.left_child)
        self.assertEqual(None, node_e.right_child)

        self.assertEqual(node_f, node_g.parent)
        self.assertEqual(None, node_g.left_child)
        self.assertEqual(None, node_g.right_child)

        self.assert_properties(node_d)

        self.assertTrue(node_e.is_leaf())

        node_e.splice_out()

        self.assertEqual(None, node_d.parent)
        self.assertEqual(node_b, node_d.left_child)
        self.assertEqual(node_f, node_d.right_child)

        self.assertEqual(node_d, node_b.parent)
        self.assertEqual(node_a, node_b.left_child)
        self.assertEqual(None, node_b.right_child)

        self.assertEqual(node_d, node_f.parent)
        self.assertEqual(None, node_f.left_child)
        self.assertEqual(node_g, node_f.right_child)

        self.assertEqual(node_b, node_a.parent)
        self.assertEqual(None, node_a.left_child)
        self.assertEqual(None, node_a.right_child)

        self.assertEqual(node_f, node_g.parent)
        self.assertEqual(None, node_g.left_child)
        self.assertEqual(None, node_g.right_child)

        self.assert_properties(node_d)

        self.assertTrue(node_g.is_leaf())

        node_g.splice_out()

        self.assertEqual(None, node_d.parent)
        self.assertEqual(node_b, node_d.left_child)
        self.assertEqual(node_f, node_d.right_child)

        self.assertEqual(node_d, node_b.parent)
        self.assertEqual(node_a, node_b.left_child)
        self.assertEqual(None, node_b.right_child)

        self.assertEqual(node_d, node_f.parent)
        self.assertEqual(None, node_f.left_child)
        self.assertEqual(None, node_f.right_child)

        self.assertEqual(node_b, node_a.parent)
        self.assertEqual(None, node_a.left_child)
        self.assertEqual(None, node_a.right_child)

        self.assert_properties(node_d)

        self.assertTrue(node_b.has_left_child())
        self.assertFalse(node_b.has_right_child())
        self.assertTrue(node_b.has_any_children())

        node_b.splice_out()

        self.assertEqual(None, node_d.parent)
        self.assertEqual(node_a, node_d.left_child)
        self.assertEqual(node_f, node_d.right_child)

        self.assertEqual(node_d, node_a.parent)
        self.assertEqual(None, node_a.left_child)
        self.assertEqual(None, node_a.right_child)

        self.assertEqual(node_d, node_f.parent)
        self.assertEqual(None, node_f.left_child)
        self.assertEqual(None, node_f.right_child)

        self.assert_properties(node_d)

    def test_splice_out_on_a_c_g_and_f(self):
        node_a, node_b, node_c, node_d, node_e, node_f, node_g = \
                                                   self.create_seven_node_tree()

        self.assertTrue(node_a.is_leaf())

        node_a.splice_out()

        self.assertEqual(None, node_d.parent)
        self.assertEqual(node_b, node_d.left_child)
        self.assertEqual(node_f, node_d.right_child)

        self.assertEqual(node_d, node_b.parent)
        self.assertEqual(None, node_b.left_child)
        self.assertEqual(node_c, node_b.right_child)

        self.assertEqual(node_d, node_f.parent)
        self.assertEqual(node_e, node_f.left_child)
        self.assertEqual(node_g, node_f.right_child)

        self.assertEqual(node_b, node_c.parent)
        self.assertEqual(None, node_c.left_child)
        self.assertEqual(None, node_c.right_child)

        self.assertEqual(node_f, node_e.parent)
        self.assertEqual(None, node_e.left_child)
        self.assertEqual(None, node_e.right_child)

        self.assertEqual(node_f, node_g.parent)
        self.assertEqual(None, node_g.left_child)
        self.assertEqual(None, node_g.right_child)

        self.assert_properties(node_d)

        self.assertTrue(node_c.is_leaf())

        node_c.splice_out()

        self.assertEqual(None, node_d.parent)
        self.assertEqual(node_b, node_d.left_child)
        self.assertEqual(node_f, node_d.right_child)

        self.assertEqual(node_d, node_b.parent)
        self.assertEqual(None, node_b.left_child)
        self.assertEqual(None, node_b.right_child)

        self.assertEqual(node_d, node_f.parent)
        self.assertEqual(node_e, node_f.left_child)
        self.assertEqual(node_g, node_f.right_child)

        self.assertEqual(node_f, node_e.parent)
        self.assertEqual(None, node_e.left_child)
        self.assertEqual(None, node_e.right_child)

        self.assertEqual(node_f, node_g.parent)
        self.assertEqual(None, node_g.left_child)
        self.assertEqual(None, node_g.right_child)

        self.assert_properties(node_d)

        self.assertTrue(node_g.is_leaf())

        node_g.splice_out()

        self.assertEqual(None, node_d.parent)
        self.assertEqual(node_b, node_d.left_child)
        self.assertEqual(node_f, node_d.right_child)

        self.assertEqual(node_d, node_b.parent)
        self.assertEqual(None, node_b.left_child)
        self.assertEqual(None, node_b.right_child)

        self.assertEqual(node_d, node_f.parent)
        self.assertEqual(node_e, node_f.left_child)
        self.assertEqual(None, node_f.right_child)

        self.assertEqual(node_f, node_e.parent)
        self.assertEqual(None, node_e.left_child)
        self.assertEqual(None, node_e.right_child)

        self.assert_properties(node_d)

        self.assertTrue(node_f.has_left_child())
        self.assertFalse(node_f.has_right_child())
        self.assertTrue(node_f.has_any_children())

        node_f.splice_out()

        self.assertEqual(None, node_d.parent)
        self.assertEqual(node_b, node_d.left_child)
        self.assertEqual(node_e, node_d.right_child)

        self.assertEqual(node_d, node_b.parent)
        self.assertEqual(None, node_b.left_child)
        self.assertEqual(None, node_b.right_child)

        self.assertEqual(node_d, node_e.parent)
        self.assertEqual(None, node_e.left_child)
        self.assertEqual(None, node_e.right_child)

        self.assert_properties(node_d)

    def test_splice_out_on_a_e_g_and_b(self):
        node_a, node_b, node_c, node_d, node_e, node_f, node_g = \
                                                   self.create_seven_node_tree()

        self.assertTrue(node_a.is_leaf())

        node_a.splice_out()

        self.assertEqual(None, node_d.parent)
        self.assertEqual(node_b, node_d.left_child)
        self.assertEqual(node_f, node_d.right_child)

        self.assertEqual(node_d, node_b.parent)
        self.assertEqual(None, node_b.left_child)
        self.assertEqual(node_c, node_b.right_child)

        self.assertEqual(node_d, node_f.parent)
        self.assertEqual(node_e, node_f.left_child)
        self.assertEqual(node_g, node_f.right_child)

        self.assertEqual(node_b, node_c.parent)
        self.assertEqual(None, node_c.left_child)
        self.assertEqual(None, node_c.right_child)

        self.assertEqual(node_f, node_e.parent)
        self.assertEqual(None, node_e.left_child)
        self.assertEqual(None, node_e.right_child)

        self.assertEqual(node_f, node_g.parent)
        self.assertEqual(None, node_g.left_child)
        self.assertEqual(None, node_g.right_child)

        self.assert_properties(node_d)

        self.assertTrue(node_e.is_leaf())

        node_e.splice_out()

        self.assertEqual(None, node_d.parent)
        self.assertEqual(node_b, node_d.left_child)
        self.assertEqual(node_f, node_d.right_child)

        self.assertEqual(node_d, node_b.parent)
        self.assertEqual(None, node_b.left_child)
        self.assertEqual(node_c, node_b.right_child)

        self.assertEqual(node_d, node_f.parent)
        self.assertEqual(None, node_f.left_child)
        self.assertEqual(node_g, node_f.right_child)

        self.assertEqual(node_b, node_c.parent)
        self.assertEqual(None, node_c.left_child)
        self.assertEqual(None, node_c.right_child)

        self.assertEqual(node_f, node_g.parent)
        self.assertEqual(None, node_g.left_child)
        self.assertEqual(None, node_g.right_child)

        self.assert_properties(node_d)

        self.assertTrue(node_g.is_leaf())

        node_g.splice_out()

        self.assertEqual(None, node_d.parent)
        self.assertEqual(node_b, node_d.left_child)
        self.assertEqual(node_f, node_d.right_child)

        self.assertEqual(node_d, node_b.parent)
        self.assertEqual(None, node_b.left_child)
        self.assertEqual(node_c, node_b.right_child)

        self.assertEqual(node_d, node_f.parent)
        self.assertEqual(None, node_f.left_child)
        self.assertEqual(None, node_f.right_child)

        self.assertEqual(node_b, node_c.parent)
        self.assertEqual(None, node_c.left_child)
        self.assertEqual(None, node_c.right_child)

        self.assert_properties(node_d)

        self.assertFalse(node_b.has_left_child())
        self.assertTrue(node_b.has_right_child())
        self.assertTrue(node_b.has_any_children())

        node_b.splice_out()

        self.assertEqual(None, node_d.parent)
        self.assertEqual(node_c, node_d.left_child)
        self.assertEqual(node_f, node_d.right_child)

        self.assertEqual(node_d, node_c.parent)
        self.assertEqual(None, node_c.left_child)
        self.assertEqual(None, node_c.right_child)

        self.assertEqual(node_d, node_f.parent)
        self.assertEqual(None, node_f.left_child)
        self.assertEqual(None, node_f.right_child)

        self.assert_properties(node_d)

    def test_splice_out_on_a_c_e_and_f(self):
        node_a, node_b, node_c, node_d, node_e, node_f, node_g = \
                                                   self.create_seven_node_tree()

        self.assertTrue(node_a.is_leaf())

        node_a.splice_out()

        self.assertEqual(None, node_d.parent)
        self.assertEqual(node_b, node_d.left_child)
        self.assertEqual(node_f, node_d.right_child)

        self.assertEqual(node_d, node_b.parent)
        self.assertEqual(None, node_b.left_child)
        self.assertEqual(node_c, node_b.right_child)

        self.assertEqual(node_d, node_f.parent)
        self.assertEqual(node_e, node_f.left_child)
        self.assertEqual(node_g, node_f.right_child)

        self.assertEqual(node_b, node_c.parent)
        self.assertEqual(None, node_c.left_child)
        self.assertEqual(None, node_c.right_child)

        self.assertEqual(node_f, node_e.parent)
        self.assertEqual(None, node_e.left_child)
        self.assertEqual(None, node_e.right_child)

        self.assertEqual(node_f, node_g.parent)
        self.assertEqual(None, node_g.left_child)
        self.assertEqual(None, node_g.right_child)

        self.assert_properties(node_d)

        self.assertTrue(node_c.is_leaf())

        node_c.splice_out()

        self.assertEqual(None, node_d.parent)
        self.assertEqual(node_b, node_d.left_child)
        self.assertEqual(node_f, node_d.right_child)

        self.assertEqual(node_d, node_b.parent)
        self.assertEqual(None, node_b.left_child)
        self.assertEqual(None, node_b.right_child)

        self.assertEqual(node_d, node_f.parent)
        self.assertEqual(node_e, node_f.left_child)
        self.assertEqual(node_g, node_f.right_child)

        self.assertEqual(node_f, node_e.parent)
        self.assertEqual(None, node_e.left_child)
        self.assertEqual(None, node_e.right_child)

        self.assertEqual(node_f, node_g.parent)
        self.assertEqual(None, node_g.left_child)
        self.assertEqual(None, node_g.right_child)

        self.assert_properties(node_d)

        self.assertTrue(node_e.is_leaf())

        node_e.splice_out()

        self.assertEqual(None, node_d.parent)
        self.assertEqual(node_b, node_d.left_child)
        self.assertEqual(node_f, node_d.right_child)

        self.assertEqual(node_d, node_b.parent)
        self.assertEqual(None, node_b.left_child)
        self.assertEqual(None, node_b.right_child)

        self.assertEqual(node_d, node_f.parent)
        self.assertEqual(None, node_f.left_child)
        self.assertEqual(node_g, node_f.right_child)

        self.assertEqual(node_f, node_g.parent)
        self.assertEqual(None, node_g.left_child)
        self.assertEqual(None, node_g.right_child)

        self.assert_properties(node_d)

        self.assertFalse(node_f.has_left_child())
        self.assertTrue(node_f.has_right_child())
        self.assertTrue(node_f.has_any_children())

        node_f.splice_out()

        self.assertEqual(None, node_d.parent)
        self.assertEqual(node_b, node_d.left_child)
        self.assertEqual(node_g, node_d.right_child)

        self.assertEqual(node_d, node_b.parent)
        self.assertEqual(None, node_b.left_child)
        self.assertEqual(None, node_b.right_child)

        self.assertEqual(node_d, node_g.parent)
        self.assertEqual(None, node_g.left_child)
        self.assertEqual(None, node_g.right_child)

        self.assert_properties(node_d)

    def test_splice_out_on_node_b_and_parent(self):
        node_a, node_b, node_c, node_d, node_e, node_f, node_g = \
                                                   self.create_seven_node_tree()

        self.assertTrue(node_b.has_both_children())

        node_b.splice_out()

        self.assertEqual(None, node_d.parent)
        self.assertEqual(node_a, node_d.left_child)
        self.assertEqual(node_f, node_d.right_child)

        self.assertEqual(node_d, node_a.parent)
        self.assertEqual(None, node_a.left_child)
        self.assertEqual(None, node_a.right_child)

        self.assertEqual(node_d, node_f.parent)
        self.assertEqual(node_e, node_f.left_child)
        self.assertEqual(node_g, node_f.right_child)

        self.assertEqual(node_f, node_e.parent)
        self.assertEqual(None, node_e.left_child)
        self.assertEqual(None, node_e.right_child)

        self.assertEqual(node_f, node_g.parent)
        self.assertEqual(None, node_g.left_child)
        self.assertEqual(None, node_g.right_child)

        node_a.splice_out()

        self.assertEqual(None, node_d.parent)
        self.assertEqual(None, node_d.left_child)
        self.assertEqual(node_f, node_d.right_child)

        self.assertEqual(node_d, node_f.parent)
        self.assertEqual(node_e, node_f.left_child)
        self.assertEqual(node_g, node_f.right_child)

        self.assertEqual(node_f, node_e.parent)
        self.assertEqual(None, node_e.left_child)
        self.assertEqual(None, node_e.right_child)

        self.assertEqual(node_f, node_g.parent)
        self.assertEqual(None, node_g.left_child)
        self.assertEqual(None, node_g.right_child)

    def test_splice_out_on_node_f_and_parent(self):
        node_a, node_b, node_c, node_d, node_e, node_f, node_g = \
                                                   self.create_seven_node_tree()

        self.assertTrue(node_f.has_both_children())

        node_f.splice_out()

        self.assertEqual(None, node_d.parent)
        self.assertEqual(node_b, node_d.left_child)
        self.assertEqual(node_e, node_d.right_child)

        self.assertEqual(node_d, node_b.parent)
        self.assertEqual(node_a, node_b.left_child)
        self.assertEqual(node_c, node_b.right_child)

        self.assertEqual(node_b, node_a.parent)
        self.assertEqual(None, node_a.left_child)
        self.assertEqual(None, node_a.right_child)

        self.assertEqual(node_b, node_c.parent)
        self.assertEqual(None, node_c.left_child)
        self.assertEqual(None, node_c.right_child)

        self.assertEqual(node_d, node_e.parent)
        self.assertEqual(None, node_e.left_child)
        self.assertEqual(None, node_e.right_child)

        node_e.splice_out()

        self.assertEqual(None, node_d.parent)
        self.assertEqual(node_b, node_d.left_child)
        self.assertEqual(None, node_d.right_child)

        self.assertEqual(node_d, node_b.parent)
        self.assertEqual(node_a, node_b.left_child)
        self.assertEqual(node_c, node_b.right_child)

        self.assertEqual(node_b, node_a.parent)
        self.assertEqual(None, node_a.left_child)
        self.assertEqual(None, node_a.right_child)

        self.assertEqual(node_b, node_c.parent)
        self.assertEqual(None, node_c.left_child)
        self.assertEqual(None, node_c.right_child)

    def test_update_on_seven_node_tree(self):
        node_a, node_b, node_c, node_d, node_e, node_f, node_g = \
                                                   self.create_seven_node_tree()

        node_a.height = -1
        node_b.height = -1
        node_c.height = -1
        node_d.height = -1
        node_e.height = -1
        node_f.height = -1
        node_g.height = -1

        self.assertEqual(-1, node_a.height)
        self.assertEqual(-1, node_b.height)
        self.assertEqual(-1, node_c.height)
        self.assertEqual(-1, node_d.height)
        self.assertEqual(-1, node_e.height)
        self.assertEqual(-1, node_f.height)
        self.assertEqual(-1, node_g.height)

        node_a.update_heights()

        self.assertEqual(0, node_a.height)
        self.assertEqual(1, node_b.height)
        self.assertEqual(-1, node_c.height)
        self.assertEqual(2, node_d.height)
        self.assertEqual(-1, node_e.height)
        self.assertEqual(-1, node_f.height)
        self.assertEqual(-1, node_g.height)

        node_b.update_heights()

        self.assertEqual(0, node_a.height)
        self.assertEqual(1, node_b.height)
        self.assertEqual(-1, node_c.height)
        self.assertEqual(2, node_d.height)
        self.assertEqual(-1, node_e.height)
        self.assertEqual(-1, node_f.height)
        self.assertEqual(-1, node_g.height)

        node_c.update_heights()

        self.assertEqual(0, node_a.height)
        self.assertEqual(1, node_b.height)
        self.assertEqual(0, node_c.height)
        self.assertEqual(2, node_d.height)
        self.assertEqual(-1, node_e.height)
        self.assertEqual(-1, node_f.height)
        self.assertEqual(-1, node_g.height)

        node_d.update_heights()

        self.assertEqual(0, node_a.height)
        self.assertEqual(1, node_b.height)
        self.assertEqual(0, node_c.height)
        self.assertEqual(2, node_d.height)
        self.assertEqual(-1, node_e.height)
        self.assertEqual(-1, node_f.height)
        self.assertEqual(-1, node_g.height)

        node_e.update_heights()

        self.assertEqual(0, node_a.height)
        self.assertEqual(1, node_b.height)
        self.assertEqual(0, node_c.height)
        self.assertEqual(2, node_d.height)
        self.assertEqual(0, node_e.height)
        self.assertEqual(1, node_f.height)
        self.assertEqual(-1, node_g.height)

        node_f.update_heights()

        self.assertEqual(0, node_a.height)
        self.assertEqual(1, node_b.height)
        self.assertEqual(0, node_c.height)
        self.assertEqual(2, node_d.height)
        self.assertEqual(0, node_e.height)
        self.assertEqual(1, node_f.height)
        self.assertEqual(-1, node_g.height)

        node_g.update_heights()

        self.assertEqual(0, node_a.height)
        self.assertEqual(1, node_b.height)
        self.assertEqual(0, node_c.height)
        self.assertEqual(2, node_d.height)
        self.assertEqual(0, node_e.height)
        self.assertEqual(1, node_f.height)
        self.assertEqual(0, node_g.height)

    def test_balance_factor_on_five_node_left_heavy_tree(self):
        node_d = self.node_type('d', 'd-value')
        node_c = self.node_type('c', 'c-value', parent=node_d)
        node_e = self.node_type('e', 'e-value', parent=node_d)
        node_d.left_child = node_c
        node_d.right_child = node_e
        node_b = self.node_type('b', 'b-value', parent=node_c)
        node_c.left_child = node_b
        node_a = self.node_type('a', 'a-value', parent=node_b)
        node_b.left_child = node_a

        node_a.update_heights()
        node_c.update_heights()
        node_b.update_heights()
        node_d.update_heights()
        node_e.update_heights()

        self.assertEqual(3, node_d.height)
        self.assertEqual(2, node_c.height)
        self.assertEqual(0, node_e.height)
        self.assertEqual(0, node_a.height)
        self.assertEqual(1, node_b.height)

        self.assertEqual(2, node_d.balance_factor())
        self.assertEqual(2, node_c.balance_factor())
        self.assertEqual(0, node_e.balance_factor())
        self.assertEqual(0, node_a.balance_factor())
        self.assertEqual(1, node_b.balance_factor())

    def test_balance_factor_on_five_node_right_heavy_tree(self):
        node_d = self.node_type('d', 'd-value')
        node_c = self.node_type('c', 'c-value', parent=node_d)
        node_e = self.node_type('e', 'e-value', parent=node_d)
        node_d.left_child = node_c
        node_d.right_child = node_e
        node_f = self.node_type('f', 'f-value', parent=node_e)
        node_e.right_child = node_f
        node_g = self.node_type('g', 'g-value', parent=node_f)
        node_f.right_child = node_g

        node_f.update_heights()
        node_g.update_heights()
        node_c.update_heights()
        node_e.update_heights()
        node_d.update_heights()

        self.assertEqual(3, node_d.height)
        self.assertEqual(0, node_c.height)
        self.assertEqual(2, node_e.height)
        self.assertEqual(1, node_f.height)
        self.assertEqual(0, node_g.height)

        self.assertEqual(-2, node_d.balance_factor())
        self.assertEqual(0, node_c.balance_factor())
        self.assertEqual(-2, node_e.balance_factor())
        self.assertEqual(-1, node_f.balance_factor())
        self.assertEqual(0, node_g.balance_factor())

class BinarySearchTreeTestCase(unittest.TestCase):

    def setUp(self):
        self.tree = binary_search_tree.BinarySearchTree()
        self.node_type = binary_search_tree.TreeNode

    def tearDown(self):
        pass

    def assert_binary_search_property(self, root):
        if root is None:
            return

        nodes = [ root ]

        while len(nodes) > 0:
            node = nodes.pop()

            if node.left_child is not None:
                self.assertTrue(node.left_child.key < node.key)
            if node.right_child is not None:
                self.assertTrue(node.key < node.right_child.key)

            if node.left_child is not None:
                nodes.append(node.left_child)
            if node.right_child is not None:
                nodes.append(node.right_child)

    def assert_height_property(self, root):
        if root is None:
            return

        nodes = [ root ]

        while len(nodes) > 0:
            node = nodes.pop()

            expected_height = 0
            if node.has_any_children():
                expected_height = (1 + max((node.left_child.height
                                            if node.left_child is not None
                                            else 0),
                                           (node.right_child.height
                                            if node.right_child is not None
                                            else 0)))
            self.assertEqual(expected_height,
                             node.height)

            if node.left_child is not None:
                nodes.append(node.left_child)
            if node.right_child is not None:
                nodes.append(node.right_child)

    def assert_properties(self, root):
        self.assert_binary_search_property(root)
        self.assert_height_property(root)

    def assert_one_node_tree_as_d(self):
        self.assertEqual(1, self.tree.size)
        self.assert_properties(self.tree.root)

        self.assertEqual('d', self.tree.root.key)
        self.assertEqual(None, self.tree.root.left_child)
        self.assertEqual(None, self.tree.root.right_child)
        self.assertEqual(None, self.tree.root.parent)

    def assert_seven_node_tree_as_d_b_f_a_c_e_g(self):
        self.assertEqual(7, self.tree.size)
        self.assert_properties(self.tree.root)

        self.assertEqual('d', self.tree.root.key)
        self.assertEqual('b', self.tree.root.left_child.key)
        self.assertEqual('f', self.tree.root.right_child.key)
        self.assertEqual(None, self.tree.root.parent)

        self.assertEqual('b', self.tree.root.left_child.key)
        self.assertEqual('a', self.tree.root.left_child.left_child.key)
        self.assertEqual('c', self.tree.root.left_child.right_child.key)
        self.assertEqual('d', self.tree.root.left_child.parent.key)

        self.assertEqual('f', self.tree.root.right_child.key)
        self.assertEqual('e', self.tree.root.right_child.left_child.key)
        self.assertEqual('g', self.tree.root.right_child.right_child.key)
        self.assertEqual('d', self.tree.root.right_child.parent.key)

        self.assertEqual('a', self.tree.root.left_child.left_child.key)
        self.assertEqual(None,
                         self.tree.root.left_child.left_child.left_child)
        self.assertEqual(None,
                         self.tree.root.left_child.left_child.right_child)
        self.assertEqual('b', self.tree.root.left_child.left_child.parent.key)

        self.assertEqual('c', self.tree.root.left_child.right_child.key)
        self.assertEqual(None,
                         self.tree.root.left_child.right_child.left_child)
        self.assertEqual(None,
                         self.tree.root.left_child.right_child.right_child)
        self.assertEqual('b', self.tree.root.left_child.right_child.parent.key)

        self.assertEqual('e', self.tree.root.right_child.left_child.key)
        self.assertEqual(None,
                         self.tree.root.right_child.left_child.left_child)
        self.assertEqual(None,
                         self.tree.root.right_child.left_child.right_child)
        self.assertEqual('f', self.tree.root.right_child.left_child.parent.key)

        self.assertEqual('g', self.tree.root.right_child.right_child.key)
        self.assertEqual(None,
                         self.tree.root.right_child.right_child.left_child)
        self.assertEqual(None,
                         self.tree.root.right_child.right_child.right_child)
        self.assertEqual('f', self.tree.root.right_child.right_child.parent.key)

    def create_one_node_tree_as_d(self):
        node_d = self.node_type('d', 'd-value')
        self.tree.root = node_d
        self.tree._size = 1

        node_d.update_heights()

        self.assert_one_node_tree_as_d()

    def create_seven_node_tree(self):
        node_d = self.node_type('d', 'd-value')
        node_b = self.node_type('b', 'b-value', parent=node_d)
        node_f = self.node_type('f', 'f-value', parent=node_d)
        node_d.left_child = node_b
        node_d.right_child = node_f
        node_a = self.node_type('a', 'a-value', parent=node_b)
        node_c = self.node_type('c', 'c-value', parent=node_b)
        node_b.left_child = node_a
        node_b.right_child = node_c
        node_e = self.node_type('e', 'e-value', parent=node_f)
        node_g = self.node_type('g', 'g-value', parent=node_f)
        node_f.left_child = node_e
        node_f.right_child = node_g
        self.tree.root = node_d
        self.tree._size = 7

        node_a.update_heights()
        node_b.update_heights()
        node_c.update_heights()
        node_d.update_heights()
        node_e.update_heights()
        node_f.update_heights()
        node_g.update_heights()

        self.assert_seven_node_tree_as_d_b_f_a_c_e_g()

    def test_constructor(self):
        self.assertEqual(None, self.tree.root)
        self.assertEqual(0, self.tree._size)

    def test_str_of_empty_tree(self):
        self.assertEquals('root: [None], size: 0', str(self.tree))

    def test_str_of_nonempty_tree(self):
        self.create_seven_node_tree()

        self.assertEquals('root: [key: d, value: d-value], size: 7',
                          str(self.tree))

    def test_repr_of_empty_tree(self):
        self.assertEquals('None', repr(self.tree))

    def test_repr(self):
        self.create_seven_node_tree()

        self.assertEquals('root: [key: d, value: d-value], size: 7, nodes: ' +
                          '[key: d, value: d-value, parent: [None], ' +
                          'left: [key: b, value: b-value], ' +
                          'right: [key: f, value: f-value], height: 2], ' +
                          '[key: f, value: f-value, parent: [key: d, value: ' +
                          'd-value], left: [key: e, value: e-value], ' +
                          'right: [key: g, value: g-value], height: 1], ' +
                          '[key: g, value: g-value, parent: [key: f, value: ' +
                          'f-value], left: [None], right: [None], ' +
                          'height: 0], [key: e, value: e-value, parent: ' +
                          '[key: f, value: f-value], left: [None], right: ' +
                          '[None], height: 0], [key: b, value: b-value, ' +
                          'parent: [key: d, value: d-value], left: [key: a, ' +
                          'value: a-value], right: [key: c, value: c-value], ' +
                          'height: 1], [key: c, value: c-value, parent: ' +
                          '[key: b, value: b-value], left: [None], right: ' +
                          '[None], height: 0], [key: a, value: a-value, ' +
                          'parent: [key: b, value: b-value], left: [None], ' +
                          'right: [None], height: 0]',
                          repr(self.tree))

    def test_len_of_empty_tree(self):
        self.assertEqual(0, self.tree.__len__())
        self.assertEqual(0, len(self.tree))

    def test_len_of_seven_node_tree(self):
        self.create_seven_node_tree()

        self.assertEqual(7, self.tree.__len__())
        self.assertEqual(7, len(self.tree))

    def test_getitem_on_empty_tree(self):
        self.assertEqual(None, self.tree['a'])

        self.assertEqual(0, self.tree.size)
        self.assert_properties(self.tree.root)

    def test_getitem_on_seven_node_tree(self):
        self.create_seven_node_tree()

        self.assertEqual('a-value', self.tree['a'])
        self.assertEqual('b-value', self.tree['b'])
        self.assertEqual('c-value', self.tree['c'])
        self.assertEqual('d-value', self.tree['d'])
        self.assertEqual('e-value', self.tree['e'])
        self.assertEqual('f-value', self.tree['f'])
        self.assertEqual('g-value', self.tree['g'])
        self.assertEqual(None, self.tree['z'])

        self.assertEqual(7, self.tree.size)
        self.assert_properties(self.tree.root)

    def test_setitem_on_empty_tree_to_add_seven_nodes(self):
        self.assertEqual(None, self.tree.get('a'))
        self.assertEqual(0, self.tree.size)

        self.tree['d'] = 'd-value'

        self.assertEqual(1, self.tree.size)
        self.assert_properties(self.tree.root)

        self.assertEqual('d', self.tree.root.key)
        self.assertEqual('d-value', self.tree.root.value)
        self.assertEqual(None, self.tree.root.left_child)
        self.assertEqual(None, self.tree.root.right_child)
        self.assertEqual(None, self.tree.root.parent)

        self.tree['b'] = 'b-value'

        self.assertEqual(2, self.tree.size)
        self.assert_properties(self.tree.root)

        self.assertEqual('d', self.tree.root.key)
        self.assertEqual('d-value', self.tree.root.value)
        self.assertEqual('b', self.tree.root.left_child.key)
        self.assertEqual(None, self.tree.root.right_child)
        self.assertEqual(None, self.tree.root.parent)

        self.assertEqual('b', self.tree.root.left_child.key)
        self.assertEqual('b-value', self.tree.root.left_child.value)
        self.assertEqual(None, self.tree.root.left_child.left_child)
        self.assertEqual(None, self.tree.root.left_child.right_child)
        self.assertEqual('d', self.tree.root.left_child.parent.key)

        self.tree['f'] = 'f-value'

        self.assertEqual(3, self.tree.size)
        self.assert_properties(self.tree.root)

        self.assertEqual('d', self.tree.root.key)
        self.assertEqual('d-value', self.tree.root.value)
        self.assertEqual('b', self.tree.root.left_child.key)
        self.assertEqual('f', self.tree.root.right_child.key)
        self.assertEqual(None, self.tree.root.parent)

        self.assertEqual('b', self.tree.root.left_child.key)
        self.assertEqual('b-value', self.tree.root.left_child.value)
        self.assertEqual(None, self.tree.root.left_child.left_child)
        self.assertEqual(None, self.tree.root.left_child.right_child)
        self.assertEqual('d', self.tree.root.left_child.parent.key)

        self.assertEqual('f', self.tree.root.right_child.key)
        self.assertEqual('f-value', self.tree.root.right_child.value)
        self.assertEqual(None, self.tree.root.right_child.left_child)
        self.assertEqual(None, self.tree.root.right_child.right_child)
        self.assertEqual('d', self.tree.root.right_child.parent.key)

        self.tree['a'] = 'a-value'

        self.assertEqual(4, self.tree.size)
        self.assert_properties(self.tree.root)

        self.assertEqual('d', self.tree.root.key)
        self.assertEqual('d-value', self.tree.root.value)
        self.assertEqual('b', self.tree.root.left_child.key)
        self.assertEqual('f', self.tree.root.right_child.key)
        self.assertEqual(None, self.tree.root.parent)

        self.assertEqual('b', self.tree.root.left_child.key)
        self.assertEqual('b-value', self.tree.root.left_child.value)
        self.assertEqual('a', self.tree.root.left_child.left_child.key)
        self.assertEqual(None, self.tree.root.left_child.right_child)
        self.assertEqual('d', self.tree.root.left_child.parent.key)

        self.assertEqual('f', self.tree.root.right_child.key)
        self.assertEqual('f-value', self.tree.root.right_child.value)
        self.assertEqual(None, self.tree.root.right_child.left_child)
        self.assertEqual(None, self.tree.root.right_child.right_child)
        self.assertEqual('d', self.tree.root.right_child.parent.key)

        self.assertEqual('a', self.tree.root.left_child.left_child.key)
        self.assertEqual('a-value', self.tree.root.left_child.left_child.value)
        self.assertEqual(None, self.tree.root.left_child.left_child.left_child)
        self.assertEqual(None, self.tree.root.left_child.left_child.right_child)
        self.assertEqual('b', self.tree.root.left_child.left_child.parent.key)

        self.tree['c'] = 'c-value'

        self.assertEqual(5, self.tree.size)
        self.assert_properties(self.tree.root)

        self.assertEqual('d', self.tree.root.key)
        self.assertEqual('d-value', self.tree.root.value)
        self.assertEqual('b', self.tree.root.left_child.key)
        self.assertEqual('f', self.tree.root.right_child.key)
        self.assertEqual(None, self.tree.root.parent)

        self.assertEqual('b', self.tree.root.left_child.key)
        self.assertEqual('b-value', self.tree.root.left_child.value)
        self.assertEqual('a', self.tree.root.left_child.left_child.key)
        self.assertEqual('c', self.tree.root.left_child.right_child.key)
        self.assertEqual('d', self.tree.root.left_child.parent.key)

        self.assertEqual('f', self.tree.root.right_child.key)
        self.assertEqual('f-value', self.tree.root.right_child.value)
        self.assertEqual(None, self.tree.root.right_child.left_child)
        self.assertEqual(None, self.tree.root.right_child.right_child)
        self.assertEqual('d', self.tree.root.right_child.parent.key)

        self.assertEqual('a', self.tree.root.left_child.left_child.key)
        self.assertEqual('a-value', self.tree.root.left_child.left_child.value)
        self.assertEqual(None, self.tree.root.left_child.left_child.left_child)
        self.assertEqual(None, self.tree.root.left_child.left_child.right_child)
        self.assertEqual('b', self.tree.root.left_child.left_child.parent.key)

        self.assertEqual('c', self.tree.root.left_child.right_child.key)
        self.assertEqual('c-value', self.tree.root.left_child.right_child.value)
        self.assertEqual(None,
                         self.tree.root.left_child.right_child.left_child)
        self.assertEqual(None,
                         self.tree.root.left_child.right_child.right_child)
        self.assertEqual('b',
                         self.tree.root.left_child.right_child.parent.key)

        self.tree['e'] = 'e-value'

        self.assertEqual(6, self.tree.size)
        self.assert_properties(self.tree.root)

        self.assertEqual('d', self.tree.root.key)
        self.assertEqual('d-value', self.tree.root.value)
        self.assertEqual('b', self.tree.root.left_child.key)
        self.assertEqual('f', self.tree.root.right_child.key)
        self.assertEqual(None, self.tree.root.parent)

        self.assertEqual('b', self.tree.root.left_child.key)
        self.assertEqual('b-value', self.tree.root.left_child.value)
        self.assertEqual('a', self.tree.root.left_child.left_child.key)
        self.assertEqual('c', self.tree.root.left_child.right_child.key)
        self.assertEqual('d', self.tree.root.left_child.parent.key)

        self.assertEqual('f', self.tree.root.right_child.key)
        self.assertEqual('f-value', self.tree.root.right_child.value)
        self.assertEqual('e', self.tree.root.right_child.left_child.key)
        self.assertEqual(None, self.tree.root.right_child.right_child)
        self.assertEqual('d', self.tree.root.right_child.parent.key)

        self.assertEqual('a', self.tree.root.left_child.left_child.key)
        self.assertEqual('a-value', self.tree.root.left_child.left_child.value)
        self.assertEqual(None, self.tree.root.left_child.left_child.left_child)
        self.assertEqual(None, self.tree.root.left_child.left_child.right_child)
        self.assertEqual('b', self.tree.root.left_child.left_child.parent.key)

        self.assertEqual('c', self.tree.root.left_child.right_child.key)
        self.assertEqual('c-value', self.tree.root.left_child.right_child.value)
        self.assertEqual(None,
                         self.tree.root.left_child.right_child.left_child)
        self.assertEqual(None,
                         self.tree.root.left_child.right_child.right_child)
        self.assertEqual('b',
                         self.tree.root.left_child.right_child.parent.key)

        self.assertEqual('e', self.tree.root.right_child.left_child.key)
        self.assertEqual('e-value', self.tree.root.right_child.left_child.value)
        self.assertEqual(None,
                         self.tree.root.right_child.left_child.left_child)
        self.assertEqual(None,
                         self.tree.root.right_child.left_child.right_child)
        self.assertEqual('f', self.tree.root.right_child.left_child.parent.key)

        self.tree['g'] = 'g-value'

        self.assertEqual(7, self.tree.size)
        self.assert_properties(self.tree.root)

        self.assertEqual('d', self.tree.root.key)
        self.assertEqual('d-value', self.tree.root.value)
        self.assertEqual('b', self.tree.root.left_child.key)
        self.assertEqual('f', self.tree.root.right_child.key)
        self.assertEqual(None, self.tree.root.parent)

        self.assertEqual('b', self.tree.root.left_child.key)
        self.assertEqual('b-value', self.tree.root.left_child.value)
        self.assertEqual('a', self.tree.root.left_child.left_child.key)
        self.assertEqual('c', self.tree.root.left_child.right_child.key)
        self.assertEqual('d', self.tree.root.left_child.parent.key)

        self.assertEqual('f', self.tree.root.right_child.key)
        self.assertEqual('f-value', self.tree.root.right_child.value)
        self.assertEqual('e', self.tree.root.right_child.left_child.key)
        self.assertEqual('g', self.tree.root.right_child.right_child.key)
        self.assertEqual('d', self.tree.root.right_child.parent.key)

        self.assertEqual('a', self.tree.root.left_child.left_child.key)
        self.assertEqual('a-value', self.tree.root.left_child.left_child.value)
        self.assertEqual(None, self.tree.root.left_child.left_child.left_child)
        self.assertEqual(None, self.tree.root.left_child.left_child.right_child)
        self.assertEqual('b', self.tree.root.left_child.left_child.parent.key)

        self.assertEqual('c', self.tree.root.left_child.right_child.key)
        self.assertEqual('c-value', self.tree.root.left_child.right_child.value)
        self.assertEqual(None,
                         self.tree.root.left_child.right_child.left_child)
        self.assertEqual(None,
                         self.tree.root.left_child.right_child.right_child)
        self.assertEqual('b',
                         self.tree.root.left_child.right_child.parent.key)

        self.assertEqual('e', self.tree.root.right_child.left_child.key)
        self.assertEqual('e-value', self.tree.root.right_child.left_child.value)
        self.assertEqual(None,
                         self.tree.root.right_child.left_child.left_child)
        self.assertEqual(None,
                         self.tree.root.right_child.left_child.right_child)
        self.assertEqual('f', self.tree.root.right_child.left_child.parent.key)

        self.assertEqual('g', self.tree.root.right_child.right_child.key)
        self.assertEqual('g-value',
                         self.tree.root.right_child.right_child.value)
        self.assertEqual(None,
                         self.tree.root.right_child.right_child.left_child)
        self.assertEqual(None,
                         self.tree.root.right_child.right_child.right_child)
        self.assertEqual('f', self.tree.root.right_child.right_child.parent.key)

        self.tree['a'] = 'new-a-value'

        self.assertEqual(7, self.tree.size)
        self.assert_properties(self.tree.root)

        self.assertEqual('d', self.tree.root.key)
        self.assertEqual('d-value', self.tree.root.value)
        self.assertEqual('b', self.tree.root.left_child.key)
        self.assertEqual('f', self.tree.root.right_child.key)
        self.assertEqual(None, self.tree.root.parent)

        self.assertEqual('b', self.tree.root.left_child.key)
        self.assertEqual('b-value', self.tree.root.left_child.value)
        self.assertEqual('a', self.tree.root.left_child.left_child.key)
        self.assertEqual('c', self.tree.root.left_child.right_child.key)
        self.assertEqual('d', self.tree.root.left_child.parent.key)

        self.assertEqual('f', self.tree.root.right_child.key)
        self.assertEqual('f-value', self.tree.root.right_child.value)
        self.assertEqual('e', self.tree.root.right_child.left_child.key)
        self.assertEqual('g', self.tree.root.right_child.right_child.key)
        self.assertEqual('d', self.tree.root.right_child.parent.key)

        self.assertEqual('a', self.tree.root.left_child.left_child.key)
        self.assertEqual('new-a-value',
                         self.tree.root.left_child.left_child.value)
        self.assertEqual(None,
                         self.tree.root.left_child.left_child.left_child)
        self.assertEqual(None,
                         self.tree.root.left_child.left_child.right_child)
        self.assertEqual('b', self.tree.root.left_child.left_child.parent.key)

        self.assertEqual('c', self.tree.root.left_child.right_child.key)
        self.assertEqual('c-value', self.tree.root.left_child.right_child.value)
        self.assertEqual(None,
                         self.tree.root.left_child.right_child.left_child)
        self.assertEqual(None,
                         self.tree.root.left_child.right_child.right_child)
        self.assertEqual('b', self.tree.root.left_child.right_child.parent.key)

        self.assertEqual('e', self.tree.root.right_child.left_child.key)
        self.assertEqual('e-value', self.tree.root.right_child.left_child.value)
        self.assertEqual(None,
                         self.tree.root.right_child.left_child.left_child)
        self.assertEqual(None,
                         self.tree.root.right_child.left_child.right_child)
        self.assertEqual('f', self.tree.root.right_child.left_child.parent.key)

        self.assertEqual('g', self.tree.root.right_child.right_child.key)
        self.assertEqual('g-value',
                         self.tree.root.right_child.right_child.value)
        self.assertEqual(None,
                         self.tree.root.right_child.right_child.left_child)
        self.assertEqual(None,
                         self.tree.root.right_child.right_child.right_child)
        self.assertEqual('f', self.tree.root.right_child.right_child.parent.key)

    def test_delitem_on_seven_node_tree(self):
        self.create_seven_node_tree()

        with self.assertRaisesRegex(KeyError,
                                    'The key not in the tree.'):
            del self.tree['z']

        del self.tree['a']

        self.assertEqual(6, self.tree.size)
        self.assert_properties(self.tree.root)

        self.assertEqual('d', self.tree.root.key)
        self.assertEqual('d-value', self.tree.root.value)
        self.assertEqual('b', self.tree.root.left_child.key)
        self.assertEqual('f', self.tree.root.right_child.key)
        self.assertEqual(None, self.tree.root.parent)

        self.assertEqual('b', self.tree.root.left_child.key)
        self.assertEqual('b-value', self.tree.root.left_child.value)
        self.assertEqual(None, self.tree.root.left_child.left_child)
        self.assertEqual('c', self.tree.root.left_child.right_child.key)

        self.assertEqual('f', self.tree.root.right_child.key)
        self.assertEqual('f-value', self.tree.root.right_child.value)
        self.assertEqual('e', self.tree.root.right_child.left_child.key)
        self.assertEqual('g', self.tree.root.right_child.right_child.key)

        self.assertEqual('c', self.tree.root.left_child.right_child.key)
        self.assertEqual('c-value', self.tree.root.left_child.right_child.value)
        self.assertEqual(None,
                         self.tree.root.left_child.right_child.left_child)
        self.assertEqual(None,
                         self.tree.root.left_child.right_child.right_child)

        self.assertEqual('e', self.tree.root.right_child.left_child.key)
        self.assertEqual('e-value', self.tree.root.right_child.left_child.value)
        self.assertEqual(None,
                         self.tree.root.right_child.left_child.left_child)
        self.assertEqual(None,
                         self.tree.root.right_child.left_child.right_child)

        self.assertEqual('g', self.tree.root.right_child.right_child.key)
        self.assertEqual('g-value',
                         self.tree.root.right_child.right_child.value)
        self.assertEqual(None,
                         self.tree.root.right_child.right_child.left_child)
        self.assertEqual(None,
                         self.tree.root.right_child.right_child.right_child)

        del self.tree['c']

        self.assertEqual(5, self.tree.size)
        self.assert_properties(self.tree.root)

        self.assertEqual('d', self.tree.root.key)
        self.assertEqual('d-value', self.tree.root.value)
        self.assertEqual('b', self.tree.root.left_child.key)
        self.assertEqual('f', self.tree.root.right_child.key)
        self.assertEqual(None, self.tree.root.parent)

        self.assertEqual('b', self.tree.root.left_child.key)
        self.assertEqual('b-value', self.tree.root.left_child.value)
        self.assertEqual(None, self.tree.root.left_child.left_child)
        self.assertEqual(None, self.tree.root.left_child.right_child)

        self.assertEqual('f', self.tree.root.right_child.key)
        self.assertEqual('f-value', self.tree.root.right_child.value)
        self.assertEqual('e', self.tree.root.right_child.left_child.key)
        self.assertEqual('g', self.tree.root.right_child.right_child.key)

        self.assertEqual('e', self.tree.root.right_child.left_child.key)
        self.assertEqual('e-value', self.tree.root.right_child.left_child.value)
        self.assertEqual(None,
                         self.tree.root.right_child.left_child.left_child)
        self.assertEqual(None,
                         self.tree.root.right_child.left_child.right_child)

        self.assertEqual('g', self.tree.root.right_child.right_child.key)
        self.assertEqual('g-value',
                         self.tree.root.right_child.right_child.value)
        self.assertEqual(None,
                         self.tree.root.right_child.right_child.left_child)
        self.assertEqual(None,
                         self.tree.root.right_child.right_child.right_child)

        del self.tree['e']

        self.assertEqual(4, self.tree.size)
        self.assert_properties(self.tree.root)

        self.assertEqual('d', self.tree.root.key)
        self.assertEqual('d-value', self.tree.root.value)
        self.assertEqual('b', self.tree.root.left_child.key)
        self.assertEqual('f', self.tree.root.right_child.key)
        self.assertEqual(None, self.tree.root.parent)

        self.assertEqual('b', self.tree.root.left_child.key)
        self.assertEqual('b-value', self.tree.root.left_child.value)
        self.assertEqual(None, self.tree.root.left_child.left_child)
        self.assertEqual(None, self.tree.root.left_child.right_child)

        self.assertEqual('f', self.tree.root.right_child.key)
        self.assertEqual('f-value', self.tree.root.right_child.value)
        self.assertEqual(None, self.tree.root.right_child.left_child)
        self.assertEqual('g', self.tree.root.right_child.right_child.key)

        self.assertEqual('g', self.tree.root.right_child.right_child.key)
        self.assertEqual('g-value',
                         self.tree.root.right_child.right_child.value)
        self.assertEqual(None,
                         self.tree.root.right_child.right_child.left_child)
        self.assertEqual(None,
                         self.tree.root.right_child.right_child.right_child)

        del self.tree['g']

        self.assertEqual(3, self.tree.size)
        self.assert_properties(self.tree.root)

        self.assertEqual('d', self.tree.root.key)
        self.assertEqual('d-value', self.tree.root.value)
        self.assertEqual('b', self.tree.root.left_child.key)
        self.assertEqual('f', self.tree.root.right_child.key)
        self.assertEqual(None, self.tree.root.parent)

        self.assertEqual('b', self.tree.root.left_child.key)
        self.assertEqual('b-value', self.tree.root.left_child.value)
        self.assertEqual(None, self.tree.root.left_child.left_child)
        self.assertEqual(None, self.tree.root.left_child.right_child)

        self.assertEqual('f', self.tree.root.right_child.key)
        self.assertEqual('f-value', self.tree.root.right_child.value)
        self.assertEqual(None, self.tree.root.right_child.left_child)
        self.assertEqual(None, self.tree.root.right_child.right_child)

        del self.tree['b']

        self.assertEqual(2, self.tree.size)
        self.assert_properties(self.tree.root)

        self.assertEqual('d', self.tree.root.key)
        self.assertEqual('d-value', self.tree.root.value)
        self.assertEqual(None, self.tree.root.left_child)
        self.assertEqual('f', self.tree.root.right_child.key)
        self.assertEqual(None, self.tree.root.parent)

        self.assertEqual('f', self.tree.root.right_child.key)
        self.assertEqual('f-value', self.tree.root.right_child.value)
        self.assertEqual(None, self.tree.root.right_child.left_child)
        self.assertEqual(None, self.tree.root.right_child.right_child)

        del self.tree['f']

        self.assertEqual(1, self.tree.size)
        self.assert_properties(self.tree.root)

        self.assertEqual('d', self.tree.root.key)
        self.assertEqual('d-value', self.tree.root.value)
        self.assertEqual(None, self.tree.root.left_child)
        self.assertEqual(None, self.tree.root.right_child)
        self.assertEqual(None, self.tree.root.parent)

        del self.tree['d']

        self.assertEqual(0, self.tree.size)
        self.assert_properties(self.tree.root)

        with self.assertRaisesRegex(KeyError,
                                    'The key not in the tree.'):
            del self.tree['z']

    def test_contains_on_empty_tree(self):
        self.assertFalse('a' in self.tree)

    def test_contains_on_seven_node_tree(self):
        self.create_seven_node_tree()

        self.assertTrue('a' in self.tree)
        self.assertTrue('b' in self.tree)
        self.assertTrue('c' in self.tree)
        self.assertTrue('d' in self.tree)
        self.assertTrue('e' in self.tree)
        self.assertTrue('f' in self.tree)
        self.assertTrue('g' in self.tree)
        self.assertFalse('z' in self.tree)
        self.assertTrue('z' not in self.tree)

    def test_iter_on_seven_node_tree(self):
        self.create_seven_node_tree()

        expected_keys = [ 'a', 'b', 'c', 'd', 'e', 'f', 'g',  ]
        for actual_key in self.tree:
            self.assertTrue(actual_key in expected_keys)

    def test_under_get_on_empty_tree(self):
        self.assertEqual(None, self.tree._get('a', self.tree.root))

        self.assertEqual(0, self.tree.size)
        self.assert_properties(self.tree.root)

    def test_under_get_on_seven_node_tree(self):
        self.create_seven_node_tree()

        self.assertEqual(self.tree.root.left_child.left_child,
                         self.tree._get('a', self.tree.root))
        self.assertEqual(self.tree.root.left_child,
                         self.tree._get('b', self.tree.root))
        self.assertEqual(self.tree.root.left_child.right_child,
                         self.tree._get('c', self.tree.root))
        self.assertEqual(self.tree.root,
                         self.tree._get('d', self.tree.root))
        self.assertEqual(self.tree.root.right_child.left_child,
                         self.tree._get('e', self.tree.root))
        self.assertEqual(self.tree.root.right_child,
                         self.tree._get('f', self.tree.root))
        self.assertEqual(self.tree.root.right_child.right_child,
                         self.tree._get('g', self.tree.root))
        self.assertEqual(None, self.tree._get('z', self.tree.root))

        self.assertEqual(7, self.tree.size)
        self.assert_properties(self.tree.root)

    def test_under_put_on_empty_tree(self):
        self.assertEqual(None, self.tree._get('a', self.tree.root))
        self.assertEqual(0, self.tree.size)

        with self.assertRaisesRegex(AttributeError,
                                    "'NoneType' object has no attribute 'key'"):
            self.tree._put('a', 'a-value', self.tree.root)

    def test_under_put_on_one_node_tree_with_a(self):
        self.create_one_node_tree_as_d()

        duplicate_found = self.tree._put('a', 'a-value', self.tree.root)

        self.assertFalse(duplicate_found)
        self.assertEqual(1, self.tree.size)
        self.assert_properties(self.tree.root)

        self.assertEqual('d', self.tree.root.key)
        self.assertEqual('d-value', self.tree.root.value)
        self.assertEqual('a', self.tree.root.left_child.key)
        self.assertEqual(None, self.tree.root.right_child)
        self.assertEqual(None, self.tree.root.parent)

        self.assertEqual('a', self.tree.root.left_child.key)
        self.assertEqual('a-value', self.tree.root.left_child.value)
        self.assertEqual(None, self.tree.root.left_child.left_child)
        self.assertEqual(None, self.tree.root.left_child.right_child)
        self.assertEqual('d', self.tree.root.left_child.parent.key)

    def test_under_put_on_one_node_tree_with_g(self):
        self.create_one_node_tree_as_d()

        duplicate_found = self.tree._put('g', 'g-value', self.tree.root)

        self.assertFalse(duplicate_found)
        self.assertEqual(1, self.tree.size)
        self.assert_properties(self.tree.root)

        self.assertEqual('d', self.tree.root.key)
        self.assertEqual('d-value', self.tree.root.value)
        self.assertEqual(None, self.tree.root.left_child)
        self.assertEqual('g', self.tree.root.right_child.key)
        self.assertEqual(None, self.tree.root.parent)

        self.assertEqual('g', self.tree.root.right_child.key)
        self.assertEqual('g-value', self.tree.root.right_child.value)
        self.assertEqual(None, self.tree.root.right_child.left_child)
        self.assertEqual(None, self.tree.root.right_child.right_child)
        self.assertEqual('d', self.tree.root.right_child.parent.key)

    def test_under_put_on_one_node_tree_with_b_f_a_c_e_g(self):
        self.create_one_node_tree_as_d()

        duplicate_found = self.tree._put('b', 'b-value', self.tree.root)

        self.assertFalse(duplicate_found)
        self.assertEqual(1, self.tree.size)
        self.assert_properties(self.tree.root)

        self.assertEqual('d', self.tree.root.key)
        self.assertEqual('d-value', self.tree.root.value)
        self.assertEqual('b', self.tree.root.left_child.key)
        self.assertEqual(None, self.tree.root.right_child)
        self.assertEqual(None, self.tree.root.parent)

        self.assertEqual('b', self.tree.root.left_child.key)
        self.assertEqual('b-value', self.tree.root.left_child.value)
        self.assertEqual(None, self.tree.root.left_child.left_child)
        self.assertEqual(None, self.tree.root.left_child.right_child)
        self.assertEqual('d', self.tree.root.left_child.parent.key)

        duplicate_found = self.tree._put('f', 'f-value', self.tree.root)

        self.assertFalse(duplicate_found)
        self.assertEqual(1, self.tree.size)
        self.assert_properties(self.tree.root)

        self.assertEqual('d', self.tree.root.key)
        self.assertEqual('d-value', self.tree.root.value)
        self.assertEqual('b', self.tree.root.left_child.key)
        self.assertEqual('f', self.tree.root.right_child.key)
        self.assertEqual(None, self.tree.root.parent)

        self.assertEqual('b', self.tree.root.left_child.key)
        self.assertEqual('b-value', self.tree.root.left_child.value)
        self.assertEqual(None, self.tree.root.left_child.left_child)
        self.assertEqual(None, self.tree.root.left_child.right_child)
        self.assertEqual('d', self.tree.root.left_child.parent.key)

        self.assertEqual('f', self.tree.root.right_child.key)
        self.assertEqual('f-value', self.tree.root.right_child.value)
        self.assertEqual(None, self.tree.root.right_child.left_child)
        self.assertEqual(None, self.tree.root.right_child.right_child)
        self.assertEqual('d', self.tree.root.right_child.parent.key)

        duplicate_found = self.tree._put('a', 'a-value', self.tree.root)

        self.assertFalse(duplicate_found)
        self.assertEqual(1, self.tree.size)
        self.assert_properties(self.tree.root)

        self.assertEqual('d', self.tree.root.key)
        self.assertEqual('d-value', self.tree.root.value)
        self.assertEqual('b', self.tree.root.left_child.key)
        self.assertEqual('f', self.tree.root.right_child.key)
        self.assertEqual(None, self.tree.root.parent)

        self.assertEqual('b', self.tree.root.left_child.key)
        self.assertEqual('b-value', self.tree.root.left_child.value)
        self.assertEqual('a', self.tree.root.left_child.left_child.key)
        self.assertEqual(None, self.tree.root.left_child.right_child)
        self.assertEqual('d', self.tree.root.left_child.parent.key)

        self.assertEqual('f', self.tree.root.right_child.key)
        self.assertEqual('f-value', self.tree.root.right_child.value)
        self.assertEqual(None, self.tree.root.right_child.left_child)
        self.assertEqual(None, self.tree.root.right_child.right_child)
        self.assertEqual('d', self.tree.root.right_child.parent.key)

        self.assertEqual('a', self.tree.root.left_child.left_child.key)
        self.assertEqual('a-value', self.tree.root.left_child.left_child.value)
        self.assertEqual(None, self.tree.root.left_child.left_child.left_child)
        self.assertEqual(None, self.tree.root.left_child.left_child.right_child)
        self.assertEqual('b', self.tree.root.left_child.left_child.parent.key)

        duplicate_found = self.tree._put('c', 'c-value', self.tree.root)

        self.assertFalse(duplicate_found)
        self.assertEqual(1, self.tree.size)
        self.assert_properties(self.tree.root)

        self.assertEqual('d', self.tree.root.key)
        self.assertEqual('d-value', self.tree.root.value)
        self.assertEqual('b', self.tree.root.left_child.key)
        self.assertEqual('f', self.tree.root.right_child.key)
        self.assertEqual(None, self.tree.root.parent)

        self.assertEqual('b', self.tree.root.left_child.key)
        self.assertEqual('b-value', self.tree.root.left_child.value)
        self.assertEqual('a', self.tree.root.left_child.left_child.key)
        self.assertEqual('c', self.tree.root.left_child.right_child.key)
        self.assertEqual('d', self.tree.root.left_child.parent.key)

        self.assertEqual('f', self.tree.root.right_child.key)
        self.assertEqual('f-value', self.tree.root.right_child.value)
        self.assertEqual(None, self.tree.root.right_child.left_child)
        self.assertEqual(None, self.tree.root.right_child.right_child)
        self.assertEqual('d', self.tree.root.right_child.parent.key)

        self.assertEqual('a', self.tree.root.left_child.left_child.key)
        self.assertEqual('a-value', self.tree.root.left_child.left_child.value)
        self.assertEqual(None, self.tree.root.left_child.left_child.left_child)
        self.assertEqual(None, self.tree.root.left_child.left_child.right_child)
        self.assertEqual('b', self.tree.root.left_child.left_child.parent.key)

        self.assertEqual('c', self.tree.root.left_child.right_child.key)
        self.assertEqual('c-value', self.tree.root.left_child.right_child.value)
        self.assertEqual(None,
                         self.tree.root.left_child.right_child.left_child)
        self.assertEqual(None,
                         self.tree.root.left_child.right_child.right_child)
        self.assertEqual('b',
                         self.tree.root.left_child.right_child.parent.key)

        duplicate_found = self.tree._put('e', 'e-value', self.tree.root)

        self.assertFalse(duplicate_found)
        self.assertEqual(1, self.tree.size)
        self.assert_properties(self.tree.root)

        self.assertEqual('d', self.tree.root.key)
        self.assertEqual('d-value', self.tree.root.value)
        self.assertEqual('b', self.tree.root.left_child.key)
        self.assertEqual('f', self.tree.root.right_child.key)
        self.assertEqual(None, self.tree.root.parent)

        self.assertEqual('b', self.tree.root.left_child.key)
        self.assertEqual('b-value', self.tree.root.left_child.value)
        self.assertEqual('a', self.tree.root.left_child.left_child.key)
        self.assertEqual('c', self.tree.root.left_child.right_child.key)
        self.assertEqual('d', self.tree.root.left_child.parent.key)

        self.assertEqual('f', self.tree.root.right_child.key)
        self.assertEqual('f-value', self.tree.root.right_child.value)
        self.assertEqual('e', self.tree.root.right_child.left_child.key)
        self.assertEqual(None, self.tree.root.right_child.right_child)
        self.assertEqual('d', self.tree.root.right_child.parent.key)

        self.assertEqual('a', self.tree.root.left_child.left_child.key)
        self.assertEqual('a-value', self.tree.root.left_child.left_child.value)
        self.assertEqual(None, self.tree.root.left_child.left_child.left_child)
        self.assertEqual(None, self.tree.root.left_child.left_child.right_child)
        self.assertEqual('b', self.tree.root.left_child.left_child.parent.key)

        self.assertEqual('c', self.tree.root.left_child.right_child.key)
        self.assertEqual('c-value', self.tree.root.left_child.right_child.value)
        self.assertEqual(None,
                         self.tree.root.left_child.right_child.left_child)
        self.assertEqual(None,
                         self.tree.root.left_child.right_child.right_child)
        self.assertEqual('b',
                         self.tree.root.left_child.right_child.parent.key)

        self.assertEqual('e', self.tree.root.right_child.left_child.key)
        self.assertEqual('e-value', self.tree.root.right_child.left_child.value)
        self.assertEqual(None,
                         self.tree.root.right_child.left_child.left_child)
        self.assertEqual(None,
                         self.tree.root.right_child.left_child.right_child)
        self.assertEqual('f', self.tree.root.right_child.left_child.parent.key)

        duplicate_found = self.tree._put('g', 'g-value', self.tree.root)

        self.assertFalse(duplicate_found)
        self.assertEqual(1, self.tree.size)
        self.assert_properties(self.tree.root)

        self.assertEqual('d', self.tree.root.key)
        self.assertEqual('d-value', self.tree.root.value)
        self.assertEqual('b', self.tree.root.left_child.key)
        self.assertEqual('f', self.tree.root.right_child.key)
        self.assertEqual(None, self.tree.root.parent)

        self.assertEqual('b', self.tree.root.left_child.key)
        self.assertEqual('b-value', self.tree.root.left_child.value)
        self.assertEqual('a', self.tree.root.left_child.left_child.key)
        self.assertEqual('c', self.tree.root.left_child.right_child.key)
        self.assertEqual('d', self.tree.root.left_child.parent.key)

        self.assertEqual('f', self.tree.root.right_child.key)
        self.assertEqual('f-value', self.tree.root.right_child.value)
        self.assertEqual('e', self.tree.root.right_child.left_child.key)
        self.assertEqual('g', self.tree.root.right_child.right_child.key)
        self.assertEqual('d', self.tree.root.right_child.parent.key)

        self.assertEqual('a', self.tree.root.left_child.left_child.key)
        self.assertEqual('a-value', self.tree.root.left_child.left_child.value)
        self.assertEqual(None, self.tree.root.left_child.left_child.left_child)
        self.assertEqual(None, self.tree.root.left_child.left_child.right_child)
        self.assertEqual('b', self.tree.root.left_child.left_child.parent.key)

        self.assertEqual('c', self.tree.root.left_child.right_child.key)
        self.assertEqual('c-value', self.tree.root.left_child.right_child.value)
        self.assertEqual(None,
                         self.tree.root.left_child.right_child.left_child)
        self.assertEqual(None,
                         self.tree.root.left_child.right_child.right_child)
        self.assertEqual('b',
                         self.tree.root.left_child.right_child.parent.key)

        self.assertEqual('e', self.tree.root.right_child.left_child.key)
        self.assertEqual('e-value', self.tree.root.right_child.left_child.value)
        self.assertEqual(None,
                         self.tree.root.right_child.left_child.left_child)
        self.assertEqual(None,
                         self.tree.root.right_child.left_child.right_child)
        self.assertEqual('f', self.tree.root.right_child.left_child.parent.key)

        self.assertEqual('g', self.tree.root.right_child.right_child.key)
        self.assertEqual('g-value',
                         self.tree.root.right_child.right_child.value)
        self.assertEqual(None,
                         self.tree.root.right_child.right_child.left_child)
        self.assertEqual(None,
                         self.tree.root.right_child.right_child.right_child)
        self.assertEqual('f', self.tree.root.right_child.right_child.parent.key)

    def test_under_put_on_seven_node_tree_with_duplicate_key(self):
        self.create_seven_node_tree()

        duplicate_found = self.tree._put('a', 'new-a-value', self.tree.root)

        self.assertTrue(duplicate_found)
        self.assertEqual(7, self.tree.size)
        self.assert_properties(self.tree.root)

        self.assertEqual('d', self.tree.root.key)
        self.assertEqual('d-value', self.tree.root.value)
        self.assertEqual('b', self.tree.root.left_child.key)
        self.assertEqual('f', self.tree.root.right_child.key)
        self.assertEqual(None, self.tree.root.parent)

        self.assertEqual('b', self.tree.root.left_child.key)
        self.assertEqual('b-value', self.tree.root.left_child.value)
        self.assertEqual('a', self.tree.root.left_child.left_child.key)
        self.assertEqual('c', self.tree.root.left_child.right_child.key)
        self.assertEqual('d', self.tree.root.left_child.parent.key)

        self.assertEqual('f', self.tree.root.right_child.key)
        self.assertEqual('f-value', self.tree.root.right_child.value)
        self.assertEqual('e', self.tree.root.right_child.left_child.key)
        self.assertEqual('g', self.tree.root.right_child.right_child.key)
        self.assertEqual('d', self.tree.root.right_child.parent.key)

        self.assertEqual('a', self.tree.root.left_child.left_child.key)
        self.assertEqual('new-a-value',
                         self.tree.root.left_child.left_child.value)
        self.assertEqual(None,
                         self.tree.root.left_child.left_child.left_child)
        self.assertEqual(None,
                         self.tree.root.left_child.left_child.right_child)
        self.assertEqual('b', self.tree.root.left_child.left_child.parent.key)

        self.assertEqual('c', self.tree.root.left_child.right_child.key)
        self.assertEqual('c-value', self.tree.root.left_child.right_child.value)
        self.assertEqual(None,
                         self.tree.root.left_child.right_child.left_child)
        self.assertEqual(None,
                         self.tree.root.left_child.right_child.right_child)
        self.assertEqual('b', self.tree.root.left_child.right_child.parent.key)

        self.assertEqual('e', self.tree.root.right_child.left_child.key)
        self.assertEqual('e-value', self.tree.root.right_child.left_child.value)
        self.assertEqual(None,
                         self.tree.root.right_child.left_child.left_child)
        self.assertEqual(None,
                         self.tree.root.right_child.left_child.right_child)
        self.assertEqual('f', self.tree.root.right_child.left_child.parent.key)

        self.assertEqual('g', self.tree.root.right_child.right_child.key)
        self.assertEqual('g-value',
                         self.tree.root.right_child.right_child.value)
        self.assertEqual(None,
                         self.tree.root.right_child.right_child.left_child)
        self.assertEqual(None,
                         self.tree.root.right_child.right_child.right_child)
        self.assertEqual('f', self.tree.root.right_child.right_child.parent.key)

    def test_under_remove_left_child_as_leaf(self):
        self.create_one_node_tree_as_d()

        node = self.tree.root

        self.assertEqual('d', node.key)

        with self.assertRaisesRegex(
                              AttributeError,
                              "NoneType' object has no attribute 'left_child'"):

            self.tree._remove(node)

    def test_under_remove_left_child_as_leaf(self):
        self.create_seven_node_tree()

        node = self.tree.root.left_child.left_child

        self.assertEqual('a', node.key)

        self.tree._remove(node)

        self.assertEqual(7, self.tree.size)
        self.assert_properties(self.tree.root)

        self.assertEqual('d', self.tree.root.key)
        self.assertEqual('d-value', self.tree.root.value)
        self.assertEqual('b', self.tree.root.left_child.key)
        self.assertEqual('f', self.tree.root.right_child.key)
        self.assertEqual(None, self.tree.root.parent)

        self.assertEqual('b', self.tree.root.left_child.key)
        self.assertEqual('b-value', self.tree.root.left_child.value)
        self.assertEqual(None, self.tree.root.left_child.left_child)
        self.assertEqual('c', self.tree.root.left_child.right_child.key)
        self.assertEqual('d', self.tree.root.left_child.parent.key)

        self.assertEqual('f', self.tree.root.right_child.key)
        self.assertEqual('f-value', self.tree.root.right_child.value)
        self.assertEqual('e', self.tree.root.right_child.left_child.key)
        self.assertEqual('g', self.tree.root.right_child.right_child.key)
        self.assertEqual('d', self.tree.root.right_child.parent.key)

        self.assertEqual('c', self.tree.root.left_child.right_child.key)
        self.assertEqual('c-value', self.tree.root.left_child.right_child.value)
        self.assertEqual(None,
                         self.tree.root.left_child.right_child.left_child)
        self.assertEqual(None,
                         self.tree.root.left_child.right_child.right_child)
        self.assertEqual('b', self.tree.root.left_child.right_child.parent.key)

        self.assertEqual('e', self.tree.root.right_child.left_child.key)
        self.assertEqual('e-value', self.tree.root.right_child.left_child.value)
        self.assertEqual(None,
                         self.tree.root.right_child.left_child.left_child)
        self.assertEqual(None,
                         self.tree.root.right_child.left_child.right_child)
        self.assertEqual('f', self.tree.root.right_child.left_child.parent.key)

        self.assertEqual('g', self.tree.root.right_child.right_child.key)
        self.assertEqual('g-value',
                         self.tree.root.right_child.right_child.value)
        self.assertEqual(None,
                         self.tree.root.right_child.right_child.left_child)
        self.assertEqual(None,
                         self.tree.root.right_child.right_child.right_child)
        self.assertEqual('f', self.tree.root.right_child.right_child.parent.key)

    def test_under_remove_right_child_as_leaf(self):
        self.create_seven_node_tree()

        node = self.tree.root.left_child.right_child

        self.assertEqual('c', node.key)

        self.tree._remove(node)

        self.assertEqual(7, self.tree.size)
        self.assert_properties(self.tree.root)

        self.assertEqual('d', self.tree.root.key)
        self.assertEqual('d-value', self.tree.root.value)
        self.assertEqual('b', self.tree.root.left_child.key)
        self.assertEqual('f', self.tree.root.right_child.key)
        self.assertEqual(None, self.tree.root.parent)

        self.assertEqual('b', self.tree.root.left_child.key)
        self.assertEqual('b-value', self.tree.root.left_child.value)
        self.assertEqual('a', self.tree.root.left_child.left_child.key)
        self.assertEqual(None, self.tree.root.left_child.right_child)
        self.assertEqual('d', self.tree.root.left_child.parent.key)

        self.assertEqual('f', self.tree.root.right_child.key)
        self.assertEqual('f-value', self.tree.root.right_child.value)
        self.assertEqual('e', self.tree.root.right_child.left_child.key)
        self.assertEqual('g', self.tree.root.right_child.right_child.key)
        self.assertEqual('d', self.tree.root.right_child.parent.key)

        self.assertEqual('a', self.tree.root.left_child.left_child.key)
        self.assertEqual('a-value', self.tree.root.left_child.left_child.value)
        self.assertEqual(None,
                         self.tree.root.left_child.left_child.left_child)
        self.assertEqual(None,
                         self.tree.root.left_child.left_child.right_child)
        self.assertEqual('b', self.tree.root.left_child.left_child.parent.key)

        self.assertEqual('e', self.tree.root.right_child.left_child.key)
        self.assertEqual('e-value', self.tree.root.right_child.left_child.value)
        self.assertEqual(None,
                         self.tree.root.right_child.left_child.left_child)
        self.assertEqual(None,
                         self.tree.root.right_child.left_child.right_child)
        self.assertEqual('f', self.tree.root.right_child.left_child.parent.key)

        self.assertEqual('g', self.tree.root.right_child.right_child.key)
        self.assertEqual('g-value',
                         self.tree.root.right_child.right_child.value)
        self.assertEqual(None,
                         self.tree.root.right_child.right_child.left_child)
        self.assertEqual(None,
                         self.tree.root.right_child.right_child.right_child)
        self.assertEqual('f', self.tree.root.right_child.right_child.parent.key)

    def test_under_remove_two_leaf_nodes(self):
        node_d = self.node_type('d', 'd-value')
        node_b = self.node_type('b', 'b-value', parent=node_d)
        node_f = self.node_type('f', 'f-value', parent=node_d)
        node_d.left_child = node_b
        node_d.right_child = node_f
        node_a = self.node_type('a', 'a-value', parent=node_b)
        node_c = self.node_type('c', 'c-value', parent=node_b)
        node_b.left_child = node_a
        node_b.right_child = node_c
        node_e = self.node_type('e', 'e-value', parent=node_f)
        node_g = self.node_type('g', 'g-value', parent=node_f)
        node_f.left_child = node_e
        node_f.right_child = node_g
        self.tree.root = node_d
        self.tree._size = 7

        node_a.update_heights()
        node_b.update_heights()
        node_c.update_heights()
        node_d.update_heights()
        node_e.update_heights()
        node_f.update_heights()
        node_g.update_heights()

        node = self.tree.root.left_child.left_child

        self.assertEqual('a', node.key)

        self.tree._remove(node)

        node = self.tree.root.left_child.right_child

        self.assertEqual('c', node.key)

        self.tree._remove(node)

        self.assertEqual(7, self.tree.size)
        self.assert_properties(self.tree.root)

        self.assertEqual('d', self.tree.root.key)
        self.assertEqual('d-value', self.tree.root.value)
        self.assertEqual('b', self.tree.root.left_child.key)
        self.assertEqual('f', self.tree.root.right_child.key)
        self.assertEqual(None, self.tree.root.parent)

        self.assertEqual('b', self.tree.root.left_child.key)
        self.assertEqual('b-value', self.tree.root.left_child.value)
        self.assertEqual(None, self.tree.root.left_child.left_child)
        self.assertEqual(None, self.tree.root.left_child.right_child)
        self.assertEqual('d', self.tree.root.left_child.parent.key)

        self.assertEqual('f', self.tree.root.right_child.key)
        self.assertEqual('f-value', self.tree.root.right_child.value)
        self.assertEqual('e', self.tree.root.right_child.left_child.key)
        self.assertEqual('g', self.tree.root.right_child.right_child.key)
        self.assertEqual('d', self.tree.root.right_child.parent.key)

        self.assertEqual('e', self.tree.root.right_child.left_child.key)
        self.assertEqual('e-value', self.tree.root.right_child.left_child.value)
        self.assertEqual(None,
                         self.tree.root.right_child.left_child.left_child)
        self.assertEqual(None,
                         self.tree.root.right_child.left_child.right_child)
        self.assertEqual('f', self.tree.root.right_child.left_child.parent.key)

        self.assertEqual('g', self.tree.root.right_child.right_child.key)
        self.assertEqual('g-value',
                         self.tree.root.right_child.right_child.value)
        self.assertEqual(None,
                         self.tree.root.right_child.right_child.left_child)
        self.assertEqual(None,
                         self.tree.root.right_child.right_child.right_child)
        self.assertEqual('f',
                         self.tree.root.right_child.right_child.parent.key)

    def test_under_remove_both_children_node_and_immediate_leaf_successor(self):
        node_d = self.node_type('d', 'd-value')
        node_b = self.node_type('b', 'b-value', parent=node_d)
        node_d.left_child = node_b
        node_a = self.node_type('a', 'a-value', parent=node_b)
        node_c = self.node_type('c', 'c-value', parent=node_b)
        node_b.left_child = node_a
        node_b.right_child = node_c
        self.tree.root = node_d
        self.tree._size = 4

        node_a.update_heights()
        node_b.update_heights()
        node_c.update_heights()
        node_d.update_heights()

        node = self.tree.root.left_child

        self.assertEqual('b', node.key)

        self.tree._remove(node)

        self.assertEqual(4, self.tree.size)
        self.assert_properties(self.tree.root)

        self.assertEqual('d', self.tree.root.key)
        self.assertEqual('d-value', self.tree.root.value)
        self.assertEqual('c', self.tree.root.left_child.key)
        self.assertEqual(None, self.tree.root.right_child)
        self.assertEqual(None, self.tree.root.parent)

        self.assertEqual('c', self.tree.root.left_child.key)
        self.assertEqual('c-value', self.tree.root.left_child.value)
        self.assertEqual('a', self.tree.root.left_child.left_child.key)
        self.assertEqual(None, self.tree.root.left_child.right_child)
        self.assertEqual('d',  self.tree.root.left_child.parent.key)

        self.assertEqual('a', self.tree.root.left_child.left_child.key)
        self.assertEqual('a-value', self.tree.root.left_child.left_child.value)
        self.assertEqual(None,
                         self.tree.root.left_child.left_child.left_child)
        self.assertEqual(None,
                         self.tree.root.left_child.left_child.right_child)
        self.assertEqual('c',  self.tree.root.left_child.left_child.parent.key)

    def test_under_remove_both_children_node_and_leaf_successor(self):
        node_d = self.node_type('d', 'd-value')
        node_b = self.node_type('b', 'b-value', parent=node_d)
        node_f = self.node_type('f', 'f-value', parent=node_d)
        node_d.left_child = node_b
        node_d.right_child = node_f
        node_e = self.node_type('e', 'e-value', parent=node_f)
        node_f.left_child = node_e
        self.tree.root = node_d
        self.tree._size = 4

        node_b.update_heights()
        node_d.update_heights()
        node_e.update_heights()
        node_f.update_heights()

        node = self.tree.root

        self.assertEqual('d', node.key)

        self.tree._remove(node)

        self.assertEqual(4, self.tree.size)
        self.assert_properties(self.tree.root)

        self.assertEqual('e', self.tree.root.key)
        self.assertEqual('e-value', self.tree.root.value)
        self.assertEqual('b', self.tree.root.left_child.key)
        self.assertEqual('f', self.tree.root.right_child.key)
        self.assertEqual(None, self.tree.root.parent)

        self.assertEqual('b', self.tree.root.left_child.key)
        self.assertEqual('b-value', self.tree.root.left_child.value)
        self.assertEqual(None, self.tree.root.left_child.left_child)
        self.assertEqual(None, self.tree.root.left_child.right_child)
        self.assertEqual('e',  self.tree.root.left_child.parent.key)

        self.assertEqual('f', self.tree.root.right_child.key)
        self.assertEqual('f-value', self.tree.root.right_child.value)
        self.assertEqual(None, self.tree.root.right_child.left_child)
        self.assertEqual(None, self.tree.root.right_child.right_child)
        self.assertEqual('e', self.tree.root.right_child.parent.key)

    def test_under_remove_both_children_node_and_one_child_successor(self):
        node_e = self.node_type('e', 'e-value')
        node_b = self.node_type('b', 'b-value', parent=node_e)
        node_f = self.node_type('f', 'f-value', parent=node_e)
        node_e.left_child = node_b
        node_e.right_child = node_f
        node_g = self.node_type('g', 'g-value', parent=node_f)
        node_f.right_child = node_g
        self.tree.root = node_e
        self.tree._size = 4

        node_b.update_heights()
        node_g.update_heights()
        node_f.update_heights()
        node_e.update_heights()

        node = self.tree.root

        self.assertEqual('e', node.key)

        self.tree._remove(node)

        self.assertEqual(4, self.tree.size)
        self.assert_properties(self.tree.root)

        self.assertEqual('f', self.tree.root.key)
        self.assertEqual('f-value', self.tree.root.value)
        self.assertEqual('b', self.tree.root.left_child.key)
        self.assertEqual('g', self.tree.root.right_child.key)
        self.assertEqual(None, self.tree.root.parent)

        self.assertEqual('b', self.tree.root.left_child.key)
        self.assertEqual('b-value', self.tree.root.left_child.value)
        self.assertEqual(None, self.tree.root.left_child.left_child)
        self.assertEqual(None, self.tree.root.left_child.right_child)
        self.assertEqual('f', self.tree.root.left_child.parent.key)

        self.assertEqual('g', self.tree.root.right_child.key)
        self.assertEqual('g-value', self.tree.root.right_child.value)
        self.assertEqual(None, self.tree.root.right_child.left_child)
        self.assertEqual(None, self.tree.root.right_child.right_child)
        self.assertEqual('f', self.tree.root.right_child.parent.key)

    def test_under_remove_one_left_child_node_of_left_parent(self):
        node_d = self.node_type('d', 'd-value')
        node_b = self.node_type('b', 'b-value', parent=node_d)
        node_d.left_child = node_b
        node_a = self.node_type('a', 'a-value', parent=node_b)
        node_b.left_child = node_a
        self.tree.root = node_d
        self.tree._size = 3

        node_a.update_heights()
        node_b.update_heights()
        node_d.update_heights()

        node = self.tree.root.left_child

        self.assertEqual('b', node.key)

        self.tree._remove(node)

        self.assertEqual(3, self.tree.size)
        self.assert_properties(self.tree.root)

        self.assertEqual('d', self.tree.root.key)
        self.assertEqual('d-value', self.tree.root.value)
        self.assertEqual('a', self.tree.root.left_child.key)
        self.assertEqual(None, self.tree.root.right_child)
        self.assertEqual(None, self.tree.root.parent)

        self.assertEqual('a', self.tree.root.left_child.key)
        self.assertEqual('a-value', self.tree.root.left_child.value)
        self.assertEqual(None, self.tree.root.left_child.left_child)
        self.assertEqual(None, self.tree.root.left_child.right_child)
        self.assertEqual('d', self.tree.root.left_child.parent.key)

    def test_under_remove_one_left_child_node_of_right_parent(self):
        node_d = self.node_type('d', 'd-value')
        node_f = self.node_type('f', 'f-value', parent=node_d)
        node_d.right_child = node_f
        node_e = self.node_type('e', 'e-value', parent=node_f)
        node_f.left_child = node_e
        self.tree.root = node_d
        self.tree._size = 3

        node_e.update_heights()
        node_f.update_heights()
        node_d.update_heights()

        node = self.tree.root.right_child

        self.assertEqual('f', node.key)

        self.tree._remove(node)

        self.assertEqual(3, self.tree.size)
        self.assert_properties(self.tree.root)

        self.assertEqual('d', self.tree.root.key)
        self.assertEqual('d-value', self.tree.root.value)
        self.assertEqual(None, self.tree.root.left_child)
        self.assertEqual('e', self.tree.root.right_child.key)
        self.assertEqual(None, self.tree.root.parent)

        self.assertEqual('e', self.tree.root.right_child.key)
        self.assertEqual('e-value', self.tree.root.right_child.value)
        self.assertEqual(None, self.tree.root.right_child.left_child)
        self.assertEqual(None, self.tree.root.right_child.right_child)
        self.assertEqual('d', self.tree.root.right_child.parent.key)

    def test_under_remove_one_left_child_node_of_parent(self):
        node_d = self.node_type('d', 'd-value')
        node_b = self.node_type('b', 'b-value', parent=node_d)
        node_d.left_child = node_b
        self.tree.root = node_d
        self.tree._size = 2

        node_b.update_heights()
        node_d.update_heights()

        node = self.tree.root

        self.assertEqual('d', node.key)

        self.tree._remove(node)

        self.assertEqual(2, self.tree.size)
        self.assert_properties(self.tree.root)

        self.assertEqual('b', self.tree.root.key)
        self.assertEqual('b-value', self.tree.root.value)
        self.assertEqual(None, self.tree.root.left_child)
        self.assertEqual(None, self.tree.root.right_child)
        self.assertEqual(None, self.tree.root.parent)

    def test_under_remove_one_right_child_node_of_left_parent(self):
        node_d = self.node_type('d', 'd-value')
        node_b = self.node_type('b', 'b-value', parent=node_d)
        node_d.left_child = node_b
        node_c = self.node_type('c', 'c-value', parent=node_b)
        node_b.right_child = node_c
        self.tree.root = node_d
        self.tree._size = 3

        node_c.update_heights()
        node_b.update_heights()
        node_d.update_heights()

        node = self.tree.root.left_child

        self.assertEqual('b', node.key)

        self.tree._remove(node)

        self.assertEqual(3, self.tree.size)
        self.assert_properties(self.tree.root)

        self.assertEqual('d', self.tree.root.key)
        self.assertEqual('d-value', self.tree.root.value)
        self.assertEqual('c', self.tree.root.left_child.key)
        self.assertEqual(None, self.tree.root.right_child)
        self.assertEqual(None, self.tree.root.parent)

        self.assertEqual('c', self.tree.root.left_child.key)
        self.assertEqual('c-value', self.tree.root.left_child.value)
        self.assertEqual(None, self.tree.root.left_child.left_child)
        self.assertEqual(None, self.tree.root.left_child.right_child)
        self.assertEqual('d', self.tree.root.left_child.parent.key)

    def test_under_remove_one_right_child_node_of_right_parent(self):
        node_d = self.node_type('d', 'd-value')
        node_f = self.node_type('f', 'f-value', parent=node_d)
        node_d.right_child = node_f
        node_g = self.node_type('g', 'g-value', parent=node_f)
        node_f.right_child = node_g
        self.tree.root = node_d
        self.tree._size = 3

        node_g.update_heights()
        node_f.update_heights()
        node_d.update_heights()

        node = self.tree.root.right_child

        self.assertEqual('f', node.key)

        self.tree._remove(node)

        self.assertEqual(3, self.tree.size)
        self.assert_properties(self.tree.root)

        self.assertEqual('d', self.tree.root.key)
        self.assertEqual('d-value', self.tree.root.value)
        self.assertEqual(None, self.tree.root.left_child)
        self.assertEqual('g', self.tree.root.right_child.key)
        self.assertEqual(None, self.tree.root.parent)

        self.assertEqual('g', self.tree.root.right_child.key)
        self.assertEqual('g-value', self.tree.root.right_child.value)
        self.assertEqual(None, self.tree.root.right_child.left_child)
        self.assertEqual(None, self.tree.root.right_child.right_child)
        self.assertEqual('d', self.tree.root.right_child.parent.key)

    def test_under_remove_one_right_child_node_of_parent(self):
        node_d = self.node_type('d', 'd-value')
        node_f = self.node_type('f', 'f-value', parent=node_d)
        node_d.right_child = node_f
        self.tree.root = node_d
        self.tree._size = 2

        node_f.update_heights()
        node_d.update_heights()

        node = self.tree.root

        self.assertEqual('d', node.key)

        self.tree._remove(node)

        self.assertEqual(2, self.tree.size)
        self.assert_properties(self.tree.root)

        self.assertEqual('f', self.tree.root.key)
        self.assertEqual('f-value', self.tree.root.value)
        self.assertEqual(None, self.tree.root.left_child)
        self.assertEqual(None, self.tree.root.right_child)
        self.assertEqual(None, self.tree.root.parent)

    def test_under_remove_on_seven_node_tree(self):
        self.create_seven_node_tree()

        node = self.tree.root.left_child.left_child

        self.assertEqual('a', node.key)

        self.tree._remove(node)

        self.assertEqual(7, self.tree.size)
        self.assert_properties(self.tree.root)

        self.assertEqual('d', self.tree.root.key)
        self.assertEqual('d-value', self.tree.root.value)
        self.assertEqual('b', self.tree.root.left_child.key)
        self.assertEqual('f', self.tree.root.right_child.key)
        self.assertEqual(None, self.tree.root.parent)

        self.assertEqual('b', self.tree.root.left_child.key)
        self.assertEqual('b-value', self.tree.root.left_child.value)
        self.assertEqual(None, self.tree.root.left_child.left_child)
        self.assertEqual('c', self.tree.root.left_child.right_child.key)

        self.assertEqual('f', self.tree.root.right_child.key)
        self.assertEqual('f-value', self.tree.root.right_child.value)
        self.assertEqual('e', self.tree.root.right_child.left_child.key)
        self.assertEqual('g', self.tree.root.right_child.right_child.key)

        self.assertEqual('c', self.tree.root.left_child.right_child.key)
        self.assertEqual('c-value', self.tree.root.left_child.right_child.value)
        self.assertEqual(None,
                         self.tree.root.left_child.right_child.left_child)
        self.assertEqual(None,
                         self.tree.root.left_child.right_child.right_child)

        self.assertEqual('e', self.tree.root.right_child.left_child.key)
        self.assertEqual('e-value', self.tree.root.right_child.left_child.value)
        self.assertEqual(None,
                         self.tree.root.right_child.left_child.left_child)
        self.assertEqual(None,
                         self.tree.root.right_child.left_child.right_child)

        self.assertEqual('g', self.tree.root.right_child.right_child.key)
        self.assertEqual('g-value',
                         self.tree.root.right_child.right_child.value)
        self.assertEqual(None,
                         self.tree.root.right_child.right_child.left_child)
        self.assertEqual(None,
                         self.tree.root.right_child.right_child.right_child)

        node = self.tree.root.left_child.right_child

        self.assertEqual('c', node.key)

        self.tree._remove(node)

        self.assertEqual(7, self.tree.size)
        self.assert_properties(self.tree.root)

        self.assertEqual('d', self.tree.root.key)
        self.assertEqual('d-value', self.tree.root.value)
        self.assertEqual('b', self.tree.root.left_child.key)
        self.assertEqual('f', self.tree.root.right_child.key)
        self.assertEqual(None, self.tree.root.parent)

        self.assertEqual('b', self.tree.root.left_child.key)
        self.assertEqual('b-value', self.tree.root.left_child.value)
        self.assertEqual(None, self.tree.root.left_child.left_child)
        self.assertEqual(None, self.tree.root.left_child.right_child)

        self.assertEqual('f', self.tree.root.right_child.key)
        self.assertEqual('f-value', self.tree.root.right_child.value)
        self.assertEqual('e', self.tree.root.right_child.left_child.key)
        self.assertEqual('g', self.tree.root.right_child.right_child.key)

        self.assertEqual('e', self.tree.root.right_child.left_child.key)
        self.assertEqual('e-value', self.tree.root.right_child.left_child.value)
        self.assertEqual(None,
                         self.tree.root.right_child.left_child.left_child)
        self.assertEqual(None,
                         self.tree.root.right_child.left_child.right_child)

        self.assertEqual('g', self.tree.root.right_child.right_child.key)
        self.assertEqual('g-value', self.tree.root.right_child.right_child.value)
        self.assertEqual(None,
                         self.tree.root.right_child.right_child.left_child)
        self.assertEqual(None,
                         self.tree.root.right_child.right_child.right_child)

        node = self.tree.root.right_child.left_child

        self.assertEqual('e', node.key)

        self.tree._remove(node)

        self.assertEqual(7, self.tree.size)
        self.assert_properties(self.tree.root)

        self.assertEqual('d', self.tree.root.key)
        self.assertEqual('d-value', self.tree.root.value)
        self.assertEqual('b', self.tree.root.left_child.key)
        self.assertEqual('f', self.tree.root.right_child.key)
        self.assertEqual(None, self.tree.root.parent)

        self.assertEqual('b', self.tree.root.left_child.key)
        self.assertEqual('b-value', self.tree.root.left_child.value)
        self.assertEqual(None, self.tree.root.left_child.left_child)
        self.assertEqual(None, self.tree.root.left_child.right_child)

        self.assertEqual('f', self.tree.root.right_child.key)
        self.assertEqual('f-value', self.tree.root.right_child.value)
        self.assertEqual(None, self.tree.root.right_child.left_child)
        self.assertEqual('g', self.tree.root.right_child.right_child.key)

        self.assertEqual('g', self.tree.root.right_child.right_child.key)
        self.assertEqual('g-value', self.tree.root.right_child.right_child.value)
        self.assertEqual(None,
                         self.tree.root.right_child.right_child.left_child)
        self.assertEqual(None,
                         self.tree.root.right_child.right_child.right_child)

        node = self.tree.root.right_child.right_child

        self.assertEqual('g', node.key)

        self.tree._remove(node)

        self.assertEqual(7, self.tree.size)
        self.assert_properties(self.tree.root)

        self.assertEqual('d', self.tree.root.key)
        self.assertEqual('d-value', self.tree.root.value)
        self.assertEqual('b', self.tree.root.left_child.key)
        self.assertEqual('f', self.tree.root.right_child.key)
        self.assertEqual(None, self.tree.root.parent)

        self.assertEqual('b', self.tree.root.left_child.key)
        self.assertEqual('b-value', self.tree.root.left_child.value)
        self.assertEqual(None, self.tree.root.left_child.left_child)
        self.assertEqual(None, self.tree.root.left_child.right_child)

        self.assertEqual('f', self.tree.root.right_child.key)
        self.assertEqual('f-value', self.tree.root.right_child.value)
        self.assertEqual(None, self.tree.root.right_child.left_child)
        self.assertEqual(None, self.tree.root.right_child.right_child)

        node = self.tree.root.left_child

        self.assertEqual('b', node.key)

        self.tree._remove(node)

        self.assertEqual(7, self.tree.size)
        self.assert_properties(self.tree.root)

        self.assertEqual('d', self.tree.root.key)
        self.assertEqual('d-value', self.tree.root.value)
        self.assertEqual(None, self.tree.root.left_child)
        self.assertEqual('f', self.tree.root.right_child.key)
        self.assertEqual(None, self.tree.root.parent)

        self.assertEqual('f', self.tree.root.right_child.key)
        self.assertEqual('f-value', self.tree.root.right_child.value)
        self.assertEqual(None, self.tree.root.right_child.left_child)
        self.assertEqual(None, self.tree.root.right_child.right_child)

        node = self.tree.root.right_child

        self.assertEqual('f', node.key)

        self.tree._remove(node)

        self.assertEqual(7, self.tree.size)
        self.assert_properties(self.tree.root)

        self.assertEqual('d', self.tree.root.key)
        self.assertEqual('d-value', self.tree.root.value)
        self.assertEqual(None, self.tree.root.left_child)
        self.assertEqual(None, self.tree.root.right_child)
        self.assertEqual(None, self.tree.root.parent)

        node = self.tree.root

        self.assertEqual('d', node.key)

        with self.assertRaisesRegex(
                              AttributeError,
                              "NoneType' object has no attribute 'left_child'"):

            self.tree._remove(node)

    def test_size_of_empty_tree(self):
        self.assertEqual(0, self.tree.size)

    def test_size_of_seven_node_tree(self):
        self.create_seven_node_tree()

        self.assertEqual(7, self.tree.size)

    def test_get_on_empty_tree(self):
        self.assertEqual(None, self.tree.get('a'))

        self.assertEqual(0, self.tree.size)
        self.assert_properties(self.tree.root)

    def test_get_on_seven_node_tree(self):
        self.create_seven_node_tree()

        self.assertEqual('a-value', self.tree.get('a'))
        self.assertEqual('b-value', self.tree.get('b'))
        self.assertEqual('c-value', self.tree.get('c'))
        self.assertEqual('d-value', self.tree.get('d'))
        self.assertEqual('e-value', self.tree.get('e'))
        self.assertEqual('f-value', self.tree.get('f'))
        self.assertEqual('g-value', self.tree.get('g'))
        self.assertEqual(None, self.tree.get('z'))

        self.assertEqual(7, self.tree.size)
        self.assert_properties(self.tree.root)

    def test_put_on_empty_tree(self):
        self.assertEqual(None, self.tree.get('a'))
        self.assertEqual(0, self.tree.size)

        self.tree.put('a', 'a-value')

        self.assertEqual(1, self.tree.size)
        self.assert_properties(self.tree.root)

    def test_put_on_one_node_tree_with_a(self):
        self.create_one_node_tree_as_d()

        self.tree.put('a', 'a-value')

        self.assertEqual(2, self.tree.size)
        self.assert_properties(self.tree.root)

        self.assertEqual('d', self.tree.root.key)
        self.assertEqual('d-value', self.tree.root.value)
        self.assertEqual('a', self.tree.root.left_child.key)
        self.assertEqual(None, self.tree.root.right_child)
        self.assertEqual(None, self.tree.root.parent)

        self.assertEqual('a', self.tree.root.left_child.key)
        self.assertEqual('a-value', self.tree.root.left_child.value)
        self.assertEqual(None, self.tree.root.left_child.left_child)
        self.assertEqual(None, self.tree.root.left_child.right_child)
        self.assertEqual('d', self.tree.root.left_child.parent.key)

    def test_put_on_one_node_tree_with_g(self):
        self.create_one_node_tree_as_d()

        self.tree.put('g', 'g-value')

        self.assertEqual(2, self.tree.size)
        self.assert_properties(self.tree.root)

        self.assertEqual('d', self.tree.root.key)
        self.assertEqual('d-value', self.tree.root.value)
        self.assertEqual(None, self.tree.root.left_child)
        self.assertEqual('g', self.tree.root.right_child.key)
        self.assertEqual(None, self.tree.root.parent)

        self.assertEqual('g', self.tree.root.right_child.key)
        self.assertEqual('g-value', self.tree.root.right_child.value)
        self.assertEqual(None, self.tree.root.right_child.left_child)
        self.assertEqual(None, self.tree.root.right_child.right_child)
        self.assertEqual('d', self.tree.root.right_child.parent.key)

    def test_put_on_one_node_tree_with_b_f_a_c_e_g(self):
        self.create_one_node_tree_as_d()

        self.tree.put('b', 'b-value')

        self.assertEqual(2, self.tree.size)
        self.assert_properties(self.tree.root)

        self.assertEqual('d', self.tree.root.key)
        self.assertEqual('d-value', self.tree.root.value)
        self.assertEqual('b', self.tree.root.left_child.key)
        self.assertEqual(None, self.tree.root.right_child)
        self.assertEqual(None, self.tree.root.parent)

        self.assertEqual('b', self.tree.root.left_child.key)
        self.assertEqual('b-value', self.tree.root.left_child.value)
        self.assertEqual(None, self.tree.root.left_child.left_child)
        self.assertEqual(None, self.tree.root.left_child.right_child)
        self.assertEqual('d', self.tree.root.left_child.parent.key)

        self.tree.put('f', 'f-value')

        self.assertEqual(3, self.tree.size)
        self.assert_properties(self.tree.root)

        self.assertEqual('d', self.tree.root.key)
        self.assertEqual('d-value', self.tree.root.value)
        self.assertEqual('b', self.tree.root.left_child.key)
        self.assertEqual('f', self.tree.root.right_child.key)
        self.assertEqual(None, self.tree.root.parent)

        self.assertEqual('b', self.tree.root.left_child.key)
        self.assertEqual('b-value', self.tree.root.left_child.value)
        self.assertEqual(None, self.tree.root.left_child.left_child)
        self.assertEqual(None, self.tree.root.left_child.right_child)
        self.assertEqual('d', self.tree.root.left_child.parent.key)

        self.assertEqual('f', self.tree.root.right_child.key)
        self.assertEqual('f-value', self.tree.root.right_child.value)
        self.assertEqual(None, self.tree.root.right_child.left_child)
        self.assertEqual(None, self.tree.root.right_child.right_child)
        self.assertEqual('d', self.tree.root.right_child.parent.key)

        self.tree.put('a', 'a-value')

        self.assertEqual(4, self.tree.size)
        self.assert_properties(self.tree.root)

        self.assertEqual('d', self.tree.root.key)
        self.assertEqual('d-value', self.tree.root.value)
        self.assertEqual('b', self.tree.root.left_child.key)
        self.assertEqual('f', self.tree.root.right_child.key)
        self.assertEqual(None, self.tree.root.parent)

        self.assertEqual('b', self.tree.root.left_child.key)
        self.assertEqual('b-value', self.tree.root.left_child.value)
        self.assertEqual('a', self.tree.root.left_child.left_child.key)
        self.assertEqual(None, self.tree.root.left_child.right_child)
        self.assertEqual('d', self.tree.root.left_child.parent.key)

        self.assertEqual('f', self.tree.root.right_child.key)
        self.assertEqual('f-value', self.tree.root.right_child.value)
        self.assertEqual(None, self.tree.root.right_child.left_child)
        self.assertEqual(None, self.tree.root.right_child.right_child)
        self.assertEqual('d', self.tree.root.right_child.parent.key)

        self.assertEqual('a', self.tree.root.left_child.left_child.key)
        self.assertEqual('a-value', self.tree.root.left_child.left_child.value)
        self.assertEqual(None, self.tree.root.left_child.left_child.left_child)
        self.assertEqual(None, self.tree.root.left_child.left_child.right_child)
        self.assertEqual('b', self.tree.root.left_child.left_child.parent.key)

        self.tree.put('c', 'c-value')

        self.assertEqual(5, self.tree.size)
        self.assert_properties(self.tree.root)

        self.assertEqual('d', self.tree.root.key)
        self.assertEqual('d-value', self.tree.root.value)
        self.assertEqual('b', self.tree.root.left_child.key)
        self.assertEqual('f', self.tree.root.right_child.key)
        self.assertEqual(None, self.tree.root.parent)

        self.assertEqual('b', self.tree.root.left_child.key)
        self.assertEqual('b-value', self.tree.root.left_child.value)
        self.assertEqual('a', self.tree.root.left_child.left_child.key)
        self.assertEqual('c', self.tree.root.left_child.right_child.key)
        self.assertEqual('d', self.tree.root.left_child.parent.key)

        self.assertEqual('f', self.tree.root.right_child.key)
        self.assertEqual('f-value', self.tree.root.right_child.value)
        self.assertEqual(None, self.tree.root.right_child.left_child)
        self.assertEqual(None, self.tree.root.right_child.right_child)
        self.assertEqual('d', self.tree.root.right_child.parent.key)

        self.assertEqual('a', self.tree.root.left_child.left_child.key)
        self.assertEqual('a-value', self.tree.root.left_child.left_child.value)
        self.assertEqual(None, self.tree.root.left_child.left_child.left_child)
        self.assertEqual(None, self.tree.root.left_child.left_child.right_child)
        self.assertEqual('b', self.tree.root.left_child.left_child.parent.key)

        self.assertEqual('c', self.tree.root.left_child.right_child.key)
        self.assertEqual('c-value', self.tree.root.left_child.right_child.value)
        self.assertEqual(None,
                         self.tree.root.left_child.right_child.left_child)
        self.assertEqual(None,
                         self.tree.root.left_child.right_child.right_child)
        self.assertEqual('b',
                         self.tree.root.left_child.right_child.parent.key)

        self.tree.put('e', 'e-value')

        self.assertEqual(6, self.tree.size)
        self.assert_properties(self.tree.root)

        self.assertEqual('d', self.tree.root.key)
        self.assertEqual('d-value', self.tree.root.value)
        self.assertEqual('b', self.tree.root.left_child.key)
        self.assertEqual('f', self.tree.root.right_child.key)
        self.assertEqual(None, self.tree.root.parent)

        self.assertEqual('b', self.tree.root.left_child.key)
        self.assertEqual('b-value', self.tree.root.left_child.value)
        self.assertEqual('a', self.tree.root.left_child.left_child.key)
        self.assertEqual('c', self.tree.root.left_child.right_child.key)
        self.assertEqual('d', self.tree.root.left_child.parent.key)

        self.assertEqual('f', self.tree.root.right_child.key)
        self.assertEqual('f-value', self.tree.root.right_child.value)
        self.assertEqual('e', self.tree.root.right_child.left_child.key)
        self.assertEqual(None, self.tree.root.right_child.right_child)
        self.assertEqual('d', self.tree.root.right_child.parent.key)

        self.assertEqual('a', self.tree.root.left_child.left_child.key)
        self.assertEqual('a-value', self.tree.root.left_child.left_child.value)
        self.assertEqual(None, self.tree.root.left_child.left_child.left_child)
        self.assertEqual(None, self.tree.root.left_child.left_child.right_child)
        self.assertEqual('b', self.tree.root.left_child.left_child.parent.key)

        self.assertEqual('c', self.tree.root.left_child.right_child.key)
        self.assertEqual('c-value', self.tree.root.left_child.right_child.value)
        self.assertEqual(None,
                         self.tree.root.left_child.right_child.left_child)
        self.assertEqual(None,
                         self.tree.root.left_child.right_child.right_child)
        self.assertEqual('b',
                         self.tree.root.left_child.right_child.parent.key)

        self.assertEqual('e', self.tree.root.right_child.left_child.key)
        self.assertEqual('e-value', self.tree.root.right_child.left_child.value)
        self.assertEqual(None,
                         self.tree.root.right_child.left_child.left_child)
        self.assertEqual(None,
                         self.tree.root.right_child.left_child.right_child)
        self.assertEqual('f', self.tree.root.right_child.left_child.parent.key)

        self.tree.put('g', 'g-value')

        self.assertEqual(7, self.tree.size)
        self.assert_properties(self.tree.root)

        self.assertEqual('d', self.tree.root.key)
        self.assertEqual('d-value', self.tree.root.value)
        self.assertEqual('b', self.tree.root.left_child.key)
        self.assertEqual('f', self.tree.root.right_child.key)
        self.assertEqual(None, self.tree.root.parent)

        self.assertEqual('b', self.tree.root.left_child.key)
        self.assertEqual('b-value', self.tree.root.left_child.value)
        self.assertEqual('a', self.tree.root.left_child.left_child.key)
        self.assertEqual('c', self.tree.root.left_child.right_child.key)
        self.assertEqual('d', self.tree.root.left_child.parent.key)

        self.assertEqual('f', self.tree.root.right_child.key)
        self.assertEqual('f-value', self.tree.root.right_child.value)
        self.assertEqual('e', self.tree.root.right_child.left_child.key)
        self.assertEqual('g', self.tree.root.right_child.right_child.key)
        self.assertEqual('d', self.tree.root.right_child.parent.key)

        self.assertEqual('a', self.tree.root.left_child.left_child.key)
        self.assertEqual('a-value', self.tree.root.left_child.left_child.value)
        self.assertEqual(None, self.tree.root.left_child.left_child.left_child)
        self.assertEqual(None, self.tree.root.left_child.left_child.right_child)
        self.assertEqual('b', self.tree.root.left_child.left_child.parent.key)

        self.assertEqual('c', self.tree.root.left_child.right_child.key)
        self.assertEqual('c-value', self.tree.root.left_child.right_child.value)
        self.assertEqual(None,
                         self.tree.root.left_child.right_child.left_child)
        self.assertEqual(None,
                         self.tree.root.left_child.right_child.right_child)
        self.assertEqual('b',
                         self.tree.root.left_child.right_child.parent.key)

        self.assertEqual('e', self.tree.root.right_child.left_child.key)
        self.assertEqual('e-value', self.tree.root.right_child.left_child.value)
        self.assertEqual(None,
                         self.tree.root.right_child.left_child.left_child)
        self.assertEqual(None,
                         self.tree.root.right_child.left_child.right_child)
        self.assertEqual('f', self.tree.root.right_child.left_child.parent.key)

        self.assertEqual('g', self.tree.root.right_child.right_child.key)
        self.assertEqual('g-value',
                         self.tree.root.right_child.right_child.value)
        self.assertEqual(None,
                         self.tree.root.right_child.right_child.left_child)
        self.assertEqual(None,
                         self.tree.root.right_child.right_child.right_child)
        self.assertEqual('f', self.tree.root.right_child.right_child.parent.key)

    def test_put_on_seven_node_tree_with_duplicate_key(self):
        self.create_seven_node_tree()

        self.tree.put('a', 'new-a-value')

        self.assertEqual(7, self.tree.size)
        self.assert_properties(self.tree.root)

        self.assertEqual('d', self.tree.root.key)
        self.assertEqual('d-value', self.tree.root.value)
        self.assertEqual('b', self.tree.root.left_child.key)
        self.assertEqual('f', self.tree.root.right_child.key)
        self.assertEqual(None, self.tree.root.parent)

        self.assertEqual('b', self.tree.root.left_child.key)
        self.assertEqual('b-value', self.tree.root.left_child.value)
        self.assertEqual('a', self.tree.root.left_child.left_child.key)
        self.assertEqual('c', self.tree.root.left_child.right_child.key)
        self.assertEqual('d', self.tree.root.left_child.parent.key)

        self.assertEqual('f', self.tree.root.right_child.key)
        self.assertEqual('f-value', self.tree.root.right_child.value)
        self.assertEqual('e', self.tree.root.right_child.left_child.key)
        self.assertEqual('g', self.tree.root.right_child.right_child.key)
        self.assertEqual('d', self.tree.root.right_child.parent.key)

        self.assertEqual('a', self.tree.root.left_child.left_child.key)
        self.assertEqual('new-a-value',
                         self.tree.root.left_child.left_child.value)
        self.assertEqual(None,
                         self.tree.root.left_child.left_child.left_child)
        self.assertEqual(None,
                         self.tree.root.left_child.left_child.right_child)
        self.assertEqual('b', self.tree.root.left_child.left_child.parent.key)

        self.assertEqual('c', self.tree.root.left_child.right_child.key)
        self.assertEqual('c-value', self.tree.root.left_child.right_child.value)
        self.assertEqual(None,
                         self.tree.root.left_child.right_child.left_child)
        self.assertEqual(None,
                         self.tree.root.left_child.right_child.right_child)
        self.assertEqual('b', self.tree.root.left_child.right_child.parent.key)

        self.assertEqual('e', self.tree.root.right_child.left_child.key)
        self.assertEqual('e-value', self.tree.root.right_child.left_child.value)
        self.assertEqual(None,
                         self.tree.root.right_child.left_child.left_child)
        self.assertEqual(None,
                         self.tree.root.right_child.left_child.right_child)
        self.assertEqual('f', self.tree.root.right_child.left_child.parent.key)

        self.assertEqual('g', self.tree.root.right_child.right_child.key)
        self.assertEqual('g-value',
                         self.tree.root.right_child.right_child.value)
        self.assertEqual(None,
                         self.tree.root.right_child.right_child.left_child)
        self.assertEqual(None,
                         self.tree.root.right_child.right_child.right_child)
        self.assertEqual('f', self.tree.root.right_child.right_child.parent.key)

    def test_delete_with_missing_key_on_empty_tree(self):
        with self.assertRaisesRegex(KeyError,
                                    'The key not in the tree.'):
            self.tree.delete('a')

    def test_delete_with_missing_key_on_nonempty_tree(self):
        self.create_seven_node_tree()

        with self.assertRaisesRegex(KeyError,
                                    'The key not in the tree.'):
            self.tree.delete('z')

    def test_delete_on_one_node_tree(self):
        self.create_one_node_tree_as_d()

        self.tree.delete(self.tree.root.key)

        self.assertEqual(0, self.tree.size)
        self.assert_properties(self.tree.root)

    def test_delete_left_child_as_leaf(self):
        self.create_seven_node_tree()

        self.tree.delete('a')

        self.assertEqual(6, self.tree.size)
        self.assert_properties(self.tree.root)

        self.assertEqual('d', self.tree.root.key)
        self.assertEqual('d-value', self.tree.root.value)
        self.assertEqual('b', self.tree.root.left_child.key)
        self.assertEqual('f', self.tree.root.right_child.key)
        self.assertEqual(None, self.tree.root.parent)

        self.assertEqual('b', self.tree.root.left_child.key)
        self.assertEqual('b-value', self.tree.root.left_child.value)
        self.assertEqual(None, self.tree.root.left_child.left_child)
        self.assertEqual('c', self.tree.root.left_child.right_child.key)
        self.assertEqual('d', self.tree.root.left_child.parent.key)

        self.assertEqual('f', self.tree.root.right_child.key)
        self.assertEqual('f-value', self.tree.root.right_child.value)
        self.assertEqual('e', self.tree.root.right_child.left_child.key)
        self.assertEqual('g', self.tree.root.right_child.right_child.key)
        self.assertEqual('d', self.tree.root.right_child.parent.key)

        self.assertEqual('c', self.tree.root.left_child.right_child.key)
        self.assertEqual('c-value', self.tree.root.left_child.right_child.value)
        self.assertEqual(None,
                         self.tree.root.left_child.right_child.left_child)
        self.assertEqual(None,
                         self.tree.root.left_child.right_child.right_child)
        self.assertEqual('b', self.tree.root.left_child.right_child.parent.key)

        self.assertEqual('e', self.tree.root.right_child.left_child.key)
        self.assertEqual('e-value', self.tree.root.right_child.left_child.value)
        self.assertEqual(None,
                         self.tree.root.right_child.left_child.left_child)
        self.assertEqual(None,
                         self.tree.root.right_child.left_child.right_child)
        self.assertEqual('f', self.tree.root.right_child.left_child.parent.key)

        self.assertEqual('g', self.tree.root.right_child.right_child.key)
        self.assertEqual('g-value',
                         self.tree.root.right_child.right_child.value)
        self.assertEqual(None,
                         self.tree.root.right_child.right_child.left_child)
        self.assertEqual(None,
                         self.tree.root.right_child.right_child.right_child)
        self.assertEqual('f', self.tree.root.right_child.right_child.parent.key)

    def test_delete_right_child_as_leaf(self):
        self.create_seven_node_tree()

        self.tree.delete('c')

        self.assertEqual(6, self.tree.size)
        self.assert_properties(self.tree.root)

        self.assertEqual('d', self.tree.root.key)
        self.assertEqual('d-value', self.tree.root.value)
        self.assertEqual('b', self.tree.root.left_child.key)
        self.assertEqual('f', self.tree.root.right_child.key)
        self.assertEqual(None, self.tree.root.parent)

        self.assertEqual('b', self.tree.root.left_child.key)
        self.assertEqual('b-value', self.tree.root.left_child.value)
        self.assertEqual('a', self.tree.root.left_child.left_child.key)
        self.assertEqual(None, self.tree.root.left_child.right_child)
        self.assertEqual('d', self.tree.root.left_child.parent.key)

        self.assertEqual('f', self.tree.root.right_child.key)
        self.assertEqual('f-value', self.tree.root.right_child.value)
        self.assertEqual('e', self.tree.root.right_child.left_child.key)
        self.assertEqual('g', self.tree.root.right_child.right_child.key)
        self.assertEqual('d', self.tree.root.right_child.parent.key)

        self.assertEqual('a', self.tree.root.left_child.left_child.key)
        self.assertEqual('a-value', self.tree.root.left_child.left_child.value)
        self.assertEqual(None,
                         self.tree.root.left_child.left_child.left_child)
        self.assertEqual(None,
                         self.tree.root.left_child.left_child.right_child)
        self.assertEqual('b', self.tree.root.left_child.left_child.parent.key)

        self.assertEqual('e', self.tree.root.right_child.left_child.key)
        self.assertEqual('e-value', self.tree.root.right_child.left_child.value)
        self.assertEqual(None,
                         self.tree.root.right_child.left_child.left_child)
        self.assertEqual(None,
                         self.tree.root.right_child.left_child.right_child)
        self.assertEqual('f', self.tree.root.right_child.left_child.parent.key)

        self.assertEqual('g', self.tree.root.right_child.right_child.key)
        self.assertEqual('g-value',
                         self.tree.root.right_child.right_child.value)
        self.assertEqual(None,
                         self.tree.root.right_child.right_child.left_child)
        self.assertEqual(None,
                         self.tree.root.right_child.right_child.right_child)
        self.assertEqual('f', self.tree.root.right_child.right_child.parent.key)

    def test_delete_two_leaf_nodes(self):
        self.create_seven_node_tree()

        self.tree.delete('a')
        self.tree.delete('c')

        self.assertEqual(5, self.tree.size)
        self.assert_properties(self.tree.root)

        self.assertEqual('d', self.tree.root.key)
        self.assertEqual('d-value', self.tree.root.value)
        self.assertEqual('b', self.tree.root.left_child.key)
        self.assertEqual('f', self.tree.root.right_child.key)
        self.assertEqual(None, self.tree.root.parent)

        self.assertEqual('b', self.tree.root.left_child.key)
        self.assertEqual('b-value', self.tree.root.left_child.value)
        self.assertEqual(None, self.tree.root.left_child.left_child)
        self.assertEqual(None, self.tree.root.left_child.right_child)
        self.assertEqual('d', self.tree.root.left_child.parent.key)

        self.assertEqual('f', self.tree.root.right_child.key)
        self.assertEqual('f-value', self.tree.root.right_child.value)
        self.assertEqual('e', self.tree.root.right_child.left_child.key)
        self.assertEqual('g', self.tree.root.right_child.right_child.key)
        self.assertEqual('d', self.tree.root.right_child.parent.key)

        self.assertEqual('e', self.tree.root.right_child.left_child.key)
        self.assertEqual('e-value', self.tree.root.right_child.left_child.value)
        self.assertEqual(None,
                         self.tree.root.right_child.left_child.left_child)
        self.assertEqual(None,
                         self.tree.root.right_child.left_child.right_child)
        self.assertEqual('f', self.tree.root.right_child.left_child.parent.key)

        self.assertEqual('g', self.tree.root.right_child.right_child.key)
        self.assertEqual('g-value',
                         self.tree.root.right_child.right_child.value)
        self.assertEqual(None,
                         self.tree.root.right_child.right_child.left_child)
        self.assertEqual(None,
                         self.tree.root.right_child.right_child.right_child)
        self.assertEqual('f',
                         self.tree.root.right_child.right_child.parent.key)

    def test_delete_both_children_node_and_immediate_leaf_successor(self):
        node_d = self.node_type('d', 'd-value')
        node_b = self.node_type('b', 'b-value', parent=node_d)
        node_d.left_child = node_b
        node_a = self.node_type('a', 'a-value', parent=node_b)
        node_c = self.node_type('c', 'c-value', parent=node_b)
        node_b.left_child = node_a
        node_b.right_child = node_c
        self.tree.root = node_d
        self.tree._size = 4

        node_a.update_heights()
        node_c.update_heights()
        node_b.update_heights()
        node_d.update_heights()

        self.tree.delete('b')

        self.assertEqual(3, self.tree.size)
        self.assert_properties(self.tree.root)

        self.assertEqual('d', self.tree.root.key)
        self.assertEqual('d-value', self.tree.root.value)
        self.assertEqual('c', self.tree.root.left_child.key)
        self.assertEqual(None, self.tree.root.right_child)
        self.assertEqual(None, self.tree.root.parent)

        self.assertEqual('c', self.tree.root.left_child.key)
        self.assertEqual('c-value', self.tree.root.left_child.value)
        self.assertEqual('a', self.tree.root.left_child.left_child.key)
        self.assertEqual(None, self.tree.root.left_child.right_child)
        self.assertEqual('d',  self.tree.root.left_child.parent.key)

        self.assertEqual('a', self.tree.root.left_child.left_child.key)
        self.assertEqual('a-value', self.tree.root.left_child.left_child.value)
        self.assertEqual(None,
                         self.tree.root.left_child.left_child.left_child)
        self.assertEqual(None,
                         self.tree.root.left_child.left_child.right_child)
        self.assertEqual('c',  self.tree.root.left_child.left_child.parent.key)

    def test_delete_both_children_node_and_leaf_successor(self):
        node_d = self.node_type('d', 'd-value')
        node_b = self.node_type('b', 'b-value', parent=node_d)
        node_f = self.node_type('f', 'f-value', parent=node_d)
        node_d.left_child = node_b
        node_d.right_child = node_f
        node_e = self.node_type('e', 'e-value', parent=node_f)
        node_f.left_child = node_e
        self.tree.root = node_d
        self.tree._size = 4

        node_b.update_heights()
        node_e.update_heights()
        node_f.update_heights()
        node_d.update_heights()

        self.tree.delete('d')

        self.assertEqual(3, self.tree.size)
        self.assert_properties(self.tree.root)

        self.assertEqual('e', self.tree.root.key)
        self.assertEqual('e-value', self.tree.root.value)
        self.assertEqual('b', self.tree.root.left_child.key)
        self.assertEqual('f', self.tree.root.right_child.key)
        self.assertEqual(None, self.tree.root.parent)

        self.assertEqual('b', self.tree.root.left_child.key)
        self.assertEqual('b-value', self.tree.root.left_child.value)
        self.assertEqual(None, self.tree.root.left_child.left_child)
        self.assertEqual(None, self.tree.root.left_child.right_child)
        self.assertEqual('e',  self.tree.root.left_child.parent.key)

        self.assertEqual('f', self.tree.root.right_child.key)
        self.assertEqual('f-value', self.tree.root.right_child.value)
        self.assertEqual(None, self.tree.root.right_child.left_child)
        self.assertEqual(None, self.tree.root.right_child.right_child)
        self.assertEqual('e', self.tree.root.right_child.parent.key)

    def test_delete_both_children_node_and_one_child_successor(self):
        node_e = self.node_type('e', 'e-value')
        node_b = self.node_type('b', 'b-value', parent=node_e)
        node_f = self.node_type('f', 'f-value', parent=node_e)
        node_e.left_child = node_b
        node_e.right_child = node_f
        node_g = self.node_type('g', 'g-value', parent=node_f)
        node_f.right_child = node_g
        self.tree.root = node_e
        self.tree._size = 4

        node_b.update_heights()
        node_g.update_heights()
        node_f.update_heights()
        node_e.update_heights()

        self.tree.delete('e')

        self.assertEqual(3, self.tree.size)
        self.assert_properties(self.tree.root)

        self.assertEqual('f', self.tree.root.key)
        self.assertEqual('f-value', self.tree.root.value)
        self.assertEqual('b', self.tree.root.left_child.key)
        self.assertEqual('g', self.tree.root.right_child.key)
        self.assertEqual(None, self.tree.root.parent)

        self.assertEqual('b', self.tree.root.left_child.key)
        self.assertEqual('b-value', self.tree.root.left_child.value)
        self.assertEqual(None, self.tree.root.left_child.left_child)
        self.assertEqual(None, self.tree.root.left_child.right_child)
        self.assertEqual('f', self.tree.root.left_child.parent.key)

        self.assertEqual('g', self.tree.root.right_child.key)
        self.assertEqual('g-value', self.tree.root.right_child.value)
        self.assertEqual(None, self.tree.root.right_child.left_child)
        self.assertEqual(None, self.tree.root.right_child.right_child)
        self.assertEqual('f', self.tree.root.right_child.parent.key)

    def test_delete_one_left_child_node_of_left_parent(self):
        node_d = self.node_type('d', 'd-value')
        node_b = self.node_type('b', 'b-value', parent=node_d)
        node_d.left_child = node_b
        node_a = self.node_type('a', 'a-value', parent=node_b)
        node_b.left_child = node_a
        self.tree.root = node_d
        self.tree._size = 3

        node_a.update_heights()
        node_b.update_heights()
        node_d.update_heights()

        self.tree.delete('b')

        self.assertEqual(2, self.tree.size)
        self.assert_properties(self.tree.root)

        self.assertEqual('d', self.tree.root.key)
        self.assertEqual('d-value', self.tree.root.value)
        self.assertEqual('a', self.tree.root.left_child.key)
        self.assertEqual(None, self.tree.root.right_child)
        self.assertEqual(None, self.tree.root.parent)

        self.assertEqual('a', self.tree.root.left_child.key)
        self.assertEqual('a-value', self.tree.root.left_child.value)
        self.assertEqual(None, self.tree.root.left_child.left_child)
        self.assertEqual(None, self.tree.root.left_child.right_child)
        self.assertEqual('d', self.tree.root.left_child.parent.key)

    def test_delete_one_left_child_node_of_right_parent(self):
        node_d = self.node_type('d', 'd-value')
        node_f = self.node_type('f', 'f-value', parent=node_d)
        node_d.right_child = node_f
        node_e = self.node_type('e', 'e-value', parent=node_f)
        node_f.left_child = node_e
        self.tree.root = node_d
        self.tree._size = 3

        node_e.update_heights()
        node_f.update_heights()
        node_d.update_heights()

        self.tree.delete('f')

        self.assertEqual(2, self.tree.size)
        self.assert_properties(self.tree.root)

        self.assertEqual('d', self.tree.root.key)
        self.assertEqual('d-value', self.tree.root.value)
        self.assertEqual(None, self.tree.root.left_child)
        self.assertEqual('e', self.tree.root.right_child.key)
        self.assertEqual(None, self.tree.root.parent)

        self.assertEqual('e', self.tree.root.right_child.key)
        self.assertEqual('e-value', self.tree.root.right_child.value)
        self.assertEqual(None, self.tree.root.right_child.left_child)
        self.assertEqual(None, self.tree.root.right_child.right_child)
        self.assertEqual('d', self.tree.root.right_child.parent.key)

    def test_delete_one_left_child_node_of_parent(self):
        node_d = self.node_type('d', 'd-value')
        node_b = self.node_type('b', 'b-value', parent=node_d)
        node_d.left_child = node_b
        self.tree.root = node_d
        self.tree._size = 2

        node_b.update_heights()
        node_d.update_heights()

        self.tree.delete('d')

        self.assertEqual(1, self.tree.size)
        self.assert_properties(self.tree.root)

        self.assertEqual('b', self.tree.root.key)
        self.assertEqual('b-value', self.tree.root.value)
        self.assertEqual(None, self.tree.root.left_child)
        self.assertEqual(None, self.tree.root.right_child)
        self.assertEqual(None, self.tree.root.parent)

    def test_delete_one_right_child_node_of_left_parent(self):
        node_d = self.node_type('d', 'd-value')
        node_b = self.node_type('b', 'b-value', parent=node_d)
        node_d.left_child = node_b
        node_c = self.node_type('c', 'c-value', parent=node_b)
        node_b.right_child = node_c
        self.tree.root = node_d
        self.tree._size = 3

        node_b.update_heights()
        node_c.update_heights()
        node_d.update_heights()

        self.tree.delete('b')

        self.assertEqual(2, self.tree.size)
        self.assert_properties(self.tree.root)

        self.assertEqual('d', self.tree.root.key)
        self.assertEqual('d-value', self.tree.root.value)
        self.assertEqual('c', self.tree.root.left_child.key)
        self.assertEqual(None, self.tree.root.right_child)
        self.assertEqual(None, self.tree.root.parent)

        self.assertEqual('c', self.tree.root.left_child.key)
        self.assertEqual('c-value', self.tree.root.left_child.value)
        self.assertEqual(None, self.tree.root.left_child.left_child)
        self.assertEqual(None, self.tree.root.left_child.right_child)
        self.assertEqual('d', self.tree.root.left_child.parent.key)

    def test_delete_one_right_child_node_of_right_parent(self):
        node_d = self.node_type('d', 'd-value')
        node_f = self.node_type('f', 'f-value', parent=node_d)
        node_d.right_child = node_f
        node_g = self.node_type('g', 'g-value', parent=node_f)
        node_f.right_child = node_g
        self.tree.root = node_d
        self.tree._size = 3

        node_f.update_heights()
        node_g.update_heights()
        node_d.update_heights()

        self.tree.delete('f')

        self.assertEqual(2, self.tree.size)
        self.assert_properties(self.tree.root)

        self.assertEqual('d', self.tree.root.key)
        self.assertEqual('d-value', self.tree.root.value)
        self.assertEqual(None, self.tree.root.left_child)
        self.assertEqual('g', self.tree.root.right_child.key)
        self.assertEqual(None, self.tree.root.parent)

        self.assertEqual('g', self.tree.root.right_child.key)
        self.assertEqual('g-value', self.tree.root.right_child.value)
        self.assertEqual(None, self.tree.root.right_child.left_child)
        self.assertEqual(None, self.tree.root.right_child.right_child)
        self.assertEqual('d', self.tree.root.right_child.parent.key)

    def test_delete_one_right_child_node_of_parent(self):
        node_d = self.node_type('d', 'd-value')
        node_f = self.node_type('f', 'f-value', parent=node_d)
        node_d.right_child = node_f
        self.tree.root = node_d
        self.tree._size = 2

        node_f.update_heights()
        node_d.update_heights()

        self.tree.delete('d')

        self.assertEqual(1, self.tree.size)
        self.assert_properties(self.tree.root)

        self.assertEqual('f', self.tree.root.key)
        self.assertEqual('f-value', self.tree.root.value)
        self.assertEqual(None, self.tree.root.left_child)
        self.assertEqual(None, self.tree.root.right_child)
        self.assertEqual(None, self.tree.root.parent)

    def test_delete_on_seven_node_tree(self):
        self.create_seven_node_tree()

        self.tree.delete('a')

        self.assertEqual(6, self.tree.size)
        self.assert_properties(self.tree.root)

        self.assertEqual('d', self.tree.root.key)
        self.assertEqual('d-value', self.tree.root.value)
        self.assertEqual('b', self.tree.root.left_child.key)
        self.assertEqual('f', self.tree.root.right_child.key)
        self.assertEqual(None, self.tree.root.parent)

        self.assertEqual('b', self.tree.root.left_child.key)
        self.assertEqual('b-value', self.tree.root.left_child.value)
        self.assertEqual(None, self.tree.root.left_child.left_child)
        self.assertEqual('c', self.tree.root.left_child.right_child.key)

        self.assertEqual('f', self.tree.root.right_child.key)
        self.assertEqual('f-value', self.tree.root.right_child.value)
        self.assertEqual('e', self.tree.root.right_child.left_child.key)
        self.assertEqual('g', self.tree.root.right_child.right_child.key)

        self.assertEqual('c', self.tree.root.left_child.right_child.key)
        self.assertEqual('c-value', self.tree.root.left_child.right_child.value)
        self.assertEqual(None,
                         self.tree.root.left_child.right_child.left_child)
        self.assertEqual(None,
                         self.tree.root.left_child.right_child.right_child)

        self.assertEqual('e', self.tree.root.right_child.left_child.key)
        self.assertEqual('e-value', self.tree.root.right_child.left_child.value)
        self.assertEqual(None,
                         self.tree.root.right_child.left_child.left_child)
        self.assertEqual(None,
                         self.tree.root.right_child.left_child.right_child)

        self.assertEqual('g', self.tree.root.right_child.right_child.key)
        self.assertEqual('g-value', self.tree.root.right_child.right_child.value)
        self.assertEqual(None,
                         self.tree.root.right_child.right_child.left_child)
        self.assertEqual(None,
                         self.tree.root.right_child.right_child.right_child)

        self.tree.delete('c')

        self.assertEqual(5, self.tree.size)
        self.assert_properties(self.tree.root)

        self.assertEqual('d', self.tree.root.key)
        self.assertEqual('d-value', self.tree.root.value)
        self.assertEqual('b', self.tree.root.left_child.key)
        self.assertEqual('f', self.tree.root.right_child.key)
        self.assertEqual(None, self.tree.root.parent)

        self.assertEqual('b', self.tree.root.left_child.key)
        self.assertEqual('b-value', self.tree.root.left_child.value)
        self.assertEqual(None, self.tree.root.left_child.left_child)
        self.assertEqual(None, self.tree.root.left_child.right_child)

        self.assertEqual('f', self.tree.root.right_child.key)
        self.assertEqual('f-value', self.tree.root.right_child.value)
        self.assertEqual('e', self.tree.root.right_child.left_child.key)
        self.assertEqual('g', self.tree.root.right_child.right_child.key)

        self.assertEqual('e', self.tree.root.right_child.left_child.key)
        self.assertEqual('e-value', self.tree.root.right_child.left_child.value)
        self.assertEqual(None,
                         self.tree.root.right_child.left_child.left_child)
        self.assertEqual(None,
                         self.tree.root.right_child.left_child.right_child)

        self.assertEqual('g', self.tree.root.right_child.right_child.key)
        self.assertEqual('g-value', self.tree.root.right_child.right_child.value)
        self.assertEqual(None,
                         self.tree.root.right_child.right_child.left_child)
        self.assertEqual(None,
                         self.tree.root.right_child.right_child.right_child)

        self.tree.delete('e')

        self.assertEqual(4, self.tree.size)
        self.assert_properties(self.tree.root)

        self.assertEqual('d', self.tree.root.key)
        self.assertEqual('d-value', self.tree.root.value)
        self.assertEqual('b', self.tree.root.left_child.key)
        self.assertEqual('f', self.tree.root.right_child.key)
        self.assertEqual(None, self.tree.root.parent)

        self.assertEqual('b', self.tree.root.left_child.key)
        self.assertEqual('b-value', self.tree.root.left_child.value)
        self.assertEqual(None, self.tree.root.left_child.left_child)
        self.assertEqual(None, self.tree.root.left_child.right_child)

        self.assertEqual('f', self.tree.root.right_child.key)
        self.assertEqual('f-value', self.tree.root.right_child.value)
        self.assertEqual(None, self.tree.root.right_child.left_child)
        self.assertEqual('g', self.tree.root.right_child.right_child.key)

        self.assertEqual('g', self.tree.root.right_child.right_child.key)
        self.assertEqual('g-value', self.tree.root.right_child.right_child.value)
        self.assertEqual(None,
                         self.tree.root.right_child.right_child.left_child)
        self.assertEqual(None,
                         self.tree.root.right_child.right_child.right_child)

        self.tree.delete('g')

        self.assertEqual(3, self.tree.size)
        self.assert_properties(self.tree.root)

        self.assertEqual('d', self.tree.root.key)
        self.assertEqual('d-value', self.tree.root.value)
        self.assertEqual('b', self.tree.root.left_child.key)
        self.assertEqual('f', self.tree.root.right_child.key)
        self.assertEqual(None, self.tree.root.parent)

        self.assertEqual('b', self.tree.root.left_child.key)
        self.assertEqual('b-value', self.tree.root.left_child.value)
        self.assertEqual(None, self.tree.root.left_child.left_child)
        self.assertEqual(None, self.tree.root.left_child.right_child)

        self.assertEqual('f', self.tree.root.right_child.key)
        self.assertEqual('f-value', self.tree.root.right_child.value)
        self.assertEqual(None, self.tree.root.right_child.left_child)
        self.assertEqual(None, self.tree.root.right_child.right_child)

        self.tree.delete('b')

        self.assertEqual(2, self.tree.size)
        self.assert_properties(self.tree.root)

        self.assertEqual('d', self.tree.root.key)
        self.assertEqual('d-value', self.tree.root.value)
        self.assertEqual(None, self.tree.root.left_child)
        self.assertEqual('f', self.tree.root.right_child.key)
        self.assertEqual(None, self.tree.root.parent)

        self.assertEqual('f', self.tree.root.right_child.key)
        self.assertEqual('f-value', self.tree.root.right_child.value)
        self.assertEqual(None, self.tree.root.right_child.left_child)
        self.assertEqual(None, self.tree.root.right_child.right_child)

        self.tree.delete('f')

        self.assertEqual(1, self.tree.size)
        self.assert_properties(self.tree.root)

        self.assertEqual('d', self.tree.root.key)
        self.assertEqual('d-value', self.tree.root.value)
        self.assertEqual(None, self.tree.root.left_child)
        self.assertEqual(None, self.tree.root.right_child)
        self.assertEqual(None, self.tree.root.parent)

        self.tree.delete('d')

        self.assertEqual(0, self.tree.size)
        self.assert_properties(self.tree.root)

class AvlTreeTestCase(BinarySearchTreeTestCase):

    def setUp(self):
        self.tree = binary_search_tree.AvlTree()
        self.node_type = binary_search_tree.TreeNode

    def tearDown(self):
        pass

    def assert_balance(self, root):
        if root is None:
            return

        nodes = [ root ]

        while len(nodes) > 0:
            node = nodes.pop()

            self.assertTrue(node.balance_factor() <= 1 or
                            node.balance_factor() >= -1)

            if node.left_child is not None:
                nodes.append(node.left_child)
            if node.right_child is not None:
                nodes.append(node.right_child)

    def assert_properties(self, root):
        super(AvlTreeTestCase, self).assert_properties(root)

        self.assert_balance(root)

    def assert_three_node_tree_as_b_a_c(self):
        self.assertEqual(3, self.tree.size)
        self.assert_properties(self.tree.root)

        self.assertEqual('b', self.tree.root.key)
        self.assertEqual('b-value', self.tree.root.value)
        self.assertEqual('a', self.tree.root.left_child.key)
        self.assertEqual('c', self.tree.root.right_child.key)
        self.assertEqual(None, self.tree.root.parent)

        self.assertEqual('a', self.tree.root.left_child.key)
        self.assertEqual('a-value', self.tree.root.left_child.value)
        self.assertEqual(None,
                         self.tree.root.left_child.left_child)
        self.assertEqual(None,
                         self.tree.root.left_child.right_child)
        self.assertEqual('b', self.tree.root.left_child.parent.key)

        self.assertEqual('c', self.tree.root.right_child.key)
        self.assertEqual('c-value', self.tree.root.right_child.value)
        self.assertEqual(None,
                         self.tree.root.right_child.left_child)
        self.assertEqual(None,
                         self.tree.root.right_child.right_child)
        self.assertEqual('b', self.tree.root.right_child.parent.key)

    def assert_five_node_tree_as_b_a_d_c_e(self):
        self.assertEqual(5, self.tree.size)
        self.assert_properties(self.tree.root)

        self.assertEqual('b', self.tree.root.key)
        self.assertEqual('b-value', self.tree.root.value)
        self.assertEqual('a', self.tree.root.left_child.key)
        self.assertEqual('d', self.tree.root.right_child.key)
        self.assertEqual(None, self.tree.root.parent)

        self.assertEqual('a', self.tree.root.left_child.key)
        self.assertEqual('a-value', self.tree.root.left_child.value)
        self.assertEqual(None, self.tree.root.left_child.left_child)
        self.assertEqual(None, self.tree.root.left_child.right_child)
        self.assertEqual('b', self.tree.root.left_child.parent.key)

        self.assertEqual('d', self.tree.root.right_child.key)
        self.assertEqual('d-value', self.tree.root.right_child.value)
        self.assertEqual('c', self.tree.root.right_child.left_child.key)
        self.assertEqual('e', self.tree.root.right_child.right_child.key)
        self.assertEqual('b', self.tree.root.right_child.parent.key)

        self.assertEqual('c', self.tree.root.right_child.left_child.key)
        self.assertEqual('c-value', self.tree.root.right_child.left_child.value)
        self.assertEqual(None,
                         self.tree.root.right_child.left_child.left_child)
        self.assertEqual(None,
                         self.tree.root.right_child.left_child.right_child)
        self.assertEqual('d', self.tree.root.right_child.left_child.parent.key)

        self.assertEqual('e', self.tree.root.right_child.right_child.key)
        self.assertEqual('e-value',
                         self.tree.root.right_child.right_child.value)
        self.assertEqual(None,
                         self.tree.root.right_child.right_child.left_child)
        self.assertEqual(None,
                         self.tree.root.right_child.right_child.right_child)
        self.assertEqual('d', self.tree.root.right_child.right_child.parent.key)

    def assert_five_node_tree_as_d_b_e_a_c(self):
        self.assertEqual(5, self.tree.size)
        self.assert_properties(self.tree.root)

        self.assertEqual('d', self.tree.root.key)
        self.assertEqual('d-value', self.tree.root.value)
        self.assertEqual('b', self.tree.root.left_child.key)
        self.assertEqual('e', self.tree.root.right_child.key)
        self.assertEqual(None, self.tree.root.parent)

        self.assertEqual('b', self.tree.root.left_child.key)
        self.assertEqual('b-value', self.tree.root.left_child.value)
        self.assertEqual('a', self.tree.root.left_child.left_child.key)
        self.assertEqual('c', self.tree.root.left_child.right_child.key)
        self.assertEqual('d', self.tree.root.left_child.parent.key)

        self.assertEqual('e', self.tree.root.right_child.key)
        self.assertEqual('e-value', self.tree.root.right_child.value)
        self.assertEqual(None, self.tree.root.right_child.left_child)
        self.assertEqual(None, self.tree.root.right_child.right_child)
        self.assertEqual('d', self.tree.root.right_child.parent.key)

        self.assertEqual('a', self.tree.root.left_child.left_child.key)
        self.assertEqual('a-value', self.tree.root.left_child.left_child.value)
        self.assertEqual(None, self.tree.root.left_child.left_child.left_child)
        self.assertEqual(None, self.tree.root.left_child.left_child.right_child)
        self.assertEqual('b', self.tree.root.left_child.left_child.parent.key)

        self.assertEqual('c', self.tree.root.left_child.right_child.key)
        self.assertEqual('c-value', self.tree.root.left_child.right_child.value)
        self.assertEqual(None, self.tree.root.left_child.right_child.left_child)
        self.assertEqual(None,
                         self.tree.root.left_child.right_child.right_child)
        self.assertEqual('b', self.tree.root.left_child.right_child.parent.key)

    def create_three_node_tree_as_b_a_c(self):
        node_b = self.node_type('b', 'b-value')
        node_a = self.node_type('a', 'a-value', parent=node_b)
        node_c = self.node_type('c', 'c-value', parent=node_b)
        node_b.left_child = node_a
        node_b.right_child = node_c
        self.tree.root = node_b
        self.tree._size = 3

        node_a.update_heights()
        node_b.update_heights()
        node_c.update_heights()

        self.assert_three_node_tree_as_b_a_c()

    def create_five_node_tree_as_b_a_d_c_e(self):
        node_b = self.node_type('b', 'b-value')
        node_a = self.node_type('a', 'a-value', parent=node_b)
        node_d = self.node_type('d', 'd-value', parent=node_b)
        node_b.left_child = node_a
        node_b.right_child = node_d
        node_c = self.node_type('c', 'c-value', parent=node_d)
        node_e = self.node_type('e', 'e-value', parent=node_d)
        node_d.left_child = node_c
        node_d.right_child = node_e
        self.tree.root = node_b
        self.tree._size = 5

        node_a.update_heights()
        node_b.update_heights()
        node_c.update_heights()
        node_d.update_heights()
        node_e.update_heights()

        self.assert_five_node_tree_as_b_a_d_c_e()

    def create_five_node_tree_as_d_b_e_a_c(self):
        node_d = self.node_type('d', 'd-value')
        node_b = self.node_type('b', 'b-value', parent=node_d)
        node_e = self.node_type('e', 'e-value', parent=node_d)
        node_d.left_child = node_b
        node_d.right_child = node_e
        node_a = self.node_type('a', 'a-value', parent=node_b)
        node_c = self.node_type('c', 'c-value', parent=node_b)
        node_b.left_child = node_a
        node_b.right_child = node_c
        self.tree.root = node_d
        self.tree._size = 5

        node_a.update_heights()
        node_b.update_heights()
        node_c.update_heights()
        node_d.update_heights()
        node_e.update_heights()

        self.assert_five_node_tree_as_d_b_e_a_c()

    def test_rotate_left_on_b_a_c(self):
        self.create_three_node_tree_as_b_a_c()

        self.tree.rotate_left(self.tree.root)

        self.assertEqual(3, self.tree.size)
        self.assert_properties(self.tree.root)

        self.assertEqual('c', self.tree.root.key)
        self.assertEqual('c-value', self.tree.root.value)
        self.assertEqual('b', self.tree.root.left_child.key)
        self.assertEqual(None, self.tree.root.right_child)
        self.assertEqual(None, self.tree.root.parent)

        self.assertEqual('b', self.tree.root.left_child.key)
        self.assertEqual('b-value', self.tree.root.left_child.value)
        self.assertEqual('a', self.tree.root.left_child.left_child.key)
        self.assertEqual(None, self.tree.root.left_child.right_child)
        self.assertEqual('c', self.tree.root.left_child.parent.key)

        self.assertEqual('a', self.tree.root.left_child.left_child.key)
        self.assertEqual('a-value', self.tree.root.left_child.left_child.value)
        self.assertEqual(None,
                         self.tree.root.left_child.left_child.left_child)
        self.assertEqual(None,
                         self.tree.root.left_child.left_child.right_child)
        self.assertEqual('b', self.tree.root.left_child.left_child.parent.key)

    def test_rotate_left_on_b_a_d_c_e(self):
        self.create_five_node_tree_as_b_a_d_c_e()

        self.tree.rotate_left(self.tree.root)

        self.assertEqual(5, self.tree.size)
        self.assert_properties(self.tree.root)

        self.assertEqual('d', self.tree.root.key)
        self.assertEqual('d-value', self.tree.root.value)
        self.assertEqual('b', self.tree.root.left_child.key)
        self.assertEqual('e', self.tree.root.right_child.key)
        self.assertEqual(None, self.tree.root.parent)

        self.assertEqual('b', self.tree.root.left_child.key)
        self.assertEqual('b-value', self.tree.root.left_child.value)
        self.assertEqual('a', self.tree.root.left_child.left_child.key)
        self.assertEqual('c', self.tree.root.left_child.right_child.key)
        self.assertEqual('d', self.tree.root.left_child.parent.key)

        self.assertEqual('e', self.tree.root.right_child.key)
        self.assertEqual('e-value', self.tree.root.right_child.value)
        self.assertEqual(None, self.tree.root.right_child.left_child)
        self.assertEqual(None, self.tree.root.right_child.right_child)
        self.assertEqual('d', self.tree.root.right_child.parent.key)

        self.assertEqual('a', self.tree.root.left_child.left_child.key)
        self.assertEqual('a-value', self.tree.root.left_child.left_child.value)
        self.assertEqual(None, self.tree.root.left_child.left_child.left_child)
        self.assertEqual(None, self.tree.root.left_child.left_child.right_child)
        self.assertEqual('b', self.tree.root.left_child.left_child.parent.key)

        self.assertEqual('c', self.tree.root.left_child.right_child.key)
        self.assertEqual('c-value', self.tree.root.left_child.right_child.value)
        self.assertEqual(None, self.tree.root.left_child.right_child.left_child)
        self.assertEqual(None,
                         self.tree.root.left_child.right_child.right_child)
        self.assertEqual('b', self.tree.root.left_child.right_child.parent.key)

    def test_rotate_right_on_b_a_c(self):
        self.create_three_node_tree_as_b_a_c()

        self.tree.rotate_right(self.tree.root)

        self.assertEqual(3, self.tree.size)
        self.assert_properties(self.tree.root)

        self.assertEqual('a', self.tree.root.key)
        self.assertEqual('a-value', self.tree.root.value)
        self.assertEqual(None, self.tree.root.left_child)
        self.assertEqual('b', self.tree.root.right_child.key)
        self.assertEqual(None, self.tree.root.parent)

        self.assertEqual('b', self.tree.root.right_child.key)
        self.assertEqual('b-value', self.tree.root.right_child.value)
        self.assertEqual(None, self.tree.root.right_child.left_child)
        self.assertEqual('c', self.tree.root.right_child.right_child.key)
        self.assertEqual('a', self.tree.root.right_child.parent.key)

        self.assertEqual('c', self.tree.root.right_child.right_child.key)
        self.assertEqual('c-value',
                         self.tree.root.right_child.right_child.value)
        self.assertEqual(None,
                         self.tree.root.right_child.right_child.left_child)
        self.assertEqual(None,
                         self.tree.root.right_child.right_child.right_child)
        self.assertEqual('b', self.tree.root.right_child.right_child.parent.key)

    def test_rotate_right_on_d_b_e_a_c(self):
        self.create_five_node_tree_as_d_b_e_a_c()

        self.tree.rotate_right(self.tree.root)

        self.assertEqual(5, self.tree.size)
        self.assert_properties(self.tree.root)

        self.assertEqual('b', self.tree.root.key)
        self.assertEqual('b-value', self.tree.root.value)
        self.assertEqual('a', self.tree.root.left_child.key)
        self.assertEqual('d', self.tree.root.right_child.key)
        self.assertEqual(None, self.tree.root.parent)

        self.assertEqual('a', self.tree.root.left_child.key)
        self.assertEqual('a-value', self.tree.root.left_child.value)
        self.assertEqual(None, self.tree.root.left_child.left_child)
        self.assertEqual(None, self.tree.root.left_child.right_child)
        self.assertEqual('b', self.tree.root.left_child.parent.key)

        self.assertEqual('d', self.tree.root.right_child.key)
        self.assertEqual('d-value', self.tree.root.right_child.value)
        self.assertEqual('c', self.tree.root.right_child.left_child.key)
        self.assertEqual('e', self.tree.root.right_child.right_child.key)
        self.assertEqual('b', self.tree.root.right_child.parent.key)

        self.assertEqual('c', self.tree.root.right_child.left_child.key)
        self.assertEqual('c-value', self.tree.root.right_child.left_child.value)
        self.assertEqual(None,
                         self.tree.root.right_child.left_child.left_child)
        self.assertEqual(None,
                         self.tree.root.right_child.left_child.right_child)
        self.assertEqual('d', self.tree.root.right_child.left_child.parent.key)

        self.assertEqual('e', self.tree.root.right_child.right_child.key)
        self.assertEqual('e-value',
                         self.tree.root.right_child.right_child.value)
        self.assertEqual(None,
                         self.tree.root.right_child.right_child.left_child)
        self.assertEqual(None,
                         self.tree.root.right_child.right_child.right_child)
        self.assertEqual('d', self.tree.root.right_child.right_child.parent.key)

    def test_rebalance_tree_as_c_b_a(self):
        node_c = self.node_type('c', 'c-value')
        node_b = self.node_type('b', 'b-value', parent=node_c)
        node_c.left_child = node_b
        node_a = self.node_type('a', 'a-value', parent=node_b)
        node_b.left_child = node_a
        self.tree.root = node_c
        self.tree._size = 3

        node_a.update_heights()
        node_b.update_heights()
        node_c.update_heights()

        self.assertEqual(3, self.tree.size)
        self.assert_properties(self.tree.root)

        self.assertEqual('c', self.tree.root.key)
        self.assertEqual('c-value', self.tree.root.value)
        self.assertEqual('b', self.tree.root.left_child.key)
        self.assertEqual(None, self.tree.root.right_child)
        self.assertEqual(None, self.tree.root.parent)

        self.assertEqual('b', self.tree.root.left_child.key)
        self.assertEqual('b-value', self.tree.root.left_child.value)
        self.assertEqual('a', self.tree.root.left_child.left_child.key)
        self.assertEqual(None, self.tree.root.left_child.right_child)
        self.assertEqual('c', self.tree.root.left_child.parent.key)

        self.assertEqual('a', self.tree.root.left_child.left_child.key)
        self.assertEqual('a-value', self.tree.root.left_child.left_child.value)
        self.assertEqual(None, self.tree.root.left_child.left_child.left_child)
        self.assertEqual(None, self.tree.root.left_child.left_child.right_child)
        self.assertEqual('b', self.tree.root.left_child.left_child.parent.key)

        self.assertEqual(2, self.tree.root.balance_factor())
        self.assertEqual(1, self.tree.root.left_child.balance_factor())
        self.assertEqual(0,
                         self.tree.root.left_child.left_child.balance_factor())

        self.tree.rebalance(self.tree.root)

        self.assertEqual(3, self.tree.size)
        self.assert_properties(self.tree.root)

        self.assertEqual('b', self.tree.root.key)
        self.assertEqual('b-value', self.tree.root.value)
        self.assertEqual('a', self.tree.root.left_child.key)
        self.assertEqual('c', self.tree.root.right_child.key)
        self.assertEqual(None, self.tree.root.parent)

        self.assertEqual('a', self.tree.root.left_child.key)
        self.assertEqual('a-value', self.tree.root.left_child.value)
        self.assertEqual(None, self.tree.root.left_child.left_child)
        self.assertEqual(None, self.tree.root.left_child.right_child)
        self.assertEqual('b', self.tree.root.left_child.parent.key)

        self.assertEqual('c', self.tree.root.right_child.key)
        self.assertEqual('c-value', self.tree.root.right_child.value)
        self.assertEqual(None, self.tree.root.right_child.left_child)
        self.assertEqual(None, self.tree.root.right_child.right_child)
        self.assertEqual('b', self.tree.root.right_child.parent.key)

    def test_rebalance_tree_as_d_a_b_c(self):
        node_d = self.node_type('d', 'd-value')
        node_a = self.node_type('a', 'a-value', parent=node_d)
        node_d.left_child = node_a
        node_b = self.node_type('b', 'b-value', parent=node_a)
        node_a.right_child = node_b
        node_c = self.node_type('c', 'c-value', parent=node_b)
        node_b.right_child = node_c
        self.tree.root = node_d
        self.tree._size = 4

        node_a.update_heights()
        node_b.update_heights()
        node_c.update_heights()
        node_d.update_heights()

        self.assertEqual(4, self.tree.size)
        self.assert_properties(self.tree.root)

        self.assertEqual('d', self.tree.root.key)
        self.assertEqual('d-value', self.tree.root.value)
        self.assertEqual('a', self.tree.root.left_child.key)
        self.assertEqual(None, self.tree.root.right_child)
        self.assertEqual(None, self.tree.root.parent)

        self.assertEqual('a', self.tree.root.left_child.key)
        self.assertEqual('a-value', self.tree.root.left_child.value)
        self.assertEqual(None, self.tree.root.left_child.left_child)
        self.assertEqual('b', self.tree.root.left_child.right_child.key)
        self.assertEqual('d', self.tree.root.left_child.parent.key)

        self.assertEqual('b', self.tree.root.left_child.right_child.key)
        self.assertEqual('b-value', self.tree.root.left_child.right_child.value)
        self.assertEqual(None, self.tree.root.left_child.right_child.left_child)
        self.assertEqual('c',
                         self.tree.root.left_child.right_child.right_child.key)
        self.assertEqual('a', self.tree.root.left_child.right_child.parent.key)

        self.assertEqual('c',
                         self.tree.root.left_child.right_child.right_child.key)
        self.assertEqual('c-value',
                         (self.tree.root.left_child.right_child. \
                         right_child.value))
        self.assertEqual(None,
                         (self.tree.root.left_child.right_child. \
                          right_child.left_child))
        self.assertEqual(None,
                         (self.tree.root.left_child.right_child. \
                          right_child.right_child))
        self.assertEqual('b',
                         (self.tree.root.left_child.right_child. \
                          right_child.parent.key))

        self.assertEqual(3, self.tree.root.balance_factor())
        self.assertEqual(-2, self.tree.root.left_child.balance_factor())
        self.assertEqual(-1,
                         self.tree.root.left_child.right_child.balance_factor())
        self.assertEqual(0,
                         (self.tree.root.left_child.right_child. \
                          right_child.balance_factor()))

        self.tree.rebalance(self.tree.root)

        self.assertEqual(4, self.tree.size)
        self.assert_properties(self.tree.root)

        self.assertEqual('b', self.tree.root.key)
        self.assertEqual('b-value', self.tree.root.value)
        self.assertEqual('a', self.tree.root.left_child.key)
        self.assertEqual('d', self.tree.root.right_child.key)
        self.assertEqual(None, self.tree.root.parent)

        self.assertEqual('a', self.tree.root.left_child.key)
        self.assertEqual('a-value', self.tree.root.left_child.value)
        self.assertEqual(None, self.tree.root.left_child.left_child)
        self.assertEqual(None, self.tree.root.left_child.right_child)
        self.assertEqual('b', self.tree.root.left_child.parent.key)

        self.assertEqual('d', self.tree.root.right_child.key)
        self.assertEqual('d-value', self.tree.root.right_child.value)
        self.assertEqual('c', self.tree.root.right_child.left_child.key)
        self.assertEqual(None, self.tree.root.right_child.right_child)
        self.assertEqual('b', self.tree.root.right_child.parent.key)

        self.assertEqual('a', self.tree.root.left_child.key)
        self.assertEqual('a-value', self.tree.root.left_child.value)
        self.assertEqual(None, self.tree.root.left_child.left_child)
        self.assertEqual(None, self.tree.root.left_child.right_child)
        self.assertEqual('b', self.tree.root.left_child.parent.key)

        self.assertEqual('c', self.tree.root.right_child.left_child.key)
        self.assertEqual('c-value', self.tree.root.right_child.left_child.value)
        self.assertEqual(None,
                         self.tree.root.right_child.left_child.left_child)
        self.assertEqual(None,
                         self.tree.root.right_child.left_child.right_child)
        self.assertEqual('d',
                         self.tree.root.right_child.left_child.parent.key)

    def test_rebalance_tree_as_a_b_c(self):
        node_a = self.node_type('a', 'a-value')
        node_b = self.node_type('b', 'b-value', parent=node_a)
        node_c = self.node_type('c', 'c-value', parent=node_b)
        node_a.right_child = node_b
        node_b.right_child = node_c
        self.tree.root = node_a
        self.tree._size = 3

        node_a.update_heights()
        node_b.update_heights()
        node_c.update_heights()

        self.assertEqual(3, self.tree.size)
        self.assert_properties(self.tree.root)

        self.assertEqual('a', self.tree.root.key)
        self.assertEqual('a-value', self.tree.root.value)
        self.assertEqual(None, self.tree.root.left_child)
        self.assertEqual('b', self.tree.root.right_child.key)
        self.assertEqual(None, self.tree.root.parent)

        self.assertEqual('b', self.tree.root.right_child.key)
        self.assertEqual('b-value', self.tree.root.right_child.value)
        self.assertEqual(None, self.tree.root.right_child.left_child)
        self.assertEqual('c', self.tree.root.right_child.right_child.key)
        self.assertEqual('a', self.tree.root.right_child.parent.key)

        self.assertEqual('c', self.tree.root.right_child.right_child.key)
        self.assertEqual('c-value',
                         self.tree.root.right_child.right_child.value)
        self.assertEqual(None,
                         self.tree.root.right_child.right_child.left_child)
        self.assertEqual(None,
                         self.tree.root.right_child.right_child.right_child)
        self.assertEqual('b', self.tree.root.right_child.right_child.parent.key)

        self.assertEqual(-2, self.tree.root.balance_factor())
        self.assertEqual(-1, self.tree.root.right_child.balance_factor())
        self.assertEqual(0,
                         (self.tree.root.right_child.right_child. \
                          balance_factor()))

        self.tree.rebalance(self.tree.root)

        self.assertEqual(3, self.tree.size)
        self.assert_properties(self.tree.root)

        self.assertEqual('b', self.tree.root.key)
        self.assertEqual('b-value', self.tree.root.value)
        self.assertEqual('a', self.tree.root.left_child.key)
        self.assertEqual('c', self.tree.root.right_child.key)
        self.assertEqual(None, self.tree.root.parent)

        self.assertEqual('a', self.tree.root.left_child.key)
        self.assertEqual('a-value', self.tree.root.left_child.value)
        self.assertEqual(None, self.tree.root.left_child.left_child)
        self.assertEqual(None, self.tree.root.left_child.right_child)
        self.assertEqual('b', self.tree.root.left_child.parent.key)

        self.assertEqual('c', self.tree.root.right_child.key)
        self.assertEqual('c-value', self.tree.root.right_child.value)
        self.assertEqual(None, self.tree.root.right_child.left_child)
        self.assertEqual(None, self.tree.root.right_child.right_child)
        self.assertEqual('b', self.tree.root.right_child.parent.key)

    def test_rebalance_tree_as_a_d_c_b(self):
        node_a = self.node_type('a', 'a-value')
        node_d = self.node_type('d', 'd-value', parent=node_a)
        node_a.right_child = node_d
        node_c = self.node_type('c', 'c-value', parent=node_d)
        node_d.left_child = node_c
        node_b = self.node_type('b', 'b-value', parent=node_c)
        node_c.left_child = node_b
        self.tree.root = node_a
        self.tree._size = 4

        node_a.update_heights()
        node_b.update_heights()
        node_c.update_heights()
        node_d.update_heights()

        self.assertEqual(4, self.tree.size)
        self.assert_properties(self.tree.root)

        self.assertEqual('a', self.tree.root.key)
        self.assertEqual('a-value', self.tree.root.value)
        self.assertEqual(None, self.tree.root.left_child)
        self.assertEqual('d', self.tree.root.right_child.key)
        self.assertEqual(None, self.tree.root.parent)

        self.assertEqual('d', self.tree.root.right_child.key)
        self.assertEqual('d-value', self.tree.root.right_child.value)
        self.assertEqual('c', self.tree.root.right_child.left_child.key)
        self.assertEqual(None, self.tree.root.right_child.right_child)
        self.assertEqual('a', self.tree.root.right_child.parent.key)

        self.assertEqual('c', self.tree.root.right_child.left_child.key)
        self.assertEqual('c-value', self.tree.root.right_child.left_child.value)
        self.assertEqual('b',
                         self.tree.root.right_child.left_child.left_child.key)
        self.assertEqual(None,
                         self.tree.root.right_child.left_child.right_child)
        self.assertEqual('d', self.tree.root.right_child.left_child.parent.key)

        self.assertEqual('b',
                         self.tree.root.right_child.left_child.left_child.key)
        self.assertEqual('b-value',
                         self.tree.root.right_child.left_child.left_child.value)
        self.assertEqual(None,
                         (self.tree.root.right_child.left_child.left_child. \
                          left_child))
        self.assertEqual(None,
                         (self.tree.root.right_child.left_child.left_child. \
                          right_child))
        self.assertEqual('c',
                         (self.tree.root.right_child.left_child.left_child. \
                          parent.key))

        self.assertEqual(-3, self.tree.root.balance_factor())
        self.assertEqual(2, self.tree.root.right_child.balance_factor())
        self.assertEqual(1,
                         self.tree.root.right_child.left_child.balance_factor())
        self.assertEqual(0,
                         (self.tree.root.right_child.left_child. \
                          left_child.balance_factor()))

        self.tree.rebalance(self.tree.root)

        self.assertEqual(4, self.tree.size)
        self.assert_properties(self.tree.root)

        self.assertEqual('c', self.tree.root.key)
        self.assertEqual('c-value', self.tree.root.value)
        self.assertEqual('a', self.tree.root.left_child.key)
        self.assertEqual('d', self.tree.root.right_child.key)
        self.assertEqual(None, self.tree.root.parent)

        self.assertEqual('a', self.tree.root.left_child.key)
        self.assertEqual('a-value', self.tree.root.left_child.value)
        self.assertEqual(None, self.tree.root.left_child.left_child)
        self.assertEqual('b', self.tree.root.left_child.right_child.key)
        self.assertEqual('c', self.tree.root.left_child.parent.key)

        self.assertEqual('d', self.tree.root.right_child.key)
        self.assertEqual('d-value', self.tree.root.right_child.value)
        self.assertEqual(None, self.tree.root.right_child.left_child)
        self.assertEqual(None, self.tree.root.right_child.right_child)
        self.assertEqual('c', self.tree.root.right_child.parent.key)

        self.assertEqual('b', self.tree.root.left_child.right_child.key)
        self.assertEqual('b-value', self.tree.root.left_child.right_child.value)
        self.assertEqual(None,
                         self.tree.root.left_child.right_child.left_child)
        self.assertEqual(None,
                         self.tree.root.left_child.right_child.right_child)
        self.assertEqual('a', self.tree.root.left_child.right_child.parent.key)

    def test_random_tree(self):
        items = [ 'a', 'b', 'c', 'd', 'e', 'f', 'g', 'h', 'i', 'j', 'k', 'l',
                 'm', 'n', 'o', 'p', 'q', 'r', 's', 't', 'u', 'v', 'w', 'x',
                 'y', 'z' ]

        self.assertEqual(26, len(items))

        items_to_add = [x for x in items]
        while len(items_to_add) > 0:
            i = random.randint(0, len(items_to_add) - 1)
            item = items_to_add.pop(i)
            self.tree[item] = item + '-value'

            self.assert_properties(self.tree.root)

        self.assertEqual(26, self.tree.size)

        for x in items:
            self.assertEqual(x + '-value', self.tree[x])

        items_to_remove = [x for x in items]
        while len(items_to_remove) > 0:
            i = random.randint(0, len(items_to_remove) - 1)
            item = items_to_remove.pop(i)
            del self.tree[item]

            self.assert_properties(self.tree.root)

        self.assertEqual(0, self.tree.size)

if __name__ == '__main__':
    class_names = [
                       TreeNodeTestCase,
                       BinarySearchTreeTestCase,
                       AvlTreeTestCase,
                  ]

    suite = unittest.TestSuite()

    for c in class_names:
        suite.addTest(unittest.defaultTestLoader.loadTestsFromTestCase(c))

    unittest.TextTestRunner().run(suite)
