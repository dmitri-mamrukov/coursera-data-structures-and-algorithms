#!/usr/bin/python3

import unittest

import generalized_suffix_tree

class GeneralizedSuffixTreeNodeTestCase(unittest.TestCase):

    def setUp(self):
        pass

    def tearDown(self):
        pass

    def test_constructor_with_parent(self):
        parent = 123

        node = generalized_suffix_tree.GeneralizedSuffixTree.Node(parent)

        self.assertEqual(parent, node._parent)
        self.assertEqual([], node._children)
        self.assertEqual(set(), node._words)

    def test_constructor_with_parent_and_words(self):
        parent = 123
        words = set()
        words.add('word1')
        words.add('word2')
        words.add('word3')

        node = generalized_suffix_tree.GeneralizedSuffixTree.Node(parent,
                                                                  words)

        self.assertEqual(parent, node._parent)
        self.assertEqual(parent, node.parent)
        self.assertEqual([], node._children)
        self.assertEqual([], node.children)
        self.assertEqual(words, node._words)
        self.assertEqual(words, node.words)

    def test_repr(self):
        parent = 123
        words = set()
        words.add('banana')

        node = generalized_suffix_tree.GeneralizedSuffixTree.Node(parent,
                                                                  words)

        self.assertEqual("parent=123, children=[], words={'banana'}",
                         repr(node))

class GeneralizedSuffixTreeEdgeTestCase(unittest.TestCase):

    def setUp(self):
        pass

    def tearDown(self):
        pass

    def test_constructor(self):
        word = 'word'
        start_index = 1
        stop_index = 2

        edge = generalized_suffix_tree.GeneralizedSuffixTree.Edge(word,
                                                                  start_index,
                                                                  stop_index)

        self.assertEqual(word, edge._word_index)
        self.assertEqual(start_index, edge._start_index)
        self.assertEqual(stop_index, edge._stop_index)

    def test_repr(self):
        word = 'banana'
        start_index = 1
        stop_index = 2

        edge = generalized_suffix_tree.GeneralizedSuffixTree.Edge(word,
                                                                  start_index,
                                                                  stop_index)

        self.assertEqual('word=banana, start_index=1, stop_index=2',
                         repr(edge))

class GeneralizedSuffixTreeTestCase(unittest.TestCase):

    def setUp(self):
        pass

    def tearDown(self):
        pass

    def assert_items(self, expected_items, actual_items):
        try:
            self.assertEqual(len(expected_items), len(actual_items))
            expected_count = {}
            for expected_item in expected_items:
                if not expected_item in expected_count:
                    expected_count[expected_item] = 0
                expected_count[expected_item] += 1
            count = {}
            for item in actual_items:
                if not item in count:
                    count[item] = 0
                count[item] += 1

            for item in actual_items:
                self.assertEqual(expected_count[item],
                                 count[item],
                                 'Item ' + str(item) +
                                 ' has different counts.')
        except Exception:
            self.fail('Expected: {}, actual: {} '.format(expected_items,
                                                     actual_items))

    def assert_edge_strings(self, expected_edges, tree):
        self.assert_items(expected_edges,
                          [tree.edge_substring(e)
                           for e in tree._edges.values()])

    def test_constructor_with_one_word(self):
        words = [ 'word', ]

        tree = generalized_suffix_tree.GeneralizedSuffixTree(words)

        self.assertEqual([ 'word$', ], tree._words)

        expected_nodes = []
        expected_edges = []

        self.assertEqual(6, len(tree._nodes))
        self.assertEqual(5, len(tree._edges))
        self.assertEqual(len(tree._nodes) - 1, len(tree._edges))

        self.assertEqual(-1, tree._nodes[0].parent)
        self.assertEqual([ 1, 2, 3, 4, 5, ], tree._nodes[0].children)
        self.assertEqual(set([ 0, ]), tree._nodes[0].words)
        expected_nodes.append(0)
        self.assertEqual(0, tree._nodes[1].parent)
        self.assertEqual([], tree._nodes[1].children)
        self.assertEqual(set([ 0, ]), tree._nodes[1].words)
        expected_nodes.append(1)
        self.assertEqual(0, tree._nodes[2].parent)
        self.assertEqual([], tree._nodes[2].children)
        self.assertEqual(set([ 0, ]), tree._nodes[2].words)
        expected_nodes.append(2)
        self.assertEqual(0, tree._nodes[3].parent)
        self.assertEqual([], tree._nodes[3].children)
        self.assertEqual(set([ 0, ]), tree._nodes[3].words)
        expected_nodes.append(3)
        self.assertEqual(0, tree._nodes[4].parent)
        self.assertEqual([], tree._nodes[4].children)
        self.assertEqual(set([ 0, ]), tree._nodes[4].words)
        expected_nodes.append(4)
        self.assertEqual(0, tree._nodes[5].parent)
        self.assertEqual([], tree._nodes[5].children)
        self.assertEqual(set([ 0, ]), tree._nodes[5].words)
        expected_nodes.append(5)

        self.assert_items(expected_nodes, list(range(len(tree._nodes))))

        edge = tree._edges[(0, 1)]
        self.assertEqual(0, edge._word_index)
        self.assertEqual(0, edge._start_index)
        self.assertEqual(5, edge._stop_index)
        word = tree._words[edge._word_index]
        self.assertEqual('word$', word[edge._start_index:edge._stop_index])
        expected_edges.append(edge)
        edge = tree._edges[(0, 2)]
        self.assertEqual(0, edge._word_index)
        self.assertEqual(1, edge._start_index)
        self.assertEqual(5, edge._stop_index)
        word = tree._words[edge._word_index]
        self.assertEqual('ord$', word[edge._start_index:edge._stop_index])
        expected_edges.append(edge)
        edge = tree._edges[(0, 3)]
        self.assertEqual(0, edge._word_index)
        self.assertEqual(2, edge._start_index)
        self.assertEqual(5, edge._stop_index)
        word = tree._words[edge._word_index]
        self.assertEqual('rd$', word[edge._start_index:edge._stop_index])
        expected_edges.append(edge)
        edge = tree._edges[(0, 4)]
        self.assertEqual(0, edge._word_index)
        self.assertEqual(3, edge._start_index)
        self.assertEqual(5, edge._stop_index)
        word = tree._words[edge._word_index]
        self.assertEqual('d$', word[edge._start_index:edge._stop_index])
        expected_edges.append(edge)
        edge = tree._edges[(0, 5)]
        self.assertEqual(0, edge._word_index)
        self.assertEqual(4, edge._start_index)
        self.assertEqual(5, edge._stop_index)
        word = tree._words[edge._word_index]
        self.assertEqual('$', word[edge._start_index:edge._stop_index])
        expected_edges.append(edge)

        self.assert_items(expected_edges, tree._edges.values())

    def test_constructor_with_two_words(self):
        words = [ 'panama', 'banana', ]

        tree = generalized_suffix_tree.GeneralizedSuffixTree(words)

        self.assertEqual([ 'panama$0', 'banana$1', ], tree._words)

        expected_nodes = []
        expected_edges = []

        self.assertEqual(18, len(tree._nodes))
        self.assertEqual(17, len(tree._edges))
        self.assertEqual(len(tree._nodes) - 1, len(tree._edges))

        self.assertEqual(-1, tree._nodes[0].parent)
        self.assertEqual([ 1, 4, 6, 8, 9, 12, 17, ], tree._nodes[0].children)
        self.assertEqual(set([ 0, 1, ]), tree._nodes[0].words)
        expected_nodes.append(0)
        self.assertEqual(0, tree._nodes[1].parent)
        self.assertEqual([], tree._nodes[1].children)
        self.assertEqual(set([ 0, ]), tree._nodes[1].words)
        expected_nodes.append(1)
        self.assertEqual(0, tree._nodes[4].parent)
        self.assertEqual([ 5, 7, 10, 16, ], tree._nodes[4].children)
        self.assertEqual(set([ 0, 1, ]), tree._nodes[4].words)
        expected_nodes.append(4)
        self.assertEqual(0, tree._nodes[6].parent)
        self.assertEqual([], tree._nodes[6].children)
        self.assertEqual(set([ 0, ]), tree._nodes[6].words)
        expected_nodes.append(6)
        self.assertEqual(0, tree._nodes[8].parent)
        self.assertEqual([], tree._nodes[8].children)
        self.assertEqual(set([ 0, ]), tree._nodes[8].words)
        expected_nodes.append(8)
        self.assertEqual(0, tree._nodes[9].parent)
        self.assertEqual([], tree._nodes[9].children)
        self.assertEqual(set([ 1, ]), tree._nodes[9].words)
        expected_nodes.append(9)
        self.assertEqual(0, tree._nodes[12].parent)
        self.assertEqual([ 3, 13, 15, ], tree._nodes[12].children)
        self.assertEqual(set([ 0, 1, ]), tree._nodes[12].words)
        expected_nodes.append(12)
        self.assertEqual(0, tree._nodes[17].parent)
        self.assertEqual([], tree._nodes[17].children)
        self.assertEqual(set([ 1, ]), tree._nodes[17].words)
        expected_nodes.append(17)
        self.assertEqual(4, tree._nodes[5].parent)
        self.assertEqual([], tree._nodes[5].children)
        self.assertEqual(set([ 0, ]), tree._nodes[5].words)
        expected_nodes.append(5)
        self.assertEqual(4, tree._nodes[7].parent)
        self.assertEqual([], tree._nodes[7].children)
        self.assertEqual(set([ 0, ]), tree._nodes[7].words)
        expected_nodes.append(7)
        self.assertEqual(4, tree._nodes[10].parent)
        self.assertEqual([ 2, 11, 14, ], tree._nodes[10].children)
        self.assertEqual(set([ 0, 1, ]), tree._nodes[10].words)
        expected_nodes.append(10)
        self.assertEqual(4, tree._nodes[16].parent)
        self.assertEqual([], tree._nodes[16].children)
        self.assertEqual(set([ 1, ]), tree._nodes[16].words)
        expected_nodes.append(16)
        self.assertEqual(12, tree._nodes[3].parent)
        self.assertEqual([], tree._nodes[3].children)
        self.assertEqual(set([ 0, ]), tree._nodes[3].words)
        expected_nodes.append(3)
        self.assertEqual(12, tree._nodes[13].parent)
        self.assertEqual([], tree._nodes[13].children)
        self.assertEqual(set([ 1, ]), tree._nodes[13].words)
        expected_nodes.append(13)
        self.assertEqual(12, tree._nodes[15].parent)
        self.assertEqual([], tree._nodes[15].children)
        self.assertEqual(set([ 1, ]), tree._nodes[15].words)
        expected_nodes.append(15)
        self.assertEqual(10, tree._nodes[2].parent)
        self.assertEqual([], tree._nodes[2].children)
        self.assertEqual(set([ 0, ]), tree._nodes[2].words)
        expected_nodes.append(2)
        self.assertEqual(10, tree._nodes[11].parent)
        self.assertEqual([], tree._nodes[11].children)
        self.assertEqual(set([ 1, ]), tree._nodes[11].words)
        expected_nodes.append(11)
        self.assertEqual(10, tree._nodes[14].parent)
        self.assertEqual([], tree._nodes[14].children)
        self.assertEqual(set([ 1, ]), tree._nodes[14].words)
        expected_nodes.append(14)

        self.assert_items(expected_nodes, list(range(len(tree._nodes))))

        edge = tree._edges[(0, 1)]
        self.assertEqual(0, edge._word_index)
        self.assertEqual(0, edge._start_index)
        self.assertEqual(8, edge._stop_index)
        word = tree._words[edge._word_index]
        self.assertEqual('panama$0', word[edge._start_index:edge._stop_index])
        expected_edges.append(edge)
        edge = tree._edges[(0, 4)]
        self.assertEqual(0, edge._word_index)
        self.assertEqual(1, edge._start_index)
        self.assertEqual(2, edge._stop_index)
        word = tree._words[edge._word_index]
        self.assertEqual('a', word[edge._start_index:edge._stop_index])
        expected_edges.append(edge)
        edge = tree._edges[(0, 6)]
        self.assertEqual(0, edge._word_index)
        self.assertEqual(4, edge._start_index)
        self.assertEqual(8, edge._stop_index)
        word = tree._words[edge._word_index]
        self.assertEqual('ma$0', word[edge._start_index:edge._stop_index])
        expected_edges.append(edge)
        edge = tree._edges[(0, 8)]
        self.assertEqual(0, edge._word_index)
        self.assertEqual(6, edge._start_index)
        self.assertEqual(8, edge._stop_index)
        word = tree._words[edge._word_index]
        self.assertEqual('$0', word[edge._start_index:edge._stop_index])
        expected_edges.append(edge)
        edge = tree._edges[(0, 9)]
        self.assertEqual(1, edge._word_index)
        self.assertEqual(0, edge._start_index)
        self.assertEqual(8, edge._stop_index)
        word = tree._words[edge._word_index]
        self.assertEqual('banana$1', word[edge._start_index:edge._stop_index])
        expected_edges.append(edge)
        edge = tree._edges[(0, 12)]
        self.assertEqual(0, edge._word_index)
        self.assertEqual(2, edge._start_index)
        self.assertEqual(4, edge._stop_index)
        word = tree._words[edge._word_index]
        self.assertEqual('na', word[edge._start_index:edge._stop_index])
        expected_edges.append(edge)
        edge = tree._edges[(0, 17)]
        self.assertEqual(1, edge._word_index)
        self.assertEqual(6, edge._start_index)
        self.assertEqual(8, edge._stop_index)
        word = tree._words[edge._word_index]
        self.assertEqual('$1', word[edge._start_index:edge._stop_index])
        expected_edges.append(edge)
        edge = tree._edges[(4, 5)]
        self.assertEqual(0, edge._word_index)
        self.assertEqual(4, edge._start_index)
        self.assertEqual(8, edge._stop_index)
        word = tree._words[edge._word_index]
        self.assertEqual('ma$0', word[edge._start_index:edge._stop_index])
        expected_edges.append(edge)
        edge = tree._edges[(4, 7)]
        self.assertEqual(0, edge._word_index)
        self.assertEqual(6, edge._start_index)
        self.assertEqual(8, edge._stop_index)
        word = tree._words[edge._word_index]
        self.assertEqual('$0', word[edge._start_index:edge._stop_index])
        expected_edges.append(edge)
        edge = tree._edges[(4, 10)]
        self.assertEqual(0, edge._word_index)
        self.assertEqual(2, edge._start_index)
        self.assertEqual(4, edge._stop_index)
        word = tree._words[edge._word_index]
        self.assertEqual('na', word[edge._start_index:edge._stop_index])
        expected_edges.append(edge)
        edge = tree._edges[(4, 16)]
        self.assertEqual(1, edge._word_index)
        self.assertEqual(6, edge._start_index)
        self.assertEqual(8, edge._stop_index)
        word = tree._words[edge._word_index]
        self.assertEqual('$1', word[edge._start_index:edge._stop_index])
        expected_edges.append(edge)
        edge = tree._edges[(12, 3)]
        self.assertEqual(0, edge._word_index)
        self.assertEqual(4, edge._start_index)
        self.assertEqual(8, edge._stop_index)
        word = tree._words[edge._word_index]
        self.assertEqual('ma$0', word[edge._start_index:edge._stop_index])
        expected_edges.append(edge)
        edge = tree._edges[(12, 13)]
        self.assertEqual(1, edge._word_index)
        self.assertEqual(4, edge._start_index)
        self.assertEqual(8, edge._stop_index)
        word = tree._words[edge._word_index]
        self.assertEqual('na$1', word[edge._start_index:edge._stop_index])
        expected_edges.append(edge)
        edge = tree._edges[(12, 15)]
        self.assertEqual(1, edge._word_index)
        self.assertEqual(6, edge._start_index)
        self.assertEqual(8, edge._stop_index)
        word = tree._words[edge._word_index]
        self.assertEqual('$1', word[edge._start_index:edge._stop_index])
        expected_edges.append(edge)
        edge = tree._edges[(10, 2)]
        self.assertEqual(0, edge._word_index)
        self.assertEqual(4, edge._start_index)
        self.assertEqual(8, edge._stop_index)
        word = tree._words[edge._word_index]
        self.assertEqual('ma$0', word[edge._start_index:edge._stop_index])
        expected_edges.append(edge)
        edge = tree._edges[(10, 11)]
        self.assertEqual(1, edge._word_index)
        self.assertEqual(4, edge._start_index)
        self.assertEqual(8, edge._stop_index)
        word = tree._words[edge._word_index]
        self.assertEqual('na$1', word[edge._start_index:edge._stop_index])
        expected_edges.append(edge)
        edge = tree._edges[(10, 14)]
        self.assertEqual(1, edge._word_index)
        self.assertEqual(6, edge._start_index)
        self.assertEqual(8, edge._stop_index)
        word = tree._words[edge._word_index]
        self.assertEqual('$1', word[edge._start_index:edge._stop_index])
        expected_edges.append(edge)

        self.assert_items(expected_edges, tree._edges.values())

    def test_edge_substring_in_tree_with_one_word(self):
        words = [ 'word', ]

        tree = generalized_suffix_tree.GeneralizedSuffixTree(words)

        self.assertEqual([ 'word$', ], tree._words)

        self.assertEqual(5, len(tree._edges))

        edge = tree._edges[(0, 1)]
        self.assertEqual('word$', tree.edge_substring(edge))
        edge = tree._edges[(0, 2)]
        self.assertEqual('ord$', tree.edge_substring(edge))
        edge = tree._edges[(0, 3)]
        self.assertEqual('rd$', tree.edge_substring(edge))
        edge = tree._edges[(0, 4)]
        self.assertEqual('d$', tree.edge_substring(edge))
        edge = tree._edges[(0, 5)]
        self.assertEqual('$', tree.edge_substring(edge))

    def test_edge_substring_in_tree_with_two_words(self):
        words = [ 'panama', 'banana', ]

        tree = generalized_suffix_tree.GeneralizedSuffixTree(words)

        self.assertEqual([ 'panama$0', 'banana$1', ], tree._words)

        self.assertEqual(17, len(tree._edges))

        edge = tree._edges[(0, 1)]
        self.assertEqual('panama$0', tree.edge_substring(edge))
        edge = tree._edges[(0, 4)]
        self.assertEqual('a', tree.edge_substring(edge))
        edge = tree._edges[(0, 6)]
        self.assertEqual('ma$0', tree.edge_substring(edge))
        edge = tree._edges[(0, 8)]
        self.assertEqual('$0', tree.edge_substring(edge))
        edge = tree._edges[(0, 9)]
        self.assertEqual('banana$1', tree.edge_substring(edge))
        edge = tree._edges[(0, 12)]
        self.assertEqual('na', tree.edge_substring(edge))
        edge = tree._edges[(0, 17)]
        self.assertEqual('$1', tree.edge_substring(edge))
        edge = tree._edges[(4, 5)]
        self.assertEqual('ma$0', tree.edge_substring(edge))
        edge = tree._edges[(4, 7)]
        self.assertEqual('$0', tree.edge_substring(edge))
        edge = tree._edges[(4, 10)]
        self.assertEqual('na', tree.edge_substring(edge))
        edge = tree._edges[(4, 16)]
        self.assertEqual('$1', tree.edge_substring(edge))
        edge = tree._edges[(12, 3)]
        self.assertEqual('ma$0', tree.edge_substring(edge))
        edge = tree._edges[(12, 13)]
        self.assertEqual('na$1', tree.edge_substring(edge))
        edge = tree._edges[(12, 15)]
        self.assertEqual('$1', tree.edge_substring(edge))
        edge = tree._edges[(10, 2)]
        self.assertEqual('ma$0', tree.edge_substring(edge))
        edge = tree._edges[(10, 11)]
        self.assertEqual('na$1', tree.edge_substring(edge))
        edge = tree._edges[(10, 14)]
        self.assertEqual('$1', tree.edge_substring(edge))

    def test_node_substring_in_tree_with_one_word(self):
        words = [ 'word', ]

        tree = generalized_suffix_tree.GeneralizedSuffixTree(words)

        self.assertEqual([ 'word$', ], tree._words)

        self.assertEqual(6, len(tree._nodes))

        self.assertEqual('', tree.node_substring(0))
        self.assertEqual('word$', tree.node_substring(1))
        self.assertEqual('ord$', tree.node_substring(2))
        self.assertEqual('rd$', tree.node_substring(3))
        self.assertEqual('d$', tree.node_substring(4))
        self.assertEqual('$', tree.node_substring(5))

    def test_node_substring_in_tree_with_two_words(self):
        words = [ 'panama', 'banana', ]

        tree = generalized_suffix_tree.GeneralizedSuffixTree(words)

        self.assertEqual([ 'panama$0', 'banana$1', ], tree._words)

        self.assertEqual(18, len(tree._nodes))

        self.assertEqual('', tree.node_substring(0))
        self.assertEqual('panama$0', tree.node_substring(1))
        self.assertEqual('anama$0', tree.node_substring(2))
        self.assertEqual('nama$0', tree.node_substring(3))
        self.assertEqual('a', tree.node_substring(4))
        self.assertEqual('ama$0', tree.node_substring(5))
        self.assertEqual('ma$0', tree.node_substring(6))
        self.assertEqual('a$0', tree.node_substring(7))
        self.assertEqual('$0', tree.node_substring(8))
        self.assertEqual('banana$1', tree.node_substring(9))
        self.assertEqual('ana', tree.node_substring(10))
        self.assertEqual('anana$1', tree.node_substring(11))
        self.assertEqual('na', tree.node_substring(12))
        self.assertEqual('nana$1', tree.node_substring(13))
        self.assertEqual('ana$1', tree.node_substring(14))
        self.assertEqual('na$1', tree.node_substring(15))
        self.assertEqual('a$1', tree.node_substring(16))
        self.assertEqual('$1', tree.node_substring(17))

    def test_node_depth_in_tree_with_one_word(self):
        words = [ 'word', ]

        tree = generalized_suffix_tree.GeneralizedSuffixTree(words)

        self.assertEqual([ 'word$', ], tree._words)

        self.assertEqual(6, len(tree._nodes))

        self.assertEqual('', tree.node_substring(0))
        self.assertEqual(0, tree.node_depth(0))
        self.assertEqual('word$', tree.node_substring(1))
        self.assertEqual(4, tree.node_depth(1))
        self.assertEqual('ord$', tree.node_substring(2))
        self.assertEqual(3, tree.node_depth(2))
        self.assertEqual('rd$', tree.node_substring(3))
        self.assertEqual(2, tree.node_depth(3))
        self.assertEqual('d$', tree.node_substring(4))
        self.assertEqual(1, tree.node_depth(4))
        self.assertEqual('$', tree.node_substring(5))
        self.assertEqual(0, tree.node_depth(5))

    def test_node_depth_in_tree_with_two_words(self):
        words = [ 'panama', 'banana', ]

        tree = generalized_suffix_tree.GeneralizedSuffixTree(words)

        self.assertEqual([ 'panama$0', 'banana$1', ], tree._words)

        self.assertEqual(17, len(tree._edges))

        self.assertEqual('', tree.node_substring(0))
        self.assertEqual(0, tree.node_depth(0))
        self.assertEqual('panama$0', tree.node_substring(1))
        self.assertEqual(6, tree.node_depth(1))
        self.assertEqual('anama$0', tree.node_substring(2))
        self.assertEqual(5, tree.node_depth(2))
        self.assertEqual('nama$0', tree.node_substring(3))
        self.assertEqual(4, tree.node_depth(3))
        self.assertEqual('a', tree.node_substring(4))
        self.assertEqual(1, tree.node_depth(4))
        self.assertEqual('ama$0', tree.node_substring(5))
        self.assertEqual(3, tree.node_depth(5))
        self.assertEqual('ma$0', tree.node_substring(6))
        self.assertEqual(2, tree.node_depth(6))
        self.assertEqual('a$0', tree.node_substring(7))
        self.assertEqual(1, tree.node_depth(7))
        self.assertEqual('$0', tree.node_substring(8))
        self.assertEqual(0, tree.node_depth(8))
        self.assertEqual('banana$1', tree.node_substring(9))
        self.assertEqual(6, tree.node_depth(9))
        self.assertEqual('ana', tree.node_substring(10))
        self.assertEqual(3, tree.node_depth(10))
        self.assertEqual('anana$1', tree.node_substring(11))
        self.assertEqual(5, tree.node_depth(11))
        self.assertEqual('na', tree.node_substring(12))
        self.assertEqual(2, tree.node_depth(12))
        self.assertEqual('nana$1', tree.node_substring(13))
        self.assertEqual(4, tree.node_depth(13))
        self.assertEqual('ana$1', tree.node_substring(14))
        self.assertEqual(3, tree.node_depth(14))
        self.assertEqual('na$1', tree.node_substring(15))
        self.assertEqual(2, tree.node_depth(15))
        self.assertEqual('a$1', tree.node_substring(16))
        self.assertEqual(1, tree.node_depth(16))
        self.assertEqual('$1', tree.node_substring(17))
        self.assertEqual(0, tree.node_depth(17))

    def test_edges_for_a(self):
        words = [ 'A', ]

        tree = generalized_suffix_tree.GeneralizedSuffixTree(words)

        self.assertEqual([ 'A$', ], tree._words)

        expected_edges = [ 'A$', '$', ]

        self.assert_edge_strings(expected_edges, tree)

    def test_edges_for_aca(self):
        words = [ 'ACA', ]

        tree = generalized_suffix_tree.GeneralizedSuffixTree(words)

        self.assertEqual([ 'ACA$', ], tree._words)

        expected_edges = [ 'CA$', 'A', '$', 'CA$', '$', ]

        self.assert_edge_strings(expected_edges, tree)

    def test_edges_for_ataaatg(self):
        words = [ 'ATAAATG', ]

        tree = generalized_suffix_tree.GeneralizedSuffixTree(words)

        self.assertEqual([ 'ATAAATG$', ], tree._words)

        expected_edges = [ 'A', 'T', 'G$', '$', 'A', 'T', 'ATG$', 'TG$',
                          'AAATG$', 'G$', 'AAATG$', 'G$', ]

        self.assert_edge_strings(expected_edges, tree)

if __name__ == '__main__':
    class_names = [
                      GeneralizedSuffixTreeNodeTestCase,
                      GeneralizedSuffixTreeEdgeTestCase,
                      GeneralizedSuffixTreeTestCase,
                  ]

    suite = unittest.TestSuite()

    for c in class_names:
        suite.addTest(unittest.defaultTestLoader.loadTestsFromTestCase(c))

    unittest.TextTestRunner().run(suite)
