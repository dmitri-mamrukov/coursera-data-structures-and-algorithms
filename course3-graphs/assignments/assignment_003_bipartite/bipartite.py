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

    def is_bipartite(self, graph):
        """
        A bipartite graph is a graph whose nodes can be divided into two
        independent sets, A and B such that every edge (u, v) either connects
        a vertex from A to B or a vertex from B to A. In other words,
        for every edge (u, v), either u belongs to A and v to B, or u belongs
        to B and v to A. We can also say that there is no edge that connects
        nodes of the same set.

        Performs the traversal in the Breadth First order.
        """

        if len(graph.nodes()) == 0:
            return True

        start = next(iter(graph.nodes()))

        color = {}
        for node in graph.nodes():
            color[node] = None

        color[start] = 0

        queue = []
        queue.append(start)

        while len(queue) > 0:
            node = queue.pop(0)
            for neighbor in graph.neighbors(node):
                if color[neighbor] is None:
                    queue.append(neighbor)
                    color[neighbor] = 1 - color[node]
                elif color[neighbor] == color[node]:
                    return False

        return True

class Solver:
    """
    Given an undirected graph with n vertices and m edges, checks whether it
    is bipartite.
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
            graph.add_undirected_edge(u, v)

        result = GraphUtil().is_bipartite(graph)

        self._output(1 if result == True else 0)

if __name__ == '__main__':
    Solver().solve()
