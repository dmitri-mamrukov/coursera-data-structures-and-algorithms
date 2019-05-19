#!/usr/bin/python3

import io
import sys

TRACE = False

class SuffixTree():
    """
    A utility that constructs a suffix tree from a given text,
    suffix array and Longest-Common-Prefix array.
    """

    class Node():
        """
        Represents the suffix tree node.
        """

        def __init__(self,
                     id,
                     parent,
                     children,
                     string_depth,
                     edge_start,
                     edge_end):
            """
            Initializes.
            """

            self._id = id
            self._parent = parent
            self._children = children
            self._string_depth = string_depth
            self._edge_start = edge_start
            self._edge_end = edge_end

        @property
        def id(self):
            """
            Returns the ID of this node.
            """

            return self._id

        @property
        def parent(self):
            """
            Returns the ID of the parent node.
            """

            return self._parent

        @property
        def children(self):
            """
            Returns the IDs of the child nodes.
            """

            return self._children

        def __repr__(self):
            """
            Returns the string representation.
            """

            child_strings = []
            for child in self.children.values():
                child_strings.append(str(child.id))
            child_strings = '[' + ', '.join(child_strings) + ']'
            parent_id = 'None' if self.parent is None else self.parent.id

            return ('id={}, parent={}, children={}, string-depth={}, '
                    'edge-start={}, edge-end={}').format(self.id,
                                                         parent_id,
                                                         child_strings,
                                                         self._string_depth,
                                                         self._edge_start,
                                                         self._edge_end)

    @staticmethod
    def _create_new_leaf(next_node_id, node, text, suffix):
        """
        Creates a new leaf node.
        """

        last_index = len(text) - 1

        leaf = SuffixTree.Node(next_node_id,
                               node,
                               {},
                               len(text) - suffix,
                               suffix + node._string_depth,
                               last_index)
        start_char = text[leaf._edge_start]
        node.children[start_char] = leaf

        return leaf

    @staticmethod
    def _split_edge(next_node_id, node, text, start, offset):
        """
        Creates new edges from the parent node to a mid node and from the
        mid node to the parent node's child node.
        """

        start_char = text[start]
        mid_char = text[start + offset]
        mid_node = SuffixTree.Node(next_node_id,
                                   node,
                                   {},
                                   node._string_depth + offset,
                                   start,
                                   start + offset - 1)

        old_child_node = node.children[start_char]
        old_child_node._parent = mid_node
        old_child_node._edge_start += offset
        mid_node.children[mid_char] = old_child_node
        node.children[start_char] = mid_node

        return mid_node

    @staticmethod
    def construct_suffix_tree(text, suffix_array, lcp_array):
        """
        Constructs a suffix tree, using the suffix array and longest-common
        prefix array.

        Algorithm:

            * Start from the root node.
            * Grow the first edge for the first suffix.
            * For each next suffix, go up from the leaf until LCP with
              the previous suffix is above.
            * Build a new edge for the new suffix.
        """

        nodes = []
        root = SuffixTree.Node(len(nodes), None, {}, 0, None, None)
        nodes.append(root)

        lcp_prev = 0
        curr_node = root
        for i in range(0, len(text)):
            suffix = suffix_array[i]
            while curr_node._string_depth > lcp_prev:
                curr_node = curr_node.parent
            if curr_node._string_depth == lcp_prev:
                curr_node = SuffixTree._create_new_leaf(len(nodes),
                                                        curr_node,
                                                        text,
                                                        suffix)
                nodes.append(curr_node)
            else:
                edge_start = suffix_array[i - 1] + curr_node._string_depth
                offset = lcp_prev - curr_node._string_depth
                mid_node = SuffixTree._split_edge(len(nodes),
                                                  curr_node,
                                                  text,
                                                  edge_start,
                                                  offset)
                nodes.append(mid_node)
                curr_node = SuffixTree._create_new_leaf(len(nodes),
                                                        mid_node,
                                                        text,
                                                        suffix)
                nodes.append(curr_node)

            if i < len(text) - 1:
                lcp_prev = lcp_array[i]

        return root, nodes

    @staticmethod
    def edge_strings(text, root):
        """
        Returns a list of all edge strings.
        """

        edge_strings = []

        node = root
        queue = [ node ]
        while len(queue) > 0:
            node = queue.pop(0)
            if node._edge_start is not None:
                edge_strings.append(text[node._edge_start:node._edge_end + 1])
            for child in node.children.values():
                queue.append(child)

        return edge_strings

class Solver:
    """
    Constructs a suffix tree from the suffix array and LCP array of a string.
    """

    def __init__(self):
        """
        Initializes the solver.
        """

        if __name__ == '__main__':
            input_stream = io.TextIOWrapper(sys.stdin.buffer, encoding='utf-8')
            self.input_processor = input_stream

    def _input(self):
        """
        Reads a line of the input and returns it without the newline and spaces.
        """

        return self.input_processor.readline().strip()

    def _output(self, text):
        """
        Outputs the text.
        """

        print(text)

    def build_tree(self, text, suffix_array, lcp_array):
        """
        Builds a suffix tree of the string text given its suffix array and LCP
        array. Returns the tree as a mapping from a node ID to the list of all
        outgoing edges of the corresponding node. The edges in the list are
        sorted in the ascending order by the first character of the edge label.
        """

        root, nodes = SuffixTree.construct_suffix_tree(text,
                                                       suffix_array,
                                                       lcp_array)
        tree_info = {}
        for node in nodes:
            edge_info = []
            for child_node in node.children.values():
                edge_info.append((child_node.id,
                                  child_node._edge_start,
                                  child_node._edge_end + 1,
                                  text[child_node._edge_start]))

            if len(edge_info) > 0:
                # Sort the edges by their first characters.
                edge_info.sort(key=lambda x: x[3])
                tree_info[node.id] = edge_info

        if TRACE:
            print(text)
            print(tree_info)
            print()

        return tree_info

    def output_tree(self, tree_info):
        """
        Outputs the edges of the suffix tree in the required order.
        Note that we use here the contract that the root of the tree
        will have node ID = 0 and that each vector of outgoing edges
        will be sorted by the first character of the corresponding edge label.

        The following code does not use recursion to avoid stack overflow
        issues. It uses two stacks to convert recursive function to a while
        loop.

        This code is an equivalent of

            OutputEdges(tree, 0);

        for the following _recursive_ function OutputEdges:

        def OutputEdges(tree, node_id):
            edges = tree[node_id]
            for edge in edges:
                print("%d %d" % (edge[1], edge[2]))
                OutputEdges(tree, edge[0]);
        """

        stack = [ (0, 0) ]
        result_edges = []
        while len(stack) > 0:
            (node, edge_index) = stack[-1]
            stack.pop()

            if not node in tree_info:
                continue

            edges = tree_info[node]

            if edge_index + 1 < len(edges):
                stack.append((node, edge_index + 1))

            self._output('{} {}'.format(edges[edge_index][1],
                                        edges[edge_index][2]))

            stack.append((edges[edge_index][0], 0))

    def solve(self):
        """
        Solves the problem.
        """

        text = self._input()
        suffix_array = list(map(int, self._input().split()))
        lcp_array = list(map(int, self._input().split()))

        tree_info = self.build_tree(text, suffix_array, lcp_array)

        self._output(text)
        self.output_tree(tree_info)

if __name__ == '__main__':
    Solver().solve()
