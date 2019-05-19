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
        node11 = node1.add_child('11')
        node12 = node1.add_child('12')
        node13 = node1.add_child('13')

        function(node1, self.node_visitor)

        self.assertEqual([ node1,
            node11, node12, node13 ],
            self.visited_nodes)

    def assert_depth_first_traverse_on_two_level_tree(self, function):
        node1 = TreeNode('1')
        node11 = node1.add_child('11')
        node111 = node11.add_child('111')
        node12 = node1.add_child('12')
        node13 = node1.add_child('13')

        function(node1, self.node_visitor)

        self.assertEqual([ node1,
            node11,
            node111,
            node12, node13 ],
            self.visited_nodes)

    def assert_depth_first_traverse_on_three_level_tree(self, function):
        node1 = TreeNode('1')
        node11 = node1.add_child('11')
        node111 = node11.add_child('111')
        node1111 = node111.add_child('1111')
        node1112 = node111.add_child('1112')
        node12 = node1.add_child('12')
        node121 = node12.add_child('121')
        node122 = node12.add_child('122')
        node13 = node1.add_child('13')

        function(node1, self.node_visitor)

        self.assertEqual([ node1,
            node11,
            node111,
            node1111,
            node1112,
            node12,
            node121,
            node122,
            node13 ],
            self.visited_nodes)

    def assert_depth_first_traverse_on_five_level_chain_tree(self, function):
        node1 = TreeNode('1')
        node11 = node1.add_child('11')
        node111 = node11.add_child('111')
        node1111 = node111.add_child('1111')
        node11111 = node1111.add_child('11111')
        node111111 = node11111.add_child('111111')

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
        self.assertEqual([], node.children)

    def test_constructor_with_key_and_parent(self):
        key1 = 'a'
        root = TreeNode(key1)

        self.assertEqual(None, root.parent)
        self.assertEqual(key1, root.key)
        self.assertEqual([], root.children)

        key2 = 'b'
        node = TreeNode(key2, root)

        self.assertEqual(root, node.parent)
        self.assertEqual(key2, node.key)
        self.assertEqual([], node.children)

        self.assertEqual(None, root.parent)
        self.assertEqual(key1, root.key)
        self.assertEqual([], root.children)

    def test_str_node_without_parent(self):
        node = TreeNode('a')

        self.assertEqual('a', str(node))

    def test_str_node_with_parent(self):
        root = TreeNode('a')
        node = root.add_child('b')

        self.assertEqual('a', str(root))
        self.assertEqual('b', str(node))

    def test_repr_node_without_parent(self):
        node = TreeNode('a')

        self.assertEqual('[key=a, parent=None, children=[]]', repr(node))

    def test_repr_node_with_parent(self):
        root = TreeNode('a')
        node = root.add_child('b')

        self.assertEqual(
            '[key=a, parent=None, children=[[key=b, parent=a, children=[]]]]',
            repr(root))
        self.assertEqual('[key=b, parent=a, children=[]]', repr(node))

    def test_add_child(self):
        key1 = 'a'
        root = TreeNode(key1)

        key2 = 'b'
        node = root.add_child(key2)

        self.assertEqual(None, root.parent)
        self.assertEqual(key1, root.key)
        self.assertEqual([ node ], root.children)

        self.assertEqual(root, node.parent)
        self.assertEqual(key2, node.key)
        self.assertEqual([], node.children)

    def test_height_of_one_node(self):
        node = TreeNode('a')

        self.assertEqual(0, node.height)

    def test_height_of_one_level_tree(self):
        node1 = TreeNode('1')
        node11 = node1.add_child('11')
        node12 = node1.add_child('12')
        node13 = node1.add_child('13')

        self.assertEqual(1, node1.height)
        self.assertEqual(0, node11.height)
        self.assertEqual(0, node12.height)
        self.assertEqual(0, node13.height)

    def test_height_of_two_level_tree(self):
        node1 = TreeNode('1')
        node11 = node1.add_child('11')
        node111 = node11.add_child('111')
        node12 = node1.add_child('12')
        node13 = node1.add_child('13')

        self.assertEqual(2, node1.height)
        self.assertEqual(1, node11.height)
        self.assertEqual(0, node111.height)
        self.assertEqual(0, node12.height)
        self.assertEqual(0, node13.height)

    def test_height_of_three_level_tree(self):
        node1 = TreeNode('1')
        node11 = node1.add_child('11')
        node111 = node11.add_child('111')
        node1111 = node111.add_child('1111')
        node1112 = node111.add_child('1112')
        node12 = node1.add_child('12')
        node121 = node12.add_child('121')
        node122 = node12.add_child('122')
        node13 = node1.add_child('13')

        self.assertEqual(3, node1.height)
        self.assertEqual(2, node11.height)
        self.assertEqual(1, node111.height)
        self.assertEqual(0, node1111.height)
        self.assertEqual(0, node1112.height)
        self.assertEqual(1, node12.height)
        self.assertEqual(0, node121.height)
        self.assertEqual(0, node122.height)
        self.assertEqual(0, node13.height)

    def test_height_of_five_level_chain_tree(self):
        node1 = TreeNode('1')
        node11 = node1.add_child('11')
        node111 = node11.add_child('111')
        node1111 = node111.add_child('1111')
        node11111 = node1111.add_child('11111')
        node111111 = node11111.add_child('111111')

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
        node11 = node1.add_child('11')
        node12 = node1.add_child('12')
        node13 = node1.add_child('13')

        self.assertEqual(4, node1.size)
        self.assertEqual(1, node11.size)
        self.assertEqual(1, node12.size)
        self.assertEqual(1, node13.size)

    def test_size_of_two_level_tree(self):
        node1 = TreeNode('1')
        node11 = node1.add_child('11')
        node111 = node11.add_child('111')
        node12 = node1.add_child('12')
        node13 = node1.add_child('13')

        self.assertEqual(5, node1.size)
        self.assertEqual(2, node11.size)
        self.assertEqual(1, node111.size)
        self.assertEqual(1, node12.size)
        self.assertEqual(1, node13.size)

    def test_size_three_level_tree(self):
        node1 = TreeNode('1')
        node11 = node1.add_child('11')
        node111 = node11.add_child('111')
        node1111 = node111.add_child('1111')
        node1112 = node111.add_child('1112')
        node12 = node1.add_child('12')
        node121 = node12.add_child('121')
        node122 = node12.add_child('122')
        node13 = node1.add_child('13')

        self.assertEqual(9, node1.size)
        self.assertEqual(4, node11.size)
        self.assertEqual(3, node111.size)
        self.assertEqual(1, node1111.size)
        self.assertEqual(1, node1112.size)
        self.assertEqual(3, node12.size)
        self.assertEqual(1, node121.size)
        self.assertEqual(1, node122.size)
        self.assertEqual(1, node13.size)

    def test_size_of_five_level_chain_tree(self):
        node1 = TreeNode('1')
        node11 = node1.add_child('11')
        node111 = node11.add_child('111')
        node1111 = node111.add_child('1111')
        node11111 = node1111.add_child('11111')
        node111111 = node11111.add_child('111111')

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
        node11 = node1.add_child('11')
        node12 = node1.add_child('12')
        node13 = node1.add_child('13')

        node1.breadth_first_traverse(self.node_visitor)

        self.assertEqual([ node1,
            node11, node12, node13 ],
            self.visited_nodes)

    def test_breadth_first_traverse_on_two_level_tree(self):
        node1 = TreeNode('1')
        node11 = node1.add_child('11')
        node111 = node11.add_child('111')
        node12 = node1.add_child('12')
        node13 = node1.add_child('13')

        node1.breadth_first_traverse(self.node_visitor)

        self.assertEqual([ node1,
            node11, node12, node13,
            node111 ],
            self.visited_nodes)

    def test_breadth_first_traverse_on_three_level_tree(self):
        node1 = TreeNode('1')
        node11 = node1.add_child('11')
        node111 = node11.add_child('111')
        node1111 = node111.add_child('1111')
        node1112 = node111.add_child('1112')
        node12 = node1.add_child('12')
        node121 = node12.add_child('121')
        node122 = node12.add_child('122')
        node13 = node1.add_child('13')

        node1.breadth_first_traverse(self.node_visitor)

        self.assertEqual([ node1,
            node11, node12, node13,
            node111,
            node121, node122,
            node1111, node1112 ],
            self.visited_nodes)

    def test_breadth_first_traverse_on_five_level_chain_tree(self):
        node1 = TreeNode('1')
        node11 = node1.add_child('11')
        node111 = node11.add_child('111')
        node1111 = node111.add_child('1111')
        node11111 = node1111.add_child('11111')
        node111111 = node11111.add_child('111111')

        node1.breadth_first_traverse(self.node_visitor)

        self.assertEqual([ node1,
            node11,
            node111,
            node1111,
            node11111,
            node111111 ],
            self.visited_nodes)

    def test_depth_first_traverse_gen_on_one_node(self):
        node = TreeNode('a')

        generated_nodes = [ n for n in node.depth_first_traverse_gen() ]

        self.assertEqual([ node ], generated_nodes)

    def test_depth_first_traverse_gen_on_one_level_tree(self):
        node1 = TreeNode('1')
        node11 = node1.add_child('11')
        node12 = node1.add_child('12')
        node13 = node1.add_child('13')

        generated_nodes = [ n for n in node1.depth_first_traverse_gen() ]

        self.assertEqual([ node1,
            node11, node12, node13 ],
            generated_nodes)

    def test_depth_first_traverse_gen_on_two_level_tree(self):
        node1 = TreeNode('1')
        node11 = node1.add_child('11')
        node111 = node11.add_child('111')
        node12 = node1.add_child('12')
        node13 = node1.add_child('13')

        generated_nodes = [ n for n in node1.depth_first_traverse_gen() ]

        self.assertEqual([ node1,
            node11,
            node111,
            node12, node13 ],
            generated_nodes)

    def test_depth_first_traverse_gen_on_three_level_tree(self):
        node1 = TreeNode('1')
        node11 = node1.add_child('11')
        node111 = node11.add_child('111')
        node1111 = node111.add_child('1111')
        node1112 = node111.add_child('1112')
        node12 = node1.add_child('12')
        node121 = node12.add_child('121')
        node122 = node12.add_child('122')
        node13 = node1.add_child('13')

        generated_nodes = [ n for n in node1.depth_first_traverse_gen() ]

        self.assertEqual([ node1,
            node11,
            node111,
            node1111,
            node1112,
            node12,
            node121,
            node122,
            node13 ],
            generated_nodes)

    def test_depth_first_traverse_gen_on_five_level_chain_tree(self):
        node1 = TreeNode('1')
        node11 = node1.add_child('11')
        node111 = node11.add_child('111')
        node1111 = node111.add_child('1111')
        node11111 = node1111.add_child('11111')
        node111111 = node11111.add_child('111111')

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
        node11 = node1.add_child('11')
        node12 = node1.add_child('12')
        node13 = node1.add_child('13')

        generated_nodes = [ n for n in node1.breadth_first_traverse_gen() ]

        self.assertEqual([ node1,
            node11, node12, node13 ],
            generated_nodes)

    def test_breadth_first_traverse_gen_on_two_level_tree(self):
        node1 = TreeNode('1')
        node11 = node1.add_child('11')
        node111 = node11.add_child('111')
        node12 = node1.add_child('12')
        node13 = node1.add_child('13')

        generated_nodes = [ n for n in node1.breadth_first_traverse_gen() ]

        self.assertEqual([ node1,
            node11, node12, node13,
            node111 ],
            generated_nodes)

    def test_breadth_first_traverse_gen_on_three_level_tree(self):
        node1 = TreeNode('1')
        node11 = node1.add_child('11')
        node111 = node11.add_child('111')
        node1111 = node111.add_child('1111')
        node1112 = node111.add_child('1112')
        node12 = node1.add_child('12')
        node121 = node12.add_child('121')
        node122 = node12.add_child('122')
        node13 = node1.add_child('13')

        generated_nodes = [ n for n in node1.breadth_first_traverse_gen() ]

        self.assertEqual([ node1,
            node11, node12, node13,
            node111,
            node121, node122,
            node1111, node1112 ],
            generated_nodes)

    def test_breadth_first_traverse_gen_on_five_level_chain_tree(self):
        node1 = TreeNode('1')
        node11 = node1.add_child('11')
        node111 = node11.add_child('111')
        node1111 = node111.add_child('1111')
        node11111 = node1111.add_child('11111')
        node111111 = node11111.add_child('111111')

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
