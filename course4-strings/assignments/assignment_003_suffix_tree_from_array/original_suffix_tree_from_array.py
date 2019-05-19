#!/usr/bin/python3

import io
import sys

class SuffixTree():
    """
    A utility that constructs a suffix tree from a given word,
    suffix array and Longest-Common-Prefix array.
    """

    WORD_DELIMITER_CHAR = '$'

    class Node():
        """
        Represents the suffix tree node.
        """

        def __init__(self, parent):
            """
            Initializes.
            """

            self._parent = parent
            self._children = []

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

        def update_parent(self, parent):
            """
            Updates the node's parent.
            """

            self._parent = parent

        def add_child(self, child):
            """
            Add the child to the node.
            """

            self.children.append(child)

        def remove_child(self, child):
            """
            Removes the child from the node.
            """

            self.children.remove(child)

        def __repr__(self):
            """
            Returns the string representation.
            """

            return 'parent={}, children={}'.format(self.parent,
                                                   self.children)

    class Edge():
        """
        Represents the suffix tree edge.
        """

        def __init__(self, start, end):
            """
            Initializes.
            """

            self._start = start
            self._end = end

        @property
        def start(self):
            """
            Returns the start index.
            """

            return self._start

        @property
        def end(self):
            """
            Returns the end index.
            """

            return self._end

        def __repr__(self):
            """
            Returns the string representation.
            """

            return '(start={}, end={})'.format(self.start, self.end)

    def __init__(self, word, suffix_array, lcp_array):
        """
        Initializes.

        Assumes that the word has the end-marker symbol '$'.
        """

        self._word = word
        self._suffix_array = suffix_array
        self._lcp_array = lcp_array

        self._nodes = [ SuffixTree.Node(-1) ]
        self._edges = {}

        self._add_word()

    def _add_word(self):
        """
        Adds a word to the suffix tree.
        """

        # Add each suffix of the word to the suffix tree.
        prev_lcp_distance = 0
        for i, item in enumerate(self._suffix_array):
            # Get the insertion point and associated suffix.
            suffix = self._word[item:]
            insertion_parent, insertion_suffix = self._insert_node(
                                                              suffix,
                                                              prev_lcp_distance)

            # Add a new node as a child to its parent node.
            child_node = SuffixTree.Node(insertion_parent)
            child_id = len(self._nodes)
            parent = self._nodes[insertion_parent]
            self._nodes.append(child_node)
            parent.add_child(child_id)

            # Create an edge associated with the new node.
            start = len(self._word) - len(insertion_suffix)
            end = len(self._word)
            edge = SuffixTree.Edge(start, end)
            new_node = len(self._nodes) - 1
            self._edges[insertion_parent, new_node] = edge

            if i < len(self._word) - 1:
                prev_lcp_distance = self._lcp_array[i]

    def _insert_node(self, suffix, lcp_distance, current_node=0):
        """
        Traverses the tree to determine the insertion point of the given suffix.
        """

        if lcp_distance == 0:
            return current_node, suffix

        # The distance to the next node is the length of the edge word
        # associated with traveling to the rightmost path.
        right_most_child = self._nodes[current_node].children[-1]
        edge = self._edges[current_node, right_most_child]
        edge_word = self.edge_word(edge)
        distance_to_next_node = len(edge_word)

        if distance_to_next_node <= lcp_distance:
            next_suffix = suffix[distance_to_next_node:]
            next_lcp_distance = lcp_distance - distance_to_next_node
            next_node = self._nodes[current_node].children[-1]

            return self._insert_node(next_suffix, next_lcp_distance, next_node)
        else:
            child = self._nodes[current_node].children[-1]
            split_pos = lcp_distance
            insertion_node = self._split_edge(current_node, child, split_pos)
            insertion_suffix = suffix[lcp_distance:]

            return insertion_node, insertion_suffix

    def _split_edge(self, parent, child, split_pos):
        """
        Splits the edge between the given parent and child nodes at the given
        split position.

        Inserts a new node at the split position and returns the index of the
        new node.
        """

        # Create a new node.
        new_node = len(self._nodes)
        self._nodes.append(SuffixTree.Node(parent))
        self._nodes[new_node].add_child(child)

        # Make the new node the parent's child.
        # Remove the child from the parent's children.
        self._nodes[parent].add_child(new_node)
        self._nodes[parent].remove_child(child)

        # Update the child's parent as the new node.
        self._nodes[child].update_parent(new_node)

        # Create new edges.
        # One is from the parent to the new node.
        # The other one is from the new node to the child.
        old_edge = self._edges[parent, child]
        self._edges[parent, new_node] = SuffixTree.Edge(
                                                     old_edge.start,
                                                     old_edge.start + split_pos)
        self._edges[new_node, child] =  SuffixTree.Edge(
                                                     old_edge.start + split_pos,
                                                     old_edge.end)

        # Remove the old edge.
        del self._edges[parent, child]

        return new_node

    def edge_word(self, edge):
        """
        Returns the substring associated with a given edge.
        """

        return self._word[edge.start:edge.end]

    def node_word(self, node):
        """
        Returns the substring associated with a traversal to the given node.
        """

        word = ''
        curr_node = node
        while self._nodes[curr_node].parent != -1:
            # Prepend the substring associated with each edge until we reach
            # the root of the suffix tree.
            parent = self._nodes[curr_node].parent
            edge = self._edges[parent, curr_node]
            word = self.edge_word(edge) + word
            curr_node = self._nodes[curr_node].parent

        return word

    def node_depth(self, node):
        """
        Returns the node's depth in the tree, which means the length of the
        substring that leads to the given node.

        Note: The substring does not include the out-of-alphabet character.

        Algorithm:

            - If the node ID is that of the root node, return 0.

            - Check the first edge for whether it includes the delimited
              character. The depth is initialized to the first edge's word's
              length.

            - Continue traversing the tree from the given node to the root.
              Increment the depth by each edge's word length.
        """

        if node == 0:
            return 0

        edge = self._edges[self._nodes[node].parent, node]
        edge_word = self.edge_word(edge)
        depth = None
        if SuffixTree.WORD_DELIMITER_CHAR not in edge_word:
            depth = len(edge_word)
        else:
            marker_index = edge_word.index(SuffixTree.WORD_DELIMITER_CHAR)
            depth = len(edge_word[:marker_index])

        curr_node = self._nodes[node].parent
        while self._nodes[curr_node].parent != -1:
            edge = self._edges[self._nodes[curr_node].parent, curr_node]
            edge_word = self.edge_word(edge)
            depth += len(edge_word)

            curr_node = self._nodes[curr_node].parent

        return depth

    def edge_strings(self):
        """
        Returns a list of all the edge strings in the tree.
        """

        return [self.edge_word(e) for e in self._edges.values()]

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
        outgoing edges of the corresponding node. The edges in the list must be
        sorted in the ascending order by the first character of the edge label.

        The root must have node ID = 0, and all other node IDs must be different
        nonnegative integers. Each edge must be represented by a tuple
        (node, start, end), where

            * node is the node ID of the ending node of the edge

            * start is the starting position (0-based) of the substring of text
              corresponding to the edge label

            * end is the first position (0-based) after the end of the
              substring corresponding to the edge label

        For example, if text = "ACACAA$", an edge with label "$" from root to
        a node with ID 1 must be represented by a tuple (1, 6, 7). This edge
        must be present in the list tree[0] (corresponding to the root node),
        and it should be the first edge in the list (because it has the
        smallest first character of all edges outgoing from the root).
        """

        tree = SuffixTree(text, suffix_array, lcp_array)

        tree_info = {}

        for node_id in range(0, len(tree._nodes)):
            node = tree._nodes[node_id]

            edge_info = []
            for child_id in node.children:
                edge = tree._edges[(node_id, child_id)]
                edge_info.append((text[edge.start],
                                  child_id,
                                  edge.start,
                                  edge.end))
            edge_info.sort(key=lambda x: x[1])
            edge_info_final = [(id, start, end)
                               for (ch, id, start, end) in edge_info]

            tree_info[node_id] = edge_info_final

        print(tree_info)
        print()

        return tree, tree_info

    def solve(self):
        """
        Solves the problem.
        """

        text = self._input()
        suffix_array = list(map(int, self._input().split()))
        lcp_array = list(map(int, self._input().split()))

        tree, tree_info = self.build_tree(text, suffix_array, lcp_array)

        self._output(text)

        queue = [ 0 ]
        while len(queue) > 0:
            node_id = queue.pop(0)
            node = tree._nodes[node_id]
            if node.parent != -1:
                edge = tree._edges[(node.parent, node_id)]
                print('{} {}'.format(edge.start, edge.end))
            queue += node.children
            prev_node = node
        print()

if __name__ == '__main__':
    Solver().solve()
