#!/usr/bin/python3

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

    def _relax(self, graph, distance_map, u, v):
        edge_distance = distance_map[u] + graph.weight((u, v))
        if distance_map[v] > edge_distance:
            distance_map[v] = edge_distance

            return True

        return False

    def bellman_ford_shortest_paths(self, graph, start):
        """
        Finds the shortest paths between nodes in a graph, which may have
        negative weights. Detects a negative cycle and reports it by returning
        a set of negative cycle nodes.

        One can do BFS on the set of negative cycle nodes A to find all
        arbitrarily short paths:

            - Put all nodes from A in queue Q.
            - Do breadth-first search with queue Q and find all nodes
              reachable from A.
            - Denote the set of these nodes by B.
            - All those nodes in B and only those can have arbitrarily short
              paths from the start node. That is, there exist arbitrarily
              short paths from the start to node u if and only if u is in the
              set B.
        """

        distance_map = {}
        for node in graph.nodes():
            distance_map[node] = float('inf')

        distance_map[start] = 0

        for i in range(len(graph.nodes()) - 1):
            for u, v in graph.edges():
                self._relax(graph, distance_map, u, v)

        negative_cycle_nodes = set()
        for u, v in graph.edges():
            edge_distance = distance_map[u] + graph.weight((u, v))
            if distance_map[v] > edge_distance:
                negative_cycle_nodes.add(v)

        return distance_map, negative_cycle_nodes

class Solver:
    """
    Given an directed graph with possibly negative edge weights and with n
    vertices and m edges as well as its vertex s, compute the length of
    shortest paths from s to all other vertices of the graph.
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
            u, v, weight = map(int, self._input().split())
            graph.add_directed_edge(u, v, weight)

        start = int(self._input())

        distance_map, negative_cycle_nodes = \
                           GraphUtil().bellman_ford_shortest_paths(graph, start)

        queue = [x for x in negative_cycle_nodes]
        all_negative_cycle_nodes = set()

        while len(queue) > 0:
            node = queue.pop(0)
            all_negative_cycle_nodes.add(node)

            for neighbor in graph.neighbors(node):
                if neighbor not in all_negative_cycle_nodes:
                    queue.append(neighbor)

        for node in range(1, n + 1):
            if node in all_negative_cycle_nodes:
                self._output('-')
                continue

            distance = distance_map[node]
            if distance == float('inf'):
                self._output('*')
            else:
                self._output(str(distance))

if __name__ == '__main__':
    Solver().solve()
