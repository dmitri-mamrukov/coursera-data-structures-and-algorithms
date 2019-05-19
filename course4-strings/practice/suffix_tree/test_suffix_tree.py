#!/usr/bin/python3

import unittest

import suffix_tree

class SuffixTreeNodeTestCase(unittest.TestCase):

    def setUp(self):
        pass

    def tearDown(self):
        pass

    def test_constructor(self):
        label = 'test-label'

        node = suffix_tree.SuffixTree.Node(label)

        self.assertEqual(label, node._label)
        self.assertEqual({}, node._edges)

    def test_repr(self):
        label = 'test-label'

        node = suffix_tree.SuffixTree.Node(label)

        self.assertEqual(label + ': ' + str({}), repr(node))

class SuffixTreeConstructionTestCase(unittest.TestCase):

    def setUp(self):
        pass

    def tearDown(self):
        pass

    def assert_tree(self, expected_root, tree):
        tree_queue = []
        tree_queue.append(tree._root)
        expected_tree_queue = []
        expected_tree_queue.append(expected_root)

        while len(tree_queue) > 0:
            node = tree_queue.pop(0)
            expected_node = expected_tree_queue.pop(0)
            self.assertEqual(expected_node._label, node._label)

            for symbol, neighbor in node._edges.items():
                tree_queue.append(neighbor)
                expected_tree_queue.append(expected_node._edges[symbol])

    def test_empty_text(self):
        text = ''

        tree = suffix_tree.SuffixTree(text)

        expected_root = suffix_tree.SuffixTree.Node(None)
        expected_root._edges['$'] = suffix_tree.SuffixTree.Node('$')

        self.assert_tree(expected_root, tree)

    def test_a(self):
        text = 'a'

        tree = suffix_tree.SuffixTree(text)

        expected_root = suffix_tree.SuffixTree.Node(None)
        expected_root._edges['a'] = suffix_tree.SuffixTree.Node('a$')
        expected_root._edges['$'] = suffix_tree.SuffixTree.Node('$')

        self.assert_tree(expected_root, tree)

    def test_ab(self):
        text = 'ab'

        tree = suffix_tree.SuffixTree(text)

        expected_root = suffix_tree.SuffixTree.Node(None)
        expected_root._edges['a'] = suffix_tree.SuffixTree.Node('ab$')
        expected_root._edges['b'] = suffix_tree.SuffixTree.Node('b$')
        expected_root._edges['$'] = suffix_tree.SuffixTree.Node('$')

        self.assert_tree(expected_root, tree)

    def test_aca(self):
        text = 'aca'

        tree = suffix_tree.SuffixTree(text)

        expected_root = suffix_tree.SuffixTree.Node(None)
        node = suffix_tree.SuffixTree.Node('a')
        node._edges['c'] = suffix_tree.SuffixTree.Node('ca$')
        node._edges['$'] = suffix_tree.SuffixTree.Node('$')
        expected_root._edges['a'] = node
        expected_root._edges['c'] = suffix_tree.SuffixTree.Node('ca$')
        expected_root._edges['$'] = suffix_tree.SuffixTree.Node('$')

        self.assert_tree(expected_root, tree)

    def test_abac(self):
        text = 'abac'

        tree = suffix_tree.SuffixTree(text)

        expected_root = suffix_tree.SuffixTree.Node(None)
        node = suffix_tree.SuffixTree.Node('a')
        node._edges['b'] = suffix_tree.SuffixTree.Node('bac$')
        node._edges['c'] = suffix_tree.SuffixTree.Node('c$')
        expected_root._edges['a'] = node
        expected_root._edges['b'] = suffix_tree.SuffixTree.Node('bac$')
        expected_root._edges['c'] = suffix_tree.SuffixTree.Node('c$')
        expected_root._edges['$'] = suffix_tree.SuffixTree.Node('$')

        self.assert_tree(expected_root, tree)

    def test_abab(self):
        text = 'abab'

        tree = suffix_tree.SuffixTree(text)

        expected_root = suffix_tree.SuffixTree.Node(None)
        node = suffix_tree.SuffixTree.Node('ab')
        node._edges['a'] = suffix_tree.SuffixTree.Node('ab$')
        node._edges['$'] = suffix_tree.SuffixTree.Node('$')
        expected_root._edges['a'] = node
        node = suffix_tree.SuffixTree.Node('b')
        node._edges['a'] = suffix_tree.SuffixTree.Node('ab$')
        node._edges['$'] = suffix_tree.SuffixTree.Node('$')
        expected_root._edges['b'] = node
        expected_root._edges['$'] = suffix_tree.SuffixTree.Node('$')

        self.assert_tree(expected_root, tree)

    def test_ataaatg(self):
        text = 'ataaatg'

        tree = suffix_tree.SuffixTree(text)

        expected_root = suffix_tree.SuffixTree.Node(None)
        node = suffix_tree.SuffixTree.Node('a')
        child1 = suffix_tree.SuffixTree.Node('t')
        child1._edges['a'] = suffix_tree.SuffixTree.Node('aaatg$')
        child1._edges['g'] = suffix_tree.SuffixTree.Node('g$')
        node._edges['t'] = child1
        child2 = suffix_tree.SuffixTree.Node('a')
        child2._edges['a'] = suffix_tree.SuffixTree.Node('atg$')
        child2._edges['t'] = suffix_tree.SuffixTree.Node('tg$')
        node._edges['a'] = child2
        expected_root._edges['a'] = node
        node = suffix_tree.SuffixTree.Node('t')
        node._edges['a'] = suffix_tree.SuffixTree.Node('aaatg$')
        node._edges['g'] = suffix_tree.SuffixTree.Node('g$')
        expected_root._edges['t'] = node
        expected_root._edges['g'] = suffix_tree.SuffixTree.Node('g$')
        expected_root._edges['$'] = suffix_tree.SuffixTree.Node('$')

        self.assert_tree(expected_root, tree)

    def test_panamabananas(self):
        text = 'panamabananas'

        tree = suffix_tree.SuffixTree(text)

        expected_root = suffix_tree.SuffixTree.Node(None)
        expected_root._edges['p'] = suffix_tree.SuffixTree.Node(
                                                               'panamabananas$')
        node = suffix_tree.SuffixTree.Node('a')
        child_node = suffix_tree.SuffixTree.Node('na')
        child_node._edges['m'] = suffix_tree.SuffixTree.Node('mabananas$')
        child_node._edges['n'] = suffix_tree.SuffixTree.Node('nas$')
        child_node._edges['s'] = suffix_tree.SuffixTree.Node('s$')
        node._edges['n'] = child_node
        node._edges['m'] = suffix_tree.SuffixTree.Node('mabananas$')
        node._edges['b'] = suffix_tree.SuffixTree.Node('bananas$')
        node._edges['s'] = suffix_tree.SuffixTree.Node('s$')
        expected_root._edges['a'] = node
        node = suffix_tree.SuffixTree.Node('na')
        node._edges['m'] = suffix_tree.SuffixTree.Node('mabananas$')
        node._edges['n'] = suffix_tree.SuffixTree.Node('nas$')
        node._edges['s'] = suffix_tree.SuffixTree.Node('s$')
        expected_root._edges['n'] = node
        expected_root._edges['m'] = suffix_tree.SuffixTree.Node(
                                                                 'mabananas$')
        expected_root._edges['b'] = suffix_tree.SuffixTree.Node('bananas$')
        expected_root._edges['s'] = suffix_tree.SuffixTree.Node('s$')
        expected_root._edges['$'] = suffix_tree.SuffixTree.Node('$')

        self.assert_tree(expected_root, tree)

    def test_repr_on_empty_text(self):
        text = ''

        tree = suffix_tree.SuffixTree(text)

        self.assertEqual("None: {'$': $: {}}",
                         repr(tree))

class SuffixTreeFollowPathTestCase(unittest.TestCase):

    def setUp(self):
        pass

    def tearDown(self):
        pass

    def assert_node(self, expected_node, node):
        if expected_node is None:
            self.assertEqual(None, node)
            return

        queue = []
        queue.append(node)
        expected_queue = []
        expected_queue.append(expected_node)

        while len(queue) > 0:
            child = queue.pop(0)
            expected_child = expected_queue.pop(0)
            self.assertEqual(expected_child._label, child._label)

            for symbol, neighbor in child._edges.items():
                queue.append(neighbor)
                expected_queue.append(expected_child._edges[symbol])

    def assert_query(self, tree, query, expected_node, expected_offset):
        node, offset = tree.follow_path(query)

        self.assert_node(expected_node, node)
        self.assertEqual(expected_offset, offset)

    def test_empty_text(self):
        text = ''

        tree = suffix_tree.SuffixTree(text)

        query = ''
        expected_node = suffix_tree.SuffixTree.Node(None)
        expected_node._edges['$'] = suffix_tree.SuffixTree.Node('$')

        self.assert_query(tree, query, expected_node, None)

        query = 'a'
        expected_node = None

        self.assert_query(tree, query, expected_node, None)

        query = '$'
        expected_node = suffix_tree.SuffixTree.Node('$')

        self.assert_query(tree, query, expected_node, None)

    def test_a(self):
        text = 'a'

        tree = suffix_tree.SuffixTree(text)

        query = ''
        expected_node = suffix_tree.SuffixTree.Node(None)
        expected_node._edges['a'] = suffix_tree.SuffixTree.Node('a$')
        expected_node._edges['$'] = suffix_tree.SuffixTree.Node('$')

        self.assert_query(tree, query, expected_node, None)

        query = 'a'
        expected_node = suffix_tree.SuffixTree.Node('a$')

        self.assert_query(tree, query, expected_node, 1)

        query = 'a$'
        expected_node = suffix_tree.SuffixTree.Node('a$')

        self.assert_query(tree, query, expected_node, None)

        query = 'ab'
        expected_node = None

        self.assert_query(tree, query, expected_node, None)

        query = 'abc'
        expected_node = None

        self.assert_query(tree, query, expected_node, None)

        query = 'x'
        expected_node = None

        self.assert_query(tree, query, expected_node, None)

        query = '$'
        expected_node = suffix_tree.SuffixTree.Node('$')

        self.assert_query(tree, query, expected_node, None)

    def test_ab(self):
        text = 'ab'

        tree = suffix_tree.SuffixTree(text)

        query = ''
        expected_node = suffix_tree.SuffixTree.Node(None)
        expected_node._edges['a'] = suffix_tree.SuffixTree.Node('ab$')
        expected_node._edges['b'] = suffix_tree.SuffixTree.Node('b$')
        expected_node._edges['$'] = suffix_tree.SuffixTree.Node('$')

        self.assert_query(tree, query, expected_node, None)

        query = 'a'
        expected_node = suffix_tree.SuffixTree.Node('ab$')

        self.assert_query(tree, query, expected_node, 1)

        query = 'a$'
        expected_node = None

        self.assert_query(tree, query, expected_node, None)

        query = 'ab'
        expected_node = suffix_tree.SuffixTree.Node('ab$')

        self.assert_query(tree, query, expected_node, 2)

        query = 'abc'
        expected_node = None

        self.assert_query(tree, query, expected_node, None)

        query = 'x'
        expected_node = None

        self.assert_query(tree, query, expected_node, None)

        query = '$'
        expected_node = suffix_tree.SuffixTree.Node('$')

        self.assert_query(tree, query, expected_node, None)

    def test_ataaatg(self):
        text = 'ataaatg'

        tree = suffix_tree.SuffixTree(text)

        query = ''
        expected_node = suffix_tree.SuffixTree.Node(None)
        node = suffix_tree.SuffixTree.Node('a')
        child1 = suffix_tree.SuffixTree.Node('t')
        child1._edges['a'] = suffix_tree.SuffixTree.Node('aaatg$')
        child1._edges['g'] = suffix_tree.SuffixTree.Node('g$')
        node._edges['t'] = child1
        child2 = suffix_tree.SuffixTree.Node('a')
        child2._edges['a'] = suffix_tree.SuffixTree.Node('atg$')
        child2._edges['t'] = suffix_tree.SuffixTree.Node('tg$')
        node._edges['a'] = child2
        expected_node._edges['a'] = node
        node = suffix_tree.SuffixTree.Node('t')
        node._edges['a'] = suffix_tree.SuffixTree.Node('aaatg$')
        node._edges['g'] = suffix_tree.SuffixTree.Node('g$')
        expected_node._edges['t'] = node
        expected_node._edges['g'] = suffix_tree.SuffixTree.Node('g$')
        expected_node._edges['$'] = suffix_tree.SuffixTree.Node('$')

        self.assert_query(tree, query, expected_node, None)

        query = 'a'
        expected_node = suffix_tree.SuffixTree.Node('a')
        child1 = suffix_tree.SuffixTree.Node('t')
        child1._edges['a'] = suffix_tree.SuffixTree.Node('aaatg$')
        child1._edges['g'] = suffix_tree.SuffixTree.Node('g$')
        expected_node._edges['t'] = child1
        child2 = suffix_tree.SuffixTree.Node('a')
        child2._edges['a'] = suffix_tree.SuffixTree.Node('atg$')
        child2._edges['t'] = suffix_tree.SuffixTree.Node('tg$')
        expected_node._edges['a'] = child2

        self.assert_query(tree, query, expected_node, None)

        query = 'aa'
        expected_node = suffix_tree.SuffixTree.Node('a')
        expected_node._edges['a'] = suffix_tree.SuffixTree.Node('atg$')
        expected_node._edges['t'] = suffix_tree.SuffixTree.Node('tg$')

        self.assert_query(tree, query, expected_node, None)

        query = 'aaa'
        expected_node = suffix_tree.SuffixTree.Node('atg$')

        self.assert_query(tree, query, expected_node, 1)

        query = 'aaat'
        expected_node = suffix_tree.SuffixTree.Node('atg$')

        self.assert_query(tree, query, expected_node, 2)

        query = 'aaatg'
        expected_node = suffix_tree.SuffixTree.Node('atg$')

        self.assert_query(tree, query, expected_node, 3)

        query = 'aaatg$'
        expected_node = suffix_tree.SuffixTree.Node('atg$')

        self.assert_query(tree, query, expected_node, None)

        query = 'aaatg$x'
        expected_node = None

        self.assert_query(tree, query, expected_node, None)

        query = 'aat'
        expected_node = suffix_tree.SuffixTree.Node('tg$')

        self.assert_query(tree, query, expected_node, 1)

        query = 'aatg'
        expected_node = suffix_tree.SuffixTree.Node('tg$')

        self.assert_query(tree, query, expected_node, 2)

        query = 'aatg$'
        expected_node = suffix_tree.SuffixTree.Node('tg$')

        self.assert_query(tree, query, expected_node, None)

        query = 'aatg$x'
        expected_node = None

        self.assert_query(tree, query, expected_node, None)

        query = 'at'
        expected_node = suffix_tree.SuffixTree.Node('t')
        expected_node._edges['a'] = suffix_tree.SuffixTree.Node('aaatg$')
        expected_node._edges['g'] = suffix_tree.SuffixTree.Node('g$')

        self.assert_query(tree, query, expected_node, None)

        query = 'ata'
        expected_node = suffix_tree.SuffixTree.Node('aaatg$')

        self.assert_query(tree, query, expected_node, 1)

        query = 'ataa'
        expected_node = suffix_tree.SuffixTree.Node('aaatg$')

        self.assert_query(tree, query, expected_node, 2)

        query = 'ataaa'
        expected_node = suffix_tree.SuffixTree.Node('aaatg$')

        self.assert_query(tree, query, expected_node, 3)

        query = 'ataaat'
        expected_node = suffix_tree.SuffixTree.Node('aaatg$')

        self.assert_query(tree, query, expected_node, 4)

        query = 'ataaatg'
        expected_node = suffix_tree.SuffixTree.Node('aaatg$')

        self.assert_query(tree, query, expected_node, 5)

        query = 'ataaatg$'
        expected_node = suffix_tree.SuffixTree.Node('aaatg$')

        self.assert_query(tree, query, expected_node, None)

        query = 'ataaatg$x'
        expected_node = None

        self.assert_query(tree, query, expected_node, None)

        query = 'atg'
        expected_node = suffix_tree.SuffixTree.Node('g$')

        self.assert_query(tree, query, expected_node, 1)

        query = 'atg$'
        expected_node = suffix_tree.SuffixTree.Node('g$')

        self.assert_query(tree, query, expected_node, None)

        query = 'atg$x'
        expected_node = None

        self.assert_query(tree, query, expected_node, None)

        query = 't'
        expected_node = suffix_tree.SuffixTree.Node('t')
        expected_node._edges['a'] = suffix_tree.SuffixTree.Node('aaatg$')
        expected_node._edges['g'] = suffix_tree.SuffixTree.Node('g$')

        self.assert_query(tree, query, expected_node, None)

        query = 'ta'
        expected_node = suffix_tree.SuffixTree.Node('aaatg$')

        self.assert_query(tree, query, expected_node, 1)

        query = 'taa'
        expected_node = suffix_tree.SuffixTree.Node('aaatg$')

        self.assert_query(tree, query, expected_node, 2)

        query = 'taaa'
        expected_node = suffix_tree.SuffixTree.Node('aaatg$')

        self.assert_query(tree, query, expected_node, 3)

        query = 'taaat'
        expected_node = suffix_tree.SuffixTree.Node('aaatg$')

        self.assert_query(tree, query, expected_node, 4)

        query = 'taaatg'
        expected_node = suffix_tree.SuffixTree.Node('aaatg$')

        self.assert_query(tree, query, expected_node, 5)

        query = 'taaatg$'
        expected_node = suffix_tree.SuffixTree.Node('aaatg$')

        self.assert_query(tree, query, expected_node, None)

        query = 'taaatg$x'
        expected_node = None

        self.assert_query(tree, query, expected_node, None)

        query = 'tg'
        expected_node = suffix_tree.SuffixTree.Node('g$')

        self.assert_query(tree, query, expected_node, 1)

        query = 'tg$'
        expected_node = suffix_tree.SuffixTree.Node('g$')

        self.assert_query(tree, query, expected_node, None)

        query = 'tg$x'
        expected_node = None

        self.assert_query(tree, query, expected_node, None)

        query = 'g'
        expected_node = suffix_tree.SuffixTree.Node('g$')

        self.assert_query(tree, query, expected_node, 1)

        query = 'g$'
        expected_node = suffix_tree.SuffixTree.Node('g$')

        self.assert_query(tree, query, expected_node, None)

        query = 'g$x'
        expected_node = None

        self.assert_query(tree, query, expected_node, None)

        query = '$'
        expected_node = suffix_tree.SuffixTree.Node('$')

        self.assert_query(tree, query, expected_node, None)

        query = '$x'
        expected_node = None

        self.assert_query(tree, query, expected_node, None)

        query = 'x'
        expected_node = None

        self.assert_query(tree, query, expected_node, None)

class SuffixTreeHasSubstringTestCase(unittest.TestCase):

    def setUp(self):
        pass

    def tearDown(self):
        pass

    def assert_query(self, tree, query, expected_result):
        result = tree.has_substring(query)

        self.assertEqual(expected_result, result)

    def test_empty_text(self):
        text = ''

        tree = suffix_tree.SuffixTree(text)

        self.assert_query(tree, '', True)
        self.assert_query(tree, 'a', False)
        self.assert_query(tree, '$', True)

    def test_a(self):
        text = 'a'

        tree = suffix_tree.SuffixTree(text)

        self.assert_query(tree, '', True)
        self.assert_query(tree, 'a', True)
        self.assert_query(tree, 'a$', True)
        self.assert_query(tree, 'ab', False)
        self.assert_query(tree, 'abc', False)
        self.assert_query(tree, 'x', False)
        self.assert_query(tree, '$', True)

    def test_ab(self):
        text = 'ab'

        tree = suffix_tree.SuffixTree(text)

        self.assert_query(tree, '', True)
        self.assert_query(tree, 'a', True)
        self.assert_query(tree, 'a$', False)
        self.assert_query(tree, 'ab', True)
        self.assert_query(tree, 'abc', False)
        self.assert_query(tree, 'x', False)
        self.assert_query(tree, '$', True)

    def test_ataaatg(self):
        text = 'ataaatg'

        tree = suffix_tree.SuffixTree(text)

        self.assert_query(tree, '', True)
        self.assert_query(tree, 'a', True)
        self.assert_query(tree, 'aa', True)
        self.assert_query(tree, 'aaa', True)
        self.assert_query(tree, 'aaat', True)
        self.assert_query(tree, 'aaatg', True)
        self.assert_query(tree, 'aaatg$', True)
        self.assert_query(tree, 'aaatg$x', False)
        self.assert_query(tree, 'aat', True)
        self.assert_query(tree, 'aatg', True)
        self.assert_query(tree, 'aatg$', True)
        self.assert_query(tree, 'aatg$x', False)
        self.assert_query(tree, 'at', True)
        self.assert_query(tree, 'ata', True)
        self.assert_query(tree, 'ataa', True)
        self.assert_query(tree, 'ataaa', True)
        self.assert_query(tree, 'ataaat', True)
        self.assert_query(tree, 'ataaatg', True)
        self.assert_query(tree, 'ataaatg$', True)
        self.assert_query(tree, 'ataaatg$x', False)
        self.assert_query(tree, 'atg', True)
        self.assert_query(tree, 'atg$', True)
        self.assert_query(tree, 'atg$x', False)
        self.assert_query(tree, 't', True)
        self.assert_query(tree, 'ta', True)
        self.assert_query(tree, 'taa', True)
        self.assert_query(tree, 'taaa', True)
        self.assert_query(tree, 'taaat', True)
        self.assert_query(tree, 'taaatg', True)
        self.assert_query(tree, 'taaatg$', True)
        self.assert_query(tree, 'taaatg$x', False)
        self.assert_query(tree, 'tg', True)
        self.assert_query(tree, 'tg$', True)
        self.assert_query(tree, 'tg$x', False)
        self.assert_query(tree, 'g', True)
        self.assert_query(tree, 'g$', True)
        self.assert_query(tree, 'g$x', False)
        self.assert_query(tree, '$', True)
        self.assert_query(tree, '$x', False)
        self.assert_query(tree, 'x', False)

class SuffixTreeHasSuffixTestCase(unittest.TestCase):

    def setUp(self):
        pass

    def tearDown(self):
        pass

    def assert_query(self, tree, query, expected_result):
        result = tree.has_suffix(query)

        self.assertEqual(expected_result, result)

    def test_empty_text(self):
        text = ''

        tree = suffix_tree.SuffixTree(text)

        self.assert_query(tree, '', True)
        self.assert_query(tree, 'a', False)
        self.assert_query(tree, '$', False)

    def test_a(self):
        text = 'a'

        tree = suffix_tree.SuffixTree(text)

        self.assert_query(tree, '', True)
        self.assert_query(tree, 'a', True)
        self.assert_query(tree, 'a$', False)
        self.assert_query(tree, 'ab', False)
        self.assert_query(tree, 'abc', False)
        self.assert_query(tree, 'x', False)
        self.assert_query(tree, '$', False)

    def test_ab(self):
        text = 'ab'

        tree = suffix_tree.SuffixTree(text)

        self.assert_query(tree, '', True)
        self.assert_query(tree, 'a', False)
        self.assert_query(tree, 'a$', False)
        self.assert_query(tree, 'ab', True)
        self.assert_query(tree, 'abc', False)
        self.assert_query(tree, 'x', False)
        self.assert_query(tree, '$', False)

    def test_ataaatg(self):
        text = 'ataaatg'

        tree = suffix_tree.SuffixTree(text)

        self.assert_query(tree, '', True)
        self.assert_query(tree, 'a', False)
        self.assert_query(tree, 'aa', False)
        self.assert_query(tree, 'aaa', False)
        self.assert_query(tree, 'aaat', False)
        self.assert_query(tree, 'aaatg', True)
        self.assert_query(tree, 'aaatg$', False)
        self.assert_query(tree, 'aaatg$x', False)
        self.assert_query(tree, 'aat', False)
        self.assert_query(tree, 'aatg', True)
        self.assert_query(tree, 'aatg$', False)
        self.assert_query(tree, 'aatg$x', False)
        self.assert_query(tree, 'at', False)
        self.assert_query(tree, 'ata', False)
        self.assert_query(tree, 'ataa', False)
        self.assert_query(tree, 'ataaa', False)
        self.assert_query(tree, 'ataaat', False)
        self.assert_query(tree, 'ataaatg', True)
        self.assert_query(tree, 'ataaatg$', False)
        self.assert_query(tree, 'ataaatg$x', False)
        self.assert_query(tree, 'atg', True)
        self.assert_query(tree, 'atg$', False)
        self.assert_query(tree, 'atg$x', False)
        self.assert_query(tree, 't', False)
        self.assert_query(tree, 'ta', False)
        self.assert_query(tree, 'taa', False)
        self.assert_query(tree, 'taaa', False)
        self.assert_query(tree, 'taaat', False)
        self.assert_query(tree, 'taaatg', True)
        self.assert_query(tree, 'taaatg$', False)
        self.assert_query(tree, 'taaatg$x', False)
        self.assert_query(tree, 'tg', True)
        self.assert_query(tree, 'tg$', False)
        self.assert_query(tree, 'tg$x', False)
        self.assert_query(tree, 'g', True)
        self.assert_query(tree, 'g$', False)
        self.assert_query(tree, 'g$x', False)
        self.assert_query(tree, '$', False)
        self.assert_query(tree, '$x', False)
        self.assert_query(tree, 'x', False)

class PositionalSuffixTreeNodeTestCase(unittest.TestCase):

    def setUp(self):
        pass

    def tearDown(self):
        pass

    def test_constructor(self):
        start = 123
        length = 5

        node = suffix_tree.PositionalSuffixTree.Node(start, length)

        self.assertEqual(start, node._start)
        self.assertEqual(length, node._length)
        self.assertEqual({}, node._edges)

    def test_repr(self):
        start = 123
        length = 5

        node = suffix_tree.PositionalSuffixTree.Node(start, length)

        self.assertEqual('(' + str(start) + ', ' + str(length) + '): ' +
                         str({}),
                         repr(node))

class PositionalSuffixTreeConstructionTestCase(unittest.TestCase):

    def setUp(self):
        pass

    def tearDown(self):
        pass

    def assert_tree(self, expected_root, tree):
        tree_queue = []
        tree_queue.append(tree._root)
        expected_tree_queue = []
        expected_tree_queue.append(expected_root)

        while len(tree_queue) > 0:
            node = tree_queue.pop(0)
            expected_node = expected_tree_queue.pop(0)
            self.assertEqual(expected_node._start, node._start)
            self.assertEqual(expected_node._length, node._length)

            for symbol, neighbor in node._edges.items():
                tree_queue.append(neighbor)
                expected_tree_queue.append(expected_node._edges[symbol])

    def test_empty_text(self):
        text = ''

        tree = suffix_tree.PositionalSuffixTree(text)

        expected_root = suffix_tree.PositionalSuffixTree.Node(None, None)
        expected_root._edges['$'] = suffix_tree.PositionalSuffixTree.Node(0, 1)

        self.assert_tree(expected_root, tree)

    def test_a(self):
        text = 'a'

        tree = suffix_tree.PositionalSuffixTree(text)

        expected_root = suffix_tree.PositionalSuffixTree.Node(None, None)
        expected_root._edges['a'] = suffix_tree.PositionalSuffixTree.Node(0, 2)
        expected_root._edges['$'] = suffix_tree.PositionalSuffixTree.Node(1, 1)

        self.assert_tree(expected_root, tree)

    def test_ab(self):
        text = 'ab'

        tree = suffix_tree.PositionalSuffixTree(text)

        expected_root = suffix_tree.PositionalSuffixTree.Node(None, None)
        expected_root._edges['a'] = suffix_tree.PositionalSuffixTree.Node(0, 3)
        expected_root._edges['b'] = suffix_tree.PositionalSuffixTree.Node(1, 2)
        expected_root._edges['$'] = suffix_tree.PositionalSuffixTree.Node(2, 1)

        self.assert_tree(expected_root, tree)

    def test_aca(self):
        text = 'aca'

        tree = suffix_tree.PositionalSuffixTree(text)

        expected_root = suffix_tree.PositionalSuffixTree.Node(None, None)
        node = suffix_tree.PositionalSuffixTree.Node(0, 1)
        node._edges['c'] = suffix_tree.PositionalSuffixTree.Node(1, 3)
        node._edges['$'] = suffix_tree.PositionalSuffixTree.Node(3, 1)
        expected_root._edges['a'] = node
        expected_root._edges['c'] = suffix_tree.PositionalSuffixTree.Node(1, 3)
        expected_root._edges['$'] = suffix_tree.PositionalSuffixTree.Node(3, 1)

        self.assert_tree(expected_root, tree)

    def test_abac(self):
        text = 'abac'

        tree = suffix_tree.PositionalSuffixTree(text)

        expected_root = suffix_tree.PositionalSuffixTree.Node(None, None)
        node = suffix_tree.PositionalSuffixTree.Node(0, 1)
        node._edges['b'] = suffix_tree.PositionalSuffixTree.Node(1, 4)
        node._edges['c'] = suffix_tree.PositionalSuffixTree.Node(3, 2)
        expected_root._edges['a'] = node
        expected_root._edges['b'] = suffix_tree.PositionalSuffixTree.Node(1, 4)
        expected_root._edges['c'] = suffix_tree.PositionalSuffixTree.Node(3, 2)
        expected_root._edges['$'] = suffix_tree.PositionalSuffixTree.Node(4, 1)

        self.assert_tree(expected_root, tree)

    def test_abab(self):
        text = 'abab'

        tree = suffix_tree.PositionalSuffixTree(text)

        expected_root = suffix_tree.PositionalSuffixTree.Node(None, None)
        node = suffix_tree.PositionalSuffixTree.Node(0, 2)
        node._edges['a'] = suffix_tree.PositionalSuffixTree.Node(2, 3)
        node._edges['$'] = suffix_tree.PositionalSuffixTree.Node(4, 1)
        expected_root._edges['a'] = node
        node = suffix_tree.PositionalSuffixTree.Node(1, 1)
        node._edges['a'] = suffix_tree.PositionalSuffixTree.Node(2, 3)
        node._edges['$'] = suffix_tree.PositionalSuffixTree.Node(4, 1)
        expected_root._edges['b'] = node
        expected_root._edges['$'] = suffix_tree.PositionalSuffixTree.Node(4, 1)

        self.assert_tree(expected_root, tree)

    def test_ataaatg(self):
        text = 'ataaatg'

        tree = suffix_tree.PositionalSuffixTree(text)

        expected_root = suffix_tree.PositionalSuffixTree.Node(None, None)
        node = suffix_tree.PositionalSuffixTree.Node(0, 1)
        child1 = suffix_tree.PositionalSuffixTree.Node(1, 1)
        child1._edges['a'] = suffix_tree.PositionalSuffixTree.Node(2, 6)
        child1._edges['g'] = suffix_tree.PositionalSuffixTree.Node(6, 2)
        node._edges['t'] = child1
        child2 = suffix_tree.PositionalSuffixTree.Node(3, 1)
        child2._edges['a'] = suffix_tree.PositionalSuffixTree.Node(4, 4)
        child2._edges['t'] = suffix_tree.PositionalSuffixTree.Node(5, 3)
        node._edges['a'] = child2
        expected_root._edges['a'] = node
        node = suffix_tree.PositionalSuffixTree.Node(1, 1)
        node._edges['a'] = suffix_tree.PositionalSuffixTree.Node(2, 6)
        node._edges['g'] = suffix_tree.PositionalSuffixTree.Node(6, 2)
        expected_root._edges['t'] = node
        expected_root._edges['g'] = suffix_tree.PositionalSuffixTree.Node(6, 2)
        expected_root._edges['$'] = suffix_tree.PositionalSuffixTree.Node(7, 1)

        self.assert_tree(expected_root, tree)

    def test_panamabananas(self):
        text = 'panamabananas'

        tree = suffix_tree.PositionalSuffixTree(text)

        expected_root = suffix_tree.PositionalSuffixTree.Node(None, None)
        expected_root._edges['p'] = suffix_tree.PositionalSuffixTree.Node(0, 14)

        node = suffix_tree.PositionalSuffixTree.Node(1, 1)
        child_node = suffix_tree.PositionalSuffixTree.Node(2, 2)
        child_node._edges['m'] = suffix_tree.PositionalSuffixTree.Node(4, 10)
        child_node._edges['n'] = suffix_tree.PositionalSuffixTree.Node(10, 4)
        child_node._edges['s'] = suffix_tree.PositionalSuffixTree.Node(12, 2)
        node._edges['n'] = child_node
        node._edges['m'] = suffix_tree.PositionalSuffixTree.Node(4, 10)
        node._edges['b'] = suffix_tree.PositionalSuffixTree.Node(6, 8)
        node._edges['s'] = suffix_tree.PositionalSuffixTree.Node(12, 2)
        expected_root._edges['a'] = node
        node = suffix_tree.PositionalSuffixTree.Node(2, 2)
        node._edges['m'] = suffix_tree.PositionalSuffixTree.Node(4, 10)
        node._edges['n'] = suffix_tree.PositionalSuffixTree.Node(10, 4)
        node._edges['s'] = suffix_tree.PositionalSuffixTree.Node(12, 2)
        expected_root._edges['n'] = node
        expected_root._edges['m'] = suffix_tree.PositionalSuffixTree.Node(4, 10)
        expected_root._edges['b'] = suffix_tree.PositionalSuffixTree.Node(6, 8)
        expected_root._edges['s'] = suffix_tree.PositionalSuffixTree.Node(12, 2)
        expected_root._edges['$'] = suffix_tree.PositionalSuffixTree.Node(13, 1)

        self.assert_tree(expected_root, tree)

    def test_repr_on_empty_text(self):
        text = ''

        tree = suffix_tree.PositionalSuffixTree(text)

        self.assertEqual("(None, None): {'$': (0, 1): {}}",
                         repr(tree))

class PositionalSuffixTreeFollowPathTestCase(unittest.TestCase):

    def setUp(self):
        pass

    def tearDown(self):
        pass

    def assert_node(self, expected_node, node):
        if expected_node is None:
            self.assertEqual(None, node)
            return

        queue = []
        queue.append(node)
        expected_queue = []
        expected_queue.append(expected_node)

        while len(queue) > 0:
            child = queue.pop(0)
            expected_child = expected_queue.pop(0)
            self.assertEqual(expected_child._start, child._start)
            self.assertEqual(expected_child._length, child._length)

            for symbol, neighbor in child._edges.items():
                queue.append(neighbor)
                expected_queue.append(expected_child._edges[symbol])

    def assert_query(self, tree, query, expected_node, expected_offset):
        node, offset = tree.follow_path(query)

        self.assert_node(expected_node, node)
        self.assertEqual(expected_offset, offset)

    def test_empty_text(self):
        text = ''

        tree = suffix_tree.PositionalSuffixTree(text)

        query = ''
        expected_node = suffix_tree.PositionalSuffixTree.Node(None, None)
        expected_node._edges['$'] = suffix_tree.PositionalSuffixTree.Node(0, 1)

        self.assert_query(tree, query, expected_node, None)

        query = 'a'
        expected_node = None

        self.assert_query(tree, query, expected_node, None)

        query = '$'
        expected_node = suffix_tree.PositionalSuffixTree.Node(0, 1)

        self.assert_query(tree, query, expected_node, None)

    def test_a(self):
        text = 'a'

        tree = suffix_tree.PositionalSuffixTree(text)

        query = ''
        expected_node = suffix_tree.PositionalSuffixTree.Node(None, None)
        expected_node._edges['a'] = suffix_tree.PositionalSuffixTree.Node(0, 2)
        expected_node._edges['$'] = suffix_tree.PositionalSuffixTree.Node(1, 1)

        self.assert_query(tree, query, expected_node, None)

        query = 'a'
        expected_node = suffix_tree.PositionalSuffixTree.Node(0, 2)

        self.assert_query(tree, query, expected_node, 1)

        query = 'a$'
        expected_node = suffix_tree.PositionalSuffixTree.Node(0, 2)

        self.assert_query(tree, query, expected_node, None)

        query = 'ab'
        expected_node = None

        self.assert_query(tree, query, expected_node, None)

        query = 'abc'
        expected_node = None

        self.assert_query(tree, query, expected_node, None)

        query = 'x'
        expected_node = None

        self.assert_query(tree, query, expected_node, None)

        query = '$'
        expected_node = suffix_tree.PositionalSuffixTree.Node(1, 1)

        self.assert_query(tree, query, expected_node, None)

    def test_ab(self):
        text = 'ab'

        tree = suffix_tree.PositionalSuffixTree(text)

        query = ''
        expected_node = suffix_tree.PositionalSuffixTree.Node(None, None)
        expected_node._edges['a'] = suffix_tree.PositionalSuffixTree.Node(0, 3)
        expected_node._edges['b'] = suffix_tree.PositionalSuffixTree.Node(1, 2)
        expected_node._edges['$'] = suffix_tree.PositionalSuffixTree.Node(2, 1)

        self.assert_query(tree, query, expected_node, None)

        query = 'a'
        expected_node = suffix_tree.PositionalSuffixTree.Node(0, 3)

        self.assert_query(tree, query, expected_node, 1)

        query = 'a$'
        expected_node = None

        self.assert_query(tree, query, expected_node, None)

        query = 'ab'
        expected_node = suffix_tree.PositionalSuffixTree.Node(0, 3)

        self.assert_query(tree, query, expected_node, 2)

        query = 'abc'
        expected_node = None

        self.assert_query(tree, query, expected_node, None)

        query = 'x'
        expected_node = None

        self.assert_query(tree, query, expected_node, None)

        query = '$'
        expected_node = suffix_tree.PositionalSuffixTree.Node(2, 1)

        self.assert_query(tree, query, expected_node, None)

    def test_ataaatg(self):
        text = 'ataaatg'

        tree = suffix_tree.PositionalSuffixTree(text)

        query = ''
        expected_node = suffix_tree.PositionalSuffixTree.Node(None, None)
        node = suffix_tree.PositionalSuffixTree.Node(0, 1)
        child1 = suffix_tree.PositionalSuffixTree.Node(1, 1)
        child1._edges['a'] = suffix_tree.PositionalSuffixTree.Node(2, 6)
        child1._edges['g'] = suffix_tree.PositionalSuffixTree.Node(6, 2)
        node._edges['t'] = child1
        child2 = suffix_tree.PositionalSuffixTree.Node(3, 1)
        child2._edges['a'] = suffix_tree.PositionalSuffixTree.Node(4, 4)
        child2._edges['t'] = suffix_tree.PositionalSuffixTree.Node(5, 3)
        node._edges['a'] = child2
        expected_node._edges['a'] = node
        node = suffix_tree.PositionalSuffixTree.Node(1, 1)
        node._edges['a'] = suffix_tree.PositionalSuffixTree.Node(2, 6)
        node._edges['g'] = suffix_tree.PositionalSuffixTree.Node(6, 2)
        expected_node._edges['t'] = node
        expected_node._edges['g'] = suffix_tree.PositionalSuffixTree.Node(6, 2)
        expected_node._edges['$'] = suffix_tree.PositionalSuffixTree.Node(7, 1)

        self.assert_query(tree, query, expected_node, None)

        query = 'a'
        expected_node = suffix_tree.PositionalSuffixTree.Node(0, 1)
        child1 = suffix_tree.PositionalSuffixTree.Node(1, 1)
        child1._edges['a'] = suffix_tree.PositionalSuffixTree.Node(2, 6)
        child1._edges['g'] = suffix_tree.PositionalSuffixTree.Node(6, 2)
        expected_node._edges['t'] = child1
        child2 = suffix_tree.PositionalSuffixTree.Node(3, 1)
        child2._edges['a'] = suffix_tree.PositionalSuffixTree.Node(4, 4)
        child2._edges['t'] = suffix_tree.PositionalSuffixTree.Node(5, 3)
        expected_node._edges['a'] = child2

        self.assert_query(tree, query, expected_node, None)

        query = 'aa'
        expected_node = suffix_tree.PositionalSuffixTree.Node(3, 1)
        expected_node._edges['a'] = suffix_tree.PositionalSuffixTree.Node(4, 4)
        expected_node._edges['t'] = suffix_tree.PositionalSuffixTree.Node(5, 3)

        self.assert_query(tree, query, expected_node, None)

        query = 'aaa'
        expected_node = suffix_tree.PositionalSuffixTree.Node(4, 4)

        self.assert_query(tree, query, expected_node, 1)

        query = 'aaat'
        expected_node = suffix_tree.PositionalSuffixTree.Node(4, 4)

        self.assert_query(tree, query, expected_node, 2)

        query = 'aaatg'
        expected_node = suffix_tree.PositionalSuffixTree.Node(4, 4)

        self.assert_query(tree, query, expected_node, 3)

        query = 'aaatg$'
        expected_node = suffix_tree.PositionalSuffixTree.Node(4, 4)

        self.assert_query(tree, query, expected_node, None)

        query = 'aaatg$x'
        expected_node = None

        self.assert_query(tree, query, expected_node, None)

        query = 'aat'
        expected_node = suffix_tree.PositionalSuffixTree.Node(5, 3)

        self.assert_query(tree, query, expected_node, 1)

        query = 'aatg'
        expected_node = suffix_tree.PositionalSuffixTree.Node(5, 3)

        self.assert_query(tree, query, expected_node, 2)

        query = 'aatg$'
        expected_node = suffix_tree.PositionalSuffixTree.Node(5, 3)

        self.assert_query(tree, query, expected_node, None)

        query = 'aatg$x'
        expected_node = None

        self.assert_query(tree, query, expected_node, None)

        query = 'at'
        expected_node = suffix_tree.PositionalSuffixTree.Node(1, 1)
        expected_node._edges['a'] = suffix_tree.PositionalSuffixTree.Node(2, 6)
        expected_node._edges['g'] = suffix_tree.PositionalSuffixTree.Node(6, 2)

        self.assert_query(tree, query, expected_node, None)

        query = 'ata'
        expected_node = suffix_tree.PositionalSuffixTree.Node(2, 6)

        self.assert_query(tree, query, expected_node, 1)

        query = 'ataa'
        expected_node = suffix_tree.PositionalSuffixTree.Node(2, 6)

        self.assert_query(tree, query, expected_node, 2)

        query = 'ataaa'
        expected_node = suffix_tree.PositionalSuffixTree.Node(2, 6)

        self.assert_query(tree, query, expected_node, 3)

        query = 'ataaat'
        expected_node = suffix_tree.PositionalSuffixTree.Node(2, 6)

        self.assert_query(tree, query, expected_node, 4)

        query = 'ataaatg'
        expected_node = suffix_tree.PositionalSuffixTree.Node(2, 6)

        self.assert_query(tree, query, expected_node, 5)

        query = 'ataaatg$'
        expected_node = suffix_tree.PositionalSuffixTree.Node(2, 6)

        self.assert_query(tree, query, expected_node, None)

        query = 'ataaatg$x'
        expected_node = None

        self.assert_query(tree, query, expected_node, None)

        query = 'atg'
        expected_node = suffix_tree.PositionalSuffixTree.Node(6, 2)

        self.assert_query(tree, query, expected_node, 1)

        query = 'atg$'
        expected_node = suffix_tree.PositionalSuffixTree.Node(6, 2)

        self.assert_query(tree, query, expected_node, None)

        query = 'atg$x'
        expected_node = None

        self.assert_query(tree, query, expected_node, None)

        query = 't'
        expected_node = suffix_tree.PositionalSuffixTree.Node(1, 1)
        expected_node._edges['a'] = suffix_tree.PositionalSuffixTree.Node(2, 6)
        expected_node._edges['g'] = suffix_tree.PositionalSuffixTree.Node(6, 2)

        self.assert_query(tree, query, expected_node, None)

        query = 'ta'
        expected_node = suffix_tree.PositionalSuffixTree.Node(2, 6)

        self.assert_query(tree, query, expected_node, 1)

        query = 'taa'
        expected_node = suffix_tree.PositionalSuffixTree.Node(2, 6)

        self.assert_query(tree, query, expected_node, 2)

        query = 'taaa'
        expected_node = suffix_tree.PositionalSuffixTree.Node(2, 6)

        self.assert_query(tree, query, expected_node, 3)

        query = 'taaat'
        expected_node = suffix_tree.PositionalSuffixTree.Node(2, 6)

        self.assert_query(tree, query, expected_node, 4)

        query = 'taaatg'
        expected_node = suffix_tree.PositionalSuffixTree.Node(2, 6)

        self.assert_query(tree, query, expected_node, 5)

        query = 'taaatg$'
        expected_node = suffix_tree.PositionalSuffixTree.Node(2, 6)

        self.assert_query(tree, query, expected_node, None)

        query = 'taaatg$x'
        expected_node = None

        self.assert_query(tree, query, expected_node, None)

        query = 'tg'
        expected_node = suffix_tree.PositionalSuffixTree.Node(6, 2)

        self.assert_query(tree, query, expected_node, 1)

        query = 'tg$'
        expected_node = suffix_tree.PositionalSuffixTree.Node(6, 2)

        self.assert_query(tree, query, expected_node, None)

        query = 'tg$x'
        expected_node = None

        self.assert_query(tree, query, expected_node, None)

        query = 'g'
        expected_node = suffix_tree.PositionalSuffixTree.Node(6, 2)

        self.assert_query(tree, query, expected_node, 1)

        query = 'g$'
        expected_node = suffix_tree.PositionalSuffixTree.Node(6, 2)

        self.assert_query(tree, query, expected_node, None)

        query = 'g$x'
        expected_node = None

        self.assert_query(tree, query, expected_node, None)

        query = '$'
        expected_node = suffix_tree.PositionalSuffixTree.Node(7, 1)

        self.assert_query(tree, query, expected_node, None)

        query = '$x'
        expected_node = None

        self.assert_query(tree, query, expected_node, None)

        query = 'x'
        expected_node = None

        self.assert_query(tree, query, expected_node, None)

class PositionalSuffixTreeHasSubstringTestCase(unittest.TestCase):

    def setUp(self):
        pass

    def tearDown(self):
        pass

    def assert_query(self, tree, query, expected_result):
        result = tree.has_substring(query)

        self.assertEqual(expected_result, result)

    def test_empty_text(self):
        text = ''

        tree = suffix_tree.PositionalSuffixTree(text)

        self.assert_query(tree, '', True)
        self.assert_query(tree, 'a', False)
        self.assert_query(tree, '$', True)

    def test_a(self):
        text = 'a'

        tree = suffix_tree.PositionalSuffixTree(text)

        self.assert_query(tree, '', True)
        self.assert_query(tree, 'a', True)
        self.assert_query(tree, 'a$', True)
        self.assert_query(tree, 'ab', False)
        self.assert_query(tree, 'abc', False)
        self.assert_query(tree, 'x', False)
        self.assert_query(tree, '$', True)

    def test_ab(self):
        text = 'ab'

        tree = suffix_tree.PositionalSuffixTree(text)

        self.assert_query(tree, '', True)
        self.assert_query(tree, 'a', True)
        self.assert_query(tree, 'a$', False)
        self.assert_query(tree, 'ab', True)
        self.assert_query(tree, 'abc', False)
        self.assert_query(tree, 'x', False)
        self.assert_query(tree, '$', True)

    def test_ataaatg(self):
        text = 'ataaatg'

        tree = suffix_tree.PositionalSuffixTree(text)

        self.assert_query(tree, '', True)
        self.assert_query(tree, 'a', True)
        self.assert_query(tree, 'aa', True)
        self.assert_query(tree, 'aaa', True)
        self.assert_query(tree, 'aaat', True)
        self.assert_query(tree, 'aaatg', True)
        self.assert_query(tree, 'aaatg$', True)
        self.assert_query(tree, 'aaatg$x', False)
        self.assert_query(tree, 'aat', True)
        self.assert_query(tree, 'aatg', True)
        self.assert_query(tree, 'aatg$', True)
        self.assert_query(tree, 'aatg$x', False)
        self.assert_query(tree, 'at', True)
        self.assert_query(tree, 'ata', True)
        self.assert_query(tree, 'ataa', True)
        self.assert_query(tree, 'ataaa', True)
        self.assert_query(tree, 'ataaat', True)
        self.assert_query(tree, 'ataaatg', True)
        self.assert_query(tree, 'ataaatg$', True)
        self.assert_query(tree, 'ataaatg$x', False)
        self.assert_query(tree, 'atg', True)
        self.assert_query(tree, 'atg$', True)
        self.assert_query(tree, 'atg$x', False)
        self.assert_query(tree, 't', True)
        self.assert_query(tree, 'ta', True)
        self.assert_query(tree, 'taa', True)
        self.assert_query(tree, 'taaa', True)
        self.assert_query(tree, 'taaat', True)
        self.assert_query(tree, 'taaatg', True)
        self.assert_query(tree, 'taaatg$', True)
        self.assert_query(tree, 'taaatg$x', False)
        self.assert_query(tree, 'tg', True)
        self.assert_query(tree, 'tg$', True)
        self.assert_query(tree, 'tg$x', False)
        self.assert_query(tree, 'g', True)
        self.assert_query(tree, 'g$', True)
        self.assert_query(tree, 'g$x', False)
        self.assert_query(tree, '$', True)
        self.assert_query(tree, '$x', False)
        self.assert_query(tree, 'x', False)

class PositionalSuffixTreeHasSuffixTestCase(unittest.TestCase):

    def setUp(self):
        pass

    def tearDown(self):
        pass

    def assert_query(self, tree, query, expected_result):
        result = tree.has_suffix(query)

        self.assertEqual(expected_result, result)

    def test_empty_text(self):
        text = ''

        tree = suffix_tree.PositionalSuffixTree(text)

        self.assert_query(tree, '', True)
        self.assert_query(tree, 'a', False)
        self.assert_query(tree, '$', False)

    def test_a(self):
        text = 'a'

        tree = suffix_tree.PositionalSuffixTree(text)

        self.assert_query(tree, '', True)
        self.assert_query(tree, 'a', True)
        self.assert_query(tree, 'a$', False)
        self.assert_query(tree, 'ab', False)
        self.assert_query(tree, 'abc', False)
        self.assert_query(tree, 'x', False)
        self.assert_query(tree, '$', False)

    def test_ab(self):
        text = 'ab'

        tree = suffix_tree.PositionalSuffixTree(text)

        self.assert_query(tree, '', True)
        self.assert_query(tree, 'a', False)
        self.assert_query(tree, 'a$', False)
        self.assert_query(tree, 'ab', True)
        self.assert_query(tree, 'abc', False)
        self.assert_query(tree, 'x', False)
        self.assert_query(tree, '$', False)

    def test_ataaatg(self):
        text = 'ataaatg'

        tree = suffix_tree.PositionalSuffixTree(text)

        self.assert_query(tree, '', True)
        self.assert_query(tree, 'a', False)
        self.assert_query(tree, 'aa', False)
        self.assert_query(tree, 'aaa', False)
        self.assert_query(tree, 'aaat', False)
        self.assert_query(tree, 'aaatg', True)
        self.assert_query(tree, 'aaatg$', False)
        self.assert_query(tree, 'aaatg$x', False)
        self.assert_query(tree, 'aat', False)
        self.assert_query(tree, 'aatg', True)
        self.assert_query(tree, 'aatg$', False)
        self.assert_query(tree, 'aatg$x', False)
        self.assert_query(tree, 'at', False)
        self.assert_query(tree, 'ata', False)
        self.assert_query(tree, 'ataa', False)
        self.assert_query(tree, 'ataaa', False)
        self.assert_query(tree, 'ataaat', False)
        self.assert_query(tree, 'ataaatg', True)
        self.assert_query(tree, 'ataaatg$', False)
        self.assert_query(tree, 'ataaatg$x', False)
        self.assert_query(tree, 'atg', True)
        self.assert_query(tree, 'atg$', False)
        self.assert_query(tree, 'atg$x', False)
        self.assert_query(tree, 't', False)
        self.assert_query(tree, 'ta', False)
        self.assert_query(tree, 'taa', False)
        self.assert_query(tree, 'taaa', False)
        self.assert_query(tree, 'taaat', False)
        self.assert_query(tree, 'taaatg', True)
        self.assert_query(tree, 'taaatg$', False)
        self.assert_query(tree, 'taaatg$x', False)
        self.assert_query(tree, 'tg', True)
        self.assert_query(tree, 'tg$', False)
        self.assert_query(tree, 'tg$x', False)
        self.assert_query(tree, 'g', True)
        self.assert_query(tree, 'g$', False)
        self.assert_query(tree, 'g$x', False)
        self.assert_query(tree, '$', False)
        self.assert_query(tree, '$x', False)
        self.assert_query(tree, 'x', False)

class UkkonenSuffixTreeNodeTestCase(unittest.TestCase):

    def setUp(self):
        pass

    def tearDown(self):
        pass

    def test_constructor(self):
        node = suffix_tree.UkkonenSuffixTree.Node()

        self.assertEqual(-1, node.suffix_node)

    def test_repr(self):
        node = suffix_tree.UkkonenSuffixTree.Node()

        self.assertEqual('Node(-1)', repr(node))

class UkkonenSuffixTreeEdgeTestCase(unittest.TestCase):

    def setUp(self):
        pass

    def tearDown(self):
        pass

    def test_constructor(self):
        first_char_index = 1
        last_char_index = 2
        source_node_index = 3
        destination_node_index = 4

        edge = suffix_tree.UkkonenSuffixTree.Edge(first_char_index,
                                                  last_char_index,
                                                  source_node_index,
                                                  destination_node_index)

        self.assertEqual(first_char_index, edge.first_char_index)
        self.assertEqual(last_char_index, edge.last_char_index)
        self.assertEqual(source_node_index, edge.source_node_index)
        self.assertEqual(destination_node_index, edge.destination_node_index)

        self.assertEqual(last_char_index - first_char_index, edge.length)

    def test_repr(self):
        edge = suffix_tree.UkkonenSuffixTree.Edge(1, 2, 3, 4)

        self.assertEqual('Edge(3, 4, 1, 2)', repr(edge))

class UkkonenSuffixTreeSuffixTestCase(unittest.TestCase):

    def setUp(self):
        pass

    def tearDown(self):
        pass

    def test_constructor(self):
        source_node_index = 1
        first_char_index = 2
        last_char_index = 3

        suffix = suffix_tree.UkkonenSuffixTree.Suffix(source_node_index,
                                                      first_char_index,
                                                      last_char_index)
        self.assertEqual(source_node_index, suffix.source_node_index)
        self.assertEqual(first_char_index, suffix.first_char_index)
        self.assertEqual(last_char_index, suffix.last_char_index)

        self.assertEqual(last_char_index - first_char_index, suffix.length)

    def test_explicit(self):
        source_node_index = 1
        first_char_index = 3
        last_char_index = 2

        suffix = suffix_tree.UkkonenSuffixTree.Suffix(source_node_index,
                                                      first_char_index,
                                                      last_char_index)

        self.assertTrue(first_char_index > last_char_index)
        self.assertTrue(suffix.explicit())

    def test_implicit_as_last_char_index_equals_first_char_index(self):
        source_node_index = 1
        first_char_index = 2
        last_char_index = 2

        suffix = suffix_tree.UkkonenSuffixTree.Suffix(source_node_index,
                                                      first_char_index,
                                                      last_char_index)

        self.assertTrue(last_char_index >= first_char_index)
        self.assertTrue(suffix.implicit())

    def test_implicit_as_last_char_index_greater_than_first_char_index(self):
        source_node_index = 1
        first_char_index = 2
        last_char_index = 3

        suffix = suffix_tree.UkkonenSuffixTree.Suffix(source_node_index,
                                                      first_char_index,
                                                      last_char_index)

        self.assertTrue(last_char_index >= first_char_index)
        self.assertTrue(suffix.implicit())

class UkkonenSuffixTreeTestCase(unittest.TestCase):

    def setUp(self):
        pass

    def tearDown(self):
        pass

    def assert_edges(self, expected_edges, expected_indices, tree):
        actual_edges = []

        curr_index = tree.n
        edges = list(tree.edges.values())
        edges = sorted(edges, key=lambda x: (x.source_node_index,
                                             x.destination_node_index))
        for edge in edges:
            if edge.source_node_index == -1:
                continue

            top = min(curr_index, edge.last_char_index)
            actual_edges.append(tree.string[edge.first_char_index:top + 1])

        self.assertEqual(expected_edges, actual_edges)

        for i in range(len(expected_edges)):
            self.assertTrue(tree.has_substring(expected_edges[i]))
            self.assertEqual(expected_indices[i],
                             tree.find_substring(expected_edges[i]))

    def test_constructor_with_abc(self):
        string = 'abc'

        tree = suffix_tree.UkkonenSuffixTree(string)

        self.assertEqual(string, tree.string)

        self.assertEqual(False, tree.case_insensitive)

        self.assertEqual(2, tree.n)

        self.assertEqual(4, len(tree.nodes))
        for n in tree.nodes:
            self.assertEqual(-1, n.suffix_node)

        edge1 = (0, 'a')
        self.assertEqual(0, tree.edges[edge1].source_node_index)
        self.assertEqual(1, tree.edges[edge1].destination_node_index)
        self.assertEqual(0, tree.edges[edge1].first_char_index)
        self.assertEqual(2, tree.edges[edge1].last_char_index)
        edge2 = (0, 'b')
        self.assertEqual(0, tree.edges[edge2].source_node_index)
        self.assertEqual(2, tree.edges[edge2].destination_node_index)
        self.assertEqual(1, tree.edges[edge2].first_char_index)
        self.assertEqual(2, tree.edges[edge2].last_char_index)
        edge3 = (0, 'c')
        self.assertEqual(0, tree.edges[edge3].source_node_index)
        self.assertEqual(3, tree.edges[edge3].destination_node_index)
        self.assertEqual(2, tree.edges[edge3].first_char_index)
        self.assertEqual(2, tree.edges[edge3].last_char_index)

        self.assertEqual(0, tree.active.source_node_index)
        self.assertEqual(3, tree.active.first_char_index)
        self.assertEqual(2, tree.active.last_char_index)

    def test_constructor_with_case_sensitive_abc_as_one_capital_in_middle(self):
        string = 'aBc'
        case_insensitive = True

        tree = suffix_tree.UkkonenSuffixTree(string, case_insensitive)

        self.assertEqual(string.lower(), tree.string)

        self.assertEqual(case_insensitive, tree.case_insensitive)

        self.assertEqual(2, tree.n)

        self.assertEqual(4, len(tree.nodes))
        for n in tree.nodes:
            self.assertEqual(-1, n.suffix_node)

        edge1 = (0, 'a')
        self.assertEqual(0, tree.edges[edge1].source_node_index)
        self.assertEqual(1, tree.edges[edge1].destination_node_index)
        self.assertEqual(0, tree.edges[edge1].first_char_index)
        self.assertEqual(2, tree.edges[edge1].last_char_index)
        edge2 = (0, 'b')
        self.assertEqual(0, tree.edges[edge2].source_node_index)
        self.assertEqual(2, tree.edges[edge2].destination_node_index)
        self.assertEqual(1, tree.edges[edge2].first_char_index)
        self.assertEqual(2, tree.edges[edge2].last_char_index)
        edge3 = (0, 'c')
        self.assertEqual(0, tree.edges[edge3].source_node_index)
        self.assertEqual(3, tree.edges[edge3].destination_node_index)
        self.assertEqual(2, tree.edges[edge3].first_char_index)
        self.assertEqual(2, tree.edges[edge3].last_char_index)

        self.assertEqual(0, tree.active.source_node_index)
        self.assertEqual(3, tree.active.first_char_index)
        self.assertEqual(2, tree.active.last_char_index)

    def test_repr_of_abc(self):
        string = 'abc'
        expected_text = '\tStart \tEnd \tSuffix \tFirst \tLast \tString\n'
        expected_text += '\t0 \t1 \t-1 \t0 \t2 \tabc\n'
        expected_text += '\t0 \t2 \t-1 \t1 \t2 \tbc\n'
        expected_text += '\t0 \t3 \t-1 \t2 \t2 \tc\n'

        tree = suffix_tree.UkkonenSuffixTree(string)

        self.assertEqual(expected_text, repr(tree))

    def test_extraction_of_edges_for_a(self):
        string = 'A$'
        expected_edges = [ 'A$', '$', ]
        expected_indices = [ 0, 1, ]

        tree = suffix_tree.UkkonenSuffixTree(string)

        self.assert_edges(expected_edges, expected_indices, tree)

    def test_extraction_of_edges_for_aca(self):
        string = 'ACA$'
        expected_edges = [ 'CA$', 'A', '$', 'CA$', '$', ]
        expected_indices = [ 1, 0, 3, 1, 3, ]

        tree = suffix_tree.UkkonenSuffixTree(string)

        self.assert_edges(expected_edges, expected_indices, tree)

    def test_extraction_of_edges_for_ataaatg(self):
        string = 'ATAAATG$'
        expected_edges = [ 'A', 'T', 'G$', '$', 'A', 'T', 'ATG$', 'TG$',
                          'AAATG$', 'G$', 'AAATG$', 'G$', ]
        expected_indices = [ 0, 1, 6, 7, 0, 1, 4, 5, 2, 6, 2, 6, ]

        tree = suffix_tree.UkkonenSuffixTree(string)

        self.assert_edges(expected_edges, expected_indices, tree)

if __name__ == '__main__':
    class_names = [
                      SuffixTreeNodeTestCase,
                      SuffixTreeConstructionTestCase,
                      SuffixTreeFollowPathTestCase,
                      SuffixTreeHasSubstringTestCase,
                      SuffixTreeHasSuffixTestCase,
                      PositionalSuffixTreeNodeTestCase,
                      PositionalSuffixTreeConstructionTestCase,
                      PositionalSuffixTreeFollowPathTestCase,
                      PositionalSuffixTreeHasSubstringTestCase,
                      PositionalSuffixTreeHasSuffixTestCase,
                      UkkonenSuffixTreeNodeTestCase,
                      UkkonenSuffixTreeEdgeTestCase,
                      UkkonenSuffixTreeSuffixTestCase,
                      UkkonenSuffixTreeTestCase,
                  ]

    suite = unittest.TestSuite()

    for c in class_names:
        suite.addTest(unittest.defaultTestLoader.loadTestsFromTestCase(c))

    unittest.TextTestRunner().run(suite)
