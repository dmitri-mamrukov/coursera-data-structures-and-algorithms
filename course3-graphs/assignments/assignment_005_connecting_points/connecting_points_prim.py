#!/usr/bin/python3

import enum
import io
import math
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

class UnionFindNode:

    def __init__ (self, value):
        self.value = value
        self.parent = None
        self.rank = None

    def __str__(self):
        return str(self.value)

    def __repr__(self):
        return '[{}, parent={}, rank={}]'.format(self.value,
                                                 self.parent,
                                                 self.rank)

    def __lt__(self, other):
        if other is None or not isinstance(other, UnionFindNode):
            return False

        return self.value < other.value

    def __eq__(self, other):
        if other is None or not isinstance(other, UnionFindNode):
            return False

        return self.value == other.value

    def __gt__(self, other):
        if other is None or not isinstance(other, UnionFindNode):
            return False

        return self.value > other.value

class UnionFind:

    def make_set(self, x):
        """
        Makes a set containing only a given element (a singleton).
        """

        x.parent = x
        x.rank = 0

    def union(self, x, y):
        """
        Combines two trees into one by attaching the root of one to the root
        of the other.
        """

        x_root = self.find(x)
        y_root = self.find(y)

        if x_root.rank > y_root.rank:
            y_root.parent = x_root
        elif x_root.rank < y_root.rank:
            x_root.parent = y_root
        elif x_root != y_root:
            # x and y are not in the same set, so merge them
            y_root.parent = x_root
            x_root.rank = x_root.rank + 1

    def find(self, x):
        """
        Follows parent nodes until it reaches the root.

        Applies path compression.
        """

        if x.parent == None:
            raise ValueError('{} not in the set.'.format(x))

        if x.parent == x:
            return x
        else:
            x.parent = self.find(x.parent)

            return x.parent

class HeapMode(enum.Enum):
    min = 0
    max = 1

class HeapItem:

    def __init__(self, priority, datum=None):
        self._priority = priority
        self._datum = datum

    def __str__(self):
        return str(self.datum)

    def __repr__(self):
        return ('[priority=' + str(self.priority) +
                ', datum=' + str(self.datum) + ']')

    def __lt__(self, other):
        if self.priority < other.priority:
            return True
        elif self.priority == other.priority:
            if (self.datum is not None and other.datum is not None and
                self.datum < other.datum):
                    return True

        return False

    def __eq__(self, other):
        return (self.priority == other.priority and
            self.datum == other.datum)

    def __gt__(self, other):
        if self.priority > other.priority:
            return True
        elif self.priority == other.priority:
            if (self.datum is not None and other.datum is not None and
                self.datum > other.datum):
                    return True

        return False

    @property
    def priority(self):
        return self._priority

    @property
    def datum(self):
        return self._datum

class BinHeap:

    def __init__(self, mode=HeapMode.min):
        self._mode = mode
        self._size = 0
        self._heap_list = []

    def __str__(self):
        return str(self._heap_list)

    def __repr__(self):
        return ('[mode=' + str(self.mode) + ', size=' + str(self.size) +
                ', list=' + str(self.elements) + ']')

    @property
    def mode(self):
        return self._mode

    @property
    def size(self):
        return self._size

    @property
    def elements(self):
        return self._heap_list

    def _parent(self, index):
        return (index - 1) // 2

    def _left_child(self, index):
        return 2 * index + 1

    def _right_child(self, index):
        return 2 * index + 2

    def _has_greater_priority(self, x, y, mode):
        if mode == HeapMode.min:
            return x < y
        else:
            return x > y

    def _priority_child(self, index):
        if self._right_child(index) >= self.size:
            return self._left_child(index)
        else:
            left_child = self._left_child(index)
            right_child = self._right_child(index)
            if self._has_greater_priority(
                self._heap_list[left_child],
                self._heap_list[right_child],
                self.mode):
                return left_child
            else:
                return right_child

    def _sift_down(self, index):
        while self._left_child(index) < self.size:
            priority_child = self._priority_child(index)

            if self._has_greater_priority(
                self._heap_list[priority_child],
                self._heap_list[index],
                self.mode):
                self._heap_list[index], self._heap_list[priority_child] = \
                                              (self._heap_list[priority_child],
                                               self._heap_list[index])

            index = priority_child

    def _sift_up(self, index):
        while self._parent(index) >= 0:
            parent = self._parent(index)

            if self._has_greater_priority(
                self._heap_list[index],
                self._heap_list[parent],
                self.mode):
                self._heap_list[index], self._heap_list[parent] = \
                                                      (self._heap_list[parent],
                                                       self._heap_list[index])

            index = parent

    def build(self, list):
        self._size = len(list)
        self._heap_list = list

        i = self._parent(self.size - 1)
        while i >= 0:
            self._sift_down(i)
            i -= 1

    def extract(self):
        min_element = self._heap_list[0]
        self._heap_list[0] = self._heap_list[self.size - 1]
        self._size = self.size - 1
        self._heap_list.pop()
        self._sift_down(0)

        return min_element

    def insert(self, index):
        self._heap_list.append(index)
        self._size = self.size + 1
        self._sift_up(self.size - 1)

    def change_priority(self, index, p):
        if index < 0 or index > self.size:
            raise IndexError()

        old_item = HeapItem(self._heap_list[index].priority,
                            self._heap_list[index].datum)
        new_item = HeapItem(p, self._heap_list[index].datum)
        self._heap_list[index]._priority = p
        if self._has_greater_priority(new_item, old_item, self.mode):
            self._sift_up(index)
        else:
            self._sift_down(index)

    def sort_in_place(self, data):
        self.build(data)

        original_size = self.size
        for i in range(1, len(data)):
            self._heap_list[0], self._heap_list[self.size - 1] = \
                             self._heap_list[self.size - 1], self._heap_list[0]
            self._size -= 1
            self._sift_down(0)

        self._size = original_size

class GraphUtil:

    def _index_in_priority_queue(self, priority_queue, key):
        index = None
        for i, value in enumerate(priority_queue.elements):
            if value.datum == key:
                index = i
                break

        return index

    def prim(self, graph):
        """
        Given a connected undirected graph G = (V, E) with positive edge
        weights, computes a minimum spanning tree that consists of a subset
        of edges E′ ⊆ E of minimum total weight such that the graph (V, E′)
        is connected.

        Greedy Strategy: Repeatedly attach a vertex to the current tree by
        the next lightest edge.

        Note: The graph must be really connected undirected.
        """

        minimum_spanning_tree = Graph()

        if (len(graph.nodes()) == 0):
            return minimum_spanning_tree

        distance_map = {}
        predecessor_map = {}
        for node in graph.nodes():
            distance_map[node] = float('inf')
            predecessor_map[node] = None

        # pick any initial node (the graph must be connected)
        start = next(iter(graph.nodes()))
        distance_map[start] = 0

        priority_queue = BinHeap(HeapMode.min)
        for node, value in distance_map.items():
            minimum_spanning_tree.add_node(node)

            priority_queue.insert(HeapItem(value, node))

        while priority_queue.size > 0:
            min_item = priority_queue.extract()
            node = min_item.datum
            for neighbor in graph.neighbors(node):
                edge = (node, neighbor)
                edge_distance = graph.weight(edge)
                neighbor_index = self._index_in_priority_queue(priority_queue,
                                                               neighbor)
                if (neighbor_index != None and
                    distance_map[neighbor] > edge_distance):
                    distance_map[neighbor] = edge_distance

                    priority_queue.change_priority(neighbor_index,
                                                   edge_distance)

                    predecessor_map[neighbor] = node

        for node, value in predecessor_map.items():
            if value != None:
                edge = (value, node)
                edge_distance = graph.weight(edge)
                minimum_spanning_tree.add_undirected_edge(value,
                                                          node,
                                                          edge_distance)

        return minimum_spanning_tree

class Solver:
    """
    Given n points on a plane, connect them with segments of minimum total
    length such that there is a path between any two points. Recall that the
    length of a segment with endpoints (x1, y1) and (x2, y2) is equal to
    sqrt[(x1 − x2)^2 + (y1 − y2)^2].

    All points are pairwise different, no three points lie on the same line.
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
        n = int(self._input())

        points = []
        graph = Graph()
        for i in range(n):
            x, y = map(int, self._input().split())
            points.append((x, y))
            graph.add_node((x, y))
        for i in range(len(points)):
            for j in range(i + 1, len(points)):
                x1, y1 = points[i]
                x2, y2 = points[j]
                distance = math.sqrt(math.pow(x1 - x2, 2) +
                                     math.pow(y1 - y2, 2))
                graph.add_undirected_edge((x1, y1),
                                          (x2, y2),
                                          distance)

        tree = GraphUtil().prim(graph)

        visited_edges = set()
        total = 0
        for u, v in tree.edges():
            if (u, v) not in visited_edges:
                total += graph.weight((u, v))
                visited_edges.add((u, v))
                visited_edges.add((v, u))

        self._output(total)

if __name__ == '__main__':
    Solver().solve()
