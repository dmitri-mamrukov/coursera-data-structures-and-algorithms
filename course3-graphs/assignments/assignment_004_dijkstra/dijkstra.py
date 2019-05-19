#!/usr/bin/python3

import enum
import io
import sys

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
            if (self.datum != None and other.datum != None and
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
            if (self.datum != None and other.datum != None and
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

    def _relax(self, graph, distance_map, predecessor_map, u, v):
        edge_distance = distance_map[u] + graph.weight((u, v))
        if distance_map[v] > edge_distance:
            distance_map[v] = edge_distance
            predecessor_map[v] = u

            return True

        return False

    def dijkstra_shortest_paths(self, graph, start):
        """
        Finds the shortest paths between vertices in a graph, which may
        represent, for example, road networks. It was conceived by computer
        scientist Edsger W. Dijkstra in 1956 and published three years later.
        """

        distance_map, predecessor_map = \
                                  self._create_distance_and_previous_maps(graph)

        distance_map[start] = 0

        priority_queue = BinHeap(HeapMode.min)
        for node, value in distance_map.items():
            priority_queue.insert(HeapItem(value, node))

        while priority_queue.size > 0:
            min_item = priority_queue.extract()
            node = min_item.datum
            for neighbor in graph.neighbors(node):
                if self._relax(graph,
                               distance_map,
                               predecessor_map,
                               node,
                               neighbor):
                    index = None
                    for i, value in enumerate(priority_queue.elements):
                        if value.datum == neighbor:
                            index = i
                            break
                    edge_distance = (distance_map[node] +
                                     graph.weight((node, neighbor)))
                    priority_queue.change_priority(index, edge_distance)

        return distance_map, predecessor_map

class Solver:
    """
    Given a directed graph with positive edge weights and with n vertices and
    m edges as well as two vertices u and v, computes the weight of a shortest
    path between u and v (that is, the minimum total weight of a path from
    u to v).
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

        u, v = map(int, self._input().split())

        distance_map, previous_map = GraphUtil().dijkstra_shortest_paths(graph,
                                                                         u)

        result = distance_map[v]
        self._output(result if result != float('inf') else -1)

if __name__ == '__main__':
    Solver().solve()
