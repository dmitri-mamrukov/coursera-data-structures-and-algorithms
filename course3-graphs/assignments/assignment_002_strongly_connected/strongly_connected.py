#!/usr/bin/python3

import collections
import io
import sys

class Graph:
    """
    Represents the graph data structure.
    """

    def __init__(self):
        """
        Initializes a graph.
        """

        self._node_neighbors = {}
        self._edge_weights = {}

    def __repr__(self):
        """
        Returns a string representation of the graph.

        @rtype: string
        """

        texts = []

        nodes = [x for x in self._node_neighbors.keys()]
        nodes.sort()
        text = ', '.join(nodes)
        texts.append('[nodes: {}]'.format(text))

        edges = []
        for node, neighbors in self._node_neighbors.items():
            for neighbor in neighbors:
                item = '({}, {}) {}'.format(node,
                                              neighbor,
                                              self.weight((node, neighbor)))
                edges.append(item)
        edges.sort()
        text = ', '.join(edges)
        texts.append('[edges: {}]'.format(text))

        return ' '.join(texts)

    def nodes(self):
        """
        Returns a dictionary view of all nodes in the graph.

        @rtype: dict_keys
        """

        return self._node_neighbors.keys()

    def neighbors(self, node):
        """
        Returns a list of nodes directly accessible from the given node.

        @type  node: node
        @param node: The node identifier.
        @rtype: list
        """

        return self._node_neighbors[node]

    def edges(self):
        """
        Returns a dictionary view of all edges in the graph.

        @rtype: dict_keys
        """

        return self._edge_weights.keys()

    def weight(self, edge):
        """
        Returns the weight associated with the edge (which is a tuple of two
        nodes (u, v)).

        @type  edge: tuple
        @param edge: The tuple of two nodes (u, v)
        @rtype: number
        """

        return self._edge_weights[edge]

    def has_node(self, node):
        """
        Returns whether the requested node exists.

        @type  node: node
        @param node: The node identifier.
        @rtype: boolean
        """

        return node in self._node_neighbors

    def add_node(self, node):
        """
        Adds the given node to the graph.

        @attention: While nodes can be of any type, it is strongly recommended
                    to use only numbers and single-line strings as node
                    identifiers.

        @type  node: node
        @param node: The node identifier.
        """

        if not node in self._node_neighbors:
            self._node_neighbors[node] = []
        else:
            raise ValueError('Node %s already in the graph.' % node)

    def add_directed_edge(self, u, v, weight=0):
        """
        Add a directed edge connecting two given nodes to the graph.

        @type  u: node
        @param u: The first node identifier.
        @type  v: node
        @param v: The second node identifier.
        @type  weight: number
        @param weight: The edge's weight.
        """

        if u not in self._node_neighbors:
            raise ValueError('Node %s not in the graph.' % u)
        if v not in self._node_neighbors:
            raise ValueError('Node %s not in the graph.' % v)

        edge = (u, v)
        if edge not in self._edge_weights:
            self._node_neighbors[u].append(v)
            self._edge_weights[edge] = weight
        else:
            raise ValueError('Edge (%s, %s) already in graph.' % edge)

    def add_undirected_edge(self, u, v, weight=0):
        """
        Add an undirected edge connecting two given nodes to the graph.

        @type  u: node
        @param u: The first node identifier.
        @type  v: node
        @param v: The second node identifier.
        @type  weight: number
        @param weight: An edge weight.
        """

        if u not in self._node_neighbors:
            raise ValueError('Node %s not in the graph.' % u)
        if v not in self._node_neighbors:
            raise ValueError('Node %s not in the graph.' % v)

        edge1 = (u, v)
        edge2 = (v, u)
        if edge1 not in self._edge_weights:
            self._node_neighbors[u].append(v)
            self._edge_weights[edge1] = weight
        else:
            raise ValueError('Edge (%s, %s) already in graph.' % edge1)

        if edge2 not in self._edge_weights:
            self._node_neighbors[v].append(u)
            self._edge_weights[edge2] = weight
        else:
            raise ValueError('Edge (%s, %s) already in graph.' % edge2)

class GraphUtil:

    def __init__(self):
        self.visit_number = None
        self.preorder = collections.OrderedDict()
        self.postorder = collections.OrderedDict()
        self.component_id = {}

    def _previsit_number(self, node):
        self.preorder[node] = self.visit_number
        self.visit_number += 1

    def _postvisit_number(self, node):
        self.postorder[node] = self.visit_number
        self.visit_number += 1

    def _previsit_component_number(self, node):
        self.component_id[node] = self.component_number

    def _reverse(self, graph):
        reverse_graph = Graph()
        for node in graph.nodes():
            reverse_graph.add_node(node)
        for node in graph.nodes():
            for neighbor in graph.neighbors(node):
                reverse_graph.add_directed_edge(neighbor, node)

        return reverse_graph

    def _explore(self,
                 graph,
                 node,
                 visited,
                 previsit=None,
                 postvisit=None,
                 excluded=None):
        visited.add(node)

        if previsit is not None:
            previsit(node)

        if node in graph.nodes():
            for neighbor in graph.neighbors(node):
                if neighbor not in visited:
                    if excluded is not None and neighbor in excluded:
                        continue
                    self._explore(graph,
                                  neighbor,
                                  visited,
                                  previsit,
                                  postvisit,
                                  excluded)

        if postvisit is not None:
            postvisit(node)

    def explore(self,
                graph,
                start,
                previsit=None,
                postvisit=None,
                excluded=None):
        """
        Explores new edges in the Depth First order. Follows a long path
        forward, only backtracking when hits a dead end.
        """

        visited = set()

        if excluded is not None and start in excluded:
            pass
        else:
            self._explore(graph, start, visited, previsit, postvisit, excluded)

        return visited

    def depth_first_search(self, graph):
        """
        Finds all nodes of G, not just those reachable from some v.

        Performs the search in the Depth First order.

        Marks nodes with visit numbers (preorder and postorder).
        """

        self.visit_number = 1

        visited = set()

        for node in graph.nodes():
            if node not in visited:
                self._explore(graph,
                              node,
                              visited,
                              previsit=self._previsit_number,
                              postvisit=self._postvisit_number)

        return visited

    def strongly_connected_components(self, graph):
        """
        Definition of Strongly Connected Components:

        Two nodes v, w in a directed graph are connected if you can reach
        v from w and can reach w from v.

        Theorem:

        A directed graph can be partitioned into strongly connected components
        where two nodes are connected if and only if they are in the same
        component.
        """

        reverse_graph = self._reverse(graph)

        self.depth_first_search(reverse_graph)

        nodes_ordered_by_postorder = []
        for k, v in enumerate(self.postorder):
            nodes_ordered_by_postorder.insert(0, v)

        strongly_connected_components = []

        visited = set()
        excluded = set()
        for node in nodes_ordered_by_postorder:
            if node not in visited and node not in excluded:
                explored = self.explore(graph,
                                        node,
                                        excluded=excluded)

                strongly_connected_components.append([x for x in explored])

                visited.update(explored)
                excluded.update(explored)

        return strongly_connected_components

class Solver:
    """
    Computes the number of strongly connected components of a given directed
    graph with n vertices and m edges.
    """

    def __init__(self):
        if __name__ == '__main__':
            input_stream = io.TextIOWrapper(sys.stdin.buffer, encoding='utf-8')
            self.input_processor = input_stream

    def _input(self):
        return self.input_processor.readline().strip()

    def _output(self, text):
        print(text)

    def solve(self):
        n, m = map(int, self._input().split())

        graph = Graph()
        for i in range(1, n + 1):
            graph.add_node(i)
        for i in range(m):
            u, v = map(int, self._input().split())
            graph.add_directed_edge(u, v)

        result = GraphUtil().strongly_connected_components(graph)

        self._output(len(result))

if __name__ == '__main__':
    sys.setrecursionlimit(200000)

    Solver().solve()
