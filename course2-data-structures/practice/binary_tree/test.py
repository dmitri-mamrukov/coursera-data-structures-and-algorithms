#!/usr/bin/python3

import unittest

from tree import TreeNode

class TreeNodeTestCase(unittest.TestCase):

    visited_nodes = []

    def setUp(self):
        self.visited_nodes.clear()

    def tearDown(self):
        pass

    def node_visitor(self, node):
        self.visited_nodes.append(node)

    def assert_depth_first_traverse_on_one_node(self, function):
        node = TreeNode('a')

        function(node, self.node_visitor)

        self.assertEqual([ node ], self.visited_nodes)

    def assert_depth_first_traverse_on_one_level_tree(self, function):
        node1 = TreeNode('1')
        node11 = node1.set_left('11')
        node12 = node1.set_right('12')

        function(node1, self.node_visitor)

        self.assertEqual([ node1,
            node11, node12 ],
            self.visited_nodes)

    def assert_depth_first_traverse_on_two_level_tree(self, function):
        node1 = TreeNode('1')
        node11 = node1.set_left('11')
        node111 = node11.set_left('111')
        node12 = node1.set_right('12')

        function(node1, self.node_visitor)

        self.assertEqual([ node1,
            node11,
            node111,
            node12 ],
            self.visited_nodes)

    def assert_depth_first_traverse_on_three_level_tree(self, function):
        node1 = TreeNode('1')
        node11 = node1.set_left('11')
        node111 = node11.set_left('111')
        node1111 = node111.set_left('1111')
        node1112 = node111.set_right('1112')
        node12 = node1.set_right('12')
        node121 = node12.set_left('121')
        node122 = node12.set_right('122')

        function(node1, self.node_visitor)

        self.assertEqual([ node1,
            node11,
            node111,
            node1111,
            node1112,
            node12,
            node121,
            node122 ],
            self.visited_nodes)

    def assert_depth_first_traverse_on_five_level_chain_tree(self, function):
        node1 = TreeNode('1')
        node11 = node1.set_left('11')
        node111 = node11.set_left('111')
        node1111 = node111.set_left('1111')
        node11111 = node1111.set_left('11111')
        node111111 = node11111.set_left('111111')

        function(node1, self.node_visitor)

        self.assertEqual([ node1,
            node11,
            node111,
            node1111,
            node11111,
            node111111 ],
            self.visited_nodes)

    def test_constructor_with_key(self):
        key = 'a'
        node = TreeNode(key)

        self.assertEqual(None, node.parent)
        self.assertEqual(key, node.key)
        self.assertEqual(None, node.left)
        self.assertEqual(None, node.right)

    def test_constructor_with_key_and_parent(self):
        key1 = 'a'
        root = TreeNode(key1)

        self.assertEqual(None, root.parent)
        self.assertEqual(key1, root.key)
        self.assertEqual(None, root.left)
        self.assertEqual(None, root.right)

        key2 = 'b'
        node = TreeNode(key2, root)

        self.assertEqual(root, node.parent)
        self.assertEqual(key2, node.key)
        self.assertEqual(None, node.left)
        self.assertEqual(None, node.right)

        self.assertEqual(None, root.parent)
        self.assertEqual(key1, root.key)
        self.assertEqual(None, root.left)
        self.assertEqual(None, root.right)

    def test_str_node_without_parent(self):
        node = TreeNode('a')

        self.assertEqual('a', str(node))

    def test_str_node_with_parent(self):
        root = TreeNode('a')
        node = root.set_left('b')

        self.assertEqual('a', str(root))
        self.assertEqual('b', str(node))

    def test_repr_node_without_parent(self):
        node = TreeNode('a')

        self.assertEqual('[key=a, parent=None, left=None, right=None]',
            repr(node))

    def test_repr_node_with_parent(self):
        root = TreeNode('a')
        left = root.set_left('b')
        right = root.set_right('c')

        self.assertEqual(
            '[key=a, parent=None, left=b, right=c]',
            repr(root))
        self.assertEqual('[key=b, parent=a, left=None, right=None]',
            repr(left))
        self.assertEqual('[key=c, parent=a, left=None, right=None]',
            repr(right))

    def test_set_left(self):
        key1 = 'a'
        root = TreeNode(key1)

        key2 = 'b'
        node = root.set_left(key2)

        self.assertEqual(None, root.parent)
        self.assertEqual(key1, root.key)
        self.assertEqual(node, root.left)
        self.assertEqual(None, root.right)

        self.assertEqual(root, node.parent)
        self.assertEqual(key2, node.key)
        self.assertEqual(None, node.left)
        self.assertEqual(None, node.right)

    def test_set_left_twice(self):
        key1 = 'a'
        root = TreeNode(key1)

        key2 = 'b'
        node = root.set_left(key2)

        self.assertEqual(None, root.parent)
        self.assertEqual(key1, root.key)
        self.assertEqual(node, root.left)
        self.assertEqual(None, root.right)

        self.assertEqual(root, node.parent)
        self.assertEqual(key2, node.key)
        self.assertEqual(None, node.left)
        self.assertEqual(None, node.right)

        key3 = 'c'
        node = root.set_left(key3)

        self.assertEqual(None, root.parent)
        self.assertEqual(key1, root.key)
        self.assertEqual(node, root.left)
        self.assertEqual(None, root.right)

        self.assertEqual(root, node.parent)
        self.assertEqual(key3, node.key)
        self.assertEqual(None, node.left)
        self.assertEqual(None, node.right)

    def test_set_right(self):
        key1 = 'a'
        root = TreeNode(key1)

        key2 = 'b'
        node = root.set_right(key2)

        self.assertEqual(None, root.parent)
        self.assertEqual(key1, root.key)
        self.assertEqual(None, root.left)
        self.assertEqual(node, root.right)

        self.assertEqual(root, node.parent)
        self.assertEqual(key2, node.key)
        self.assertEqual(None, node.left)
        self.assertEqual(None, node.right)

    def test_set_left_twice(self):
        key1 = 'a'
        root = TreeNode(key1)

        key2 = 'b'
        node = root.set_right(key2)

        self.assertEqual(None, root.parent)
        self.assertEqual(key1, root.key)
        self.assertEqual(None, root.left)
        self.assertEqual(node, root.right)

        self.assertEqual(root, node.parent)
        self.assertEqual(key2, node.key)
        self.assertEqual(None, node.left)
        self.assertEqual(None, node.right)

        key3 = 'c'
        node = root.set_right(key3)

        self.assertEqual(None, root.parent)
        self.assertEqual(key1, root.key)
        self.assertEqual(None, root.left)
        self.assertEqual(node, root.right)

        self.assertEqual(root, node.parent)
        self.assertEqual(key3, node.key)
        self.assertEqual(None, node.left)
        self.assertEqual(None, node.right)

    def test_height_of_one_node(self):
        node = TreeNode('a')

        self.assertEqual(0, node.height)

    def test_height_of_one_level_tree(self):
        node1 = TreeNode('1')
        node11 = node1.set_left('11')
        node12 = node1.set_right('12')

        self.assertEqual(1, node1.height)
        self.assertEqual(0, node11.height)
        self.assertEqual(0, node12.height)

    def test_height_of_two_level_tree(self):
        node1 = TreeNode('1')
        node11 = node1.set_left('11')
        node111 = node11.set_left('111')
        node12 = node1.set_right('12')

        self.assertEqual(2, node1.height)
        self.assertEqual(1, node11.height)
        self.assertEqual(0, node111.height)
        self.assertEqual(0, node12.height)

    def test_height_of_three_level_tree(self):
        node1 = TreeNode('1')
        node11 = node1.set_left('11')
        node111 = node11.set_left('111')
        node1111 = node111.set_left('1111')
        node1112 = node111.set_right('1112')
        node12 = node1.set_right('12')
        node121 = node12.set_left('121')
        node122 = node12.set_right('122')

        self.assertEqual(3, node1.height)
        self.assertEqual(2, node11.height)
        self.assertEqual(1, node111.height)
        self.assertEqual(0, node1111.height)
        self.assertEqual(0, node1112.height)
        self.assertEqual(1, node12.height)
        self.assertEqual(0, node121.height)
        self.assertEqual(0, node122.height)

    def test_height_of_five_level_chain_tree(self):
        node1 = TreeNode('1')
        node11 = node1.set_left('11')
        node111 = node11.set_left('111')
        node1111 = node111.set_left('1111')
        node11111 = node1111.set_left('11111')
        node111111 = node11111.set_left('111111')

        self.assertEqual(5, node1.height)
        self.assertEqual(4, node11.height)
        self.assertEqual(3, node111.height)
        self.assertEqual(2, node1111.height)
        self.assertEqual(1, node11111.height)
        self.assertEqual(0, node111111.height)

    def test_size_of_one_node(self):
        node = TreeNode('a')

        self.assertEqual(1, node.size)

    def test_size_of_one_level_tree(self):
        node1 = TreeNode('1')
        node11 = node1.set_left('11')
        node12 = node1.set_right('12')

        self.assertEqual(3, node1.size)
        self.assertEqual(1, node11.size)
        self.assertEqual(1, node12.size)

    def test_size_of_two_level_tree(self):
        node1 = TreeNode('1')
        node11 = node1.set_left('11')
        node111 = node11.set_left('111')
        node12 = node1.set_right('12')

        self.assertEqual(4, node1.size)
        self.assertEqual(2, node11.size)
        self.assertEqual(1, node111.size)
        self.assertEqual(1, node12.size)

    def test_size_three_level_tree(self):
        node1 = TreeNode('1')
        node11 = node1.set_left('11')
        node111 = node11.set_left('111')
        node1111 = node111.set_left('1111')
        node1112 = node111.set_right('1112')
        node12 = node1.set_right('12')
        node121 = node12.set_left('121')
        node122 = node12.set_right('122')

        self.assertEqual(8, node1.size)
        self.assertEqual(4, node11.size)
        self.assertEqual(3, node111.size)
        self.assertEqual(1, node1111.size)
        self.assertEqual(1, node1112.size)
        self.assertEqual(3, node12.size)
        self.assertEqual(1, node121.size)
        self.assertEqual(1, node122.size)

    def test_size_of_five_level_chain_tree(self):
        node1 = TreeNode('1')
        node11 = node1.set_left('11')
        node111 = node11.set_left('111')
        node1111 = node111.set_left('1111')
        node11111 = node1111.set_left('11111')
        node111111 = node11111.set_left('111111')

        self.assertEqual(6, node1.size)
        self.assertEqual(5, node11.size)
        self.assertEqual(4, node111.size)
        self.assertEqual(3, node1111.size)
        self.assertEqual(2, node11111.size)
        self.assertEqual(1, node111111.size)

    def test_depth_first_traverse_on_one_node(self):
        self.assert_depth_first_traverse_on_one_node(
            TreeNode.depth_first_traverse)

    def test_depth_first_traverse_on_one_level_tree(self):
        self.assert_depth_first_traverse_on_one_level_tree(
            TreeNode.depth_first_traverse)

    def test_depth_first_traverse_on_two_level_tree(self):
        self.assert_depth_first_traverse_on_two_level_tree(
            TreeNode.depth_first_traverse)

    def test_depth_first_traverse_on_three_level_tree(self):
        self.assert_depth_first_traverse_on_three_level_tree(
            TreeNode.depth_first_traverse)

    def test_depth_first_traverse_on_five_level_chain_tree(self):
        self.assert_depth_first_traverse_on_five_level_chain_tree(
            TreeNode.depth_first_traverse)

    def test_depth_first_traverse_iterative_on_one_node(self):
        self.assert_depth_first_traverse_on_one_node(
            TreeNode.depth_first_traverse_iterative)

    def test_depth_first_traverse_iterative_on_one_level_tree(self):
        self.assert_depth_first_traverse_on_one_level_tree(
            TreeNode.depth_first_traverse_iterative)

    def test_depth_first_traverse_iterative_on_two_level_tree(self):
        self.assert_depth_first_traverse_on_two_level_tree(
            TreeNode.depth_first_traverse_iterative)

    def test_depth_first_traverse_iterative_on_three_level_tree(self):
        self.assert_depth_first_traverse_on_three_level_tree(
            TreeNode.depth_first_traverse_iterative)

    def test_depth_first_traverse_iterative_on_five_level_chain_tree(self):
        self.assert_depth_first_traverse_on_five_level_chain_tree(
            TreeNode.depth_first_traverse_iterative)

    def test_breadth_first_traverse_on_one_node(self):
        node = TreeNode('a')

        node.breadth_first_traverse(self.node_visitor)

        self.assertEqual([ node ], self.visited_nodes)

    def test_breadth_first_traverse_on_one_level_tree(self):
        node1 = TreeNode('1')
        node11 = node1.set_left('11')
        node12 = node1.set_right('12')

        node1.breadth_first_traverse(self.node_visitor)

        self.assertEqual([ node1,
            node11, node12 ],
            self.visited_nodes)

    def test_breadth_first_traverse_on_two_level_tree(self):
        node1 = TreeNode('1')
        node11 = node1.set_left('11')
        node111 = node11.set_left('111')
        node12 = node1.set_right('12')

        node1.breadth_first_traverse(self.node_visitor)

        self.assertEqual([ node1,
            node11, node12,
            node111 ],
            self.visited_nodes)

    def test_breadth_first_traverse_on_three_level_tree(self):
        node1 = TreeNode('1')
        node11 = node1.set_left('11')
        node111 = node11.set_left('111')
        node1111 = node111.set_left('1111')
        node1112 = node111.set_right('1112')
        node12 = node1.set_right('12')
        node121 = node12.set_left('121')
        node122 = node12.set_right('122')

        node1.breadth_first_traverse(self.node_visitor)

        self.assertEqual([ node1,
            node11, node12,
            node111,
            node121, node122,
            node1111, node1112 ],
            self.visited_nodes)

    def test_breadth_first_traverse_on_five_level_chain_tree(self):
        node1 = TreeNode('1')
        node11 = node1.set_left('11')
        node111 = node11.set_left('111')
        node1111 = node111.set_left('1111')
        node11111 = node1111.set_left('11111')
        node111111 = node11111.set_left('111111')

        node1.breadth_first_traverse(self.node_visitor)

        self.assertEqual([ node1,
            node11,
            node111,
            node1111,
            node11111,
            node111111 ],
            self.visited_nodes)

    def test_in_order_traverse_on_one_node(self):
        node = TreeNode('a')

        node.in_order_traverse(self.node_visitor)

        self.assertEqual([ node ], self.visited_nodes)

    def test_in_order_traverse_on_one_level_tree(self):
        node1 = TreeNode('1')
        node11 = node1.set_left('11')
        node12 = node1.set_right('12')

        node1.in_order_traverse(self.node_visitor)

        self.assertEqual([ node11, node1, node12 ],
            self.visited_nodes)

    def test_in_order_traverse_on_two_level_tree(self):
        node1 = TreeNode('1')
        node11 = node1.set_left('11')
        node111 = node11.set_left('111')
        node12 = node1.set_right('12')

        node1.in_order_traverse(self.node_visitor)

        self.assertEqual([ node111,
            node11, node1, node12 ],
            self.visited_nodes)

    def test_in_order_traverse_on_three_level_tree(self):
        node1 = TreeNode('1')
        node11 = node1.set_left('11')
        node111 = node11.set_left('111')
        node1111 = node111.set_left('1111')
        node1112 = node111.set_right('1112')
        node12 = node1.set_right('12')
        node121 = node12.set_left('121')
        node122 = node12.set_right('122')

        node1.in_order_traverse(self.node_visitor)

        self.assertEqual([ node1111, node111, node1112,
            node11, node1,
            node121, node12, node122 ],
            self.visited_nodes)

    def test_in_order_traverse_on_five_level_chain_tree(self):
        node1 = TreeNode('1')
        node11 = node1.set_left('11')
        node111 = node11.set_left('111')
        node1111 = node111.set_left('1111')
        node11111 = node1111.set_left('11111')
        node111111 = node11111.set_left('111111')

        node1.in_order_traverse(self.node_visitor)

        self.assertEqual([ node111111,
            node11111,
            node1111,
            node111,
            node11,
            node1 ],
            self.visited_nodes)

    def test_pre_order_traverse_on_one_node(self):
        node = TreeNode('a')

        node.pre_order_traverse(self.node_visitor)

        self.assertEqual([ node ], self.visited_nodes)

    def test_pre_order_traverse_on_one_level_tree(self):
        node1 = TreeNode('1')
        node11 = node1.set_left('11')
        node12 = node1.set_right('12')

        node1.pre_order_traverse(self.node_visitor)

        self.assertEqual([ node1, node11, node12 ],
            self.visited_nodes)

    def test_pre_order_traverse_on_two_level_tree(self):
        node1 = TreeNode('1')
        node11 = node1.set_left('11')
        node111 = node11.set_left('111')
        node12 = node1.set_right('12')

        node1.pre_order_traverse(self.node_visitor)

        self.assertEqual([ node1,
            node11, node111,
            node12 ],
            self.visited_nodes)

    def test_pre_order_traverse_on_three_level_tree(self):
        node1 = TreeNode('1')
        node11 = node1.set_left('11')
        node111 = node11.set_left('111')
        node1111 = node111.set_left('1111')
        node1112 = node111.set_right('1112')
        node12 = node1.set_right('12')
        node121 = node12.set_left('121')
        node122 = node12.set_right('122')

        node1.pre_order_traverse(self.node_visitor)

        self.assertEqual([ node1,
            node11,
            node111, node1111, node1112,
            node12, node121, node122 ],
            self.visited_nodes)

    def test_pre_order_traverse_on_five_level_chain_tree(self):
        node1 = TreeNode('1')
        node11 = node1.set_left('11')
        node111 = node11.set_left('111')
        node1111 = node111.set_left('1111')
        node11111 = node1111.set_left('11111')
        node111111 = node11111.set_left('111111')

        node1.pre_order_traverse(self.node_visitor)

        self.assertEqual([ node1,
            node11,
            node111,
            node1111,
            node11111,
            node111111 ],
            self.visited_nodes)

    def test_post_order_traverse_on_one_node(self):
        node = TreeNode('a')

        node.post_order_traverse(self.node_visitor)

        self.assertEqual([ node ], self.visited_nodes)

    def test_post_order_traverse_on_one_level_tree(self):
        node1 = TreeNode('1')
        node11 = node1.set_left('11')
        node12 = node1.set_right('12')

        node1.post_order_traverse(self.node_visitor)

        self.assertEqual([ node11, node12, node1 ],
            self.visited_nodes)

    def test_post_order_traverse_on_two_level_tree(self):
        node1 = TreeNode('1')
        node11 = node1.set_left('11')
        node111 = node11.set_left('111')
        node12 = node1.set_right('12')

        node1.post_order_traverse(self.node_visitor)

        self.assertEqual([ node111,
            node11, node12, node1 ],
            self.visited_nodes)

    def test_post_order_traverse_on_three_level_tree(self):
        node1 = TreeNode('1')
        node11 = node1.set_left('11')
        node111 = node11.set_left('111')
        node1111 = node111.set_left('1111')
        node1112 = node111.set_right('1112')
        node12 = node1.set_right('12')
        node121 = node12.set_left('121')
        node122 = node12.set_right('122')

        node1.post_order_traverse(self.node_visitor)

        self.assertEqual([ node1111, node1112, node111,
            node11,
            node121, node122, node12,
            node1 ],
            self.visited_nodes)

    def test_post_order_traverse_on_five_level_chain_tree(self):
        node1 = TreeNode('1')
        node11 = node1.set_left('11')
        node111 = node11.set_left('111')
        node1111 = node111.set_left('1111')
        node11111 = node1111.set_left('11111')
        node111111 = node11111.set_left('111111')

        node1.post_order_traverse(self.node_visitor)

        self.assertEqual([ node111111,
            node11111,
            node1111,
            node111,
            node11,
            node1 ],
            self.visited_nodes)

    def test_depth_first_traverse_gen_on_one_node(self):
        node = TreeNode('a')

        generated_nodes = [ n for n in node.depth_first_traverse_gen() ]

        self.assertEqual([ node ], generated_nodes)

    def test_depth_first_traverse_gen_on_one_level_tree(self):
        node1 = TreeNode('1')
        node11 = node1.set_left('11')
        node12 = node1.set_right('12')

        generated_nodes = [ n for n in node1.depth_first_traverse_gen() ]

        self.assertEqual([ node1,
            node11, node12 ],
            generated_nodes)

    def test_depth_first_traverse_gen_on_two_level_tree(self):
        node1 = TreeNode('1')
        node11 = node1.set_left('11')
        node111 = node11.set_left('111')
        node12 = node1.set_right('12')

        generated_nodes = [ n for n in node1.depth_first_traverse_gen() ]

        self.assertEqual([ node1,
            node11,
            node111,
            node12 ],
            generated_nodes)

    def test_depth_first_traverse_gen_on_three_level_tree(self):
        node1 = TreeNode('1')
        node11 = node1.set_left('11')
        node111 = node11.set_left('111')
        node1111 = node111.set_left('1111')
        node1112 = node111.set_right('1112')
        node12 = node1.set_right('12')
        node121 = node12.set_left('121')
        node122 = node12.set_right('122')

        generated_nodes = [ n for n in node1.depth_first_traverse_gen() ]

        self.assertEqual([ node1,
            node11,
            node111,
            node1111,
            node1112,
            node12,
            node121,
            node122 ],
            generated_nodes)

    def test_depth_first_traverse_gen_on_five_level_chain_tree(self):
        node1 = TreeNode('1')
        node11 = node1.set_left('11')
        node111 = node11.set_left('111')
        node1111 = node111.set_left('1111')
        node11111 = node1111.set_left('11111')
        node111111 = node11111.set_left('111111')

        generated_nodes = [ n for n in node1.depth_first_traverse_gen() ]

        self.assertEqual([ node1,
            node11,
            node111,
            node1111,
            node11111,
            node111111 ],
            generated_nodes)

    def test_breadth_first_traverse_gen_on_one_node(self):
        node = TreeNode('a')

        generated_nodes = [ n for n in node.breadth_first_traverse_gen() ]

        self.assertEqual([ node ], generated_nodes)

    def test_breadth_first_traverse_gen_on_one_level_tree(self):
        node1 = TreeNode('1')
        node11 = node1.set_left('11')
        node12 = node1.set_right('12')

        generated_nodes = [ n for n in node1.breadth_first_traverse_gen() ]

        self.assertEqual([ node1,
            node11, node12 ],
            generated_nodes)

    def test_breadth_first_traverse_gen_on_two_level_tree(self):
        node1 = TreeNode('1')
        node11 = node1.set_left('11')
        node111 = node11.set_left('111')
        node12 = node1.set_right('12')

        generated_nodes = [ n for n in node1.breadth_first_traverse_gen() ]

        self.assertEqual([ node1,
            node11, node12,
            node111 ],
            generated_nodes)

    def test_breadth_first_traverse_gen_on_three_level_tree(self):
        node1 = TreeNode('1')
        node11 = node1.set_left('11')
        node111 = node11.set_left('111')
        node1111 = node111.set_left('1111')
        node1112 = node111.set_right('1112')
        node12 = node1.set_right('12')
        node121 = node12.set_left('121')
        node122 = node12.set_right('122')

        generated_nodes = [ n for n in node1.breadth_first_traverse_gen() ]

        self.assertEqual([ node1,
            node11, node12,
            node111,
            node121, node122,
            node1111, node1112 ],
            generated_nodes)

    def test_breadth_first_traverse_gen_on_five_level_chain_tree(self):
        node1 = TreeNode('1')
        node11 = node1.set_left('11')
        node111 = node11.set_left('111')
        node1111 = node111.set_left('1111')
        node11111 = node1111.set_left('11111')
        node111111 = node11111.set_left('111111')

        generated_nodes = [ n for n in node1.breadth_first_traverse_gen() ]

        self.assertEqual([ node1,
            node11,
            node111,
            node1111,
            node11111,
            node111111 ],
            generated_nodes)

if __name__ == '__main__':
    unittest.main()
