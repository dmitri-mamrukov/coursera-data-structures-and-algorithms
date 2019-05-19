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

    def _create_distance_and_previous_maps(self, graph):
        distance_map = {}
        predecessor_map = {}
        for node in graph.nodes():
            distance_map[node] = float('inf')
            predecessor_map[node] = None

        return distance_map, predecessor_map

    def shortest_path_tree(self, graph, start):
        """
        Constructs a distance layer tree of the shortest paths from the
        start vertex.

        Performs the search in the Breadth First order.
        """

        distance_map, predecessor_map = \
                                  self._create_distance_and_previous_maps(graph)

        distance_map[start] = 0

        queue = []
        queue.append(start)

        while len(queue) > 0:
            node = queue.pop(0)
            for neighbor in graph.neighbors(node):
                if distance_map[neighbor] == float('inf'):
                    queue.append(neighbor)
                    distance_map[neighbor] = distance_map[node] + 1
                    predecessor_map[neighbor] = node

        return distance_map, predecessor_map

class Solver:
    """
    You would like to compute the minimum number of flight segments to get
    from one city to another one. For this, you construct the following
    undirected graph: vertices represent cities, there is an edge between two
    vertices whenever there is a flight between the corresponding two cities.
    Then, it suffices to find a shortest path from one of the given cities to
    the other one.

    Given an undirected graph with n vertices and m edges and two vertices
    u and v, computes the length of a shortest path between u and v (that is,
    the minimum number of edges in a path from u to v).
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

        start, destination = map(int, self._input().split())

        distance, previous = GraphUtil().shortest_path_tree(graph, start)

        self._output(distance[destination]
                     if distance[destination] != float('inf') else -1)

if __name__ == '__main__':
    Solver().solve()
