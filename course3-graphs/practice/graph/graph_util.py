import collections
import itertools
import math

import heap
import union_find

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

    def _postvisit_toposort(self, node):
        self.order.insert(0, node)

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

    def _create_distance_and_previous_maps(self, graph):
        distance_map = {}
        predecessor_map = {}
        for node in graph.nodes():
            distance_map[node] = math.inf
            predecessor_map[node] = None

        return distance_map, predecessor_map

    def _relax(self, graph, distance_map, predecessor_map, u, v):
        edge_distance = distance_map[u] + graph.weight((u, v))
        if distance_map[v] > edge_distance:
            distance_map[v] = edge_distance
            predecessor_map[v] = u

            return True

        return False

    def _index_in_priority_queue(self, priority_queue, key):
        index = None
        for i, value in enumerate(priority_queue.elements):
            if value.datum == key:
                index = i
                break

        return index

    def component(self, graph, start):
        """
        Explores every edge leaving every node we have found.
        """

        discovered = [ start ]
        visited = set()

        index = 0
        while index < len(discovered):
            node = discovered[index]
            visited.add(node)
            if node in graph.nodes():
                for neighbor in graph.neighbors(node):
                    if neighbor not in visited and neighbor not in discovered:
                        discovered.append(neighbor)
            index += 1

        return discovered

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

    def reaches(self, graph, x, y):
        """
        Given a graph and two distinct nodes u and v, checks if
        there is a path between u and v.
        """

        visited = set()

        self._explore(graph, x, visited)

        return True if y in visited else False

    def count_components(self, graph):
        """
        Given a graph with n nodes and m edges, computes the number of
        connected components in it.
        """

        component_count = 0
        visited = set()

        for node in graph.nodes():
            if node not in visited:
                self._explore(graph, node, visited)
                component_count += 1

        return component_count

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

    def number_all_nodes_by_component(self, graph):
        """
        Finds all nodes of G, not just those reachable from some v.
        Numbers nodes by component numbers.

        Performs the search in the Depth First order.
        """

        self.component_number = 1

        visited = set()

        for node in graph.nodes():
            if node not in visited:
                self._explore(graph,
                              node,
                              visited,
                              previsit=self._previsit_component_number)
                self.component_number += 1

        return visited, self.component_number - 1

    def has_cycle(self, graph):
        """
        Determines if the graph is a DAG, that is, it doesn't contain a cycle.

        Theorem:

        If G is a DAG, then, with an edge u to v, post(u) > post(v).
        """

        self.depth_first_search(graph)

        for from_node in graph.nodes():
            for to_node in graph.neighbors(from_node):
                if self.postorder[from_node] < self.postorder[to_node]:
                    return True

        return False

    def topological_sort(self, graph):
        """
        Topological ordering of a directed graph is a linear ordering of its
        nodes such that for every directed edge uv from node u to node
        v, u comes before v in the ordering. For instance, the nodes of
        the graph may represent tasks to be performed, and the edges may
        represent constraints that one task must be performed before another;
        in this application, a topological ordering is just a valid sequence
        for the tasks. A topological ordering is possible if and only if the
        graph has no directed cycles, that is, if it is a directed acyclic
        graph (DAG). Any DAG has at least one topological ordering, and
        algorithms are known for constructing a topological ordering of any
        DAG in linear time.

        Performs the search in the Depth First order.
        """

        visited = set()
        self.order = []

        for node in graph.nodes():
            if node not in visited:
                self._explore(graph,
                              node,
                              visited,
                              postvisit=self._postvisit_toposort)

        return self.order

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

    def shortest_path_tree(self, graph, start):
        """
        Constructs a distance layer tree of the shortest paths from the
        start node.

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
                if distance_map[neighbor] == math.inf:
                    queue.append(neighbor)
                    distance_map[neighbor] = distance_map[node] + 1
                    predecessor_map[neighbor] = node

        return distance_map, predecessor_map

    def reconstruct_shortest_path(self, start, end, predecessor_map):
        result = []

        node = end
        while node != start:
            result.insert(0, node)

            node = predecessor_map[node]
            if node is None:
                return []

        return result

    def is_bipartite(self, graph):
        """
        A bipartite graph is a graph whose nodes can be divided into two
        independent sets, A and B such that every edge (u, v) either connects
        a node from A to B or a node from B to A. In other words,
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

    def dijkstra_shortest_paths(self, graph, start):
        """
        Finds the shortest paths between nodes in a graph, which may
        represent, for example, road networks. It was conceived by computer
        scientist Edsger W. Dijkstra in 1956 and published three years later.
        """

        distance_map, predecessor_map = \
                                  self._create_distance_and_previous_maps(graph)

        distance_map[start] = 0

        priority_queue = heap.BinHeap(heap.HeapMode.min)
        for node, value in distance_map.items():
            priority_queue.insert(heap.HeapItem(value, node))

        while priority_queue.size > 0:
            min_item = priority_queue.extract()
            node = min_item.datum
            for neighbor in graph.neighbors(node):
                if self._relax(graph,
                               distance_map,
                               predecessor_map,
                               node,
                               neighbor):
                    index = self._index_in_priority_queue(priority_queue,
                                                          neighbor)
                    edge_distance = (distance_map[node] +
                                     graph.weight((node, neighbor)))
                    priority_queue.change_priority(index, edge_distance)

        return distance_map, predecessor_map

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

        distance_map, predecessor_map = \
                                  self._create_distance_and_previous_maps(graph)

        distance_map[start] = 0

        for i in range(len(graph.nodes()) - 1):
            for u, v in graph.edges():
                self._relax(graph,
                            distance_map,
                            predecessor_map,
                            u,
                            v)

        negative_cycle_nodes = set()
        for u, v in graph.edges():
            edge_distance = distance_map[u] + graph.weight((u, v))
            if distance_map[v] > edge_distance:
                negative_cycle_nodes.add(v)

        return distance_map, predecessor_map, negative_cycle_nodes

    def kruskal(self, graph):
        """
        Given a connected undirected graph G = (V, E) with positive edge
        weights, computes a minimum spanning tree that consists of a subset
        of edges E′ ⊆ E of minimum total weight such that the graph (V, E′)
        is connected.

        Greedy Strategy: Repeatedly adds the next lightest edge if this
        doesn’t produce a cycle.

        Note: The graph does not have to be undirected.
        """

        minimum_spanning_tree = Graph()

        set = union_find.UnionFind()

        node_to_wrapper_node_map = {}
        priority_queue = heap.BinHeap(heap.HeapMode.min)
        for node in graph.nodes():
            minimum_spanning_tree.add_node(node)

            wrapper_node = union_find.Node(node)
            node_to_wrapper_node_map[node] = wrapper_node
            set.make_set(wrapper_node)

        for u, v in graph.edges():
            edge = (node_to_wrapper_node_map[u], node_to_wrapper_node_map[v])
            priority_queue.insert(heap.HeapItem(graph.weight((u, v)),
                                                edge))

        while priority_queue.size > 0:
            min_item = priority_queue.extract()
            u_node, v_node = min_item.datum
            if set.find(u_node) != set.find(v_node):
                minimum_spanning_tree.add_undirected_edge(u_node.value,
                                                          v_node.value,
                                                          min_item.priority)
                set.union(u_node, v_node)

        return minimum_spanning_tree

    def prim(self, graph):
        """
        Given a connected undirected graph G = (V, E) with positive edge
        weights, computes a minimum spanning tree that consists of a subset
        of edges E′ ⊆ E of minimum total weight such that the graph (V, E′)
        is connected.

        Greedy Strategy: Repeatedly attach a node to the current tree by
        the next lightest edge.

        Note: The graph must be really connected undirected.
        """

        minimum_spanning_tree = Graph()

        if (len(graph.nodes()) == 0):
            return minimum_spanning_tree

        distance_map, predecessor_map = \
                                  self._create_distance_and_previous_maps(graph)

        # pick any initial node (the graph must be connected)
        start = next(iter(graph.nodes()))
        distance_map[start] = 0

        priority_queue = heap.BinHeap(heap.HeapMode.min)
        for node, value in distance_map.items():
            minimum_spanning_tree.add_node(node)

            priority_queue.insert(heap.HeapItem(value, node))

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
