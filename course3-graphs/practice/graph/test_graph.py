#!/usr/bin/python3

import collections
import math
import unittest

import graph_util

class Util():

    @staticmethod
    def assert_items(unittest_self, expected_items, actual_items):
        try:
            unittest_self.assertEqual(len(expected_items), len(actual_items))
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
                unittest_self.assertEqual(expected_count[item],
                                          count[item],
                                          'Item ' + str(item) +
                                          ' has different counts.')
        except Exception:
            unittest_self.fail('Expected: {}, actual: {} '.format(
                                                                 expected_items,
                                                                 actual_items))

class GraphTestCase(unittest.TestCase):

    def setUp(self):
        self.graph = graph_util.Graph()

    def tearDown(self):
        pass

    def test_constructor(self):
        self.assertEqual({}, self.graph._node_neighbors)
        self.assertEqual({}, self.graph._edge_weights)
        Util.assert_items(self, [], self.graph.nodes())
        Util.assert_items(self, [], self.graph.edges())

    def test_repr_of_empty_graph(self):
        self.assertEqual('[nodes: ] [edges: ]', repr(self.graph))

    def test_repr_of_one_node_graph(self):
        self.graph.add_node('a')

        self.assertEqual('[nodes: a] [edges: ]', repr(self.graph))

    def test_repr_of_one_directed_edge_graph(self):
        node1 = 'a'
        node2 = 'b'

        self.graph.add_node(node1)
        self.graph.add_node(node2)

        self.graph.add_directed_edge(node1, node2, 1)

        self.assertEqual("[nodes: a, b] [edges: (a, b) 1]",
                         repr(self.graph))

    def test_repr_of_one_undirected_edge_graph(self):
        node1 = 'a'
        node2 = 'b'

        self.graph.add_node(node1)
        self.graph.add_node(node2)

        self.graph.add_undirected_edge(node1, node2, 1)

        self.assertEqual("[nodes: a, b] [edges: (a, b) 1, (b, a) 1]",
                         repr(self.graph))

    def test_weight_of_nonexisting_edge(self):
        with self.assertRaisesRegex(KeyError,
                                    "\'a\', \'b\'"):
            self.graph.weight(('a', 'b'))

    def test_has_node_as_nonexisting(self):
        self.assertFalse(self.graph.has_node('non-existing-node'))

    def test_add_node(self):
        node = 'a'

        self.graph.add_node(node)

        self.assertEqual(1, len(self.graph._node_neighbors))
        self.assertEqual([], self.graph._node_neighbors[node])
        self.assertEqual(0, len(self.graph._edge_weights))
        Util.assert_items(self, [ node ], self.graph.nodes())
        Util.assert_items(self, [], self.graph.edges())

        self.assertTrue(self.graph.has_node(node))

    def test_add_node_as_existing(self):
        node = 'a'

        self.graph.add_node(node)
        with self.assertRaisesRegex(ValueError,
                                    'Node a already in the graph.'):
            self.graph.add_node(node)

        self.assertEqual(1, len(self.graph._node_neighbors))
        self.assertEqual([], self.graph._node_neighbors[node])
        self.assertEqual(0, len(self.graph._edge_weights))
        Util.assert_items(self, [ node ], self.graph.nodes())
        Util.assert_items(self, [], self.graph.edges())

    def test_add_directed_edge_with_nonexisting_nodes(self):
        node1 = 'a'
        node2 = 'b'

        with self.assertRaisesRegex(ValueError,
                                    "Node a not in the graph."):
            self.graph.add_directed_edge(node1, node2)

    def test_add_directed_edge_with_nonexisting_first_node(self):
        node1 = 'a'
        node2 = 'b'

        self.graph.add_node(node2)

        with self.assertRaisesRegex(ValueError,
                                    "Node a not in the graph."):
            self.graph.add_directed_edge(node1, node2)

    def test_add_directed_edge_with_nonexisting_second_node(self):
        node1 = 'a'
        node2 = 'b'

        self.graph.add_node(node1)

        with self.assertRaisesRegex(ValueError,
                                    "Node b not in the graph."):
            self.graph.add_directed_edge(node1, node2)

    def test_add_directed_edge_with_default_weight(self):
        node1 = 'a'
        node2 = 'b'

        self.graph.add_node(node1)
        self.graph.add_node(node2)

        self.graph.add_directed_edge(node1, node2)

        self.assertEqual(2, len(self.graph._node_neighbors))
        self.assertEqual([ node2 ], self.graph._node_neighbors[node1])
        self.assertEqual([], self.graph._node_neighbors[node2])
        self.assertEqual(1, len(self.graph._edge_weights))
        self.assertEqual(0, self.graph._edge_weights[(node1, node2)])
        self.assertEqual(0, self.graph.weight((node1, node2)))
        Util.assert_items(self, [ node1, node2 ], self.graph.nodes())
        Util.assert_items(self, [ (node1, node2) ], self.graph.edges())

        self.assertTrue(self.graph.has_node(node1))
        self.assertTrue(self.graph.has_node(node2))

    def test_add_directed_edge_with_some_weight(self):
        node1 = 'a'
        node2 = 'b'

        self.graph.add_node(node1)
        self.graph.add_node(node2)

        self.graph.add_directed_edge(node1, node2, 5)

        self.assertEqual(2, len(self.graph._node_neighbors))
        self.assertEqual([ node2 ], self.graph._node_neighbors[node1])
        self.assertEqual([], self.graph._node_neighbors[node2])
        self.assertEqual(1, len(self.graph._edge_weights))
        self.assertEqual(5, self.graph._edge_weights[(node1, node2)])
        self.assertEqual(5, self.graph.weight((node1, node2)))
        Util.assert_items(self, [ node1, node2 ], self.graph.nodes())
        Util.assert_items(self, [ (node1, node2) ], self.graph.edges())

        self.assertTrue(self.graph.has_node(node1))
        self.assertTrue(self.graph.has_node(node2))

    def test_add_undirected_edge_with_nonexisting_nodes(self):
        node1 = 'a'
        node2 = 'b'

        with self.assertRaisesRegex(ValueError,
                                    "Node a not in the graph."):
            self.graph.add_undirected_edge(node1, node2)

    def test_add_undirected_edge_with_nonexisting_first_node(self):
        node1 = 'a'
        node2 = 'b'

        self.graph.add_node(node2)

        with self.assertRaisesRegex(ValueError,
                                    "Node a not in the graph."):
            self.graph.add_undirected_edge(node1, node2)

    def test_add_undirected_edge_with_nonexisting_second_node(self):
        node1 = 'a'
        node2 = 'b'

        self.graph.add_node(node1)

        with self.assertRaisesRegex(ValueError,
                                    "Node b not in the graph."):
            self.graph.add_undirected_edge(node1, node2)

    def test_add_undirected_edge_with_default_weight(self):
        node1 = 'a'
        node2 = 'b'

        self.graph.add_node(node1)
        self.graph.add_node(node2)

        self.graph.add_undirected_edge(node1, node2)

        self.assertEqual(2, len(self.graph._node_neighbors))
        self.assertEqual([ node2 ], self.graph._node_neighbors[node1])
        self.assertEqual([ node1 ], self.graph._node_neighbors[node2])
        self.assertEqual(2, len(self.graph._edge_weights))
        self.assertEqual(0, self.graph._edge_weights[ (node1, node2) ])
        self.assertEqual(0, self.graph._edge_weights[ (node2, node1) ])
        self.assertEqual(0, self.graph.weight((node1, node2)))
        self.assertEqual(0, self.graph.weight((node2, node1)))
        Util.assert_items(self, [ node1, node2 ], self.graph.nodes())
        Util.assert_items(self, [ (node1, node2), (node2, node1) ],
                          self.graph.edges())

        self.assertTrue(self.graph.has_node(node1))
        self.assertTrue(self.graph.has_node(node2))

    def test_add_undirected_edge_with_some_weight(self):
        node1 = 'a'
        node2 = 'b'

        self.graph.add_node(node1)
        self.graph.add_node(node2)

        self.graph.add_undirected_edge(node1, node2, 5)

        self.assertEqual(2, len(self.graph._node_neighbors))
        self.assertEqual([ node2 ], self.graph._node_neighbors[node1])
        self.assertEqual([ node1 ], self.graph._node_neighbors[node2])
        self.assertEqual(2, len(self.graph._edge_weights))
        self.assertEqual(5, self.graph._edge_weights[(node1, node2)])
        self.assertEqual(5, self.graph._edge_weights[(node2, node1)])
        self.assertEqual(5, self.graph.weight((node1, node2)))
        self.assertEqual(5, self.graph.weight((node2, node1)))
        Util.assert_items(self, [ node1, node2 ], self.graph.nodes())
        Util.assert_items(self, [ (node1, node2), (node2, node1) ],
                          self.graph.edges())

        self.assertTrue(self.graph.has_node(node1))
        self.assertTrue(self.graph.has_node(node2))

class ComponentTestCase(unittest.TestCase):

    def setUp(self):
        self.util = graph_util.GraphUtil()
        self.graph = graph_util.Graph()

    def tearDown(self):
        pass

    def test_empty_graph(self):
        node = 'A'

        result = self.util.component(self.graph, node)

        self.assertEqual([ node ], result)

    def test_one_directed_edge(self):
        node1, node2 = 'A', 'B'

        self.graph.add_node(node1)
        self.graph.add_node(node2)

        self.graph.add_directed_edge(node1, node2)

        result = self.util.component(self.graph, node1)

        self.assertEqual([ node1, node2 ], result)

        result = self.util.component(self.graph, node2)

        self.assertEqual([ node2 ], result)

    def test_one_undirected_edge(self):
        node1, node2 = 'A', 'B'

        self.graph.add_node(node1)
        self.graph.add_node(node2)

        self.graph.add_undirected_edge(node1, node2)

        result = self.util.component(self.graph, node1)

        self.assertEqual([ node1, node2 ], result)

        result = self.util.component(self.graph, node2)

        self.assertEqual([ node2, node1 ], result)

    def test_two_directed_edges_as_rays(self):
        node1, node2, node3 = 'A', 'B', 'C'

        self.graph.add_node(node1)
        self.graph.add_node(node2)
        self.graph.add_node(node3)

        self.graph.add_directed_edge(node1, node2)
        self.graph.add_directed_edge(node1, node3)

        result = self.util.component(self.graph, node1)

        self.assertEqual([ node1, node2, node3 ], result)

        result = self.util.component(self.graph, node2)

        self.assertEqual([ node2 ], result)

        result = self.util.component(self.graph, node3)

        self.assertEqual([ node3 ], result)

    def test_two_directed_edges_as_chain(self):
        node1, node2, node3 = 'A', 'B', 'C'

        self.graph.add_node(node1)
        self.graph.add_node(node2)
        self.graph.add_node(node3)

        self.graph.add_directed_edge(node1, node2)
        self.graph.add_directed_edge(node2, node3)

        result = self.util.component(self.graph, node1)

        self.assertEqual([ node1, node2, node3 ], result)

        result = self.util.component(self.graph, node2)

        self.assertEqual([ node2, node3 ], result)

        result = self.util.component(self.graph, node3)

        self.assertEqual([ node3 ], result)

    def test_three_directed_edges_as_cycle(self):
        node1, node2, node3 = 'A', 'B', 'C'

        self.graph.add_node(node1)
        self.graph.add_node(node2)
        self.graph.add_node(node3)

        self.graph.add_directed_edge(node1, node2)
        self.graph.add_directed_edge(node2, node3)
        self.graph.add_directed_edge(node3, node1)

        result = self.util.component(self.graph, node1)

        self.assertEqual([ node1, node2, node3 ], result)

        result = self.util.component(self.graph, node2)

        self.assertEqual([ node2, node3, node1 ], result)

        result = self.util.component(self.graph, node3)

        self.assertEqual([ node3, node1, node2 ], result)

    def test_two_undirected_edges_as_rays(self):
        node1, node2, node3 = 'A', 'B', 'C'

        self.graph.add_node(node1)
        self.graph.add_node(node2)
        self.graph.add_node(node3)

        self.graph.add_undirected_edge(node1, node2)
        self.graph.add_undirected_edge(node1, node3)

        result = self.util.component(self.graph, node1)

        self.assertEqual([ node1, node2, node3 ], result)

        result = self.util.component(self.graph, node2)

        self.assertEqual([ node2, node1, node3 ], result)

        result = self.util.component(self.graph, node3)

        self.assertEqual([ node3, node1, node2 ], result)

    def test_two_undirected_edges_as_chain(self):
        node1, node2, node3 = 'A', 'B', 'C'

        self.graph.add_node(node1)
        self.graph.add_node(node2)
        self.graph.add_node(node3)

        self.graph.add_undirected_edge(node1, node2)
        self.graph.add_undirected_edge(node2, node3)

        result = self.util.component(self.graph, node1)

        self.assertEqual([ node1, node2, node3 ], result)

        result = self.util.component(self.graph, node2)

        self.assertEqual([ node2, node1, node3 ], result)

        result = self.util.component(self.graph, node3)

        self.assertEqual([ node3, node2, node1 ], result)

    def test_three_undirected_edges_as_cycle(self):
        node1, node2, node3 = 'A', 'B', 'C'

        self.graph.add_node(node1)
        self.graph.add_node(node2)
        self.graph.add_node(node3)

        self.graph.add_undirected_edge(node1, node2)
        self.graph.add_undirected_edge(node2, node3)
        self.graph.add_undirected_edge(node3, node1)

        result = self.util.component(self.graph, node1)

        self.assertEqual([ node1, node2, node3 ], result)

        result = self.util.component(self.graph, node2)

        self.assertEqual([ node2, node1, node3 ], result)

        result = self.util.component(self.graph, node3)

        self.assertEqual([ node3, node2, node1 ], result)

    def test_undirected_edges_as_one_component(self):
        (node_a, node_b, node_c, node_d, node_e, node_f,
         node_g, node_h) = 'A', 'B', 'C', 'D', 'E', 'F', 'G', 'H'

        self.graph.add_node(node_a)
        self.graph.add_node(node_b)
        self.graph.add_node(node_c)
        self.graph.add_node(node_d)
        self.graph.add_node(node_e)
        self.graph.add_node(node_f)
        self.graph.add_node(node_g)
        self.graph.add_node(node_h)

        self.graph.add_undirected_edge(node_a, node_b)
        self.graph.add_undirected_edge(node_a, node_c)
        self.graph.add_undirected_edge(node_b, node_c)
        self.graph.add_undirected_edge(node_c, node_d)
        self.graph.add_undirected_edge(node_c, node_h)
        self.graph.add_undirected_edge(node_d, node_e)
        self.graph.add_undirected_edge(node_e, node_f)
        self.graph.add_undirected_edge(node_e, node_g)
        self.graph.add_undirected_edge(node_f, node_g)
        self.graph.add_undirected_edge(node_g, node_h)

        result = self.util.component(self.graph, node_a)

        self.assertEqual([ node_a, node_b, node_c, node_d, node_h,
                          node_e, node_g, node_f ],
                         result)

        result = self.util.component(self.graph, node_b)

        self.assertEqual([ node_b, node_a, node_c, node_d, node_h,
                          node_e, node_g, node_f ],
                         result)

        result = self.util.component(self.graph, node_c)

        self.assertEqual([ node_c, node_a, node_b, node_d, node_h,
                          node_e, node_g, node_f ],
                         result)

        result = self.util.component(self.graph, node_d)

        self.assertEqual([ node_d, node_c, node_e, node_a, node_b,
                          node_h, node_f, node_g ],
                         result)

        result = self.util.component(self.graph, node_e)

        self.assertEqual([ node_e, node_d, node_f, node_g, node_c,
                          node_h, node_a, node_b ],
                         result)

        result = self.util.component(self.graph, node_f)

        self.assertEqual([ node_f, node_e, node_g, node_d, node_h,
                          node_c, node_a, node_b ],
                         result)

        result = self.util.component(self.graph, node_g)

        self.assertEqual([ node_g, node_e, node_f, node_h, node_d,
                          node_c, node_a, node_b ],
                         result)

        result = self.util.component(self.graph, node_h)

        self.assertEqual([ node_h, node_c, node_g, node_a, node_b,
                          node_d, node_e, node_f ],
                         result)

    def test_many_undirected_edges_as_two_components(self):
        (node_a, node_b, node_c, node_d, node_e, node_f,
         node_g, node_h, node_i, node_j) = \
            'A', 'B', 'C', 'D', 'E', 'F', 'G', 'H', 'I', 'J'

        self.graph.add_node(node_a)
        self.graph.add_node(node_b)
        self.graph.add_node(node_c)
        self.graph.add_node(node_d)
        self.graph.add_node(node_e)
        self.graph.add_node(node_f)
        self.graph.add_node(node_g)
        self.graph.add_node(node_h)
        self.graph.add_node(node_i)
        self.graph.add_node(node_j)

        self.graph.add_undirected_edge(node_a, node_c)
        self.graph.add_undirected_edge(node_a, node_d)
        self.graph.add_undirected_edge(node_a, node_f)
        self.graph.add_undirected_edge(node_b, node_e)
        self.graph.add_undirected_edge(node_c, node_h)
        self.graph.add_undirected_edge(node_c, node_i)
        self.graph.add_undirected_edge(node_e, node_g)
        self.graph.add_undirected_edge(node_e, node_j)
        self.graph.add_undirected_edge(node_f, node_i)
        self.graph.add_undirected_edge(node_h, node_i)

        result = self.util.component(self.graph, node_a)

        self.assertEqual([ node_a, node_c, node_d, node_f, node_h,
                          node_i ],
                         result)

        result = self.util.component(self.graph, node_b)

        self.assertEqual([ node_b, node_e, node_g, node_j ],
                         result)

        result = self.util.component(self.graph, node_c)

        self.assertEqual([ node_c, node_a, node_h, node_i, node_d,
                          node_f ],
                         result)

        result = self.util.component(self.graph, node_d)

        self.assertEqual([ node_d, node_a, node_c, node_f, node_h,
                          node_i ],
                         result)

        result = self.util.component(self.graph, node_e)

        self.assertEqual([ node_e, node_b, node_g, node_j ],
                         result)

        result = self.util.component(self.graph, node_f)

        self.assertEqual([ node_f, node_a, node_i, node_c, node_d,
                          node_h ],
                         result)

        result = self.util.component(self.graph, node_g)

        self.assertEqual([ node_g, node_e, node_b, node_j ],
                         result)

        result = self.util.component(self.graph, node_i)

        self.assertEqual([ node_i, node_c, node_f, node_h, node_a,
                          node_d ],
                         result)

        result = self.util.component(self.graph, node_j)

        self.assertEqual([ node_j, node_e, node_b, node_g ],
                         result)

class ExploreTestCase(unittest.TestCase):

    def setUp(self):
        self.util = graph_util.GraphUtil()
        self.graph = graph_util.Graph()

    def tearDown(self):
        pass

    def test_empty_graph(self):
        node = 'A'

        result = self.util.explore(self.graph, node)

        Util.assert_items(self, [ node ], result)

    def test_empty_graph_previsit(self):
        node = 'A'

        previsit_result = []

        result = self.util.explore(self.graph,
                                   node,
                                   lambda x: previsit_result.append(x))

        Util.assert_items(self, [ node ], result)
        self.assertEqual([ node ], previsit_result)

    def test_empty_graph_previsit_postvisit(self):
        node = 'A'

        previsit_result = []
        postvisit_result = []

        result = self.util.explore(self.graph,
                                   node,
                                   lambda x: previsit_result.append(x),
                                   lambda x: postvisit_result.append(x))

        Util.assert_items(self, [ node ], result)
        self.assertEqual([ node ], previsit_result)
        self.assertEqual([ node ], postvisit_result)

    def test_one_directed_edge(self):
        node1, node2 = 'A', 'B'

        self.graph.add_node(node1)
        self.graph.add_node(node2)

        self.graph.add_directed_edge(node1, node2)

        result = self.util.explore(self.graph, node1)

        Util.assert_items(self, [ node1, node2 ], result)

        result = self.util.explore(self.graph, node2)

        Util.assert_items(self, [ node2 ], result)

    def test_one_directed_edge_previsit(self):
        node1, node2 = 'A', 'B'

        self.graph.add_node(node1)
        self.graph.add_node(node2)

        self.graph.add_directed_edge(node1, node2)

        previsit_result = []

        result = self.util.explore(self.graph,
                                   node1,
                                   lambda x: previsit_result.append(x))

        Util.assert_items(self, [ node1, node2 ], result)
        self.assertEqual([ node1, node2 ], previsit_result)

        previsit_result = []

        result = self.util.explore(self.graph,
                                   node2,
                                   lambda x: previsit_result.append(x))

        Util.assert_items(self, [ node2 ], result)
        self.assertEqual([ node2 ], previsit_result)

    def test_one_directed_edge_previsit_postvisit(self):
        node1, node2 = 'A', 'B'

        self.graph.add_node(node1)
        self.graph.add_node(node2)

        self.graph.add_directed_edge(node1, node2)

        previsit_result = []
        postvisit_result = []

        result = self.util.explore(self.graph,
                                   node1,
                                   lambda x: previsit_result.append(x),
                                   lambda x: postvisit_result.append(x))

        Util.assert_items(self, [ node1, node2 ], result)
        self.assertEqual([ node1, node2 ], previsit_result)
        self.assertEqual([ node2, node1 ], postvisit_result)

        previsit_result = []
        postvisit_result = []

        result = self.util.explore(self.graph,
                                   node2,
                                   lambda x: previsit_result.append(x),
                                   lambda x: postvisit_result.append(x))

        Util.assert_items(self, [ node2 ], result)
        self.assertEqual([ node2 ], previsit_result)
        self.assertEqual([ node2 ], postvisit_result)

    def test_one_undirected_edge(self):
        node1, node2 = 'A', 'B'

        self.graph.add_node(node1)
        self.graph.add_node(node2)

        self.graph.add_undirected_edge(node1, node2)

        result = self.util.explore(self.graph, node1)

        Util.assert_items(self, [ node1, node2 ], result)

        result = self.util.explore(self.graph, node2)

        Util.assert_items(self, [ node1, node2 ], result)

    def test_one_undirected_edge_previsit(self):
        node1, node2 = 'A', 'B'

        self.graph.add_node(node1)
        self.graph.add_node(node2)

        self.graph.add_undirected_edge(node1, node2)

        previsit_result = []

        result = self.util.explore(self.graph,
                                   node1,
                                   lambda x: previsit_result.append(x))

        Util.assert_items(self, [ node1, node2 ], result)
        self.assertEqual([ node1, node2 ], previsit_result)

        previsit_result = []

        result = self.util.explore(self.graph,
                                   node2,
                                   lambda x: previsit_result.append(x))

        Util.assert_items(self, [ node1, node2 ], result)
        self.assertEqual([ node2, node1 ], previsit_result)

    def test_one_undirected_edge_previsit_postvisit(self):
        node1, node2 = 'A', 'B'

        self.graph.add_node(node1)
        self.graph.add_node(node2)

        self.graph.add_undirected_edge(node1, node2)

        previsit_result = []
        postvisit_result = []

        result = self.util.explore(self.graph,
                                   node1,
                                   lambda x: previsit_result.append(x),
                                   lambda x: postvisit_result.append(x))

        Util.assert_items(self, [ node1, node2 ], result)
        self.assertEqual([ node1, node2 ], previsit_result)
        self.assertEqual([ node2, node1 ], postvisit_result)

        previsit_result = []
        postvisit_result = []

        result = self.util.explore(self.graph,
                                   node2,
                                   lambda x: previsit_result.append(x),
                                   lambda x: postvisit_result.append(x))

        Util.assert_items(self, [ node1, node2 ], result)
        self.assertEqual([ node2, node1 ], previsit_result)
        self.assertEqual([ node1, node2 ], postvisit_result)

    def test_two_directed_edges_as_rays(self):
        node1, node2, node3 = 'A', 'B', 'C'

        self.graph.add_node(node1)
        self.graph.add_node(node2)
        self.graph.add_node(node3)

        self.graph.add_directed_edge(node1, node2)
        self.graph.add_directed_edge(node1, node3)

        result = self.util.explore(self.graph, node1)

        Util.assert_items(self, [ node1, node2, node3 ], result)

        result = self.util.explore(self.graph, node2)

        Util.assert_items(self, [ node2 ], result)

        result = self.util.explore(self.graph, node3)

        Util.assert_items(self, [ node3 ], result)

    def test_two_directed_edges_as_rays_previsit(self):
        node1, node2, node3 = 'A', 'B', 'C'

        self.graph.add_node(node1)
        self.graph.add_node(node2)
        self.graph.add_node(node3)

        self.graph.add_directed_edge(node1, node2)
        self.graph.add_directed_edge(node1, node3)

        previsit_result = []

        result = self.util.explore(self.graph,
                                   node1,
                                   lambda x: previsit_result.append(x))

        Util.assert_items(self, [ node1, node2, node3 ], result)
        self.assertEqual([ node1, node2, node3 ], previsit_result)

        previsit_result = []

        result = self.util.explore(self.graph,
                                   node2,
                                   lambda x: previsit_result.append(x))

        Util.assert_items(self, [ node2 ], result)
        self.assertEqual([ node2 ], previsit_result)

        previsit_result = []

        result = self.util.explore(self.graph,
                                   node3,
                                   lambda x: previsit_result.append(x))

        Util.assert_items(self, [ node3 ], result)
        self.assertEqual([ node3 ], previsit_result)

    def test_two_directed_edges_as_rays_previsit_postvisit(self):
        node1, node2, node3 = 'A', 'B', 'C'

        self.graph.add_node(node1)
        self.graph.add_node(node2)
        self.graph.add_node(node3)

        self.graph.add_directed_edge(node1, node2)
        self.graph.add_directed_edge(node1, node3)

        previsit_result = []
        postvisit_result = []

        result = self.util.explore(self.graph,
                                   node1,
                                   lambda x: previsit_result.append(x),
                                   lambda x: postvisit_result.append(x))

        Util.assert_items(self, [ node1, node2, node3 ], result)
        self.assertEqual([ node1, node2, node3 ], previsit_result)
        self.assertEqual([ node2, node3, node1 ], postvisit_result)

        previsit_result = []
        postvisit_result = []

        result = self.util.explore(self.graph,
                                   node2,
                                   lambda x: previsit_result.append(x),
                                   lambda x: postvisit_result.append(x))

        Util.assert_items(self, [ node2 ], result)
        self.assertEqual([ node2 ], previsit_result)
        self.assertEqual([ node2 ], postvisit_result)

        previsit_result = []
        postvisit_result = []

        result = self.util.explore(self.graph,
                                   node3,
                                   lambda x: previsit_result.append(x),
                                   lambda x: postvisit_result.append(x))

        Util.assert_items(self, [ node3 ], result)
        self.assertEqual([ node3 ], previsit_result)
        self.assertEqual([ node3 ], postvisit_result)

    def test_two_directed_edges_as_chain(self):
        node1, node2, node3 = 'A', 'B', 'C'

        self.graph.add_node(node1)
        self.graph.add_node(node2)
        self.graph.add_node(node3)

        self.graph.add_directed_edge(node1, node2)
        self.graph.add_directed_edge(node2, node3)

        result = self.util.explore(self.graph, node1)

        Util.assert_items(self, [ node1, node2, node3 ], result)

        result = self.util.explore(self.graph, node2)

        Util.assert_items(self, [ node2, node3 ], result)

        result = self.util.explore(self.graph, node3)

        Util.assert_items(self, [ node3 ], result)

    def test_two_directed_edges_as_chain_previsit(self):
        node1, node2, node3 = 'A', 'B', 'C'

        self.graph.add_node(node1)
        self.graph.add_node(node2)
        self.graph.add_node(node3)

        self.graph.add_directed_edge(node1, node2)
        self.graph.add_directed_edge(node2, node3)

        previsit_result = []

        result = self.util.explore(self.graph,
                                   node1,
                                   lambda x: previsit_result.append(x))

        Util.assert_items(self, [ node1, node2, node3 ], result)
        self.assertEqual([ node1, node2, node3 ], previsit_result)

        previsit_result = []

        result = self.util.explore(self.graph,
                                   node2,
                                   lambda x: previsit_result.append(x))

        Util.assert_items(self, [ node2, node3 ], result)
        self.assertEqual([ node2, node3 ], previsit_result)

        previsit_result = []

        result = self.util.explore(self.graph,
                                   node3,
                                   lambda x: previsit_result.append(x))

        Util.assert_items(self, [ node3 ], result)
        self.assertEqual([ node3 ], previsit_result)

    def test_two_directed_edges_as_chain_previsit_postvisit(self):
        node1, node2, node3 = 'A', 'B', 'C'

        self.graph.add_node(node1)
        self.graph.add_node(node2)
        self.graph.add_node(node3)

        self.graph.add_directed_edge(node1, node2)
        self.graph.add_directed_edge(node2, node3)

        previsit_result = []
        postvisit_result = []

        result = self.util.explore(self.graph,
                                   node1,
                                   lambda x: previsit_result.append(x),
                                   lambda x: postvisit_result.append(x))

        Util.assert_items(self, [ node1, node2, node3 ], result)
        self.assertEqual([ node1, node2, node3 ], previsit_result)
        self.assertEqual([ node3, node2, node1 ], postvisit_result)

        previsit_result = []
        postvisit_result = []

        result = self.util.explore(self.graph,
                                   node2,
                                   lambda x: previsit_result.append(x),
                                   lambda x: postvisit_result.append(x))

        Util.assert_items(self, [ node2, node3 ], result)
        self.assertEqual([ node2, node3 ], previsit_result)
        self.assertEqual([ node3, node2 ], postvisit_result)

        previsit_result = []
        postvisit_result = []

        result = self.util.explore(self.graph,
                                   node3,
                                   lambda x: previsit_result.append(x),
                                   lambda x: postvisit_result.append(x))

        Util.assert_items(self, [ node3 ], result)
        self.assertEqual([ node3 ], previsit_result)
        self.assertEqual([ node3 ], postvisit_result)

    def test_three_directed_edges_as_cycle(self):
        node1, node2, node3 = 'A', 'B', 'C'

        self.graph.add_node(node1)
        self.graph.add_node(node2)
        self.graph.add_node(node3)

        self.graph.add_directed_edge(node1, node2)
        self.graph.add_directed_edge(node2, node3)
        self.graph.add_directed_edge(node3, node1)

        result = self.util.explore(self.graph, node1)

        Util.assert_items(self, [ node1, node2, node3 ], result)

        result = self.util.explore(self.graph, node2)

        Util.assert_items(self, [ node2, node3, node1 ], result)

        result = self.util.explore(self.graph, node3)

        Util.assert_items(self, [ node3, node1, node2 ], result)

    def test_three_directed_edges_as_cycle_previsit(self):
        node1, node2, node3 = 'A', 'B', 'C'

        self.graph.add_node(node1)
        self.graph.add_node(node2)
        self.graph.add_node(node3)

        self.graph.add_directed_edge(node1, node2)
        self.graph.add_directed_edge(node2, node3)
        self.graph.add_directed_edge(node3, node1)

        previsit_result = []

        result = self.util.explore(self.graph,
                                   node1,
                                   lambda x: previsit_result.append(x))

        Util.assert_items(self, [ node1, node2, node3 ], result)
        self.assertEqual([ node1, node2, node3 ], previsit_result)

        previsit_result = []

        result = self.util.explore(self.graph,
                                   node2,
                                   lambda x: previsit_result.append(x))

        Util.assert_items(self, [ node2, node3, node1 ], result)
        self.assertEqual([ node2, node3, node1 ], previsit_result)

        previsit_result = []

        result = self.util.explore(self.graph,
                                   node3,
                                   lambda x: previsit_result.append(x))

        Util.assert_items(self, [ node3, node1, node2 ], result)
        self.assertEqual([ node3, node1, node2 ], previsit_result)

    def test_three_directed_edges_as_cycle_previsit_postvisit(self):
        node1, node2, node3 = 'A', 'B', 'C'

        self.graph.add_node(node1)
        self.graph.add_node(node2)
        self.graph.add_node(node3)

        self.graph.add_directed_edge(node1, node2)
        self.graph.add_directed_edge(node2, node3)
        self.graph.add_directed_edge(node3, node1)

        previsit_result = []
        postvisit_result = []

        result = self.util.explore(self.graph,
                                   node1,
                                   lambda x: previsit_result.append(x),
                                   lambda x: postvisit_result.append(x))

        Util.assert_items(self, [ node1, node2, node3 ], result)
        self.assertEqual([ node1, node2, node3 ], previsit_result)
        self.assertEqual([ node3, node2, node1 ], postvisit_result)

        previsit_result = []
        postvisit_result = []

        result = self.util.explore(self.graph,
                                   node2,
                                   lambda x: previsit_result.append(x),
                                   lambda x: postvisit_result.append(x))

        Util.assert_items(self, [ node2, node3, node1 ], result)
        self.assertEqual([ node2, node3, node1 ], previsit_result)
        self.assertEqual([ node1, node3, node2 ], postvisit_result)

        previsit_result = []
        postvisit_result = []

        result = self.util.explore(self.graph,
                                   node3,
                                   lambda x: previsit_result.append(x),
                                   lambda x: postvisit_result.append(x))

        Util.assert_items(self, [ node3, node1, node2 ], result)
        self.assertEqual([ node3, node1, node2 ], previsit_result)
        self.assertEqual([ node2, node1, node3 ], postvisit_result)

    def test_two_undirected_edges_as_rays(self):
        node1, node2, node3 = 'A', 'B', 'C'

        self.graph.add_node(node1)
        self.graph.add_node(node2)
        self.graph.add_node(node3)

        self.graph.add_undirected_edge(node1, node2)
        self.graph.add_undirected_edge(node1, node3)

        result = self.util.explore(self.graph, node1)

        Util.assert_items(self, [ node1, node2, node3 ], result)

        result = self.util.explore(self.graph, node2)

        Util.assert_items(self, [ node2, node1, node3 ], result)

        result = self.util.explore(self.graph, node3)

        Util.assert_items(self, [ node3, node1, node2 ], result)

    def test_two_undirected_edges_as_rays_previsit(self):
        node1, node2, node3 = 'A', 'B', 'C'

        self.graph.add_node(node1)
        self.graph.add_node(node2)
        self.graph.add_node(node3)

        self.graph.add_undirected_edge(node1, node2)
        self.graph.add_undirected_edge(node1, node3)

        previsit_result = []

        result = self.util.explore(self.graph,
                                   node1,
                                   lambda x: previsit_result.append(x))

        Util.assert_items(self, [ node1, node2, node3 ], result)
        self.assertEqual([ node1, node2, node3 ], previsit_result)

        previsit_result = []

        result = self.util.explore(self.graph,
                                   node2,
                                   lambda x: previsit_result.append(x))

        Util.assert_items(self, [ node2, node1, node3 ], result)
        self.assertEqual([ node2, node1, node3 ], previsit_result)

        previsit_result = []

        result = self.util.explore(self.graph,
                                   node3,
                                   lambda x: previsit_result.append(x))

        Util.assert_items(self, [ node3, node1, node2 ], result)
        self.assertEqual([ node3, node1, node2 ], previsit_result)

    def test_two_undirected_edges_as_rays_previsit_postvisit(self):
        node1, node2, node3 = 'A', 'B', 'C'

        self.graph.add_node(node1)
        self.graph.add_node(node2)
        self.graph.add_node(node3)

        self.graph.add_undirected_edge(node1, node2)
        self.graph.add_undirected_edge(node1, node3)

        previsit_result = []
        postvisit_result = []

        result = self.util.explore(self.graph,
                                   node1,
                                   lambda x: previsit_result.append(x),
                                   lambda x: postvisit_result.append(x))

        Util.assert_items(self, [ node1, node2, node3 ], result)
        self.assertEqual([ node1, node2, node3 ], previsit_result)
        self.assertEqual([ node2, node3, node1 ], postvisit_result)

        previsit_result = []
        postvisit_result = []

        result = self.util.explore(self.graph,
                                   node2,
                                   lambda x: previsit_result.append(x),
                                   lambda x: postvisit_result.append(x))

        Util.assert_items(self, [ node2, node1, node3 ], result)
        self.assertEqual([ node2, node1, node3 ], previsit_result)
        self.assertEqual([ node3, node1, node2 ], postvisit_result)

        previsit_result = []
        postvisit_result = []

        result = self.util.explore(self.graph,
                                   node3,
                                   lambda x: previsit_result.append(x),
                                   lambda x: postvisit_result.append(x))

        Util.assert_items(self, [ node3, node1, node2 ], result)
        self.assertEqual([ node3, node1, node2 ], previsit_result)
        self.assertEqual([ node2, node1, node3 ], postvisit_result)

    def test_two_undirected_edges_as_chain(self):
        node1, node2, node3 = 'A', 'B', 'C'
        self.graph.add_node(node1)
        self.graph.add_node(node2)
        self.graph.add_node(node3)
        self.graph.add_undirected_edge(node1, node2)
        self.graph.add_undirected_edge(node2, node3)

        result = self.util.explore(self.graph, node1)

        Util.assert_items(self, [ node1, node2, node3 ], result)

        result = self.util.explore(self.graph, node2)

        Util.assert_items(self, [ node2, node1, node3 ], result)

        result = self.util.explore(self.graph, node3)

        Util.assert_items(self, [ node3, node2, node1 ], result)

    def test_two_undirected_edges_as_chain_previsit(self):
        node1, node2, node3 = 'A', 'B', 'C'

        self.graph.add_node(node1)
        self.graph.add_node(node2)
        self.graph.add_node(node3)

        self.graph.add_undirected_edge(node1, node2)
        self.graph.add_undirected_edge(node2, node3)

        previsit_result = []

        result = self.util.explore(self.graph,
                                   node1,
                                   lambda x: previsit_result.append(x))

        Util.assert_items(self, [ node1, node2, node3 ], result)
        self.assertEqual([ node1, node2, node3 ], previsit_result)

        previsit_result = []

        result = self.util.explore(self.graph,
                                   node2,
                                   lambda x: previsit_result.append(x))

        Util.assert_items(self, [ node2, node1, node3 ], result)
        self.assertEqual([ node2, node1, node3 ], previsit_result)

        previsit_result = []

        result = self.util.explore(self.graph,
                                   node3,
                                   lambda x: previsit_result.append(x))

        Util.assert_items(self, [ node3, node2, node1 ], result)
        self.assertEqual([ node3, node2, node1 ], previsit_result)

    def test_two_undirected_edges_as_chain_previsit_postvisit(self):
        node1, node2, node3 = 'A', 'B', 'C'

        self.graph.add_node(node1)
        self.graph.add_node(node2)
        self.graph.add_node(node3)

        self.graph.add_undirected_edge(node1, node2)
        self.graph.add_undirected_edge(node2, node3)

        previsit_result = []
        postvisit_result = []

        result = self.util.explore(self.graph,
                                   node1,
                                   lambda x: previsit_result.append(x),
                                   lambda x: postvisit_result.append(x))

        Util.assert_items(self, [ node1, node2, node3 ], result)
        self.assertEqual([ node1, node2, node3 ], previsit_result)
        self.assertEqual([ node3, node2, node1 ], postvisit_result)

        previsit_result = []
        postvisit_result = []

        result = self.util.explore(self.graph,
                                   node2,
                                   lambda x: previsit_result.append(x),
                                   lambda x: postvisit_result.append(x))

        Util.assert_items(self, [ node2, node1, node3 ], result)
        self.assertEqual([ node2, node1, node3 ], previsit_result)
        self.assertEqual([ node1, node3, node2 ], postvisit_result)

        previsit_result = []
        postvisit_result = []

        result = self.util.explore(self.graph,
                                   node3,
                                   lambda x: previsit_result.append(x),
                                   lambda x: postvisit_result.append(x))

        Util.assert_items(self, [ node3, node2, node1 ], result)
        self.assertEqual([ node3, node2, node1 ], previsit_result)
        self.assertEqual([ node1, node2, node3 ], postvisit_result)

    def test_three_undirected_edges_as_cycle(self):
        node1, node2, node3 = 'A', 'B', 'C'

        self.graph.add_node(node1)
        self.graph.add_node(node2)
        self.graph.add_node(node3)

        self.graph.add_undirected_edge(node1, node2)
        self.graph.add_undirected_edge(node2, node3)
        self.graph.add_undirected_edge(node3, node1)

        result = self.util.explore(self.graph, node1)

        Util.assert_items(self, [ node1, node2, node3 ], result)

        result = self.util.explore(self.graph, node2)

        Util.assert_items(self, [ node2, node1, node3 ], result)

        result = self.util.explore(self.graph, node3)

        Util.assert_items(self, [ node3, node2, node1 ], result)

    def test_three_undirected_edges_as_cycle_previsit(self):
        node1, node2, node3 = 'A', 'B', 'C'

        self.graph.add_node(node1)
        self.graph.add_node(node2)
        self.graph.add_node(node3)

        self.graph.add_undirected_edge(node1, node2)
        self.graph.add_undirected_edge(node2, node3)
        self.graph.add_undirected_edge(node3, node1)

        previsit_result = []

        result = self.util.explore(self.graph,
                                   node1,
                                   lambda x: previsit_result.append(x))

        Util.assert_items(self, [ node1, node2, node3 ], result)
        self.assertEqual([ node1, node2, node3 ], previsit_result)

        previsit_result = []

        result = self.util.explore(self.graph,
                                   node2,
                                   lambda x: previsit_result.append(x))

        Util.assert_items(self, [ node2, node1, node3 ], result)
        self.assertEqual([ node2, node1, node3 ], previsit_result)

        previsit_result = []

        result = self.util.explore(self.graph,
                                   node3,
                                   lambda x: previsit_result.append(x))

        Util.assert_items(self, [ node3, node2, node1 ], result)
        self.assertEqual([ node3, node2, node1 ], previsit_result)

    def test_three_undirected_edges_as_cycle_previsit_postvisit(self):
        node1, node2, node3 = 'A', 'B', 'C'

        self.graph.add_node(node1)
        self.graph.add_node(node2)
        self.graph.add_node(node3)

        self.graph.add_undirected_edge(node1, node2)
        self.graph.add_undirected_edge(node2, node3)
        self.graph.add_undirected_edge(node3, node1)

        previsit_result = []
        postvisit_result = []

        result = self.util.explore(self.graph,
                                   node1,
                                   lambda x: previsit_result.append(x),
                                   lambda x: postvisit_result.append(x))

        Util.assert_items(self, [ node1, node2, node3 ], result)
        self.assertEqual([ node1, node2, node3 ], previsit_result)
        self.assertEqual([ node3, node2, node1 ], postvisit_result)

        previsit_result = []
        postvisit_result = []

        result = self.util.explore(self.graph,
                                   node2,
                                   lambda x: previsit_result.append(x),
                                   lambda x: postvisit_result.append(x))

        Util.assert_items(self, [ node2, node1, node3 ], result)
        self.assertEqual([ node2, node1, node3 ], previsit_result)
        self.assertEqual([ node3, node1, node2 ], postvisit_result)

        previsit_result = []
        postvisit_result = []

        result = self.util.explore(self.graph,
                                   node3,
                                   lambda x: previsit_result.append(x),
                                   lambda x: postvisit_result.append(x))

        Util.assert_items(self, [ node3, node2, node1 ], result)
        self.assertEqual([ node3, node2, node1 ], previsit_result)
        self.assertEqual([ node1, node2, node3 ], postvisit_result)

    def test_undirected_edges_as_one_component(self):
        (node_a, node_b, node_c, node_d, node_e, node_f,
         node_g, node_h) = 'A', 'B', 'C', 'D', 'E', 'F', 'G', 'H'

        self.graph.add_node(node_a)
        self.graph.add_node(node_b)
        self.graph.add_node(node_c)
        self.graph.add_node(node_d)
        self.graph.add_node(node_e)
        self.graph.add_node(node_f)
        self.graph.add_node(node_g)
        self.graph.add_node(node_h)

        self.graph.add_undirected_edge(node_a, node_b)
        self.graph.add_undirected_edge(node_a, node_c)
        self.graph.add_undirected_edge(node_b, node_c)
        self.graph.add_undirected_edge(node_c, node_d)
        self.graph.add_undirected_edge(node_c, node_h)
        self.graph.add_undirected_edge(node_d, node_e)
        self.graph.add_undirected_edge(node_e, node_f)
        self.graph.add_undirected_edge(node_e, node_g)
        self.graph.add_undirected_edge(node_f, node_g)
        self.graph.add_undirected_edge(node_g, node_h)

        result = self.util.explore(self.graph, node_a)

        Util.assert_items(self, [ node_a, node_b, node_c, node_d, node_e,
                                 node_f, node_g, node_h ],
                          result)

        result = self.util.explore(self.graph, node_b)

        Util.assert_items(self, [ node_b, node_a, node_c, node_d, node_e,
                                 node_f, node_g, node_h ],
                          result)

        result = self.util.explore(self.graph, node_c)

        Util.assert_items(self, [ node_c, node_a, node_b, node_d, node_e,
                                 node_f, node_g, node_h ],
                          result)

        result = self.util.explore(self.graph, node_d)

        Util.assert_items(self, [ node_d, node_c, node_a, node_b, node_h,
                                 node_g, node_e, node_f ],
                          result)

        result = self.util.explore(self.graph, node_e)

        Util.assert_items(self, [ node_e, node_d, node_c, node_a, node_b,
                                 node_h, node_g, node_f ],
                          result)

        result = self.util.explore(self.graph, node_f)

        Util.assert_items(self, [ node_f, node_e, node_d, node_c, node_a,
                                 node_b, node_h, node_g ],
                          result)

        result = self.util.explore(self.graph, node_g)

        Util.assert_items(self, [ node_g, node_e, node_d, node_c, node_a,
                                 node_b, node_h, node_f ],
                          result)

        result = self.util.explore(self.graph, node_h)

        Util.assert_items(self, [ node_h, node_c, node_a, node_b, node_d,
                                 node_e, node_f, node_g ],
                          result)

    def test_undirected_edges_as_one_component_previsit(self):
        (node_a, node_b, node_c, node_d, node_e, node_f,
         node_g, node_h) = 'A', 'B', 'C', 'D', 'E', 'F', 'G', 'H'

        self.graph.add_node(node_a)
        self.graph.add_node(node_b)
        self.graph.add_node(node_c)
        self.graph.add_node(node_d)
        self.graph.add_node(node_e)
        self.graph.add_node(node_f)
        self.graph.add_node(node_g)
        self.graph.add_node(node_h)

        self.graph.add_undirected_edge(node_a, node_b)
        self.graph.add_undirected_edge(node_a, node_c)
        self.graph.add_undirected_edge(node_b, node_c)
        self.graph.add_undirected_edge(node_c, node_d)
        self.graph.add_undirected_edge(node_c, node_h)
        self.graph.add_undirected_edge(node_d, node_e)
        self.graph.add_undirected_edge(node_e, node_f)
        self.graph.add_undirected_edge(node_e, node_g)
        self.graph.add_undirected_edge(node_f, node_g)
        self.graph.add_undirected_edge(node_g, node_h)

        previsit_result = []

        result = self.util.explore(self.graph,
                                   node_a,
                                   lambda x: previsit_result.append(x))

        Util.assert_items(self, [ node_a, node_b, node_c, node_d, node_e,
                                 node_f, node_g, node_h ],
                          result)
        self.assertEqual([ node_a, node_b, node_c, node_d, node_e,
                          node_f, node_g, node_h ],
                         previsit_result)

        previsit_result = []

        result = self.util.explore(self.graph,
                                   node_b,
                                   lambda x: previsit_result.append(x))

        Util.assert_items(self, [ node_b, node_a, node_c, node_d, node_e,
                                 node_f, node_g, node_h ],
                          result)
        self.assertEqual([ node_b, node_a, node_c, node_d, node_e,
                          node_f, node_g, node_h ],
                         previsit_result)

        previsit_result = []

        result = self.util.explore(self.graph,
                                   node_c,
                                   lambda x: previsit_result.append(x))

        Util.assert_items(self, [ node_c, node_a, node_b, node_d, node_e,
                                 node_f, node_g, node_h ],
                          result)
        self.assertEqual([ node_c, node_a, node_b, node_d, node_e,
                          node_f, node_g, node_h ],
                         previsit_result)

        previsit_result = []

        result = self.util.explore(self.graph,
                                   node_d,
                                   lambda x: previsit_result.append(x))

        Util.assert_items(self, [ node_d, node_c, node_a, node_b, node_h,
                                 node_g, node_e, node_f ],
                          result)
        self.assertEqual([ node_d, node_c, node_a, node_b, node_h,
                          node_g, node_e, node_f ],
                         previsit_result)

        previsit_result = []

        result = self.util.explore(self.graph,
                                   node_e,
                                   lambda x: previsit_result.append(x))

        Util.assert_items(self, [ node_e, node_d, node_c, node_a, node_b,
                                 node_h, node_g, node_f ],
                          result)
        self.assertEqual([ node_e, node_d, node_c, node_a, node_b,
                          node_h, node_g, node_f ],
                         previsit_result)

        previsit_result = []

        result = self.util.explore(self.graph,
                                   node_f,
                                   lambda x: previsit_result.append(x))

        Util.assert_items(self, [ node_f, node_e, node_d, node_c, node_a,
                                 node_b, node_h, node_g ],
                          result)
        self.assertEqual([ node_f, node_e, node_d, node_c, node_a,
                          node_b, node_h, node_g ],
                         previsit_result)

        previsit_result = []

        result = self.util.explore(self.graph,
                                   node_g,
                                   lambda x: previsit_result.append(x))

        Util.assert_items(self, [ node_g, node_e, node_d, node_c, node_a,
                                 node_b, node_h, node_f ],
                          result)
        self.assertEqual([ node_g, node_e, node_d, node_c, node_a,
                          node_b, node_h, node_f ],
                         previsit_result)

        previsit_result = []

        result = self.util.explore(self.graph,
                                   node_h,
                                   lambda x: previsit_result.append(x))

        Util.assert_items(self, [ node_h, node_c, node_a, node_b, node_d,
                                 node_e, node_f, node_g ],
                          result)
        self.assertEqual([ node_h, node_c, node_a, node_b, node_d,
                          node_e, node_f, node_g ],
                         previsit_result)

    def test_undirected_edges_as_one_component_previsit_postvisit(self):
        (node_a, node_b, node_c, node_d, node_e, node_f,
         node_g, node_h) = 'A', 'B', 'C', 'D', 'E', 'F', 'G', 'H'

        self.graph.add_node(node_a)
        self.graph.add_node(node_b)
        self.graph.add_node(node_c)
        self.graph.add_node(node_d)
        self.graph.add_node(node_e)
        self.graph.add_node(node_f)
        self.graph.add_node(node_g)
        self.graph.add_node(node_h)

        self.graph.add_undirected_edge(node_a, node_b)
        self.graph.add_undirected_edge(node_a, node_c)
        self.graph.add_undirected_edge(node_b, node_c)
        self.graph.add_undirected_edge(node_c, node_d)
        self.graph.add_undirected_edge(node_c, node_h)
        self.graph.add_undirected_edge(node_d, node_e)
        self.graph.add_undirected_edge(node_e, node_f)
        self.graph.add_undirected_edge(node_e, node_g)
        self.graph.add_undirected_edge(node_f, node_g)
        self.graph.add_undirected_edge(node_g, node_h)

        previsit_result = []
        postvisit_result = []

        result = self.util.explore(self.graph,
                                   node_a,
                                   lambda x: previsit_result.append(x),
                                   lambda x: postvisit_result.append(x))

        Util.assert_items(self, [ node_a, node_b, node_c, node_d, node_e,
                                 node_f, node_g, node_h ],
                          result)
        self.assertEqual([ node_a, node_b, node_c, node_d, node_e,
                          node_f, node_g, node_h ],
                         previsit_result)
        self.assertEqual([ node_h, node_g, node_f, node_e, node_d,
                          node_c, node_b, node_a ],
                         postvisit_result)

        previsit_result = []
        postvisit_result = []

        result = self.util.explore(self.graph,
                                   node_b,
                                   lambda x: previsit_result.append(x),
                                   lambda x: postvisit_result.append(x))

        Util.assert_items(self, [ node_b, node_a, node_c, node_d, node_e,
                                 node_f, node_g, node_h ],
                          result)
        self.assertEqual([ node_b, node_a, node_c, node_d, node_e,
                          node_f, node_g, node_h ],
                         previsit_result)
        self.assertEqual([ node_h, node_g, node_f, node_e, node_d,
                          node_c, node_a, node_b ],
                         postvisit_result)

        previsit_result = []
        postvisit_result = []

        result = self.util.explore(self.graph,
                                   node_c,
                                   lambda x: previsit_result.append(x),
                                   lambda x: postvisit_result.append(x))

        Util.assert_items(self, [ node_c, node_a, node_b, node_d, node_e,
                                 node_f, node_g, node_h ],
                          result)
        self.assertEqual([ node_c, node_a, node_b, node_d, node_e,
                          node_f, node_g, node_h ],
                         previsit_result)
        self.assertEqual([ node_b, node_a, node_h, node_g, node_f,
                          node_e, node_d, node_c ],
                         postvisit_result)

        previsit_result = []
        postvisit_result = []

        result = self.util.explore(self.graph,
                                   node_d,
                                   lambda x: previsit_result.append(x),
                                   lambda x: postvisit_result.append(x))

        Util.assert_items(self, [ node_d, node_c, node_a, node_b, node_h,
                                 node_g, node_e, node_f ],
                          result)
        self.assertEqual([ node_d, node_c, node_a, node_b, node_h,
                          node_g, node_e, node_f ],
                         previsit_result)
        self.assertEqual([ node_b, node_a, node_f, node_e, node_g,
                          node_h, node_c, node_d ],
                         postvisit_result)

        previsit_result = []
        postvisit_result = []

        result = self.util.explore(self.graph,
                                   node_e,
                                   lambda x: previsit_result.append(x),
                                   lambda x: postvisit_result.append(x))

        Util.assert_items(self, [ node_e, node_d, node_c, node_a, node_b,
                                 node_h, node_g, node_f ],
                          result)
        self.assertEqual([ node_e, node_d, node_c, node_a, node_b,
                          node_h, node_g, node_f ],
                         previsit_result)
        self.assertEqual([ node_b, node_a, node_f, node_g, node_h,
                          node_c, node_d, node_e ],
                         postvisit_result)

        previsit_result = []
        postvisit_result = []

        result = self.util.explore(self.graph,
                                   node_f,
                                   lambda x: previsit_result.append(x),
                                   lambda x: postvisit_result.append(x))

        Util.assert_items(self, [ node_f, node_e, node_d, node_c, node_a,
                                 node_b, node_h, node_g ],
                          result)
        self.assertEqual([ node_f, node_e, node_d, node_c, node_a,
                          node_b, node_h, node_g ],
                         previsit_result)
        self.assertEqual([ node_b, node_a, node_g, node_h, node_c,
                          node_d, node_e, node_f ],
                         postvisit_result)

        previsit_result = []
        postvisit_result = []

        result = self.util.explore(self.graph,
                                   node_g,
                                   lambda x: previsit_result.append(x),
                                   lambda x: postvisit_result.append(x))

        Util.assert_items(self, [ node_g, node_e, node_d, node_c, node_a,
                                 node_b, node_h, node_f ],
                          result)
        self.assertEqual([ node_g, node_e, node_d, node_c, node_a,
                          node_b, node_h, node_f ],
                         previsit_result)
        self.assertEqual([ node_b, node_a, node_h, node_c, node_d,
                          node_f, node_e, node_g ], postvisit_result)

        previsit_result = []
        postvisit_result = []

        result = self.util.explore(self.graph,
                                   node_h,
                                   lambda x: previsit_result.append(x),
                                   lambda x: postvisit_result.append(x))

        Util.assert_items(self, [ node_h, node_c, node_a, node_b, node_d,
                                 node_e, node_f, node_g ],
                          result)
        self.assertEqual([ node_h, node_c, node_a, node_b, node_d,
                          node_e, node_f, node_g ],
                         previsit_result)
        self.assertEqual([ node_b, node_a, node_g, node_f, node_e,
                          node_d, node_c, node_h ], postvisit_result)

    def test_undirected_edges_as_two_components(self):
        (node_a, node_b, node_c, node_d, node_e, node_f,
         node_g, node_h, node_i, node_j) = \
            'A', 'B', 'C', 'D', 'E', 'F', 'G', 'H', 'I', 'J'

        self.graph.add_node(node_a)
        self.graph.add_node(node_b)
        self.graph.add_node(node_c)
        self.graph.add_node(node_d)
        self.graph.add_node(node_e)
        self.graph.add_node(node_f)
        self.graph.add_node(node_g)
        self.graph.add_node(node_h)
        self.graph.add_node(node_i)
        self.graph.add_node(node_j)

        self.graph.add_undirected_edge(node_a, node_c)
        self.graph.add_undirected_edge(node_a, node_d)
        self.graph.add_undirected_edge(node_a, node_f)
        self.graph.add_undirected_edge(node_b, node_e)
        self.graph.add_undirected_edge(node_c, node_h)
        self.graph.add_undirected_edge(node_c, node_i)
        self.graph.add_undirected_edge(node_e, node_g)
        self.graph.add_undirected_edge(node_e, node_j)
        self.graph.add_undirected_edge(node_f, node_i)
        self.graph.add_undirected_edge(node_h, node_i)

        result = self.util.explore(self.graph, node_a)

        Util.assert_items(self, [ node_a, node_c, node_h, node_i, node_f,
                                 node_d ],
                          result)

        result = self.util.explore(self.graph, node_b)

        Util.assert_items(self, [ node_b, node_e, node_g, node_j ],
                          result)

        result = self.util.explore(self.graph, node_c)

        Util.assert_items(self, [ node_c, node_a, node_d, node_f, node_i,
                                 node_h ],
                          result)

        result = self.util.explore(self.graph, node_d)

        Util.assert_items(self, [ node_d, node_a, node_c, node_h, node_i,
                                 node_f ],
                          result)

        result = self.util.explore(self.graph, node_e)

        Util.assert_items(self, [ node_e, node_b, node_g, node_j ],
                          result)

        result = self.util.explore(self.graph, node_f)

        Util.assert_items(self, [ node_f, node_a, node_c, node_h, node_i,
                                 node_d ],
                          result)

        result = self.util.explore(self.graph, node_g)

        Util.assert_items(self, [ node_g, node_e, node_b, node_j ],
                          result)

        result = self.util.explore(self.graph, node_i)

        Util.assert_items(self, [ node_i, node_c, node_a, node_d, node_f,
                                 node_h ],
                          result)

        result = self.util.explore(self.graph, node_j)

        Util.assert_items(self, [ node_j, node_e, node_b, node_g ],
                          result)

    def test_undirected_edges_as_two_components_previsit(self):
        (node_a, node_b, node_c, node_d, node_e, node_f,
         node_g, node_h, node_i, node_j) = \
            'A', 'B', 'C', 'D', 'E', 'F', 'G', 'H', 'I', 'J'

        self.graph.add_node(node_a)
        self.graph.add_node(node_b)
        self.graph.add_node(node_c)
        self.graph.add_node(node_d)
        self.graph.add_node(node_e)
        self.graph.add_node(node_f)
        self.graph.add_node(node_g)
        self.graph.add_node(node_h)
        self.graph.add_node(node_i)
        self.graph.add_node(node_j)

        self.graph.add_undirected_edge(node_a, node_c)
        self.graph.add_undirected_edge(node_a, node_d)
        self.graph.add_undirected_edge(node_a, node_f)
        self.graph.add_undirected_edge(node_b, node_e)
        self.graph.add_undirected_edge(node_c, node_h)
        self.graph.add_undirected_edge(node_c, node_i)
        self.graph.add_undirected_edge(node_e, node_g)
        self.graph.add_undirected_edge(node_e, node_j)
        self.graph.add_undirected_edge(node_f, node_i)
        self.graph.add_undirected_edge(node_h, node_i)

        previsit_result = []

        result = self.util.explore(self.graph,
                                   node_a,
                                   lambda x: previsit_result.append(x))

        Util.assert_items(self, [ node_a, node_c, node_h, node_i, node_f,
                                 node_d ],
                          result)
        self.assertEqual([ node_a, node_c, node_h, node_i, node_f,
                          node_d ],
                         previsit_result)

        previsit_result = []

        result = self.util.explore(self.graph,
                                   node_b,
                                   lambda x: previsit_result.append(x))

        Util.assert_items(self, [ node_b, node_e, node_g, node_j ],
                          result)
        self.assertEqual([ node_b, node_e, node_g, node_j ],
                         previsit_result)

        previsit_result = []

        result = self.util.explore(self.graph,
                                   node_c,
                                   lambda x: previsit_result.append(x))

        Util.assert_items(self, [ node_c, node_a, node_d, node_f, node_i,
                                 node_h ],
                          result)
        self.assertEqual([ node_c, node_a, node_d, node_f, node_i,
                          node_h ],
                         previsit_result)

        previsit_result = []

        result = self.util.explore(self.graph,
                                   node_d,
                                   lambda x: previsit_result.append(x))

        Util.assert_items(self, [ node_d, node_a, node_c, node_h, node_i,
                                 node_f ],
                          result)
        self.assertEqual([ node_d, node_a, node_c, node_h, node_i,
                          node_f ],
                         previsit_result)

        previsit_result = []

        result = self.util.explore(self.graph,
                                   node_e,
                                   lambda x: previsit_result.append(x))

        Util.assert_items(self, [ node_e, node_b, node_g, node_j ],
                          result)
        self.assertEqual([ node_e, node_b, node_g, node_j ],
                         previsit_result)

        previsit_result = []

        result = self.util.explore(self.graph,
                                   node_f,
                                   lambda x: previsit_result.append(x))

        Util.assert_items(self, [ node_f, node_a, node_c, node_h, node_i,
                                 node_d ],
                          result)
        self.assertEqual([ node_f, node_a, node_c, node_h, node_i,
                          node_d ],
                         previsit_result)

        previsit_result = []

        result = self.util.explore(self.graph,
                                   node_g,
                                   lambda x: previsit_result.append(x))

        Util.assert_items(self, [ node_g, node_e, node_b, node_j ],
                          result)
        self.assertEqual([ node_g, node_e, node_b, node_j ],
                         previsit_result)

        previsit_result = []

        result = self.util.explore(self.graph,
                                   node_i,
                                   lambda x: previsit_result.append(x))

        Util.assert_items(self, [ node_i, node_c, node_a, node_d, node_f,
                                 node_h ],
                          result)
        self.assertEqual([ node_i, node_c, node_a, node_d, node_f,
                          node_h ],
                         previsit_result)

        previsit_result = []

        result = self.util.explore(self.graph,
                                   node_j,
                                   lambda x: previsit_result.append(x))

        Util.assert_items(self, [ node_j, node_e, node_b, node_g ],
                          result)
        self.assertEqual([ node_j, node_e, node_b, node_g ],
                         previsit_result)

    def test_undirected_edges_as_two_components_previsit_postvisit(self):
        (node_a, node_b, node_c, node_d, node_e, node_f,
         node_g, node_h, node_i, node_j) = \
            'A', 'B', 'C', 'D', 'E', 'F', 'G', 'H', 'I', 'J'

        self.graph.add_node(node_a)
        self.graph.add_node(node_b)
        self.graph.add_node(node_c)
        self.graph.add_node(node_d)
        self.graph.add_node(node_e)
        self.graph.add_node(node_f)
        self.graph.add_node(node_g)
        self.graph.add_node(node_h)
        self.graph.add_node(node_i)
        self.graph.add_node(node_j)

        self.graph.add_undirected_edge(node_a, node_c)
        self.graph.add_undirected_edge(node_a, node_d)
        self.graph.add_undirected_edge(node_a, node_f)
        self.graph.add_undirected_edge(node_b, node_e)
        self.graph.add_undirected_edge(node_c, node_h)
        self.graph.add_undirected_edge(node_c, node_i)
        self.graph.add_undirected_edge(node_e, node_g)
        self.graph.add_undirected_edge(node_e, node_j)
        self.graph.add_undirected_edge(node_f, node_i)
        self.graph.add_undirected_edge(node_h, node_i)

        previsit_result = []
        postvisit_result = []

        result = self.util.explore(self.graph,
                                   node_a,
                                   lambda x: previsit_result.append(x),
                                   lambda x: postvisit_result.append(x))

        Util.assert_items(self, [ node_a, node_c, node_h, node_i, node_f,
                                 node_d ],
                          result)
        self.assertEqual([ node_a, node_c, node_h, node_i, node_f,
                          node_d ],
                         previsit_result)
        self.assertEqual([ node_f, node_i, node_h, node_c, node_d,
                          node_a ],
                         postvisit_result)

        previsit_result = []
        postvisit_result = []

        result = self.util.explore(self.graph,
                                   node_b,
                                   lambda x: previsit_result.append(x),
                                   lambda x: postvisit_result.append(x))

        Util.assert_items(self, [ node_b, node_e, node_g, node_j ],
                          result)
        self.assertEqual([ node_b, node_e, node_g, node_j ],
                         previsit_result)
        self.assertEqual([ node_g, node_j, node_e, node_b ],
                         postvisit_result)

        previsit_result = []
        postvisit_result = []

        result = self.util.explore(self.graph,
                                   node_c,
                                   lambda x: previsit_result.append(x),
                                   lambda x: postvisit_result.append(x))

        Util.assert_items(self, [ node_c, node_a, node_d, node_f, node_i,
                                 node_h ],
                          result)
        self.assertEqual([ node_c, node_a, node_d, node_f, node_i,
                          node_h ],
                         previsit_result)
        self.assertEqual([ node_d, node_h, node_i, node_f, node_a,
                          node_c ],
                         postvisit_result)

        previsit_result = []
        postvisit_result = []

        result = self.util.explore(self.graph,
                                   node_d,
                                   lambda x: previsit_result.append(x),
                                   lambda x: postvisit_result.append(x))

        Util.assert_items(self, [ node_d, node_a, node_c, node_h, node_i,
                                 node_f ],
                          result)
        self.assertEqual([ node_d, node_a, node_c, node_h, node_i,
                          node_f ],
                         previsit_result)
        self.assertEqual([ node_f, node_i, node_h, node_c, node_a,
                          node_d ],
                         postvisit_result)

        previsit_result = []
        postvisit_result = []

        result = self.util.explore(self.graph,
                                   node_e,
                                   lambda x: previsit_result.append(x),
                                   lambda x: postvisit_result.append(x))

        Util.assert_items(self, [ node_e, node_b, node_g, node_j ],
                          result)
        self.assertEqual([ node_e, node_b, node_g, node_j ],
                         previsit_result)
        self.assertEqual([ node_b, node_g, node_j, node_e ],
                         postvisit_result)

        previsit_result = []
        postvisit_result = []

        result = self.util.explore(self.graph,
                                   node_f,
                                   lambda x: previsit_result.append(x),
                                   lambda x: postvisit_result.append(x))

        Util.assert_items(self, [ node_f, node_a, node_c, node_h, node_i,
                                 node_d ],
                          result)
        self.assertEqual([ node_f, node_a, node_c, node_h, node_i,
                          node_d ],
                         previsit_result)
        self.assertEqual([ node_i, node_h, node_c, node_d, node_a,
                          node_f ],
                         postvisit_result)

        previsit_result = []
        postvisit_result = []

        result = self.util.explore(self.graph,
                                   node_g,
                                   lambda x: previsit_result.append(x),
                                   lambda x: postvisit_result.append(x))

        Util.assert_items(self, [ node_g, node_e, node_b, node_j ],
                          result)
        self.assertEqual([ node_g, node_e, node_b, node_j ],
                         previsit_result)
        self.assertEqual([ node_b, node_j, node_e, node_g ],
                         postvisit_result)

        previsit_result = []
        postvisit_result = []

        result = self.util.explore(self.graph,
                                   node_i,
                                   lambda x: previsit_result.append(x),
                                   lambda x: postvisit_result.append(x))

        Util.assert_items(self, [ node_i, node_c, node_a, node_d, node_f,
                                 node_h ],
                          result)
        self.assertEqual([ node_i, node_c, node_a, node_d, node_f,
                          node_h ],
                         previsit_result)
        self.assertEqual([ node_d, node_f, node_a, node_h, node_c,
                          node_i ],
                         postvisit_result)

        previsit_result = []
        postvisit_result = []

        result = self.util.explore(self.graph,
                                   node_j,
                                   lambda x: previsit_result.append(x),
                                   lambda x: postvisit_result.append(x))

        Util.assert_items(self, [ node_j, node_e, node_b, node_g ],
                          result)
        self.assertEqual([ node_j, node_e, node_b, node_g ],
                         previsit_result)
        self.assertEqual([ node_b, node_g, node_e, node_j ],
                         postvisit_result)

    def test_two_components_previsit_postvisit_excluded(self):
        (node_a, node_b, node_c, node_d, node_e, node_f,
         node_g, node_h, node_i, node_j) = \
            'A', 'B', 'C', 'D', 'E', 'F', 'G', 'H', 'I', 'J'

        self.graph.add_node(node_a)
        self.graph.add_node(node_b)
        self.graph.add_node(node_c)
        self.graph.add_node(node_d)
        self.graph.add_node(node_e)
        self.graph.add_node(node_f)
        self.graph.add_node(node_g)
        self.graph.add_node(node_h)
        self.graph.add_node(node_i)
        self.graph.add_node(node_j)

        self.graph.add_undirected_edge(node_a, node_c)
        self.graph.add_undirected_edge(node_a, node_d)
        self.graph.add_undirected_edge(node_a, node_f)
        self.graph.add_undirected_edge(node_b, node_e)
        self.graph.add_undirected_edge(node_c, node_h)
        self.graph.add_undirected_edge(node_c, node_i)
        self.graph.add_undirected_edge(node_e, node_g)
        self.graph.add_undirected_edge(node_e, node_j)
        self.graph.add_undirected_edge(node_f, node_i)
        self.graph.add_undirected_edge(node_h, node_i)

        excluded = set()
        excluded.add(node_c)
        excluded.add(node_f)

        previsit_result = []
        postvisit_result = []

        result = self.util.explore(self.graph,
                                   node_a,
                                   lambda x: previsit_result.append(x),
                                   lambda x: postvisit_result.append(x),
                                   excluded)

        Util.assert_items(self, [ node_a, node_d ], result)
        self.assertEqual([ node_a, node_d ], previsit_result)
        self.assertEqual([ node_d, node_a ], postvisit_result)

        previsit_result = []
        postvisit_result = []

        result = self.util.explore(self.graph,
                                   node_b,
                                   lambda x: previsit_result.append(x),
                                   lambda x: postvisit_result.append(x),
                                   excluded)

        Util.assert_items(self, [ node_b, node_e, node_g, node_j ], result)
        self.assertEqual([ node_b, node_e, node_g, node_j ],
                         previsit_result)
        self.assertEqual([ node_g, node_j, node_e, node_b ],
                         postvisit_result)

        previsit_result = []
        postvisit_result = []

        result = self.util.explore(self.graph,
                                   node_c,
                                   lambda x: previsit_result.append(x),
                                   lambda x: postvisit_result.append(x),
                                   excluded)

        Util.assert_items(self, [], result)
        self.assertEqual([], previsit_result)
        self.assertEqual([], postvisit_result)

        previsit_result = []
        postvisit_result = []

        result = self.util.explore(self.graph,
                                   node_d,
                                   lambda x: previsit_result.append(x),
                                   lambda x: postvisit_result.append(x),
                                   excluded)

        Util.assert_items(self, [ node_d, node_a ], result)
        self.assertEqual([ node_d, node_a ], previsit_result)
        self.assertEqual([ node_a, node_d ], postvisit_result)

        previsit_result = []
        postvisit_result = []

        result = self.util.explore(self.graph,
                                   node_e,
                                   lambda x: previsit_result.append(x),
                                   lambda x: postvisit_result.append(x),
                                   excluded)

        Util.assert_items(self, [ node_e, node_b, node_g, node_j ], result)
        self.assertEqual([ node_e, node_b, node_g, node_j ],
                         previsit_result)
        self.assertEqual([ node_b, node_g, node_j, node_e ],
                         postvisit_result)

        previsit_result = []
        postvisit_result = []

        result = self.util.explore(self.graph,
                                   node_f,
                                   lambda x: previsit_result.append(x),
                                   lambda x: postvisit_result.append(x),
                                   excluded)

        Util.assert_items(self, [], result)
        self.assertEqual([], previsit_result)
        self.assertEqual([], postvisit_result)

        previsit_result = []
        postvisit_result = []

        result = self.util.explore(self.graph,
                                   node_g,
                                   lambda x: previsit_result.append(x),
                                   lambda x: postvisit_result.append(x),
                                   excluded)

        Util.assert_items(self, [ node_g, node_e, node_b, node_j ], result)
        self.assertEqual([ node_g, node_e, node_b, node_j ],
                         previsit_result)
        self.assertEqual([ node_b, node_j, node_e, node_g ],
                         postvisit_result)

        previsit_result = []
        postvisit_result = []

        result = self.util.explore(self.graph,
                                   node_i,
                                   lambda x: previsit_result.append(x),
                                   lambda x: postvisit_result.append(x),
                                   excluded)

        Util.assert_items(self, [ node_i, node_h ], result)
        self.assertEqual([ node_i, node_h ], previsit_result)
        self.assertEqual([ node_h, node_i ], postvisit_result)

        previsit_result = []
        postvisit_result = []

        result = self.util.explore(self.graph,
                                   node_j,
                                   lambda x: previsit_result.append(x),
                                   lambda x: postvisit_result.append(x),
                                   excluded)

        Util.assert_items(self, [ node_j, node_e, node_b, node_g ], result)
        self.assertEqual([ node_j, node_e, node_b, node_g ],
                         previsit_result)
        self.assertEqual([ node_b, node_g, node_e, node_j ],
                         postvisit_result)

class ExploreWithCustomVisitorsTestCase(unittest.TestCase):

    def setUp(self):
        self.util = graph_util.GraphUtil()
        self.graph = graph_util.Graph()
        self.clock = 1

    def tearDown(self):
        pass

    def previsit_clock(self, node):
        self.previsit_result.append((node, self.clock))
        self.clock += 1

    def postvisit_clock(self, node):
        self.postvisit_result.append((node, self.clock))
        self.clock += 1

    def test_three_components_and_clock_previsit_postvisit(self):
        (node_a, node_b, node_c, node_d, node_e, node_f,
         node_g, node_h, node_i) = \
            'A', 'B', 'C', 'D', 'E', 'F', 'G', 'H', 'I'

        self.graph.add_node(node_a)
        self.graph.add_node(node_b)
        self.graph.add_node(node_c)
        self.graph.add_node(node_d)
        self.graph.add_node(node_e)
        self.graph.add_node(node_f)
        self.graph.add_node(node_g)
        self.graph.add_node(node_h)
        self.graph.add_node(node_i)

        self.graph.add_undirected_edge(node_a, node_b)
        self.graph.add_undirected_edge(node_a, node_c)
        self.graph.add_undirected_edge(node_a, node_d)
        self.graph.add_undirected_edge(node_b, node_c)
        self.graph.add_undirected_edge(node_e, node_f)
        self.graph.add_undirected_edge(node_g, node_h)
        self.graph.add_undirected_edge(node_g, node_i)
        self.graph.add_undirected_edge(node_h, node_i)

        self.previsit_result = []
        self.postvisit_result = []

        result = self.util.explore(self.graph,
                                   node_a,
                                   self.previsit_clock,
                                   self.postvisit_clock)

        Util.assert_items(self, [ node_a, node_b, node_c, node_d ],
                          result)
        self.assertEqual([ (node_a, 1), (node_b, 2), (node_c, 3),
                         (node_d, 6) ],
                         self.previsit_result)
        self.assertEqual([ (node_c, 4), (node_b, 5), (node_d, 7),
                         (node_a, 8) ],
                         self.postvisit_result)
        self.assertEqual(9, self.clock)

        self.previsit_result = []
        self.postvisit_result = []

        result = self.util.explore(self.graph,
                                   node_e,
                                   self.previsit_clock,
                                   self.postvisit_clock)

        Util.assert_items(self, [ node_e, node_f ],
                          result)
        self.assertEqual([ (node_e, 9), (node_f, 10) ],
                         self.previsit_result)
        self.assertEqual([ (node_f, 11), (node_e, 12) ],
                         self.postvisit_result)
        self.assertEqual(13, self.clock)

        self.previsit_result = []
        self.postvisit_result = []

        result = self.util.explore(self.graph,
                                   node_g,
                                   self.previsit_clock,
                                   self.postvisit_clock)

        Util.assert_items(self, [ node_g, node_h, node_i ],
                          result)
        self.assertEqual([ (node_g, 13), (node_h, 14), (node_i, 15) ],
                         self.previsit_result)
        self.assertEqual([ (node_i, 16), (node_h, 17), (node_g, 18) ],
                         self.postvisit_result)
        self.assertEqual(19, self.clock)

class CountComponentsTestCase(unittest.TestCase):

    def setUp(self):
        self.util = graph_util.GraphUtil()
        self.graph = graph_util.Graph()

    def tearDown(self):
        pass

    def test_empty_graph(self):
        result = self.util.count_components(self.graph)

        self.assertEqual(0, result)

    def test_one_component(self):
        node1, node2, node3, node4 = 1, 2, 3, 4

        self.graph.add_node(node1)
        self.graph.add_node(node2)
        self.graph.add_node(node3)
        self.graph.add_node(node4)

        self.graph.add_undirected_edge(node1, node2)
        self.graph.add_undirected_edge(node3, node2)
        self.graph.add_undirected_edge(node4, node3)
        self.graph.add_undirected_edge(node1, node4)

        result = self.util.count_components(self.graph)

        self.assertEqual(1, result)

    def test_two_components(self):
        node1, node2, node3, node4 = 1, 2, 3, 4

        self.graph.add_node(node1)
        self.graph.add_node(node2)
        self.graph.add_node(node3)
        self.graph.add_node(node4)

        self.graph.add_undirected_edge(node1, node2)
        self.graph.add_undirected_edge(node3, node2)

        result = self.util.count_components(self.graph)

        self.assertEqual(2, result)

class ReachesTestCase(unittest.TestCase):

    def setUp(self):
        self.util = graph_util.GraphUtil()
        self.graph = graph_util.Graph()

    def tearDown(self):
        pass

    def assert_result(self, node1, node2, expected_result):
        result = self.util.reaches(self.graph, node1, node2)

        self.assertEqual(expected_result, result)

        result = self.util.reaches(self.graph, node2, node1)

        self.assertEqual(expected_result, result)

    def test_empty_graph(self):
        node1 = 'A'
        node2 = 'B'

        self.assert_result(node1, node2, False)

    def test_graph_with_first_node(self):
        node1 = 'A'
        node2 = 'B'

        self.graph.add_node(node1)

        self.assert_result(node1, node2, False)

    def test_graph_with_second_node(self):
        node1 = 'A'
        node2 = 'B'

        self.graph.add_node(node2)

        self.assert_result(node1, node2, False)

    def test_one_component(self):
        node1, node2, node3, node4 = 1, 2, 3, 4

        self.graph.add_node(node1)
        self.graph.add_node(node2)
        self.graph.add_node(node3)
        self.graph.add_node(node4)

        self.graph.add_undirected_edge(node1, node2)
        self.graph.add_undirected_edge(node3, node2)
        self.graph.add_undirected_edge(node4, node3)
        self.graph.add_undirected_edge(node1, node4)

        self.assert_result(node1, node4, True)

    def test_two_components(self):
        node1, node2, node3, node4 = 1, 2, 3, 4

        self.graph.add_node(node1)
        self.graph.add_node(node2)
        self.graph.add_node(node3)
        self.graph.add_node(node4)

        self.graph.add_undirected_edge(node1, node2)
        self.graph.add_undirected_edge(node3, node2)

        self.assert_result(node1, node4, False)

class DepthFirstSearchTestCase(unittest.TestCase):

    def setUp(self):
        self.util = graph_util.GraphUtil()
        self.graph = graph_util.Graph()

    def tearDown(self):
        pass

    def assert_all_nodes_were_found(self, graph, result):
        all_nodes = set()
        for node in self.graph.nodes():
            all_nodes.add(node)
            for neighbor in graph.neighbors(node):
                all_nodes.add(neighbor)

        Util.assert_items(self, all_nodes, result)

    def assert_order_values(self, expected_order_values):
        order_values = []
        order_values += list(self.util.preorder.values())
        order_values += list(self.util.postorder.values())

        Util.assert_items(self, expected_order_values, order_values)

    def test_empty_graph(self):
        result = self.util.depth_first_search(self.graph)

        self.assert_all_nodes_were_found(self.graph, result)

    def test_graph_with_one_node(self):
        node = 'A'

        self.graph.add_node(node)

        result = self.util.depth_first_search(self.graph)

        self.assert_all_nodes_were_found(self.graph, result)
        self.assert_order_values([x for x in range(1, 3)])

    def test_one_directed_edge(self):
        node1, node2 = 'A', 'B'

        self.graph.add_node(node1)
        self.graph.add_node(node2)

        self.graph.add_directed_edge(node1, node2)

        result = self.util.depth_first_search(self.graph)

        self.assert_all_nodes_were_found(self.graph, result)
        self.assert_order_values([x for x in range(1, 5)])

    def test_one_undirected_edge(self):
        node1, node2 = 'A', 'B'

        self.graph.add_node(node1)
        self.graph.add_node(node2)

        self.graph.add_undirected_edge(node1, node2)

        result = self.util.depth_first_search(self.graph)

        self.assert_all_nodes_were_found(self.graph, result)
        self.assert_order_values([x for x in range(1, 5)])

    def test_two_directed_edges_as_rays(self):
        node1, node2, node3 = 'A', 'B', 'C'

        self.graph.add_node(node1)
        self.graph.add_node(node2)
        self.graph.add_node(node3)

        self.graph.add_directed_edge(node1, node2)
        self.graph.add_directed_edge(node1, node3)

        result = self.util.depth_first_search(self.graph)

        self.assert_all_nodes_were_found(self.graph, result)
        self.assert_order_values([x for x in range(1, 7)])

    def test_two_directed_edges_as_chain(self):
        node1, node2, node3 = 'A', 'B', 'C'

        self.graph.add_node(node1)
        self.graph.add_node(node2)
        self.graph.add_node(node3)

        self.graph.add_directed_edge(node1, node2)
        self.graph.add_directed_edge(node2, node3)

        result = self.util.depth_first_search(self.graph)

        self.assert_all_nodes_were_found(self.graph, result)
        self.assert_order_values([x for x in range(1, 7)])

    def test_three_directed_edges_as_cycle(self):
        node1, node2, node3 = 'A', 'B', 'C'

        self.graph.add_node(node1)
        self.graph.add_node(node2)
        self.graph.add_node(node3)

        self.graph.add_directed_edge(node1, node2)
        self.graph.add_directed_edge(node2, node3)
        self.graph.add_directed_edge(node3, node1)

        result = self.util.depth_first_search(self.graph)

        self.assert_all_nodes_were_found(self.graph, result)
        self.assert_order_values([x for x in range(1, 7)])

    def test_two_undirected_edges_as_rays(self):
        node1, node2, node3 = 'A', 'B', 'C'

        self.graph.add_node(node1)
        self.graph.add_node(node2)
        self.graph.add_node(node3)

        self.graph.add_undirected_edge(node1, node2)
        self.graph.add_undirected_edge(node1, node3)

        result = self.util.depth_first_search(self.graph)

        self.assert_all_nodes_were_found(self.graph, result)
        self.assert_order_values([x for x in range(1, 7)])

    def test_two_undirected_edges_as_chain(self):
        node1, node2, node3 = 'A', 'B', 'C'

        self.graph.add_node(node1)
        self.graph.add_node(node2)
        self.graph.add_node(node3)

        self.graph.add_undirected_edge(node1, node2)
        self.graph.add_undirected_edge(node2, node3)

        result = self.util.depth_first_search(self.graph)

        self.assert_all_nodes_were_found(self.graph, result)
        self.assert_order_values([x for x in range(1, 7)])

    def test_three_undirected_edges_as_cycle(self):
        node1, node2, node3 = 'A', 'B', 'C'

        self.graph.add_node(node1)
        self.graph.add_node(node2)
        self.graph.add_node(node3)

        self.graph.add_undirected_edge(node1, node2)
        self.graph.add_undirected_edge(node2, node3)
        self.graph.add_undirected_edge(node3, node1)

        result = self.util.depth_first_search(self.graph)

        self.assert_all_nodes_were_found(self.graph, result)
        self.assert_order_values([x for x in range(1, 7)])

    def test_undirected_edges_as_one_component(self):
        (node_a, node_b, node_c, node_d, node_e, node_f,
         node_g, node_h) = 'A', 'B', 'C', 'D', 'E', 'F', 'G', 'H'

        self.graph.add_node(node_a)
        self.graph.add_node(node_b)
        self.graph.add_node(node_c)
        self.graph.add_node(node_d)
        self.graph.add_node(node_e)
        self.graph.add_node(node_f)
        self.graph.add_node(node_g)
        self.graph.add_node(node_h)

        self.graph.add_undirected_edge(node_a, node_b)
        self.graph.add_undirected_edge(node_a, node_c)
        self.graph.add_undirected_edge(node_b, node_c)
        self.graph.add_undirected_edge(node_c, node_d)
        self.graph.add_undirected_edge(node_c, node_h)
        self.graph.add_undirected_edge(node_d, node_e)
        self.graph.add_undirected_edge(node_e, node_f)
        self.graph.add_undirected_edge(node_e, node_g)
        self.graph.add_undirected_edge(node_f, node_g)
        self.graph.add_undirected_edge(node_g, node_h)

        result = self.util.depth_first_search(self.graph)

        self.assert_all_nodes_were_found(self.graph, result)
        self.assert_order_values([x for x in range(1, 17)])

    def test_many_undirected_edges_as_two_components(self):
        (node_a, node_b, node_c, node_d, node_e, node_f,
         node_g, node_h, node_i, node_j) = \
                                'A', 'B', 'C', 'D', 'E', 'F', 'G', 'H', 'I', 'J'

        self.graph.add_node(node_a)
        self.graph.add_node(node_b)
        self.graph.add_node(node_c)
        self.graph.add_node(node_d)
        self.graph.add_node(node_e)
        self.graph.add_node(node_f)
        self.graph.add_node(node_g)
        self.graph.add_node(node_h)
        self.graph.add_node(node_i)
        self.graph.add_node(node_j)

        self.graph.add_undirected_edge(node_a, node_c)
        self.graph.add_undirected_edge(node_a, node_d)
        self.graph.add_undirected_edge(node_a, node_f)
        self.graph.add_undirected_edge(node_b, node_e)
        self.graph.add_undirected_edge(node_c, node_h)
        self.graph.add_undirected_edge(node_c, node_i)
        self.graph.add_undirected_edge(node_e, node_g)
        self.graph.add_undirected_edge(node_e, node_j)
        self.graph.add_undirected_edge(node_f, node_i)
        self.graph.add_undirected_edge(node_h, node_i)

        result = self.util.depth_first_search(self.graph)

        self.assert_all_nodes_were_found(self.graph, result)
        self.assert_order_values([x for x in range(1, 21)])

    def test_many_undirected_edges_as_three_components(self):
        (node_a, node_b, node_c, node_d, node_e, node_f,
         node_g, node_h, node_i) = 'A', 'B', 'C', 'D', 'E', 'F', 'G', 'H', 'I'

        self.graph.add_node(node_a)
        self.graph.add_node(node_b)
        self.graph.add_node(node_c)
        self.graph.add_node(node_d)
        self.graph.add_node(node_e)
        self.graph.add_node(node_f)
        self.graph.add_node(node_g)
        self.graph.add_node(node_h)
        self.graph.add_node(node_i)

        self.graph.add_undirected_edge(node_a, node_b)
        self.graph.add_undirected_edge(node_a, node_c)
        self.graph.add_undirected_edge(node_a, node_d)
        self.graph.add_undirected_edge(node_b, node_c)
        self.graph.add_undirected_edge(node_e, node_f)
        self.graph.add_undirected_edge(node_g, node_h)
        self.graph.add_undirected_edge(node_g, node_i)
        self.graph.add_undirected_edge(node_h, node_i)

        result = self.util.depth_first_search(self.graph)

        self.assert_all_nodes_were_found(self.graph, result)
        self.assert_order_values([x for x in range(1, 19)])

class NumberAllNodesByComponentTestCase(unittest.TestCase):

    def setUp(self):
        self.util = graph_util.GraphUtil()
        self.graph = graph_util.Graph()

    def tearDown(self):
        pass

    def assert_all_nodes_were_found(self, graph, result):
        all_nodes = set()
        for node in self.graph.nodes():
            all_nodes.add(node)
            for neighbor in graph.neighbors(node):
                all_nodes.add(neighbor)

        Util.assert_items(self, all_nodes, result)

    def test_empty_graph(self):
        nodes, component_count = \
                             self.util.number_all_nodes_by_component(self.graph)

        self.assertEqual(0, component_count)

        self.assert_all_nodes_were_found(self.graph, nodes)

    def test_one_component_as_point(self):
        node = 'A'

        self.graph.add_node(node)

        nodes, component_count = \
                             self.util.number_all_nodes_by_component(self.graph)

        self.assertEqual(1, component_count)

        self.assert_all_nodes_were_found(self.graph, nodes)
        self.assertEqual(1, self.util.component_id[node])

    def test_one_component_as_path(self):
        node_a, node_b, node_c = 'A', 'B', 'C'

        self.graph.add_node(node_a)
        self.graph.add_node(node_b)
        self.graph.add_node(node_c)

        self.graph.add_undirected_edge(node_a, node_b)
        self.graph.add_undirected_edge(node_b, node_c)

        nodes, component_count = \
                             self.util.number_all_nodes_by_component(self.graph)

        self.assertEqual(1, component_count)

        self.assert_all_nodes_were_found(self.graph, nodes)
        self.assertEqual(1, self.util.component_id[node_a])

    def test_three_components_as_points(self):
        node_a, node_b, node_c = 'A', 'B', 'C'

        self.graph.add_node(node_a)
        self.graph.add_node(node_b)
        self.graph.add_node(node_c)

        nodes, component_count = \
                             self.util.number_all_nodes_by_component(self.graph)

        component_number1 = self.util.component_id[node_a]
        component_number2 = self.util.component_id[node_b]
        component_number3 = self.util.component_id[node_c]

        self.assertEqual(3, component_count)

        self.assertNotEqual(component_number1, component_number2)
        self.assertNotEqual(component_number1, component_number3)
        self.assertNotEqual(component_number2, component_number1)
        self.assertNotEqual(component_number2, component_number3)
        self.assertNotEqual(component_number3, component_number1)
        self.assertNotEqual(component_number3, component_number2)

        self.assert_all_nodes_were_found(self.graph, nodes)
        self.assertEqual(component_number1, self.util.component_id[node_a])
        self.assertEqual(component_number2, self.util.component_id[node_b])
        self.assertEqual(component_number3, self.util.component_id[node_c])

    def test_three_components_as_paths(self):
        (node_a, node_b, node_c, node_d, node_e, node_f,
         node_g, node_h, node_i) = 'A', 'B', 'C', 'D', 'E', 'F', 'G', 'H', 'I'

        self.graph.add_node(node_a)
        self.graph.add_node(node_b)
        self.graph.add_node(node_c)
        self.graph.add_node(node_d)
        self.graph.add_node(node_e)
        self.graph.add_node(node_f)
        self.graph.add_node(node_g)
        self.graph.add_node(node_h)
        self.graph.add_node(node_i)

        self.graph.add_undirected_edge(node_a, node_b)
        self.graph.add_undirected_edge(node_a, node_c)
        self.graph.add_undirected_edge(node_a, node_d)
        self.graph.add_undirected_edge(node_b, node_c)
        self.graph.add_undirected_edge(node_e, node_f)
        self.graph.add_undirected_edge(node_g, node_h)
        self.graph.add_undirected_edge(node_g, node_i)
        self.graph.add_undirected_edge(node_h, node_i)

        nodes, component_count = \
                             self.util.number_all_nodes_by_component(self.graph)

        component_number1 = self.util.component_id[node_a]
        component_number2 = self.util.component_id[node_e]
        component_number3 = self.util.component_id[node_h]

        self.assertEqual(3, component_count)

        self.assertNotEqual(component_number1, component_number2)
        self.assertNotEqual(component_number1, component_number3)
        self.assertNotEqual(component_number2, component_number1)
        self.assertNotEqual(component_number2, component_number3)
        self.assertNotEqual(component_number3, component_number1)
        self.assertNotEqual(component_number3, component_number2)

        self.assert_all_nodes_were_found(self.graph, nodes)
        self.assertEqual(component_number1, self.util.component_id[node_a])
        self.assertEqual(component_number1, self.util.component_id[node_b])
        self.assertEqual(component_number1, self.util.component_id[node_c])
        self.assertEqual(component_number1, self.util.component_id[node_d])
        self.assertEqual(component_number2, self.util.component_id[node_e])
        self.assertEqual(component_number2, self.util.component_id[node_f])
        self.assertEqual(component_number3, self.util.component_id[node_g])
        self.assertEqual(component_number3, self.util.component_id[node_h])
        self.assertEqual(component_number3, self.util.component_id[node_i])

    def test_six_components_as_paths_and_points(self):
        (node_a, node_b, node_c, node_d, node_e, node_f,
         node_g, node_h, node_i, node_j, node_k, node_l) = \
                      'A', 'B', 'C', 'D', 'E', 'F', 'G', 'H', 'I', 'J', 'K', 'L'

        self.graph.add_node(node_a)
        self.graph.add_node(node_b)
        self.graph.add_node(node_c)
        self.graph.add_node(node_d)
        self.graph.add_node(node_e)
        self.graph.add_node(node_f)
        self.graph.add_node(node_g)
        self.graph.add_node(node_h)
        self.graph.add_node(node_i)
        self.graph.add_node(node_j)
        self.graph.add_node(node_k)
        self.graph.add_node(node_l)

        self.graph.add_undirected_edge(node_a, node_b)
        self.graph.add_undirected_edge(node_a, node_c)
        self.graph.add_undirected_edge(node_a, node_d)
        self.graph.add_undirected_edge(node_b, node_c)
        self.graph.add_undirected_edge(node_e, node_f)
        self.graph.add_undirected_edge(node_g, node_h)
        self.graph.add_undirected_edge(node_g, node_i)
        self.graph.add_undirected_edge(node_h, node_i)

        nodes, component_count = \
                             self.util.number_all_nodes_by_component(self.graph)

        component_number1 = self.util.component_id[node_a]
        component_number2 = self.util.component_id[node_e]
        component_number3 = self.util.component_id[node_h]
        component_number4 = self.util.component_id[node_j]
        component_number5 = self.util.component_id[node_k]
        component_number6 = self.util.component_id[node_l]

        self.assertEqual(6, component_count)

        self.assertNotEqual(component_number1, component_number2)
        self.assertNotEqual(component_number1, component_number3)
        self.assertNotEqual(component_number1, component_number4)
        self.assertNotEqual(component_number1, component_number5)
        self.assertNotEqual(component_number1, component_number6)
        self.assertNotEqual(component_number2, component_number1)
        self.assertNotEqual(component_number2, component_number3)
        self.assertNotEqual(component_number2, component_number4)
        self.assertNotEqual(component_number2, component_number5)
        self.assertNotEqual(component_number2, component_number6)
        self.assertNotEqual(component_number3, component_number1)
        self.assertNotEqual(component_number3, component_number2)
        self.assertNotEqual(component_number3, component_number4)
        self.assertNotEqual(component_number3, component_number5)
        self.assertNotEqual(component_number3, component_number6)
        self.assertNotEqual(component_number4, component_number1)
        self.assertNotEqual(component_number4, component_number2)
        self.assertNotEqual(component_number4, component_number3)
        self.assertNotEqual(component_number4, component_number5)
        self.assertNotEqual(component_number4, component_number6)
        self.assertNotEqual(component_number5, component_number1)
        self.assertNotEqual(component_number5, component_number2)
        self.assertNotEqual(component_number5, component_number3)
        self.assertNotEqual(component_number5, component_number4)
        self.assertNotEqual(component_number5, component_number6)
        self.assertNotEqual(component_number6, component_number1)
        self.assertNotEqual(component_number6, component_number2)
        self.assertNotEqual(component_number6, component_number3)
        self.assertNotEqual(component_number6, component_number4)
        self.assertNotEqual(component_number6, component_number5)

        self.assert_all_nodes_were_found(self.graph, nodes)
        self.assertEqual(component_number1, self.util.component_id[node_a])
        self.assertEqual(component_number1, self.util.component_id[node_b])
        self.assertEqual(component_number1, self.util.component_id[node_c])
        self.assertEqual(component_number1, self.util.component_id[node_d])
        self.assertEqual(component_number2, self.util.component_id[node_e])
        self.assertEqual(component_number2, self.util.component_id[node_f])
        self.assertEqual(component_number3, self.util.component_id[node_g])
        self.assertEqual(component_number3, self.util.component_id[node_h])
        self.assertEqual(component_number3, self.util.component_id[node_i])
        self.assertEqual(component_number4, self.util.component_id[node_j])
        self.assertEqual(component_number5, self.util.component_id[node_k])
        self.assertEqual(component_number6, self.util.component_id[node_l])

class HasCycleTestCase(unittest.TestCase):

    def setUp(self):
        self.util = graph_util.GraphUtil()
        self.graph = graph_util.Graph()

    def tearDown(self):
        pass

    def test_empty_graph(self):
        result = self.util.has_cycle(self.graph)

        self.assertEqual(False, result)

    def test_graph_with_one_node(self):
        node = 'A'

        self.graph.add_node(node)

        result = self.util.has_cycle(self.graph)

        self.assertEqual(False, result)

    def test_one_directed_edge(self):
        node1, node2 = 'A', 'B'

        self.graph.add_node(node1)
        self.graph.add_node(node2)

        self.graph.add_directed_edge(node1, node2)

        result = self.util.has_cycle(self.graph)

        self.assertEqual(False, result)

    def test_one_undirected_edge(self):
        node1, node2 = 'A', 'B'

        self.graph.add_node(node1)
        self.graph.add_node(node2)

        self.graph.add_undirected_edge(node1, node2)

        result = self.util.has_cycle(self.graph)

        self.assertEqual(True, result)

    def test_two_directed_edges_as_rays(self):
        node1, node2, node3 = 'A', 'B', 'C'

        self.graph.add_node(node1)
        self.graph.add_node(node2)
        self.graph.add_node(node3)

        self.graph.add_directed_edge(node1, node2)
        self.graph.add_directed_edge(node1, node3)

        result = self.util.has_cycle(self.graph)

        self.assertEqual(False, result)

    def test_two_directed_edges_as_chain(self):
        node1, node2, node3 = 'A', 'B', 'C'

        self.graph.add_node(node1)
        self.graph.add_node(node2)
        self.graph.add_node(node3)

        self.graph.add_directed_edge(node1, node2)
        self.graph.add_directed_edge(node2, node3)

        result = self.util.has_cycle(self.graph)

        self.assertEqual(False, result)

    def test_three_directed_edges_as_cycle(self):
        node1, node2, node3 = 'A', 'B', 'C'

        self.graph.add_node(node1)
        self.graph.add_node(node2)
        self.graph.add_node(node3)

        self.graph.add_directed_edge(node1, node2)
        self.graph.add_directed_edge(node2, node3)
        self.graph.add_directed_edge(node3, node1)

        result = self.util.has_cycle(self.graph)

        self.assertEqual(True, result)

    def test_two_undirected_edges_as_rays(self):
        node1, node2, node3 = 'A', 'B', 'C'

        self.graph.add_node(node1)
        self.graph.add_node(node2)
        self.graph.add_node(node3)

        self.graph.add_undirected_edge(node1, node2)
        self.graph.add_undirected_edge(node1, node3)

        result = self.util.has_cycle(self.graph)

        self.assertEqual(True, result)

    def test_two_undirected_edges_as_chain(self):
        node1, node2, node3 = 'A', 'B', 'C'

        self.graph.add_node(node1)
        self.graph.add_node(node2)
        self.graph.add_node(node3)

        self.graph.add_undirected_edge(node1, node2)
        self.graph.add_undirected_edge(node2, node3)

        result = self.util.has_cycle(self.graph)

        self.assertEqual(True, result)

    def test_three_undirected_edges_as_cycle(self):
        node1, node2, node3 = 'A', 'B', 'C'

        self.graph.add_node(node1)
        self.graph.add_node(node2)
        self.graph.add_node(node3)

        self.graph.add_undirected_edge(node1, node2)
        self.graph.add_undirected_edge(node2, node3)
        self.graph.add_undirected_edge(node3, node1)

        result = self.util.has_cycle(self.graph)

        self.assertEqual(True, result)

    def test_undirected_edges_as_one_component(self):
        (node_a, node_b, node_c, node_d, node_e, node_f,
         node_g, node_h) = 'A', 'B', 'C', 'D', 'E', 'F', 'G', 'H'

        self.graph.add_node(node_a)
        self.graph.add_node(node_b)
        self.graph.add_node(node_c)
        self.graph.add_node(node_d)
        self.graph.add_node(node_e)
        self.graph.add_node(node_f)
        self.graph.add_node(node_g)
        self.graph.add_node(node_h)

        self.graph.add_undirected_edge(node_a, node_b)
        self.graph.add_undirected_edge(node_a, node_c)
        self.graph.add_undirected_edge(node_b, node_c)
        self.graph.add_undirected_edge(node_c, node_d)
        self.graph.add_undirected_edge(node_c, node_h)
        self.graph.add_undirected_edge(node_d, node_e)
        self.graph.add_undirected_edge(node_e, node_f)
        self.graph.add_undirected_edge(node_e, node_g)
        self.graph.add_undirected_edge(node_f, node_g)
        self.graph.add_undirected_edge(node_g, node_h)

        result = self.util.has_cycle(self.graph)

        self.assertEqual(True, result)

    def test_many_undirected_edges_as_two_components(self):
        (node_a, node_b, node_c, node_d, node_e, node_f,
         node_g, node_h, node_i, node_j) = \
                                'A', 'B', 'C', 'D', 'E', 'F', 'G', 'H', 'I', 'J'

        self.graph.add_node(node_a)
        self.graph.add_node(node_b)
        self.graph.add_node(node_c)
        self.graph.add_node(node_d)
        self.graph.add_node(node_e)
        self.graph.add_node(node_f)
        self.graph.add_node(node_g)
        self.graph.add_node(node_h)
        self.graph.add_node(node_i)
        self.graph.add_node(node_j)

        self.graph.add_undirected_edge(node_a, node_c)
        self.graph.add_undirected_edge(node_a, node_d)
        self.graph.add_undirected_edge(node_a, node_f)
        self.graph.add_undirected_edge(node_b, node_e)
        self.graph.add_undirected_edge(node_c, node_h)
        self.graph.add_undirected_edge(node_c, node_i)
        self.graph.add_undirected_edge(node_e, node_g)
        self.graph.add_undirected_edge(node_e, node_j)
        self.graph.add_undirected_edge(node_f, node_i)
        self.graph.add_undirected_edge(node_h, node_i)

        result = self.util.has_cycle(self.graph)

        self.assertEqual(True, result)

    def test_four_nodes_with_one_cycle_case1(self):
        node_a, node_b, node_c, node_d = 'A', 'B', 'C', 'D'

        self.graph.add_node(node_a)
        self.graph.add_node(node_b)
        self.graph.add_node(node_c)
        self.graph.add_node(node_d)

        self.graph.add_directed_edge(node_a, node_b)
        self.graph.add_directed_edge(node_b, node_c)
        self.graph.add_directed_edge(node_c, node_a)
        self.graph.add_directed_edge(node_d, node_a)

        result = self.util.has_cycle(self.graph)

        self.assertEqual(True, result)

    def test_four_nodes_with_one_cycle_case2(self):
        node1, node2, node3, node4 = 1, 2, 3, 4

        self.graph.add_node(node1)
        self.graph.add_node(node2)
        self.graph.add_node(node3)
        self.graph.add_node(node4)

        self.graph.add_directed_edge(node1, node2)
        self.graph.add_directed_edge(node4, node1)
        self.graph.add_directed_edge(node2, node3)
        self.graph.add_directed_edge(node3, node1)

        result = self.util.has_cycle(self.graph)

        self.assertEqual(True, result)

    def test_five_nodes_with_no_cycle(self):
        node_a, node_b, node_c, node_d, node_e = 'A', 'B', 'C', 'D', 'E'

        self.graph.add_node(node_a)
        self.graph.add_node(node_b)
        self.graph.add_node(node_c)
        self.graph.add_node(node_d)
        self.graph.add_node(node_e)

        self.graph.add_directed_edge(node_a, node_b)
        self.graph.add_directed_edge(node_a, node_c)
        self.graph.add_directed_edge(node_a, node_d)
        self.graph.add_directed_edge(node_b, node_c)
        self.graph.add_directed_edge(node_b, node_e)
        self.graph.add_directed_edge(node_d, node_e)

        result = self.util.has_cycle(self.graph)

        self.assertEqual(False, result)

class TopologicalSortTestCase(unittest.TestCase):

    def setUp(self):
        self.util = graph_util.GraphUtil()
        self.graph = graph_util.Graph()

    def tearDown(self):
        pass

    def assert_all_nodes_were_found(self, graph, result):
        all_nodes = set()
        for node in self.graph.nodes():
            all_nodes.add(node)
            for neighbor in graph.neighbors(node):
                all_nodes.add(neighbor)

        Util.assert_items(self, all_nodes, result)

    def test_empty_graph(self):
        result = self.util.topological_sort(self.graph)

        self.assert_all_nodes_were_found(self.graph, result)

    def test_graph_with_one_node(self):
        node = 'A'

        self.graph.add_node(node)

        result = self.util.topological_sort(self.graph)

        self.assert_all_nodes_were_found(self.graph, result)

    def test_one_directed_edge(self):
        node1, node2 = 'A', 'B'

        self.graph.add_node(node1)
        self.graph.add_node(node2)

        self.graph.add_directed_edge(node1, node2)

        result = self.util.topological_sort(self.graph)

        self.assert_all_nodes_were_found(self.graph, result)

    def test_one_undirected_edge(self):
        node1, node2 = 'A', 'B'

        self.graph.add_node(node1)
        self.graph.add_node(node2)

        self.graph.add_undirected_edge(node1, node2)

        result = self.util.topological_sort(self.graph)

        self.assert_all_nodes_were_found(self.graph, result)

    def test_two_directed_edges_as_rays(self):
        node1, node2, node3 = 'A', 'B', 'C'

        self.graph.add_node(node1)
        self.graph.add_node(node2)
        self.graph.add_node(node3)

        self.graph.add_directed_edge(node1, node2)
        self.graph.add_directed_edge(node1, node3)

        result = self.util.topological_sort(self.graph)

        self.assert_all_nodes_were_found(self.graph, result)

    def test_two_directed_edges_as_chain(self):
        node1, node2, node3 = 'A', 'B', 'C'

        self.graph.add_node(node1)
        self.graph.add_node(node2)
        self.graph.add_node(node3)

        self.graph.add_directed_edge(node1, node2)
        self.graph.add_directed_edge(node2, node3)

        result = self.util.topological_sort(self.graph)

        self.assert_all_nodes_were_found(self.graph, result)

    def test_three_directed_edges_as_cycle(self):
        node1, node2, node3 = 'A', 'B', 'C'

        self.graph.add_node(node1)
        self.graph.add_node(node2)
        self.graph.add_node(node3)

        self.graph.add_directed_edge(node1, node2)
        self.graph.add_directed_edge(node2, node3)
        self.graph.add_directed_edge(node3, node1)

        result = self.util.topological_sort(self.graph)

        self.assert_all_nodes_were_found(self.graph, result)

    def test_two_undirected_edges_as_rays(self):
        node1, node2, node3 = 'A', 'B', 'C'

        self.graph.add_node(node1)
        self.graph.add_node(node2)
        self.graph.add_node(node3)

        self.graph.add_undirected_edge(node1, node2)
        self.graph.add_undirected_edge(node1, node3)

        result = self.util.topological_sort(self.graph)

        self.assert_all_nodes_were_found(self.graph, result)

    def test_two_undirected_edges_as_chain(self):
        node1, node2, node3 = 'A', 'B', 'C'

        self.graph.add_node(node1)
        self.graph.add_node(node2)
        self.graph.add_node(node3)

        self.graph.add_undirected_edge(node1, node2)
        self.graph.add_undirected_edge(node2, node3)

        result = self.util.topological_sort(self.graph)

        self.assert_all_nodes_were_found(self.graph, result)

    def test_three_undirected_edges_as_cycle(self):
        node1, node2, node3 = 'A', 'B', 'C'

        self.graph.add_node(node1)
        self.graph.add_node(node2)
        self.graph.add_node(node3)

        self.graph.add_undirected_edge(node1, node2)
        self.graph.add_undirected_edge(node2, node3)
        self.graph.add_undirected_edge(node3, node1)

        result = self.util.topological_sort(self.graph)

        self.assert_all_nodes_were_found(self.graph, result)

    def test_undirected_edges_as_one_component(self):
        (node_a, node_b, node_c, node_d, node_e, node_f,
         node_g, node_h) = 'A', 'B', 'C', 'D', 'E', 'F', 'G', 'H'

        self.graph.add_node(node_a)
        self.graph.add_node(node_b)
        self.graph.add_node(node_c)
        self.graph.add_node(node_d)
        self.graph.add_node(node_e)
        self.graph.add_node(node_f)
        self.graph.add_node(node_g)
        self.graph.add_node(node_h)

        self.graph.add_undirected_edge(node_a, node_b)
        self.graph.add_undirected_edge(node_a, node_c)
        self.graph.add_undirected_edge(node_b, node_c)
        self.graph.add_undirected_edge(node_c, node_d)
        self.graph.add_undirected_edge(node_c, node_h)
        self.graph.add_undirected_edge(node_d, node_e)
        self.graph.add_undirected_edge(node_e, node_f)
        self.graph.add_undirected_edge(node_e, node_g)
        self.graph.add_undirected_edge(node_f, node_g)
        self.graph.add_undirected_edge(node_g, node_h)

        result = self.util.topological_sort(self.graph)

        self.assert_all_nodes_were_found(self.graph, result)

    def test_many_undirected_edges_as_two_components(self):
        (node_a, node_b, node_c, node_d, node_e, node_f,
         node_g, node_h, node_i, node_j) = \
            'A', 'B', 'C', 'D', 'E', 'F', 'G', 'H', 'I', 'J'

        self.graph.add_node(node_a)
        self.graph.add_node(node_b)
        self.graph.add_node(node_c)
        self.graph.add_node(node_d)
        self.graph.add_node(node_e)
        self.graph.add_node(node_f)
        self.graph.add_node(node_g)
        self.graph.add_node(node_h)
        self.graph.add_node(node_i)
        self.graph.add_node(node_j)

        self.graph.add_undirected_edge(node_a, node_c)
        self.graph.add_undirected_edge(node_a, node_d)
        self.graph.add_undirected_edge(node_a, node_f)
        self.graph.add_undirected_edge(node_b, node_e)
        self.graph.add_undirected_edge(node_c, node_h)
        self.graph.add_undirected_edge(node_c, node_i)
        self.graph.add_undirected_edge(node_e, node_g)
        self.graph.add_undirected_edge(node_e, node_j)
        self.graph.add_undirected_edge(node_f, node_i)
        self.graph.add_undirected_edge(node_h, node_i)

        result = self.util.topological_sort(self.graph)

        self.assert_all_nodes_were_found(self.graph, result)

    def test_many_undirected_edges_as_three_components(self):
        (node_a, node_b, node_c, node_d, node_e, node_f,
         node_g, node_h, node_i) = \
            'A', 'B', 'C', 'D', 'E', 'F', 'G', 'H', 'I'

        self.graph.add_node(node_a)
        self.graph.add_node(node_b)
        self.graph.add_node(node_c)
        self.graph.add_node(node_d)
        self.graph.add_node(node_e)
        self.graph.add_node(node_f)
        self.graph.add_node(node_g)
        self.graph.add_node(node_h)
        self.graph.add_node(node_i)

        self.graph.add_undirected_edge(node_a, node_b)
        self.graph.add_undirected_edge(node_a, node_c)
        self.graph.add_undirected_edge(node_a, node_d)
        self.graph.add_undirected_edge(node_b, node_c)
        self.graph.add_undirected_edge(node_e, node_f)
        self.graph.add_undirected_edge(node_g, node_h)
        self.graph.add_undirected_edge(node_g, node_i)
        self.graph.add_undirected_edge(node_h, node_i)

        result = self.util.topological_sort(self.graph)

        self.assert_all_nodes_were_found(self.graph, result)

    def test_four_nodes(self):
        node1, node2, node3, node4 = 1, 2, 3, 4

        self.graph.add_node(node1)
        self.graph.add_node(node2)
        self.graph.add_node(node3)
        self.graph.add_node(node4)

        self.graph.add_directed_edge(node1, node2)
        self.graph.add_directed_edge(node3, node1)
        self.graph.add_directed_edge(node4, node1)

        result = self.util.topological_sort(self.graph)

        self.assert_all_nodes_were_found(self.graph, result)

    def test_five_nodes_case1(self):
        node_a, node_b, node_c, node_d, node_e = 'A', 'B', 'C', 'D', 'E'

        self.graph.add_node(node_a)
        self.graph.add_node(node_b)
        self.graph.add_node(node_c)
        self.graph.add_node(node_d)
        self.graph.add_node(node_e)

        self.graph.add_directed_edge(node_a, node_b)
        self.graph.add_directed_edge(node_a, node_d)
        self.graph.add_directed_edge(node_a, node_e)
        self.graph.add_directed_edge(node_b, node_c)
        self.graph.add_directed_edge(node_c, node_d)
        self.graph.add_directed_edge(node_e, node_d)

        result = self.util.topological_sort(self.graph)

        self.assert_all_nodes_were_found(self.graph, result)

    def test_five_nodes_case2(self):
        node1, node2, node3, node4, node5 = 1, 2, 3, 4, 5

        self.graph.add_node(node1)
        self.graph.add_node(node2)
        self.graph.add_node(node3)
        self.graph.add_node(node4)
        self.graph.add_node(node5)

        self.graph.add_directed_edge(node2, node1)
        self.graph.add_directed_edge(node3, node1)
        self.graph.add_directed_edge(node3, node2)
        self.graph.add_directed_edge(node4, node1)
        self.graph.add_directed_edge(node4, node3)
        self.graph.add_directed_edge(node5, node2)
        self.graph.add_directed_edge(node5, node3)

        result = self.util.topological_sort(self.graph)

        self.assert_all_nodes_were_found(self.graph, result)

class StronglyConnectedComponentsTestCase(unittest.TestCase):

    def setUp(self):
        self.util = graph_util.GraphUtil()
        self.graph = graph_util.Graph()

    def tearDown(self):
        pass

    def assert_components(self, expected_components, components):
        self.assertEqual(len(expected_components), len(components))
        for i in range(len(components)):
            expected_components[i].sort()
            components[i].sort()

        expected_components.sort()
        components.sort()

        self.assertEqual(expected_components, components)

    def test_three_nodes(self):
        node_u, node_v, node_w = 'u', 'v', 'w'

        self.graph.add_node(node_u)
        self.graph.add_node(node_v)
        self.graph.add_node(node_w)

        self.graph.add_undirected_edge(node_u, node_v)
        self.graph.add_undirected_edge(node_v, node_w)

        result = self.util.strongly_connected_components(self.graph)

        expected_components = [
                                  [ node_u, node_v, node_w  ],
                              ]
        self.assert_components(expected_components, result)

    def test_four_nodes(self):
        node1, node2, node3, node4 = 1, 2, 3, 4

        self.graph.add_node(node1)
        self.graph.add_node(node2)
        self.graph.add_node(node3)
        self.graph.add_node(node4)

        self.graph.add_directed_edge(node1, node2)
        self.graph.add_directed_edge(node2, node3)
        self.graph.add_directed_edge(node3, node1)
        self.graph.add_directed_edge(node4, node1)

        result = self.util.strongly_connected_components(self.graph)

        expected_components = [
                                  [ node1, node2, node3 ],
                                  [ node4 ],
                              ]
        self.assert_components(expected_components, result)

    def test_five_nodes(self):
        node1, node2, node3, node4, node5 = 1, 2, 3, 4, 5

        self.graph.add_node(node1)
        self.graph.add_node(node2)
        self.graph.add_node(node3)
        self.graph.add_node(node4)
        self.graph.add_node(node5)

        self.graph.add_directed_edge(node2, node1)
        self.graph.add_directed_edge(node3, node1)
        self.graph.add_directed_edge(node3, node2)
        self.graph.add_directed_edge(node4, node1)
        self.graph.add_directed_edge(node4, node3)
        self.graph.add_directed_edge(node5, node2)
        self.graph.add_directed_edge(node5, node3)

        result = self.util.strongly_connected_components(self.graph)

        expected_components = [
                                  [ node1 ],
                                  [ node2 ],
                                  [ node3 ],
                                  [ node4 ],
                                  [ node5 ],
                              ]
        self.assert_components(expected_components, result)

    def test_nine_nodes_case1(self):
        (node_a, node_b, node_c, node_d, node_e, node_f,
         node_g, node_h, node_i) = \
            'A', 'B', 'C', 'D', 'E', 'F', 'G', 'H', 'I'

        self.graph.add_node(node_a)
        self.graph.add_node(node_b)
        self.graph.add_node(node_c)
        self.graph.add_node(node_d)
        self.graph.add_node(node_e)
        self.graph.add_node(node_f)
        self.graph.add_node(node_g)
        self.graph.add_node(node_h)
        self.graph.add_node(node_i)

        self.graph.add_directed_edge(node_a, node_b)
        self.graph.add_directed_edge(node_b, node_e)
        self.graph.add_directed_edge(node_b, node_f)
        self.graph.add_directed_edge(node_c, node_b)
        self.graph.add_directed_edge(node_d, node_a)
        self.graph.add_directed_edge(node_e, node_a)
        self.graph.add_directed_edge(node_e, node_c)
        self.graph.add_directed_edge(node_e, node_h)
        self.graph.add_directed_edge(node_g, node_h)
        self.graph.add_directed_edge(node_h, node_i)
        self.graph.add_directed_edge(node_i, node_f)
        self.graph.add_directed_edge(node_i, node_h)

        result = self.util.strongly_connected_components(self.graph)

        expected_components = [
                                  [ node_f ],
                                  [ node_h, node_i ],
                                  [ node_g ],
                                  [ node_a, node_b, node_c, node_e ],
                                  [ node_d ],
                              ]
        self.assert_components(expected_components, result)

    def test_nine_nodes_case2(self):
        (node_a, node_b, node_c, node_d, node_e, node_f,
         node_g, node_h, node_i) = \
            'A', 'B', 'C', 'D', 'E', 'F', 'G', 'H', 'I'

        self.graph.add_node(node_a)
        self.graph.add_node(node_b)
        self.graph.add_node(node_c)
        self.graph.add_node(node_d)
        self.graph.add_node(node_e)
        self.graph.add_node(node_f)
        self.graph.add_node(node_g)
        self.graph.add_node(node_h)
        self.graph.add_node(node_i)

        self.graph.add_directed_edge(node_a, node_e)
        self.graph.add_directed_edge(node_b, node_a)
        self.graph.add_directed_edge(node_b, node_c)
        self.graph.add_directed_edge(node_b, node_g)
        self.graph.add_directed_edge(node_c, node_i)
        self.graph.add_directed_edge(node_d, node_a)
        self.graph.add_directed_edge(node_d, node_g)
        self.graph.add_directed_edge(node_e, node_h)
        self.graph.add_directed_edge(node_f, node_b)
        self.graph.add_directed_edge(node_f, node_c)
        self.graph.add_directed_edge(node_f, node_i)
        self.graph.add_directed_edge(node_g, node_h)
        self.graph.add_directed_edge(node_h, node_f)

        result = self.util.strongly_connected_components(self.graph)

        expected_components = [
                                  [ node_i ],
                                  [ node_c ],
                                  [ node_a, node_b, node_e,
                                   node_f, node_g, node_h ],
                                  [ node_d ],
                              ]
        self.assert_components(expected_components, result)

class ShortestPathTreeTestCase(unittest.TestCase):

    def setUp(self):
        self.util = graph_util.GraphUtil()
        self.graph = graph_util.Graph()

    def tearDown(self):
        pass

    def test_graph_with_one_node(self):
        node = 'A'

        self.graph.add_node(node)

        distance_map, predecessor_map = self.util.shortest_path_tree(self.graph,
                                                                     node)

        expected_distance_map = {}
        expected_distance_map[node] = 0
        expected_predecessor_map = {}
        expected_predecessor_map[node] = None

        Util.assert_items(self, expected_distance_map, distance_map)
        Util.assert_items(self, expected_predecessor_map, predecessor_map)

        result = self.util.reconstruct_shortest_path(node,
                                                     node,
                                                     predecessor_map)

        self.assertEqual([], result)

    def test_one_directed_edge(self):
        node1, node2 = 'A', 'B'

        self.graph.add_node(node1)
        self.graph.add_node(node2)

        self.graph.add_directed_edge(node1, node2)

        distance_map, predecessor_map = self.util.shortest_path_tree(self.graph,
                                                                     node1)

        expected_distance_map = {}
        expected_distance_map[node1] = 0
        expected_distance_map[node2] = 1
        expected_predecessor_map = {}
        expected_predecessor_map[node1] = None
        expected_predecessor_map[node2] = node1

        Util.assert_items(self, expected_distance_map, distance_map)
        Util.assert_items(self, expected_predecessor_map, predecessor_map)

        result = self.util.reconstruct_shortest_path(node1,
                                                     node1,
                                                     predecessor_map)

        self.assertEqual([], result)

        result = self.util.reconstruct_shortest_path(node1,
                                                     node2,
                                                     predecessor_map)

        self.assertEqual([ node2 ], result)

        result = self.util.reconstruct_shortest_path(node2,
                                                     node2,
                                                     predecessor_map)

        self.assertEqual([], result)

    def test_one_undirected_edge(self):
        node1, node2 = 'A', 'B'

        self.graph.add_node(node1)
        self.graph.add_node(node2)

        self.graph.add_undirected_edge(node1, node2)

        distance_map, predecessor_map = self.util.shortest_path_tree(self.graph,
                                                                     node1)

        expected_distance_map = {}
        expected_distance_map[node1] = 0
        expected_distance_map[node2] = 1
        expected_predecessor_map = {}
        expected_predecessor_map[node1] = None
        expected_predecessor_map[node2] = node1

        Util.assert_items(self, expected_distance_map, distance_map)
        Util.assert_items(self, expected_predecessor_map, predecessor_map)

        result = self.util.reconstruct_shortest_path(node1,
                                                     node1,
                                                     predecessor_map)

        self.assertEqual([], result)

        result = self.util.reconstruct_shortest_path(node1,
                                                     node2,
                                                     predecessor_map)

        self.assertEqual([ node2 ], result)

        result = self.util.reconstruct_shortest_path(node2,
                                                     node2,
                                                     predecessor_map)

        self.assertEqual([], result)

    def test_two_directed_edges_as_rays(self):
        node1, node2, node3 = 'A', 'B', 'C'

        self.graph.add_node(node1)
        self.graph.add_node(node2)
        self.graph.add_node(node3)

        self.graph.add_directed_edge(node1, node2)
        self.graph.add_directed_edge(node1, node3)

        distance_map, predecessor_map = self.util.shortest_path_tree(self.graph,
                                                                     node1)

        expected_distance_map = {}
        expected_distance_map[node1] = 0
        expected_distance_map[node2] = 1
        expected_distance_map[node3] = 1
        expected_predecessor_map = {}
        expected_predecessor_map[node1] = None
        expected_predecessor_map[node2] = node1
        expected_predecessor_map[node3] = node1

        Util.assert_items(self, expected_distance_map, distance_map)
        Util.assert_items(self, expected_predecessor_map, predecessor_map)

        result = self.util.reconstruct_shortest_path(node1,
                                                     node1,
                                                     predecessor_map)

        self.assertEqual([], result)

        result = self.util.reconstruct_shortest_path(node1,
                                                     node2,
                                                     predecessor_map)

        self.assertEqual([ node2 ], result)

        result = self.util.reconstruct_shortest_path(node1,
                                                     node3,
                                                     predecessor_map)

        self.assertEqual([ node3 ], result)

        result = self.util.reconstruct_shortest_path(node2,
                                                     node2,
                                                     predecessor_map)

        self.assertEqual([], result)

        result = self.util.reconstruct_shortest_path(node2,
                                                     node3,
                                                     predecessor_map)

        self.assertEqual([], result)

        result = self.util.reconstruct_shortest_path(node3,
                                                     node3,
                                                     predecessor_map)

        self.assertEqual([], result)

    def test_two_directed_edges_as_chain(self):
        node1, node2, node3 = 'A', 'B', 'C'

        self.graph.add_node(node1)
        self.graph.add_node(node2)
        self.graph.add_node(node3)

        self.graph.add_directed_edge(node1, node2)
        self.graph.add_directed_edge(node2, node3)

        distance_map, predecessor_map = self.util.shortest_path_tree(self.graph,
                                                                     node1)

        expected_distance_map = {}
        expected_distance_map[node1] = 0
        expected_distance_map[node2] = 1
        expected_distance_map[node3] = 2
        expected_predecessor_map = {}
        expected_predecessor_map[node1] = None
        expected_predecessor_map[node2] = node1
        expected_predecessor_map[node3] = node2

        Util.assert_items(self, expected_distance_map, distance_map)
        Util.assert_items(self, expected_predecessor_map, predecessor_map)

        result = self.util.reconstruct_shortest_path(node1,
                                                     node1,
                                                     predecessor_map)

        self.assertEqual([], result)

        result = self.util.reconstruct_shortest_path(node1,
                                                     node2,
                                                     predecessor_map)

        self.assertEqual([ node2 ], result)

        result = self.util.reconstruct_shortest_path(node1,
                                                     node3,
                                                     predecessor_map)

        self.assertEqual([ node2, node3 ], result)

        result = self.util.reconstruct_shortest_path(node2,
                                                     node2,
                                                     predecessor_map)

        self.assertEqual([], result)

        result = self.util.reconstruct_shortest_path(node2,
                                                     node3,
                                                     predecessor_map)

        self.assertEqual([ node3 ], result)

        result = self.util.reconstruct_shortest_path(node3,
                                                     node3,
                                                     predecessor_map)

        self.assertEqual([], result)

    def test_three_directed_edges_as_cycle(self):
        node1, node2, node3 = 'A', 'B', 'C'

        self.graph.add_node(node1)
        self.graph.add_node(node2)
        self.graph.add_node(node3)

        self.graph.add_directed_edge(node1, node2)
        self.graph.add_directed_edge(node2, node3)
        self.graph.add_directed_edge(node3, node1)

        distance_map, predecessor_map = self.util.shortest_path_tree(self.graph,
                                                                     node1)

        expected_distance_map = {}
        expected_distance_map[node1] = 0
        expected_distance_map[node2] = 1
        expected_distance_map[node3] = 2
        expected_predecessor_map = {}
        expected_predecessor_map[node1] = None
        expected_predecessor_map[node2] = node1
        expected_predecessor_map[node3] = node2

        Util.assert_items(self, expected_distance_map, distance_map)
        Util.assert_items(self, expected_predecessor_map, predecessor_map)

    def test_two_undirected_edges_as_rays(self):
        node1, node2, node3 = 'A', 'B', 'C'

        self.graph.add_node(node1)
        self.graph.add_node(node2)
        self.graph.add_node(node3)

        self.graph.add_undirected_edge(node1, node2)
        self.graph.add_undirected_edge(node1, node3)

        distance_map, predecessor_map = self.util.shortest_path_tree(self.graph,
                                                                     node1)

        expected_distance_map = {}
        expected_distance_map[node1] = 0
        expected_distance_map[node2] = 1
        expected_distance_map[node3] = 1
        expected_predecessor_map = {}
        expected_predecessor_map[node1] = None
        expected_predecessor_map[node2] = node1
        expected_predecessor_map[node3] = node1

        Util.assert_items(self, expected_distance_map, distance_map)
        Util.assert_items(self, expected_predecessor_map, predecessor_map)

        result = self.util.reconstruct_shortest_path(node1,
                                                     node1,
                                                     predecessor_map)

        self.assertEqual([], result)

        result = self.util.reconstruct_shortest_path(node1,
                                                     node2,
                                                     predecessor_map)

        self.assertEqual([ node2 ], result)

        result = self.util.reconstruct_shortest_path(node1,
                                                     node3,
                                                     predecessor_map)

        self.assertEqual([ node3 ], result)

        result = self.util.reconstruct_shortest_path(node2,
                                                     node2,
                                                     predecessor_map)

        self.assertEqual([], result)

        result = self.util.reconstruct_shortest_path(node2,
                                                     node3,
                                                     predecessor_map)

        self.assertEqual([], result)

        result = self.util.reconstruct_shortest_path(node3,
                                                     node3,
                                                     predecessor_map)

        self.assertEqual([], result)

    def test_two_undirected_edges_as_chain(self):
        node1, node2, node3 = 'A', 'B', 'C'

        self.graph.add_node(node1)
        self.graph.add_node(node2)
        self.graph.add_node(node3)

        self.graph.add_undirected_edge(node1, node2)
        self.graph.add_undirected_edge(node2, node3)

        distance_map, predecessor_map = self.util.shortest_path_tree(self.graph,
                                                                     node1)

        expected_distance_map = {}
        expected_distance_map[node1] = 0
        expected_distance_map[node2] = 1
        expected_distance_map[node3] = 2
        expected_predecessor_map = {}
        expected_predecessor_map[node1] = None
        expected_predecessor_map[node2] = node1
        expected_predecessor_map[node3] = node2

        Util.assert_items(self, expected_distance_map, distance_map)
        Util.assert_items(self, expected_predecessor_map, predecessor_map)

        result = self.util.reconstruct_shortest_path(node1,
                                                     node1,
                                                     predecessor_map)

        self.assertEqual([], result)

        result = self.util.reconstruct_shortest_path(node1,
                                                     node2,
                                                     predecessor_map)

        self.assertEqual([ node2 ], result)

        result = self.util.reconstruct_shortest_path(node1,
                                                     node3,
                                                     predecessor_map)

        self.assertEqual([ node2, node3 ], result)

        result = self.util.reconstruct_shortest_path(node2,
                                                     node2,
                                                     predecessor_map)

        self.assertEqual([], result)

        result = self.util.reconstruct_shortest_path(node2,
                                                     node3,
                                                     predecessor_map)

        self.assertEqual([ node3 ], result)

        result = self.util.reconstruct_shortest_path(node3,
                                                     node3,
                                                     predecessor_map)

        self.assertEqual([], result)

    def test_three_undirected_edges_as_cycle(self):
        node1, node2, node3 = 'A', 'B', 'C'

        self.graph.add_node(node1)
        self.graph.add_node(node2)
        self.graph.add_node(node3)

        self.graph.add_undirected_edge(node1, node2)
        self.graph.add_undirected_edge(node2, node3)
        self.graph.add_undirected_edge(node3, node1)

        distance_map, predecessor_map = self.util.shortest_path_tree(self.graph,
                                                                     node1)

        expected_distance_map = {}
        expected_distance_map[node1] = 0
        expected_distance_map[node2] = 1
        expected_distance_map[node3] = 1
        expected_predecessor_map = {}
        expected_predecessor_map[node1] = None
        expected_predecessor_map[node2] = node1
        expected_predecessor_map[node3] = node1

        Util.assert_items(self, expected_distance_map, distance_map)
        Util.assert_items(self, expected_predecessor_map, predecessor_map)

        result = self.util.reconstruct_shortest_path(node1,
                                                     node1,
                                                     predecessor_map)

        self.assertEqual([], result)

        result = self.util.reconstruct_shortest_path(node1,
                                                     node2,
                                                     predecessor_map)

        self.assertEqual([ node2 ], result)

        result = self.util.reconstruct_shortest_path(node1,
                                                     node3,
                                                     predecessor_map)

        self.assertEqual([ node3 ], result)

        result = self.util.reconstruct_shortest_path(node2,
                                                     node2,
                                                     predecessor_map)

        self.assertEqual([], result)

        result = self.util.reconstruct_shortest_path(node2,
                                                     node3,
                                                     predecessor_map)

        self.assertEqual([], result)

        result = self.util.reconstruct_shortest_path(node3,
                                                     node3,
                                                     predecessor_map)

        self.assertEqual([], result)

    def test_undirected_edges_as_one_component(self):
        (node_a, node_b, node_c, node_d, node_e, node_f,
         node_g, node_h) = 'A', 'B', 'C', 'D', 'E', 'F', 'G', 'H'

        self.graph.add_node(node_a)
        self.graph.add_node(node_b)
        self.graph.add_node(node_c)
        self.graph.add_node(node_d)
        self.graph.add_node(node_e)
        self.graph.add_node(node_f)
        self.graph.add_node(node_g)
        self.graph.add_node(node_h)

        self.graph.add_undirected_edge(node_a, node_b)
        self.graph.add_undirected_edge(node_a, node_c)
        self.graph.add_undirected_edge(node_b, node_c)
        self.graph.add_undirected_edge(node_c, node_d)
        self.graph.add_undirected_edge(node_c, node_h)
        self.graph.add_undirected_edge(node_d, node_e)
        self.graph.add_undirected_edge(node_e, node_f)
        self.graph.add_undirected_edge(node_e, node_g)
        self.graph.add_undirected_edge(node_f, node_g)
        self.graph.add_undirected_edge(node_g, node_h)

        distance_map, predecessor_map = self.util.shortest_path_tree(self.graph,
                                                                     node_a)

        expected_distance_map = {}
        expected_distance_map[node_a] = 0
        expected_distance_map[node_b] = 1
        expected_distance_map[node_c] = 1
        expected_distance_map[node_d] = 2
        expected_distance_map[node_e] = 3
        expected_distance_map[node_f] = 4
        expected_distance_map[node_g] = 3
        expected_distance_map[node_h] = 2
        expected_predecessor_map = {}
        expected_predecessor_map[node_a] = None
        expected_predecessor_map[node_b] = node_a
        expected_predecessor_map[node_c] = node_a
        expected_predecessor_map[node_d] = node_c
        expected_predecessor_map[node_e] = node_d
        expected_predecessor_map[node_f] = node_e
        expected_predecessor_map[node_g] = node_h
        expected_predecessor_map[node_h] = node_c

        Util.assert_items(self, expected_distance_map, distance_map)
        Util.assert_items(self, expected_predecessor_map, predecessor_map)

    def test_many_undirected_edges_as_two_components(self):
        (node_a, node_b, node_c, node_d, node_e, node_f,
         node_g, node_h, node_i, node_j) = \
            'A', 'B', 'C', 'D', 'E', 'F', 'G', 'H', 'I', 'J'

        self.graph.add_node(node_a)
        self.graph.add_node(node_b)
        self.graph.add_node(node_c)
        self.graph.add_node(node_d)
        self.graph.add_node(node_e)
        self.graph.add_node(node_f)
        self.graph.add_node(node_g)
        self.graph.add_node(node_h)
        self.graph.add_node(node_i)
        self.graph.add_node(node_j)

        self.graph.add_undirected_edge(node_a, node_c)
        self.graph.add_undirected_edge(node_a, node_d)
        self.graph.add_undirected_edge(node_a, node_f)
        self.graph.add_undirected_edge(node_b, node_e)
        self.graph.add_undirected_edge(node_c, node_h)
        self.graph.add_undirected_edge(node_c, node_i)
        self.graph.add_undirected_edge(node_e, node_g)
        self.graph.add_undirected_edge(node_e, node_j)
        self.graph.add_undirected_edge(node_f, node_i)
        self.graph.add_undirected_edge(node_h, node_i)

        distance_map, predecessor_map = self.util.shortest_path_tree(self.graph,
                                                                     node_a)

        expected_distance_map = {}
        expected_distance_map[node_a] = 0
        expected_distance_map[node_b] = math.inf
        expected_distance_map[node_c] = 1
        expected_distance_map[node_d] = 1
        expected_distance_map[node_e] = math.inf
        expected_distance_map[node_f] = 1
        expected_distance_map[node_g] = math.inf
        expected_distance_map[node_h] = 2
        expected_distance_map[node_i] = 2
        expected_distance_map[node_j] = math.inf
        expected_predecessor_map = {}
        expected_predecessor_map[node_a] = None
        expected_predecessor_map[node_b] = None
        expected_predecessor_map[node_c] = node_a
        expected_predecessor_map[node_d] = node_a
        expected_predecessor_map[node_e] = None
        expected_predecessor_map[node_f] = node_a
        expected_predecessor_map[node_g] = None
        expected_predecessor_map[node_h] = node_c
        expected_predecessor_map[node_i] = node_c
        expected_predecessor_map[node_j] = None

        Util.assert_items(self, expected_distance_map, distance_map)
        Util.assert_items(self, expected_predecessor_map, predecessor_map)

    def test_many_undirected_edges_as_three_components(self):
        (node_a, node_b, node_c, node_d, node_e, node_f,
         node_g, node_h, node_i) = \
            'A', 'B', 'C', 'D', 'E', 'F', 'G', 'H', 'I'

        self.graph.add_node(node_a)
        self.graph.add_node(node_b)
        self.graph.add_node(node_c)
        self.graph.add_node(node_d)
        self.graph.add_node(node_e)
        self.graph.add_node(node_f)
        self.graph.add_node(node_g)
        self.graph.add_node(node_h)
        self.graph.add_node(node_i)

        self.graph.add_undirected_edge(node_a, node_b)
        self.graph.add_undirected_edge(node_a, node_c)
        self.graph.add_undirected_edge(node_a, node_d)
        self.graph.add_undirected_edge(node_b, node_c)
        self.graph.add_undirected_edge(node_e, node_f)
        self.graph.add_undirected_edge(node_g, node_h)
        self.graph.add_undirected_edge(node_g, node_i)
        self.graph.add_undirected_edge(node_h, node_i)

        distance_map, predecessor_map = self.util.shortest_path_tree(self.graph,
                                                                     node_a)

        expected_distance_map = {}
        expected_distance_map[node_a] = 0
        expected_distance_map[node_b] = 1
        expected_distance_map[node_c] = 1
        expected_distance_map[node_d] = 1
        expected_distance_map[node_e] = math.inf
        expected_distance_map[node_f] = math.inf
        expected_distance_map[node_g] = math.inf
        expected_distance_map[node_h] = math.inf
        expected_distance_map[node_i] = math.inf
        expected_predecessor_map = {}
        expected_predecessor_map[node_a] = None
        expected_predecessor_map[node_b] = node_a
        expected_predecessor_map[node_c] = node_a
        expected_predecessor_map[node_d] = node_a
        expected_predecessor_map[node_e] = None
        expected_predecessor_map[node_f] = None
        expected_predecessor_map[node_g] = None
        expected_predecessor_map[node_h] = None
        expected_predecessor_map[node_i] = None

        Util.assert_items(self, expected_distance_map, distance_map)
        Util.assert_items(self, expected_predecessor_map, predecessor_map)

class IsBipartiteTreeTestCase(unittest.TestCase):

    def setUp(self):
        self.util = graph_util.GraphUtil()
        self.graph = graph_util.Graph()

    def tearDown(self):
        pass

    def test_empty_graph(self):
        result = self.util.is_bipartite(self.graph)

        self.assertEqual(True, result)

    def test_graph_with_one_node(self):
        node = 'A'

        self.graph.add_node(node)

        result = self.util.is_bipartite(self.graph)

        self.assertEqual(True, result)

    def test_one_directed_edge(self):
        node1, node2 = 'A', 'B'

        self.graph.add_node(node1)
        self.graph.add_node(node2)

        self.graph.add_directed_edge(node1, node2)

        result = self.util.is_bipartite(self.graph)

        self.assertEqual(True, result)

    def test_one_undirected_edge(self):
        node1, node2 = 'A', 'B'

        self.graph.add_node(node1)
        self.graph.add_node(node2)

        self.graph.add_undirected_edge(node1, node2)

        result = self.util.is_bipartite(self.graph)

        self.assertEqual(True, result)

    def test_two_directed_edges_as_rays(self):
        node1, node2, node3 = 'A', 'B', 'C'

        self.graph.add_node(node1)
        self.graph.add_node(node2)
        self.graph.add_node(node3)

        self.graph.add_directed_edge(node1, node2)
        self.graph.add_directed_edge(node1, node3)

        result = self.util.is_bipartite(self.graph)

        self.assertEqual(True, result)

    def test_two_directed_edges_as_chain(self):
        node1, node2, node3 = 'A', 'B', 'C'

        self.graph.add_node(node1)
        self.graph.add_node(node2)
        self.graph.add_node(node3)

        self.graph.add_directed_edge(node1, node2)
        self.graph.add_directed_edge(node2, node3)

        result = self.util.is_bipartite(self.graph)

        self.assertEqual(True, result)

    def test_three_directed_edges_as_cycle(self):
        node1, node2, node3 = 'A', 'B', 'C'

        self.graph.add_node(node1)
        self.graph.add_node(node2)
        self.graph.add_node(node3)

        self.graph.add_directed_edge(node1, node2)
        self.graph.add_directed_edge(node2, node3)
        self.graph.add_directed_edge(node3, node1)

        result = self.util.is_bipartite(self.graph)

        self.assertEqual(False, result)

    def test_two_undirected_edges_as_rays(self):
        node1, node2, node3 = 'A', 'B', 'C'

        self.graph.add_node(node1)
        self.graph.add_node(node2)
        self.graph.add_node(node3)

        self.graph.add_undirected_edge(node1, node2)
        self.graph.add_undirected_edge(node1, node3)

        result = self.util.is_bipartite(self.graph)

        self.assertEqual(True, result)

    def test_two_undirected_edges_as_chain(self):
        node1, node2, node3 = 'A', 'B', 'C'

        self.graph.add_node(node1)
        self.graph.add_node(node2)
        self.graph.add_node(node3)

        self.graph.add_undirected_edge(node1, node2)
        self.graph.add_undirected_edge(node2, node3)

        result = self.util.is_bipartite(self.graph)

        self.assertEqual(True, result)

    def test_three_undirected_edges_as_cycle(self):
        node1, node2, node3 = 'A', 'B', 'C'

        self.graph.add_node(node1)
        self.graph.add_node(node2)
        self.graph.add_node(node3)

        self.graph.add_undirected_edge(node1, node2)
        self.graph.add_undirected_edge(node2, node3)
        self.graph.add_undirected_edge(node3, node1)

        result = self.util.is_bipartite(self.graph)

        self.assertEqual(False, result)

    def test_eight_node_graph(self):
        (node_a, node_b, node_c, node_d, node_e, node_f,
         node_g, node_h) = 'A', 'B', 'C', 'D', 'E', 'F', 'G', 'H'

        self.graph.add_node(node_a)
        self.graph.add_node(node_b)
        self.graph.add_node(node_c)
        self.graph.add_node(node_d)
        self.graph.add_node(node_e)
        self.graph.add_node(node_f)
        self.graph.add_node(node_g)
        self.graph.add_node(node_h)

        self.graph.add_undirected_edge(node_a, node_b)
        self.graph.add_undirected_edge(node_a, node_c)
        self.graph.add_undirected_edge(node_b, node_c)
        self.graph.add_undirected_edge(node_c, node_d)
        self.graph.add_undirected_edge(node_c, node_h)
        self.graph.add_undirected_edge(node_d, node_e)
        self.graph.add_undirected_edge(node_e, node_f)
        self.graph.add_undirected_edge(node_e, node_g)
        self.graph.add_undirected_edge(node_f, node_g)
        self.graph.add_undirected_edge(node_g, node_h)

        result = self.util.is_bipartite(self.graph)

        self.assertEqual(False, result)

    def test_four_node_graph(self):
        """
        This graph is not bipartite. To see this, assume that the node 1
        is colored white. Then the nodes 2 and 3 should be colored black
        since the graph contains the edges {1, 2} and {1, 3}. But then the
        edge {2, 3} has both endpoints of the same color.
        """

        node1, node2, node3, node4 = 1, 2, 3, 4

        self.graph.add_node(node1)
        self.graph.add_node(node2)
        self.graph.add_node(node3)
        self.graph.add_node(node4)

        self.graph.add_directed_edge(node1, node2)
        self.graph.add_directed_edge(node1, node3)
        self.graph.add_directed_edge(node1, node4)
        self.graph.add_directed_edge(node3, node1)
        self.graph.add_directed_edge(node3, node2)
        self.graph.add_directed_edge(node4, node1)

        result = self.util.is_bipartite(self.graph)

        self.assertEqual(False, result)

    def test_five_node_graph(self):
        """
        This graph is bipartite: assign the nodes 4 and 5 the white color,
        assign all the remaining nodes the black color.
        """

        node1, node2, node3, node4, node5 = 1, 2, 3, 4, 5

        self.graph.add_node(node1)
        self.graph.add_node(node2)
        self.graph.add_node(node3)
        self.graph.add_node(node4)
        self.graph.add_node(node5)

        self.graph.add_directed_edge(node1, node4)
        self.graph.add_directed_edge(node2, node4)
        self.graph.add_directed_edge(node2, node5)
        self.graph.add_directed_edge(node3, node4)
        self.graph.add_directed_edge(node4, node1)
        self.graph.add_directed_edge(node4, node2)
        self.graph.add_directed_edge(node4, node3)
        self.graph.add_directed_edge(node5, node2)

        result = self.util.is_bipartite(self.graph)

        self.assertEqual(True, result)

class DijkstraShortestPathsTestCase(unittest.TestCase):

    def setUp(self):
        self.util = graph_util.GraphUtil()
        self.graph = graph_util.Graph()

    def tearDown(self):
        pass

    def test_empty_graph(self):
        node = 'A'

        with self.assertRaisesRegex(KeyError,
                                    "\'A\'"):
            self.util.dijkstra_shortest_paths(self.graph, node)

    def test_graph_with_one_node(self):
        node = 'A'

        self.graph.add_node(node)

        distance_map, predecessor_map = self.util.dijkstra_shortest_paths(
                                                                     self.graph,
                                                                     node)

        expected_distance_map = {}
        expected_distance_map[node] = 0
        expected_predecessor_map = {}
        expected_predecessor_map[node] = None

        Util.assert_items(self, expected_distance_map, distance_map)
        Util.assert_items(self, expected_predecessor_map, predecessor_map)

    def test_one_directed_edge(self):
        node1, node2 = 'A', 'B'

        self.graph.add_node(node1)
        self.graph.add_node(node2)

        self.graph.add_directed_edge(node1, node2, 5)

        distance_map, predecessor_map = self.util.dijkstra_shortest_paths(
                                                                     self.graph,
                                                                     node1)

        expected_distance_map = {}
        expected_distance_map[node1] = 0
        expected_distance_map[node2] = 5
        expected_predecessor_map = {}
        expected_predecessor_map[node1] = None
        expected_predecessor_map[node2] = node1

        Util.assert_items(self, expected_distance_map, distance_map)
        Util.assert_items(self, expected_predecessor_map, predecessor_map)

    def test_one_undirected_edge(self):
        node1, node2 = 'A', 'B'

        self.graph.add_node(node1)
        self.graph.add_node(node2)

        self.graph.add_undirected_edge(node1, node2, 5)

        distance_map, predecessor_map = self.util.dijkstra_shortest_paths(
                                                                     self.graph,
                                                                     node1)

        expected_distance_map = {}
        expected_distance_map[node1] = 0
        expected_distance_map[node2] = 5
        expected_predecessor_map = {}
        expected_predecessor_map[node1] = None
        expected_predecessor_map[node2] = node1

        Util.assert_items(self, expected_distance_map, distance_map)
        Util.assert_items(self, expected_predecessor_map, predecessor_map)

    def test_two_directed_edges_as_rays(self):
        node1, node2, node3 = 'A', 'B', 'C'

        self.graph.add_node(node1)
        self.graph.add_node(node2)
        self.graph.add_node(node3)

        self.graph.add_directed_edge(node1, node2, 1)
        self.graph.add_directed_edge(node1, node3, 2)

        distance_map, predecessor_map = self.util.dijkstra_shortest_paths(
                                                                     self.graph,
                                                                     node1)

        expected_distance_map = {}
        expected_distance_map[node1] = 0
        expected_distance_map[node2] = 1
        expected_distance_map[node3] = 2
        expected_predecessor_map = {}
        expected_predecessor_map[node1] = None
        expected_predecessor_map[node2] = node1
        expected_predecessor_map[node3] = node1

        Util.assert_items(self, expected_distance_map, distance_map)
        Util.assert_items(self, expected_predecessor_map, predecessor_map)

    def test_two_directed_edges_as_chain(self):
        node1, node2, node3 = 'A', 'B', 'C'

        self.graph.add_node(node1)
        self.graph.add_node(node2)
        self.graph.add_node(node3)

        self.graph.add_directed_edge(node1, node2, 1)
        self.graph.add_directed_edge(node2, node3, 2)

        distance_map, predecessor_map = self.util.dijkstra_shortest_paths(
                                                                     self.graph,
                                                                     node1)

        expected_distance_map = {}
        expected_distance_map[node1] = 0
        expected_distance_map[node2] = 1
        expected_distance_map[node3] = 3
        expected_predecessor_map = {}
        expected_predecessor_map[node1] = None
        expected_predecessor_map[node2] = node1
        expected_predecessor_map[node3] = node2

        Util.assert_items(self, expected_distance_map, distance_map)
        Util.assert_items(self, expected_predecessor_map, predecessor_map)

    def test_three_directed_edges_as_cycle(self):
        node1, node2, node3 = 'A', 'B', 'C'

        self.graph.add_node(node1)
        self.graph.add_node(node2)
        self.graph.add_node(node3)

        self.graph.add_directed_edge(node1, node2, 1)
        self.graph.add_directed_edge(node2, node3, 2)
        self.graph.add_directed_edge(node3, node1, 3)

        distance_map, predecessor_map = self.util.dijkstra_shortest_paths(
                                                                     self.graph,
                                                                     node1)

        expected_distance_map = {}
        expected_distance_map[node1] = 0
        expected_distance_map[node2] = 1
        expected_distance_map[node3] = 3
        expected_predecessor_map = {}
        expected_predecessor_map[node1] = None
        expected_predecessor_map[node2] = node1
        expected_predecessor_map[node3] = node2

        Util.assert_items(self, expected_distance_map, distance_map)
        Util.assert_items(self, expected_predecessor_map, predecessor_map)

    def test_two_undirected_edges_as_rays(self):
        node1, node2, node3 = 'A', 'B', 'C'

        self.graph.add_node(node1)
        self.graph.add_node(node2)
        self.graph.add_node(node3)

        self.graph.add_undirected_edge(node1, node2, 1)
        self.graph.add_undirected_edge(node1, node3, 2)

        distance_map, predecessor_map = self.util.dijkstra_shortest_paths(
                                                                     self.graph,
                                                                     node1)

        expected_distance_map = {}
        expected_distance_map[node1] = 0
        expected_distance_map[node2] = 1
        expected_distance_map[node3] = 2
        expected_predecessor_map = {}
        expected_predecessor_map[node1] = None
        expected_predecessor_map[node2] = node1
        expected_predecessor_map[node3] = node1

        Util.assert_items(self, expected_distance_map, distance_map)
        Util.assert_items(self, expected_predecessor_map, predecessor_map)

    def test_two_undirected_edges_as_chain(self):
        node1, node2, node3 = 'A', 'B', 'C'

        self.graph.add_node(node1)
        self.graph.add_node(node2)
        self.graph.add_node(node3)

        self.graph.add_undirected_edge(node1, node2, 1)
        self.graph.add_undirected_edge(node2, node3, 2)

        distance_map, predecessor_map = self.util.dijkstra_shortest_paths(
                                                                     self.graph,
                                                                     node1)

        expected_distance_map = {}
        expected_distance_map[node1] = 0
        expected_distance_map[node2] = 1
        expected_distance_map[node3] = 3
        expected_predecessor_map = {}
        expected_predecessor_map[node1] = None
        expected_predecessor_map[node2] = node1
        expected_predecessor_map[node3] = node2

        Util.assert_items(self, expected_distance_map, distance_map)
        Util.assert_items(self, expected_predecessor_map, predecessor_map)

    def test_three_undirected_edges_as_cycle(self):
        node1, node2, node3 = 'A', 'B', 'C'

        self.graph.add_node(node1)
        self.graph.add_node(node2)
        self.graph.add_node(node3)

        self.graph.add_undirected_edge(node1, node2, 1)
        self.graph.add_undirected_edge(node2, node3, 2)
        self.graph.add_undirected_edge(node3, node1, 3)

        distance_map, predecessor_map = self.util.dijkstra_shortest_paths(
                                                                     self.graph,
                                                                     node1)

        expected_distance_map = {}
        expected_distance_map[node1] = 0
        expected_distance_map[node2] = 1
        expected_distance_map[node3] = 3
        expected_predecessor_map = {}
        expected_predecessor_map[node1] = None
        expected_predecessor_map[node2] = node1
        expected_predecessor_map[node3] = node1

        Util.assert_items(self, expected_distance_map, distance_map)
        Util.assert_items(self, expected_predecessor_map, predecessor_map)

    def test_undirected_edges_as_one_component(self):
        (node_a, node_b, node_c, node_d, node_e, node_f,
         node_g, node_h) = 'A', 'B', 'C', 'D', 'E', 'F', 'G', 'H'

        self.graph.add_node(node_a)
        self.graph.add_node(node_b)
        self.graph.add_node(node_c)
        self.graph.add_node(node_d)
        self.graph.add_node(node_e)
        self.graph.add_node(node_f)
        self.graph.add_node(node_g)
        self.graph.add_node(node_h)

        self.graph.add_undirected_edge(node_a, node_b, 1)
        self.graph.add_undirected_edge(node_a, node_c, 2)
        self.graph.add_undirected_edge(node_b, node_c, 3)
        self.graph.add_undirected_edge(node_c, node_d, 4)
        self.graph.add_undirected_edge(node_c, node_h, 5)
        self.graph.add_undirected_edge(node_d, node_e, 6)
        self.graph.add_undirected_edge(node_e, node_f, 7)
        self.graph.add_undirected_edge(node_e, node_g, 8)
        self.graph.add_undirected_edge(node_f, node_g, 9)
        self.graph.add_undirected_edge(node_g, node_h, 10)

        distance_map, predecessor_map = self.util.dijkstra_shortest_paths(
                                                                     self.graph,
                                                                     node_a)

        expected_distance_map = {}
        expected_distance_map[node_a] = 0
        expected_distance_map[node_b] = 1
        expected_distance_map[node_c] = 2
        expected_distance_map[node_d] = 6
        expected_distance_map[node_e] = 12
        expected_distance_map[node_f] = 19
        expected_distance_map[node_g] = 17
        expected_distance_map[node_h] = 7
        expected_predecessor_map = {}
        expected_predecessor_map[node_a] = None
        expected_predecessor_map[node_b] = node_a
        expected_predecessor_map[node_c] = node_a
        expected_predecessor_map[node_d] = node_c
        expected_predecessor_map[node_e] = node_d
        expected_predecessor_map[node_f] = node_e
        expected_predecessor_map[node_g] = node_h
        expected_predecessor_map[node_h] = node_c

        Util.assert_items(self, expected_distance_map, distance_map)
        Util.assert_items(self, expected_predecessor_map, predecessor_map)

    def test_many_undirected_edges_as_two_components(self):
        (node_a, node_b, node_c, node_d, node_e, node_f,
         node_g, node_h, node_i, node_j) = \
                                'A', 'B', 'C', 'D', 'E', 'F', 'G', 'H', 'I', 'J'

        self.graph.add_node(node_a)
        self.graph.add_node(node_b)
        self.graph.add_node(node_c)
        self.graph.add_node(node_d)
        self.graph.add_node(node_e)
        self.graph.add_node(node_f)
        self.graph.add_node(node_g)
        self.graph.add_node(node_h)
        self.graph.add_node(node_i)
        self.graph.add_node(node_j)

        self.graph.add_undirected_edge(node_a, node_c, 1)
        self.graph.add_undirected_edge(node_a, node_d, 2)
        self.graph.add_undirected_edge(node_a, node_f, 3)
        self.graph.add_undirected_edge(node_b, node_e, 4)
        self.graph.add_undirected_edge(node_c, node_h, 5)
        self.graph.add_undirected_edge(node_c, node_i, 6)
        self.graph.add_undirected_edge(node_e, node_g, 7)
        self.graph.add_undirected_edge(node_e, node_j, 8)
        self.graph.add_undirected_edge(node_f, node_i, 9)
        self.graph.add_undirected_edge(node_h, node_i, 10)

        distance_map, predecessor_map = self.util.dijkstra_shortest_paths(
                                                                     self.graph,
                                                                     node_a)

        expected_distance_map = {}
        expected_distance_map[node_a] = 0
        expected_distance_map[node_b] = math.inf
        expected_distance_map[node_c] = 1
        expected_distance_map[node_d] = 2
        expected_distance_map[node_e] = math.inf
        expected_distance_map[node_f] = 3
        expected_distance_map[node_g] = math.inf
        expected_distance_map[node_h] = 6
        expected_distance_map[node_i] = 7
        expected_distance_map[node_j] = math.inf
        expected_predecessor_map = {}
        expected_predecessor_map[node_a] = None
        expected_predecessor_map[node_b] = None
        expected_predecessor_map[node_c] = node_a
        expected_predecessor_map[node_d] = node_a
        expected_predecessor_map[node_e] = None
        expected_predecessor_map[node_f] = node_a
        expected_predecessor_map[node_g] = None
        expected_predecessor_map[node_h] = node_c
        expected_predecessor_map[node_i] = node_c
        expected_predecessor_map[node_j] = None

        Util.assert_items(self, expected_distance_map, distance_map)
        Util.assert_items(self, expected_predecessor_map, predecessor_map)

    def test_many_undirected_edges_as_three_components(self):
        (node_a, node_b, node_c, node_d, node_e, node_f,
         node_g, node_h, node_i) = \
                                    'A', 'B', 'C', 'D', 'E', 'F', 'G', 'H', 'I'

        self.graph.add_node(node_a)
        self.graph.add_node(node_b)
        self.graph.add_node(node_c)
        self.graph.add_node(node_d)
        self.graph.add_node(node_e)
        self.graph.add_node(node_f)
        self.graph.add_node(node_g)
        self.graph.add_node(node_h)
        self.graph.add_node(node_i)

        self.graph.add_undirected_edge(node_a, node_b, 1)
        self.graph.add_undirected_edge(node_a, node_c, 2)
        self.graph.add_undirected_edge(node_a, node_d, 3)
        self.graph.add_undirected_edge(node_b, node_c, 4)
        self.graph.add_undirected_edge(node_e, node_f, 5)
        self.graph.add_undirected_edge(node_g, node_h, 6)
        self.graph.add_undirected_edge(node_g, node_i, 7)
        self.graph.add_undirected_edge(node_h, node_i, 8)

        distance_map, predecessor_map = self.util.dijkstra_shortest_paths(
                                                                     self.graph,
                                                                     node_a)

        expected_distance_map = {}
        expected_distance_map[node_a] = 0
        expected_distance_map[node_b] = 1
        expected_distance_map[node_c] = 2
        expected_distance_map[node_d] = 3
        expected_distance_map[node_e] = math.inf
        expected_distance_map[node_f] = math.inf
        expected_distance_map[node_g] = math.inf
        expected_distance_map[node_h] = math.inf
        expected_distance_map[node_i] = math.inf
        expected_predecessor_map = {}
        expected_predecessor_map[node_a] = None
        expected_predecessor_map[node_b] = node_a
        expected_predecessor_map[node_c] = node_a
        expected_predecessor_map[node_d] = node_a
        expected_predecessor_map[node_e] = None
        expected_predecessor_map[node_f] = None
        expected_predecessor_map[node_g] = None
        expected_predecessor_map[node_h] = None
        expected_predecessor_map[node_i] = None

        Util.assert_items(self, expected_distance_map, distance_map)
        Util.assert_items(self, expected_predecessor_map, predecessor_map)

    def test_six_nodes_of_undirected_graph(self):
        (node_a, node_b, node_c, node_d, node_e, node_f) = \
                                                    'A', 'B', 'C', 'D', 'E', 'F'

        self.graph.add_node(node_a)
        self.graph.add_node(node_b)
        self.graph.add_node(node_c)
        self.graph.add_node(node_d)
        self.graph.add_node(node_e)
        self.graph.add_node(node_f)

        self.graph.add_undirected_edge(node_a, node_b, 14)
        self.graph.add_undirected_edge(node_a, node_c, 7)
        self.graph.add_undirected_edge(node_a, node_d, 9)
        self.graph.add_undirected_edge(node_b, node_d, 2)
        self.graph.add_undirected_edge(node_b, node_e, 9)
        self.graph.add_undirected_edge(node_c, node_d, 10)
        self.graph.add_undirected_edge(node_c, node_f, 15)
        self.graph.add_undirected_edge(node_d, node_f, 11)
        self.graph.add_undirected_edge(node_e, node_f, 6)

        distance_map, predecessor_map = self.util.dijkstra_shortest_paths(
                                                                     self.graph,
                                                                     node_a)

        expected_distance_map = {}
        expected_distance_map[node_a] = 0
        expected_distance_map[node_b] = 11
        expected_distance_map[node_c] = 7
        expected_distance_map[node_d] = 9
        expected_distance_map[node_e] = 20
        expected_distance_map[node_f] = 20
        expected_predecessor_map = {}
        expected_predecessor_map[node_a] = None
        expected_predecessor_map[node_b] = node_d
        expected_predecessor_map[node_c] = node_a
        expected_predecessor_map[node_d] = node_a
        expected_predecessor_map[node_e] = node_b
        expected_predecessor_map[node_f] = node_d

        Util.assert_items(self, expected_distance_map, distance_map)
        Util.assert_items(self, expected_predecessor_map, predecessor_map)

    def test_six_nodes_of_directed_graph(self):
        (node_a, node_b, node_c, node_d, node_e, node_f) = \
                                                    'A', 'B', 'C', 'D', 'E', 'F'

        self.graph.add_node(node_a)
        self.graph.add_node(node_b)
        self.graph.add_node(node_c)
        self.graph.add_node(node_d)
        self.graph.add_node(node_e)
        self.graph.add_node(node_f)

        self.graph.add_directed_edge(node_a, node_b, 3)
        self.graph.add_directed_edge(node_a, node_c, 10)
        self.graph.add_directed_edge(node_b, node_c, 8)
        self.graph.add_directed_edge(node_b, node_d, 3)
        self.graph.add_directed_edge(node_b, node_e, 5)
        self.graph.add_directed_edge(node_c, node_b, 2)
        self.graph.add_directed_edge(node_c, node_e, 5)
        self.graph.add_directed_edge(node_d, node_c, 3)
        self.graph.add_directed_edge(node_d, node_e, 1)
        self.graph.add_directed_edge(node_d, node_f, 2)
        self.graph.add_directed_edge(node_e, node_f, 0)

        distance_map, predecessor_map = self.util.dijkstra_shortest_paths(
                                                                     self.graph,
                                                                     node_a)

        expected_distance_map = {}
        expected_distance_map[node_a] = 0
        expected_distance_map[node_b] = 3
        expected_distance_map[node_c] = 9
        expected_distance_map[node_d] = 6
        expected_distance_map[node_e] = 7
        expected_distance_map[node_f] = 7
        expected_predecessor_map = {}
        expected_predecessor_map[node_a] = None
        expected_predecessor_map[node_b] = node_a
        expected_predecessor_map[node_c] = node_d
        expected_predecessor_map[node_d] = node_b
        expected_predecessor_map[node_e] = node_d
        expected_predecessor_map[node_f] = node_e

        Util.assert_items(self, expected_distance_map, distance_map)
        Util.assert_items(self, expected_predecessor_map, predecessor_map)

class BellmanForShortestPathsTestCase(unittest.TestCase):

    def setUp(self):
        self.util = graph_util.GraphUtil()
        self.graph = graph_util.Graph()

    def tearDown(self):
        pass

    def test_empty_graph(self):
        node = 'A'

        distance_map, predecessor_map, negative_cycle_nodes = \
                               self.util.bellman_ford_shortest_paths(self.graph,
                                                                     node)

        expected_distance_map = {}
        expected_distance_map[node] = 0
        expected_predecessor_map = {}

        Util.assert_items(self, expected_distance_map, distance_map)
        Util.assert_items(self, expected_predecessor_map, predecessor_map)
        self.assertEqual(0, len(negative_cycle_nodes))

    def test_graph_with_one_node(self):
        node = 'A'

        self.graph.add_node(node)

        distance_map, predecessor_map, negative_cycle_nodes = \
                               self.util.bellman_ford_shortest_paths(self.graph,
                                                                     node)

        expected_distance_map = {}
        expected_distance_map[node] = 0
        expected_predecessor_map = {}
        expected_predecessor_map[node] = None

        Util.assert_items(self, expected_distance_map, distance_map)
        Util.assert_items(self, expected_predecessor_map, predecessor_map)
        self.assertEqual(0, len(negative_cycle_nodes))

    def test_one_directed_edge(self):
        node1, node2 = 'A', 'B'

        self.graph.add_node(node1)
        self.graph.add_node(node2)

        self.graph.add_directed_edge(node1, node2, 5)

        distance_map, predecessor_map, negative_cycle_nodes = \
                               self.util.bellman_ford_shortest_paths(self.graph,
                                                                     node1)

        expected_distance_map = {}
        expected_distance_map[node1] = 0
        expected_distance_map[node2] = 5
        expected_predecessor_map = {}
        expected_predecessor_map[node1] = None
        expected_predecessor_map[node2] = node1

        Util.assert_items(self, expected_distance_map, distance_map)
        Util.assert_items(self, expected_predecessor_map, predecessor_map)
        self.assertEqual(0, len(negative_cycle_nodes))

    def test_one_undirected_edge(self):
        node1, node2 = 'A', 'B'

        self.graph.add_node(node1)
        self.graph.add_node(node2)

        self.graph.add_undirected_edge(node1, node2, 5)

        distance_map, predecessor_map, negative_cycle_nodes = \
                               self.util.bellman_ford_shortest_paths(self.graph,
                                                                     node1)

        expected_distance_map = {}
        expected_distance_map[node1] = 0
        expected_distance_map[node2] = 5
        expected_predecessor_map = {}
        expected_predecessor_map[node1] = None
        expected_predecessor_map[node2] = node1

        Util.assert_items(self, expected_distance_map, distance_map)
        Util.assert_items(self, expected_predecessor_map, predecessor_map)
        self.assertEqual(0, len(negative_cycle_nodes))

    def test_two_directed_edges_as_rays(self):
        node1, node2, node3 = 'A', 'B', 'C'

        self.graph.add_node(node1)
        self.graph.add_node(node2)
        self.graph.add_node(node3)

        self.graph.add_directed_edge(node1, node2, 5)
        self.graph.add_directed_edge(node1, node3, 10)

        distance_map, predecessor_map, negative_cycle_nodes = \
                               self.util.bellman_ford_shortest_paths(self.graph,
                                                                     node1)

        expected_distance_map = {}
        expected_distance_map[node1] = 0
        expected_distance_map[node2] = 5
        expected_distance_map[node3] = 10
        expected_predecessor_map = {}
        expected_predecessor_map[node1] = None
        expected_predecessor_map[node2] = node1
        expected_predecessor_map[node3] = node1

        Util.assert_items(self, expected_distance_map, distance_map)
        Util.assert_items(self, expected_predecessor_map, predecessor_map)
        self.assertEqual(0, len(negative_cycle_nodes))

    def test_two_directed_edges_as_chain(self):
        node1, node2, node3 = 'A', 'B', 'C'

        self.graph.add_node(node1)
        self.graph.add_node(node2)
        self.graph.add_node(node3)

        self.graph.add_directed_edge(node1, node2, 5)
        self.graph.add_directed_edge(node2, node3, 10)

        distance_map, predecessor_map, negative_cycle_nodes = \
                               self.util.bellman_ford_shortest_paths(self.graph,
                                                                     node1)

        expected_distance_map = {}
        expected_distance_map[node1] = 0
        expected_distance_map[node2] = 5
        expected_distance_map[node3] = 15
        expected_predecessor_map = {}
        expected_predecessor_map[node1] = None
        expected_predecessor_map[node2] = node1
        expected_predecessor_map[node3] = node2

        Util.assert_items(self, expected_distance_map, distance_map)
        Util.assert_items(self, expected_predecessor_map, predecessor_map)
        self.assertEqual(0, len(negative_cycle_nodes))

    def test_three_directed_edges_as_cycle(self):
        node1, node2, node3 = 'A', 'B', 'C'

        self.graph.add_node(node1)
        self.graph.add_node(node2)
        self.graph.add_node(node3)

        self.graph.add_directed_edge(node1, node2, 5)
        self.graph.add_directed_edge(node2, node3, 10)
        self.graph.add_directed_edge(node3, node1, 11)

        distance_map, predecessor_map, negative_cycle_nodes = \
                               self.util.bellman_ford_shortest_paths(self.graph,
                                                                     node1)

        expected_distance_map = {}
        expected_distance_map[node1] = 0
        expected_distance_map[node2] = 5
        expected_distance_map[node3] = 15
        expected_predecessor_map = {}
        expected_predecessor_map[node1] = None
        expected_predecessor_map[node2] = node1
        expected_predecessor_map[node3] = node2

        Util.assert_items(self, expected_distance_map, distance_map)
        Util.assert_items(self, expected_predecessor_map, predecessor_map)
        self.assertEqual(0, len(negative_cycle_nodes))

    def test_two_undirected_edges_as_rays(self):
        node1, node2, node3 = 'A', 'B', 'C'

        self.graph.add_node(node1)
        self.graph.add_node(node2)
        self.graph.add_node(node3)

        self.graph.add_undirected_edge(node1, node2, 5)
        self.graph.add_undirected_edge(node1, node3, 10)

        distance_map, predecessor_map, negative_cycle_nodes = \
                               self.util.bellman_ford_shortest_paths(self.graph,
                                                                     node1)

        expected_distance_map = {}
        expected_distance_map[node1] = 0
        expected_distance_map[node2] = 5
        expected_distance_map[node3] = 10
        expected_predecessor_map = {}
        expected_predecessor_map[node1] = None
        expected_predecessor_map[node2] = node1
        expected_predecessor_map[node3] = node1

        Util.assert_items(self, expected_distance_map, distance_map)
        Util.assert_items(self, expected_predecessor_map, predecessor_map)
        self.assertEqual(0, len(negative_cycle_nodes))

    def test_two_undirected_edges_as_chain(self):
        node1, node2, node3 = 'A', 'B', 'C'

        self.graph.add_node(node1)
        self.graph.add_node(node2)
        self.graph.add_node(node3)

        self.graph.add_undirected_edge(node1, node2, 5)
        self.graph.add_undirected_edge(node2, node3, 10)

        distance_map, predecessor_map, negative_cycle_nodes = \
                               self.util.bellman_ford_shortest_paths(self.graph,
                                                                     node1)

        expected_distance_map = {}
        expected_distance_map[node1] = 0
        expected_distance_map[node2] = 5
        expected_distance_map[node3] = 15
        expected_predecessor_map = {}
        expected_predecessor_map[node1] = None
        expected_predecessor_map[node2] = node1
        expected_predecessor_map[node3] = node2

        Util.assert_items(self, expected_distance_map, distance_map)
        Util.assert_items(self, expected_predecessor_map, predecessor_map)
        self.assertEqual(0, len(negative_cycle_nodes))

    def test_three_undirected_edges_as_cycle(self):
        node1, node2, node3 = 'A', 'B', 'C'

        self.graph.add_node(node1)
        self.graph.add_node(node2)
        self.graph.add_node(node3)

        self.graph.add_undirected_edge(node1, node2, 5)
        self.graph.add_undirected_edge(node2, node3, 10)
        self.graph.add_undirected_edge(node3, node1, 11)

        distance_map, predecessor_map, negative_cycle_nodes = \
                               self.util.bellman_ford_shortest_paths(self.graph,
                                                                     node1)

        expected_distance_map = {}
        expected_distance_map[node1] = 0
        expected_distance_map[node2] = 5
        expected_distance_map[node3] = 11
        expected_predecessor_map = {}
        expected_predecessor_map[node1] = None
        expected_predecessor_map[node2] = node1
        expected_predecessor_map[node3] = node1

        Util.assert_items(self, expected_distance_map, distance_map)
        Util.assert_items(self, expected_predecessor_map, predecessor_map)
        self.assertEqual(0, len(negative_cycle_nodes))

    def test_undirected_edges_as_one_component(self):
        (node_a, node_b, node_c, node_d, node_e, node_f,
         node_g, node_h) = 'A', 'B', 'C', 'D', 'E', 'F', 'G', 'H'

        self.graph.add_node(node_a)
        self.graph.add_node(node_b)
        self.graph.add_node(node_c)
        self.graph.add_node(node_d)
        self.graph.add_node(node_e)
        self.graph.add_node(node_f)
        self.graph.add_node(node_g)
        self.graph.add_node(node_h)

        self.graph.add_undirected_edge(node_a, node_b, 1)
        self.graph.add_undirected_edge(node_a, node_c, 2)
        self.graph.add_undirected_edge(node_b, node_c, 3)
        self.graph.add_undirected_edge(node_c, node_d, 4)
        self.graph.add_undirected_edge(node_c, node_h, 5)
        self.graph.add_undirected_edge(node_d, node_e, 6)
        self.graph.add_undirected_edge(node_e, node_f, 7)
        self.graph.add_undirected_edge(node_e, node_g, 8)
        self.graph.add_undirected_edge(node_f, node_g, 9)
        self.graph.add_undirected_edge(node_g, node_h, 10)

        distance_map, predecessor_map, negative_cycle_nodes = \
                               self.util.bellman_ford_shortest_paths(self.graph,
                                                                     node_a)

        expected_distance_map = {}
        expected_distance_map[node_a] = 0
        expected_distance_map[node_b] = 1
        expected_distance_map[node_c] = 2
        expected_distance_map[node_d] = 6
        expected_distance_map[node_e] = 12
        expected_distance_map[node_f] = 19
        expected_distance_map[node_g] = 17
        expected_distance_map[node_h] = 7
        expected_predecessor_map = {}
        expected_predecessor_map[node_a] = None
        expected_predecessor_map[node_b] = node_a
        expected_predecessor_map[node_c] = node_a
        expected_predecessor_map[node_d] = node_c
        expected_predecessor_map[node_e] = node_d
        expected_predecessor_map[node_f] = node_e
        expected_predecessor_map[node_g] = node_h
        expected_predecessor_map[node_h] = node_c

        Util.assert_items(self, expected_distance_map, distance_map)
        Util.assert_items(self, expected_predecessor_map, predecessor_map)
        self.assertEqual(0, len(negative_cycle_nodes))

    def test_many_undirected_edges_as_two_components(self):
        (node_a, node_b, node_c, node_d, node_e, node_f,
         node_g, node_h, node_i, node_j) = \
                                'A', 'B', 'C', 'D', 'E', 'F', 'G', 'H', 'I', 'J'

        self.graph.add_node(node_a)
        self.graph.add_node(node_b)
        self.graph.add_node(node_c)
        self.graph.add_node(node_d)
        self.graph.add_node(node_e)
        self.graph.add_node(node_f)
        self.graph.add_node(node_g)
        self.graph.add_node(node_h)
        self.graph.add_node(node_i)
        self.graph.add_node(node_j)

        self.graph.add_undirected_edge(node_a, node_c, 1)
        self.graph.add_undirected_edge(node_a, node_d, 2)
        self.graph.add_undirected_edge(node_a, node_f, 3)
        self.graph.add_undirected_edge(node_b, node_e, 4)
        self.graph.add_undirected_edge(node_c, node_h, 5)
        self.graph.add_undirected_edge(node_c, node_i, 6)
        self.graph.add_undirected_edge(node_e, node_g, 7)
        self.graph.add_undirected_edge(node_e, node_j, 8)
        self.graph.add_undirected_edge(node_f, node_i, 9)
        self.graph.add_undirected_edge(node_h, node_i, 10)

        distance_map, predecessor_map, negative_cycle_nodes = \
                               self.util.bellman_ford_shortest_paths(self.graph,
                                                                     node_a)

        expected_distance_map = {}
        expected_distance_map[node_a] = 0
        expected_distance_map[node_b] = math.inf
        expected_distance_map[node_c] = 1
        expected_distance_map[node_d] = 2
        expected_distance_map[node_e] = math.inf
        expected_distance_map[node_f] = 3
        expected_distance_map[node_g] = math.inf
        expected_distance_map[node_h] = 6
        expected_distance_map[node_i] = 7
        expected_distance_map[node_j] = math.inf
        expected_predecessor_map = {}
        expected_predecessor_map[node_a] = None
        expected_predecessor_map[node_b] = None
        expected_predecessor_map[node_c] = node_a
        expected_predecessor_map[node_d] = node_a
        expected_predecessor_map[node_e] = None
        expected_predecessor_map[node_f] = node_a
        expected_predecessor_map[node_g] = None
        expected_predecessor_map[node_h] = node_c
        expected_predecessor_map[node_i] = node_c
        expected_predecessor_map[node_j] = None

        Util.assert_items(self, expected_distance_map, distance_map)
        Util.assert_items(self, expected_predecessor_map, predecessor_map)
        self.assertEqual(0, len(negative_cycle_nodes))

    def test_many_undirected_edges_as_three_components(self):
        (node_a, node_b, node_c, node_d, node_e, node_f,
         node_g, node_h, node_i) = 'A', 'B', 'C', 'D', 'E', 'F', 'G', 'H', 'I'

        self.graph.add_node(node_a)
        self.graph.add_node(node_b)
        self.graph.add_node(node_c)
        self.graph.add_node(node_d)
        self.graph.add_node(node_e)
        self.graph.add_node(node_f)
        self.graph.add_node(node_g)
        self.graph.add_node(node_h)
        self.graph.add_node(node_i)

        self.graph.add_undirected_edge(node_a, node_b, 1)
        self.graph.add_undirected_edge(node_a, node_c, 2)
        self.graph.add_undirected_edge(node_a, node_d, 3)
        self.graph.add_undirected_edge(node_b, node_c, 4)
        self.graph.add_undirected_edge(node_e, node_f, 5)
        self.graph.add_undirected_edge(node_g, node_h, 6)
        self.graph.add_undirected_edge(node_g, node_i, 7)
        self.graph.add_undirected_edge(node_h, node_i, 8)

        distance_map, predecessor_map, negative_cycle_nodes = \
                               self.util.bellman_ford_shortest_paths(self.graph,
                                                                     node_a)

        expected_distance_map = {}
        expected_distance_map[node_a] = 0
        expected_distance_map[node_b] = 1
        expected_distance_map[node_c] = 2
        expected_distance_map[node_d] = 3
        expected_distance_map[node_e] = math.inf
        expected_distance_map[node_f] = math.inf
        expected_distance_map[node_g] = math.inf
        expected_distance_map[node_h] = math.inf
        expected_distance_map[node_i] = math.inf
        expected_predecessor_map = {}
        expected_predecessor_map[node_a] = None
        expected_predecessor_map[node_b] = node_a
        expected_predecessor_map[node_c] = node_a
        expected_predecessor_map[node_d] = node_a
        expected_predecessor_map[node_e] = None
        expected_predecessor_map[node_f] = None
        expected_predecessor_map[node_g] = None
        expected_predecessor_map[node_h] = None
        expected_predecessor_map[node_i] = None

        Util.assert_items(self, expected_distance_map, distance_map)
        Util.assert_items(self, expected_predecessor_map, predecessor_map)
        self.assertEqual(0, len(negative_cycle_nodes))

    def test_five_nodes_of_directed_graph_case1(self):
        node_a, node_b, node_c, node_d, node_e = 'A', 'B', 'C', 'D', 'E'

        self.graph.add_node(node_a)
        self.graph.add_node(node_b)
        self.graph.add_node(node_c)
        self.graph.add_node(node_d)
        self.graph.add_node(node_e)

        self.graph.add_directed_edge(node_a, node_b, 4)
        self.graph.add_directed_edge(node_a, node_c, 3)
        self.graph.add_directed_edge(node_b, node_c, -2)
        self.graph.add_directed_edge(node_b, node_d, 4)
        self.graph.add_directed_edge(node_c, node_d, -3)
        self.graph.add_directed_edge(node_c, node_e, 1)
        self.graph.add_directed_edge(node_d, node_e, 2)

        distance_map, predecessor_map, negative_cycle_nodes = \
                               self.util.bellman_ford_shortest_paths(self.graph,
                                                                     node_a)

        expected_distance_map = {}
        expected_distance_map[node_a] = 0
        expected_distance_map[node_b] = 4
        expected_distance_map[node_c] = 2
        expected_distance_map[node_d] = -1
        expected_distance_map[node_e] = 1
        expected_predecessor_map = {}
        expected_predecessor_map[node_a] = None
        expected_predecessor_map[node_b] = node_a
        expected_predecessor_map[node_c] = node_b
        expected_predecessor_map[node_d] = node_c
        expected_predecessor_map[node_e] = node_d

        Util.assert_items(self, expected_distance_map, distance_map)
        Util.assert_items(self, expected_predecessor_map, predecessor_map)
        self.assertEqual(0, len(negative_cycle_nodes))

    def test_five_nodes_of_directed_graph_case2(self):
        node_a, node_b, node_c, node_d, node_e = 'A', 'B', 'C', 'D', 'E'

        self.graph.add_node(node_a)
        self.graph.add_node(node_b)
        self.graph.add_node(node_c)
        self.graph.add_node(node_d)
        self.graph.add_node(node_e)

        self.graph.add_directed_edge(node_a, node_b, -3)
        self.graph.add_directed_edge(node_b, node_c, 1)
        self.graph.add_directed_edge(node_c, node_d, 1)
        self.graph.add_directed_edge(node_d, node_e, 1)

        distance_map, predecessor_map, negative_cycle_nodes = \
                               self.util.bellman_ford_shortest_paths(self.graph,
                                                                     node_a)

        expected_distance_map = {}
        expected_distance_map[node_a] = 0
        expected_distance_map[node_b] = -3
        expected_distance_map[node_c] = -2
        expected_distance_map[node_d] = -1
        expected_distance_map[node_e] = 0
        expected_predecessor_map = {}
        expected_predecessor_map[node_a] = None
        expected_predecessor_map[node_b] = node_a
        expected_predecessor_map[node_c] = node_b
        expected_predecessor_map[node_d] = node_c
        expected_predecessor_map[node_e] = node_d

        Util.assert_items(self, expected_distance_map, distance_map)
        Util.assert_items(self, expected_predecessor_map, predecessor_map)
        self.assertEqual(0, len(negative_cycle_nodes))

    def test_three_nodes_of_directed_graph_with_negative_cycle(self):
        node_a, node_b, node_c = 'A', 'B', 'C'

        self.graph.add_node(node_a)
        self.graph.add_node(node_b)
        self.graph.add_node(node_c)

        self.graph.add_directed_edge(node_a, node_b, -5)
        self.graph.add_directed_edge(node_b, node_c, 2)
        self.graph.add_directed_edge(node_c, node_a, 1)

        distance_map, predecessor_map, negative_cycle_nodes = \
                               self.util.bellman_ford_shortest_paths(self.graph,
                                                                     node_a)

        expected_predecessor_map = {}
        expected_predecessor_map[node_a] = node_c
        expected_predecessor_map[node_b] = node_a
        expected_predecessor_map[node_c] = node_b

        self.assertEqual(1, len(negative_cycle_nodes))
        if node_a in negative_cycle_nodes:
            Util.assert_items(self, [ node_a ],
                              negative_cycle_nodes)
            if predecessor_map[node_a] == node_c:
                expected_predecessor_map[node_a] = node_c
                expected_predecessor_map[node_b] = node_a
                expected_predecessor_map[node_c] = node_b
            elif predecessor_map[node_a] == None:
                expected_predecessor_map[node_a] = None
                expected_predecessor_map[node_b] = node_a
                expected_predecessor_map[node_c] = node_b
            else:
                self.fail('An unexpected value of predecessor_map[node_a].')
        elif node_b in negative_cycle_nodes:
            Util.assert_items(self, [ node_b ],
                              negative_cycle_nodes)

            expected_predecessor_map[node_a] = node_c
            expected_predecessor_map[node_b] = node_a
            expected_predecessor_map[node_c] = node_b
        elif node_c in negative_cycle_nodes:
            Util.assert_items(self, [ node_c ],
                              negative_cycle_nodes)

            expected_predecessor_map[node_a] = node_c
            expected_predecessor_map[node_b] = node_a
            expected_predecessor_map[node_c] = node_b
        else:
            self.fail('An unexpected node in negative_cycle_nodes.')

        # We do not assert distance_map because of different distance values
        # even for a single negative_cycle_nodes.
        Util.assert_items(self, expected_predecessor_map, predecessor_map)

    def test_four_nodes_of_directed_graph_with_negative_cycle(self):
        node_a, node_b, node_c, node_d = 'A', 'B', 'C', 'D'

        self.graph.add_node(node_a)
        self.graph.add_node(node_b)
        self.graph.add_node(node_c)
        self.graph.add_node(node_d)

        self.graph.add_directed_edge(node_a, node_b, -5)
        self.graph.add_directed_edge(node_b, node_c, 2)
        self.graph.add_directed_edge(node_c, node_a, 1)
        self.graph.add_directed_edge(node_d, node_a, 2)

        distance_map, predecessor_map, negative_cycle_nodes = \
                               self.util.bellman_ford_shortest_paths(self.graph,
                                                                     node_a)

        expected_predecessor_map = {}
        expected_predecessor_map[node_a] = node_c
        expected_predecessor_map[node_b] = node_a
        expected_predecessor_map[node_c] = node_b
        expected_predecessor_map[node_d] = None

        self.assertEqual(1, len(negative_cycle_nodes))
        if node_a in negative_cycle_nodes:
            Util.assert_items(self, [ node_a ],
                              negative_cycle_nodes)
        elif node_b in negative_cycle_nodes:
            Util.assert_items(self, [ node_b ],
                              negative_cycle_nodes)
        elif node_c in negative_cycle_nodes:
            Util.assert_items(self, [ node_c ],
                              negative_cycle_nodes)
        else:
            self.fail('An unexpected node in negative_cycle_nodes.')

        # We do not assert distance_map because of different distance values
        # even for a single negative_cycle_nodes.
        Util.assert_items(self, expected_predecessor_map, predecessor_map)

class KruskalTestCase(unittest.TestCase):

    def setUp(self):
        self.util = graph_util.GraphUtil()
        self.graph = graph_util.Graph()

    def tearDown(self):
        pass

    def assert_tree(self, tree, expected_total_distance):
        Util.assert_items(self, self.graph.nodes(), tree.nodes())

        total = 0
        visited = set()
        for u, v in tree.edges():
            edge = u, v
            if edge not in visited:
                total += tree.weight(edge)
                visited.add((u, v))
                visited.add((v, u))

        self.assertEqual(expected_total_distance, total)

    def assert_neighbors(self, tree, node, expected_neighbors):
        Util.assert_items(self, expected_neighbors,
                          tree.neighbors(node))

    def test_empty_graph(self):
        tree = self.util.kruskal(self.graph)

        self.assert_tree(tree, 0)

    def test_graph_with_one_node(self):
        node_a = 'A'

        self.graph.add_node(node_a)

        tree = self.util.kruskal(self.graph)

        self.assert_tree(tree, 0)
        self.assert_neighbors(tree,
                              node_a,
                              [])

    def test_one_directed_edge(self):
        node_a, node_b = 'A', 'B'

        self.graph.add_node(node_a)
        self.graph.add_node(node_b)

        self.graph.add_directed_edge(node_a, node_b, 3)

        tree = self.util.kruskal(self.graph)

        self.assert_tree(tree, 3)
        self.assert_neighbors(tree,
                              node_a,
                              [ node_b ])
        self.assertEqual(3, tree.weight((node_a, node_b)))
        self.assert_neighbors(tree,
                              node_b,
                              [ node_a ])
        self.assertEqual(3, tree.weight((node_b, node_a)))

    def test_one_undirected_edge(self):
        node_a, node_b = 'A', 'B'

        self.graph.add_node(node_a)
        self.graph.add_node(node_b)

        self.graph.add_undirected_edge(node_a, node_b, 3)

        tree = self.util.kruskal(self.graph)

        self.assert_tree(tree, 3)
        self.assert_neighbors(tree,
                              node_a,
                              [ node_b ])
        self.assertEqual(3, tree.weight((node_a, node_b)))
        self.assert_neighbors(tree,
                              node_b,
                              [ node_a ])
        self.assertEqual(3, tree.weight((node_b, node_a)))

    def test_two_directed_edges_as_rays(self):
        node_a, node_b, node_c = 'A', 'B', 'C'

        self.graph.add_node(node_a)
        self.graph.add_node(node_b)
        self.graph.add_node(node_c)

        self.graph.add_directed_edge(node_a, node_b, 3)
        self.graph.add_directed_edge(node_a, node_c, 4)

        tree = self.util.kruskal(self.graph)

        self.assert_tree(tree, 7)
        self.assert_neighbors(tree,
                              node_a,
                              [ node_b, node_c ])
        self.assertEqual(3, tree.weight((node_a, node_b)))
        self.assertEqual(4, tree.weight((node_a, node_c)))
        self.assert_neighbors(tree,
                              node_b,
                              [ node_a ])
        self.assertEqual(3, tree.weight((node_b, node_a)))
        self.assert_neighbors(tree,
                              node_c,
                              [ node_a ])
        self.assertEqual(4, tree.weight((node_c, node_a)))

    def test_two_directed_edges_as_chain(self):
        node_a, node_b, node_c = 'A', 'B', 'C'

        self.graph.add_node(node_a)
        self.graph.add_node(node_b)
        self.graph.add_node(node_c)

        self.graph.add_directed_edge(node_a, node_b, 3)
        self.graph.add_directed_edge(node_b, node_c, 4)

        tree = self.util.kruskal(self.graph)

        self.assert_tree(tree, 7)
        self.assert_neighbors(tree,
                              node_a,
                              [ node_b ])
        self.assertEqual(3, tree.weight((node_a, node_b)))
        self.assert_neighbors(tree,
                              node_b,
                              [ node_a, node_c ])
        self.assertEqual(3, tree.weight((node_b, node_a)))
        self.assertEqual(4, tree.weight((node_b, node_c)))
        self.assert_neighbors(tree,
                              node_c,
                              [ node_b ])
        self.assertEqual(4, tree.weight((node_c, node_b)))

    def test_three_directed_edges_as_cycle(self):
        node_a, node_b, node_c = 'A', 'B', 'C'

        self.graph.add_node(node_a)
        self.graph.add_node(node_b)
        self.graph.add_node(node_c)

        self.graph.add_directed_edge(node_a, node_b, 3)
        self.graph.add_directed_edge(node_b, node_c, 4)
        self.graph.add_directed_edge(node_c, node_a, 5)

        tree = self.util.kruskal(self.graph)

        self.assert_tree(tree, 7)
        self.assert_neighbors(tree,
                              node_a,
                              [ node_b ])
        self.assertEqual(3, tree.weight((node_a, node_b)))
        self.assert_neighbors(tree,
                              node_b,
                              [ node_a, node_c ])
        self.assertEqual(3, tree.weight((node_b, node_a)))
        self.assertEqual(4, tree.weight((node_b, node_c)))
        self.assert_neighbors(tree,
                              node_c,
                              [ node_b ])
        self.assertEqual(4, tree.weight((node_c, node_b)))

    def test_two_undirected_edges_as_rays(self):
        node_a, node_b, node_c = 'A', 'B', 'C'

        self.graph.add_node(node_a)
        self.graph.add_node(node_b)
        self.graph.add_node(node_c)

        self.graph.add_undirected_edge(node_a, node_b, 3)
        self.graph.add_undirected_edge(node_a, node_c, 4)

        tree = self.util.kruskal(self.graph)

        self.assert_tree(tree, 7)
        self.assert_neighbors(tree,
                              node_a,
                              [ node_b, node_c ])
        self.assertEqual(3, tree.weight((node_a, node_b)))
        self.assertEqual(4, tree.weight((node_a, node_c)))
        self.assert_neighbors(tree,
                              node_b,
                              [ node_a ])
        self.assertEqual(3, tree.weight((node_b, node_a)))
        self.assert_neighbors(tree,
                              node_c,
                              [ node_a ])
        self.assertEqual(4, tree.weight((node_c, node_a)))

    def test_two_undirected_edges_as_chain(self):
        node_a, node_b, node_c = 'A', 'B', 'C'

        self.graph.add_node(node_a)
        self.graph.add_node(node_b)
        self.graph.add_node(node_c)

        self.graph.add_undirected_edge(node_a, node_b, 3)
        self.graph.add_undirected_edge(node_b, node_c, 4)

        tree = self.util.kruskal(self.graph)

        self.assert_tree(tree, 7)
        self.assert_neighbors(tree,
                              node_a,
                              [ node_b ])
        self.assertEqual(3, tree.weight((node_a, node_b)))
        self.assert_neighbors(tree,
                              node_b,
                              [ node_a, node_c ])
        self.assertEqual(3, tree.weight((node_b, node_a)))
        self.assertEqual(4, tree.weight((node_b, node_c)))
        self.assert_neighbors(tree,
                              node_c,
                              [ node_b ])
        self.assertEqual(4, tree.weight((node_c, node_b)))

    def test_three_undirected_edges_as_cycle(self):
        node_a, node_b, node_c = 'A', 'B', 'C'

        self.graph.add_node(node_a)
        self.graph.add_node(node_b)
        self.graph.add_node(node_c)

        self.graph.add_undirected_edge(node_a, node_b, 3)
        self.graph.add_undirected_edge(node_b, node_c, 4)
        self.graph.add_undirected_edge(node_c, node_a, 5)

        tree = self.util.kruskal(self.graph)

        self.assert_tree(tree, 7)
        self.assert_neighbors(tree,
                              node_a,
                              [ node_b ])
        self.assertEqual(3, tree.weight((node_a, node_b)))
        self.assert_neighbors(tree,
                              node_b,
                              [ node_a, node_c ])
        self.assertEqual(3, tree.weight((node_b, node_a)))
        self.assertEqual(4, tree.weight((node_b, node_c)))
        self.assert_neighbors(tree,
                              node_c,
                              [ node_b ])
        self.assertEqual(4, tree.weight((node_c, node_b)))

    def test_six_nodes_of_undirected_graph(self):
        (node_a, node_b, node_c, node_d, node_e, node_f) = \
                                                    'A', 'B', 'C', 'D', 'E', 'F'

        self.graph.add_node(node_a)
        self.graph.add_node(node_b)
        self.graph.add_node(node_c)
        self.graph.add_node(node_d)
        self.graph.add_node(node_e)
        self.graph.add_node(node_f)

        self.graph.add_undirected_edge(node_a, node_b, 2)
        self.graph.add_undirected_edge(node_a, node_c, 3)
        self.graph.add_undirected_edge(node_b, node_c, 1)
        self.graph.add_undirected_edge(node_b, node_d, 4)
        self.graph.add_undirected_edge(node_c, node_d, 5)
        self.graph.add_undirected_edge(node_c, node_e, 9)
        self.graph.add_undirected_edge(node_d, node_e, 6)
        self.graph.add_undirected_edge(node_e, node_f, 1)

        tree = self.util.kruskal(self.graph)

        self.assert_tree(tree, 14)
        self.assert_neighbors(tree,
                              node_a,
                              [ node_b ])
        self.assertEqual(2, tree.weight((node_a, node_b)))
        self.assert_neighbors(tree,
                              node_b,
                              [ node_a, node_c, node_d ])
        self.assertEqual(2, tree.weight((node_b, node_a)))
        self.assertEqual(1, tree.weight((node_b, node_c)))
        self.assertEqual(4, tree.weight((node_b, node_d)))
        self.assert_neighbors(tree,
                              node_c,
                              [ node_b ])
        self.assertEqual(1, tree.weight((node_c, node_b)))
        self.assert_neighbors(tree,
                              node_d,
                              [ node_b, node_e ])
        self.assertEqual(4, tree.weight((node_d, node_b)))
        self.assertEqual(6, tree.weight((node_d, node_e)))
        self.assert_neighbors(tree,
                              node_e,
                              [ node_d, node_f ])
        self.assertEqual(6, tree.weight((node_e, node_d)))
        self.assertEqual(1, tree.weight((node_e, node_f)))

    def test_eight_nodes_of_undirected_graph(self):
        (node_a, node_b, node_c, node_d, node_e, node_f,
         node_g, node_h) = 'A', 'B', 'C', 'D', 'E', 'F', 'G', 'H'

        self.graph.add_node(node_a)
        self.graph.add_node(node_b)
        self.graph.add_node(node_c)
        self.graph.add_node(node_d)
        self.graph.add_node(node_e)
        self.graph.add_node(node_f)
        self.graph.add_node(node_g)
        self.graph.add_node(node_h)

        self.graph.add_undirected_edge(node_a, node_b, 1)
        self.graph.add_undirected_edge(node_a, node_c, 2)
        self.graph.add_undirected_edge(node_b, node_c, 3)
        self.graph.add_undirected_edge(node_c, node_d, 4)
        self.graph.add_undirected_edge(node_c, node_h, 5)
        self.graph.add_undirected_edge(node_d, node_e, 1)
        self.graph.add_undirected_edge(node_e, node_f, 2)
        self.graph.add_undirected_edge(node_e, node_g, 3)
        self.graph.add_undirected_edge(node_f, node_g, 4)
        self.graph.add_undirected_edge(node_g, node_h, 5)

        tree = self.util.kruskal(self.graph)

        self.assert_tree(tree, 18)
        self.assert_neighbors(tree,
                              node_a,
                              [ node_b, node_c ])
        self.assertEqual(1, tree.weight((node_a, node_b)))
        self.assertEqual(2, tree.weight((node_a, node_c)))
        self.assert_neighbors(tree,
                              node_b,
                              [ node_a ])
        self.assertEqual(1, tree.weight((node_b, node_a)))
        self.assert_neighbors(tree,
                              node_c,
                              [ node_a, node_d, node_h ])
        self.assertEqual(2, tree.weight((node_c, node_a)))
        self.assertEqual(4, tree.weight((node_c, node_d)))
        self.assertEqual(5, tree.weight((node_c, node_h)))
        self.assert_neighbors(tree,
                              node_d,
                              [ node_c, node_e ])
        self.assertEqual(4, tree.weight((node_d, node_c)))
        self.assertEqual(1, tree.weight((node_d, node_e)))
        self.assert_neighbors(tree,
                              node_e,
                              [ node_d, node_f, node_g ])
        self.assertEqual(1, tree.weight((node_e, node_d)))
        self.assertEqual(2, tree.weight((node_e, node_f)))
        self.assertEqual(3, tree.weight((node_e, node_g)))
        self.assert_neighbors(tree,
                              node_f,
                              [ node_e ])
        self.assertEqual(2, tree.weight((node_f, node_e)))
        self.assert_neighbors(tree,
                              node_g,
                              [ node_e ])
        self.assertEqual(3, tree.weight((node_g, node_e)))
        self.assert_neighbors(tree,
                              node_h,
                              [ node_c ])
        self.assertEqual(5, tree.weight((node_h, node_c)))

class PrimTestCase(unittest.TestCase):

    def setUp(self):
        self.util = graph_util.GraphUtil()
        self.graph = graph_util.Graph()

    def tearDown(self):
        pass

    def assert_tree(self, tree, expected_total_distance):
        Util.assert_items(self, self.graph.nodes(), tree.nodes())

        total = 0
        visited = set()
        for u, v in tree.edges():
            edge = u, v
            if edge not in visited:
                total += tree.weight(edge)
                visited.add((u, v))
                visited.add((v, u))

        self.assertEqual(expected_total_distance, total)

    def assert_neighbors(self, tree, node, expected_neighbors):
        Util.assert_items(self, expected_neighbors,
                          tree.neighbors(node))

    def test_empty_graph(self):
        tree = self.util.prim(self.graph)

        self.assert_tree(tree, 0)

    def test_graph_with_one_node(self):
        node_a = 'A'

        self.graph.add_node(node_a)

        tree = self.util.prim(self.graph)

        self.assert_tree(tree, 0)
        self.assert_neighbors(tree,
                              node_a,
                              [])

    def test_one_edge(self):
        node_a, node_b = 'A', 'B'

        self.graph.add_node(node_a)
        self.graph.add_node(node_b)

        self.graph.add_undirected_edge(node_a, node_b, 3)

        tree = self.util.prim(self.graph)

        self.assert_tree(tree, 3)
        self.assert_neighbors(tree,
                              node_a,
                              [ node_b ])
        self.assertEqual(3, tree.weight((node_a, node_b)))
        self.assert_neighbors(tree,
                              node_b,
                              [ node_a ])
        self.assertEqual(3, tree.weight((node_b, node_a)))

    def test_two_edges_as_rays(self):
        node_a, node_b, node_c = 'A', 'B', 'C'

        self.graph.add_node(node_a)
        self.graph.add_node(node_b)
        self.graph.add_node(node_c)

        self.graph.add_undirected_edge(node_a, node_b, 3)
        self.graph.add_undirected_edge(node_a, node_c, 4)

        tree = self.util.prim(self.graph)

        self.assert_tree(tree, 7)
        self.assert_neighbors(tree,
                              node_a,
                              [ node_b, node_c ])
        self.assertEqual(3, tree.weight((node_a, node_b)))
        self.assertEqual(4, tree.weight((node_a, node_c)))
        self.assert_neighbors(tree,
                              node_b,
                              [ node_a ])
        self.assertEqual(3, tree.weight((node_b, node_a)))
        self.assert_neighbors(tree,
                              node_c,
                              [ node_a ])
        self.assertEqual(4, tree.weight((node_c, node_a)))

    def test_two_edges_as_chain(self):
        node_a, node_b, node_c = 'A', 'B', 'C'

        self.graph.add_node(node_a)
        self.graph.add_node(node_b)
        self.graph.add_node(node_c)

        self.graph.add_undirected_edge(node_a, node_b, 3)
        self.graph.add_undirected_edge(node_b, node_c, 4)

        tree = self.util.prim(self.graph)

        self.assert_tree(tree, 7)
        self.assert_neighbors(tree,
                              node_a,
                              [ node_b ])
        self.assertEqual(3, tree.weight((node_a, node_b)))
        self.assert_neighbors(tree,
                              node_b,
                              [ node_a, node_c ])
        self.assertEqual(3, tree.weight((node_b, node_a)))
        self.assertEqual(4, tree.weight((node_b, node_c)))
        self.assert_neighbors(tree,
                              node_c,
                              [ node_b ])
        self.assertEqual(4, tree.weight((node_c, node_b)))

    def test_two_edges_as_cycle(self):
        node_a, node_b, node_c = 'A', 'B', 'C'

        self.graph.add_node(node_a)
        self.graph.add_node(node_b)
        self.graph.add_node(node_c)

        self.graph.add_undirected_edge(node_a, node_b, 3)
        self.graph.add_undirected_edge(node_b, node_c, 4)
        self.graph.add_undirected_edge(node_c, node_a, 5)

        tree = self.util.prim(self.graph)

        self.assert_tree(tree, 7)
        self.assert_neighbors(tree,
                              node_a,
                              [ node_b ])
        self.assertEqual(3, tree.weight((node_a, node_b)))
        self.assert_neighbors(tree,
                              node_b,
                              [ node_a, node_c ])
        self.assertEqual(3, tree.weight((node_b, node_a)))
        self.assertEqual(4, tree.weight((node_b, node_c)))
        self.assert_neighbors(tree,
                              node_c,
                              [ node_b ])
        self.assertEqual(4, tree.weight((node_c, node_b)))

    def test_six_nodes_of_graph(self):
        (node_a, node_b, node_c, node_d, node_e, node_f) = \
                                                    'A', 'B', 'C', 'D', 'E', 'F'

        self.graph.add_node(node_a)
        self.graph.add_node(node_b)
        self.graph.add_node(node_c)
        self.graph.add_node(node_d)
        self.graph.add_node(node_e)
        self.graph.add_node(node_f)

        self.graph.add_undirected_edge(node_a, node_b, 2)
        self.graph.add_undirected_edge(node_a, node_c, 3)
        self.graph.add_undirected_edge(node_b, node_c, 1)
        self.graph.add_undirected_edge(node_b, node_d, 4)
        self.graph.add_undirected_edge(node_c, node_d, 5)
        self.graph.add_undirected_edge(node_c, node_e, 9)
        self.graph.add_undirected_edge(node_d, node_e, 6)
        self.graph.add_undirected_edge(node_e, node_f, 1)

        tree = self.util.prim(self.graph)

        self.assert_tree(tree, 14)
        self.assert_neighbors(tree,
                              node_a,
                              [ node_b ])
        self.assertEqual(2, tree.weight((node_a, node_b)))
        self.assert_neighbors(tree,
                              node_b,
                              [ node_a, node_c, node_d ])
        self.assertEqual(2, tree.weight((node_b, node_a)))
        self.assertEqual(1, tree.weight((node_b, node_c)))
        self.assertEqual(4, tree.weight((node_b, node_d)))
        self.assert_neighbors(tree,
                              node_c,
                              [ node_b ])
        self.assertEqual(1, tree.weight((node_c, node_b)))
        self.assert_neighbors(tree,
                              node_d,
                              [ node_b, node_e ])
        self.assertEqual(4, tree.weight((node_d, node_b)))
        self.assertEqual(6, tree.weight((node_d, node_e)))
        self.assert_neighbors(tree,
                              node_e,
                              [ node_d, node_f ])
        self.assertEqual(6, tree.weight((node_e, node_d)))
        self.assertEqual(1, tree.weight((node_e, node_f)))

    def test_eight_nodes_of_graph(self):
        (node_a, node_b, node_c, node_d, node_e, node_f,
         node_g, node_h) = 'A', 'B', 'C', 'D', 'E', 'F', 'G', 'H'

        self.graph.add_node(node_a)
        self.graph.add_node(node_b)
        self.graph.add_node(node_c)
        self.graph.add_node(node_d)
        self.graph.add_node(node_e)
        self.graph.add_node(node_f)
        self.graph.add_node(node_g)
        self.graph.add_node(node_h)

        self.graph.add_undirected_edge(node_a, node_b, 1)
        self.graph.add_undirected_edge(node_a, node_c, 2)
        self.graph.add_undirected_edge(node_b, node_c, 3)
        self.graph.add_undirected_edge(node_c, node_d, 4)
        self.graph.add_undirected_edge(node_c, node_h, 5)
        self.graph.add_undirected_edge(node_d, node_e, 1)
        self.graph.add_undirected_edge(node_e, node_f, 2)
        self.graph.add_undirected_edge(node_e, node_g, 3)
        self.graph.add_undirected_edge(node_f, node_g, 4)
        self.graph.add_undirected_edge(node_g, node_h, 5)

        tree = self.util.prim(self.graph)

        self.assert_tree(tree, 18)
        if tree.neighbors(node_h) == [ node_c ]:
            self.assert_neighbors(tree,
                                  node_a,
                                  [ node_b, node_c ])
            self.assertEqual(1, tree.weight((node_a, node_b)))
            self.assertEqual(2, tree.weight((node_a, node_c)))
            self.assert_neighbors(tree,
                                  node_b,
                                  [ node_a ])
            self.assertEqual(1, tree.weight((node_b, node_a)))
            self.assert_neighbors(tree,
                                  node_c,
                                  [ node_a, node_d, node_h ])
            self.assertEqual(2, tree.weight((node_c, node_a)))
            self.assertEqual(4, tree.weight((node_c, node_d)))
            self.assertEqual(5, tree.weight((node_c, node_h)))
            self.assert_neighbors(tree,
                                  node_d,
                                  [ node_c, node_e ])
            self.assertEqual(4, tree.weight((node_d, node_c)))
            self.assertEqual(1, tree.weight((node_d, node_e)))
            self.assert_neighbors(tree,
                                  node_e,
                                  [ node_d, node_f, node_g ])
            self.assertEqual(1, tree.weight((node_e, node_d)))
            self.assertEqual(2, tree.weight((node_e, node_f)))
            self.assertEqual(3, tree.weight((node_e, node_g)))
            self.assert_neighbors(tree,
                                  node_f,
                                  [ node_e ])
            self.assertEqual(2, tree.weight((node_f, node_e)))
            self.assert_neighbors(tree,
                                  node_g,
                                  [ node_e ])
            self.assertEqual(3, tree.weight((node_g, node_e)))
            self.assert_neighbors(tree,
                                  node_h,
                                  [ node_c ])
            self.assertEqual(5, tree.weight((node_h, node_c)))
        elif tree.neighbors(node_h) == [ node_g ]:
            self.assert_neighbors(tree,
                                  node_a,
                                  [ node_b, node_c ])
            self.assertEqual(1, tree.weight((node_a, node_b)))
            self.assertEqual(2, tree.weight((node_a, node_c)))
            self.assert_neighbors(tree,
                                  node_b,
                                  [ node_a ])
            self.assertEqual(1, tree.weight((node_b, node_a)))
            self.assert_neighbors(tree,
                                  node_c,
                                  [ node_a, node_d ])
            self.assertEqual(2, tree.weight((node_c, node_a)))
            self.assertEqual(4, tree.weight((node_c, node_d)))
            self.assert_neighbors(tree,
                                  node_d,
                                  [ node_c, node_e ])
            self.assertEqual(4, tree.weight((node_d, node_c)))
            self.assertEqual(1, tree.weight((node_d, node_e)))
            self.assert_neighbors(tree,
                                  node_e,
                                  [ node_d, node_f, node_g ])
            self.assertEqual(1, tree.weight((node_e, node_d)))
            self.assertEqual(2, tree.weight((node_e, node_f)))
            self.assertEqual(3, tree.weight((node_e, node_g)))
            self.assert_neighbors(tree,
                                  node_f,
                                  [ node_e ])
            self.assertEqual(2, tree.weight((node_f, node_e)))
            self.assert_neighbors(tree,
                                  node_g,
                                  [ node_e, node_h ])
            self.assertEqual(3, tree.weight((node_g, node_e)))
            self.assertEqual(5, tree.weight((node_g, node_h)))
            self.assert_neighbors(tree,
                                  node_h,
                                  [ node_g ])
            self.assertEqual(5, tree.weight((node_h, node_g)))
        else:
            self.fail('An unexpected value of tree.neighbors(node_h).')

if __name__ == '__main__':
    unittest.main()
