#!/usr/bin/python3

import sys

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

        next_node_id = 0
        root = SuffixTree.Node(next_node_id, None, {}, 0, None, None)
        next_node_id += 1

        lcp_prev = 0
        curr_node = root
        for i in range(0, len(text)):
            suffix = suffix_array[i]
            while curr_node._string_depth > lcp_prev:
                curr_node = curr_node.parent
            if curr_node._string_depth == lcp_prev:
                curr_node = SuffixTree._create_new_leaf(next_node_id,
                                                        curr_node,
                                                        text,
                                                        suffix)
                next_node_id += 1
            else:
                edge_start = suffix_array[i - 1] + curr_node._string_depth
                offset = lcp_prev - curr_node._string_depth
                mid_node = SuffixTree._split_edge(next_node_id,
                                                  curr_node,
                                                  text,
                                                  edge_start,
                                                  offset)
                next_node_id += 1
                curr_node = SuffixTree._create_new_leaf(next_node_id,
                                                        mid_node,
                                                        text,
                                                        suffix)
                next_node_id += 1

            if i < len(text) - 1:
                lcp_prev = lcp_array[i]

        return root

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

    @staticmethod
    def tree_info(text, root):
        """
        Returns the tree as a mapping from a node ID to the list of all
        outgoing edges of the corresponding node. The edges in the list are
        sorted in the ascending order by the first character of the edge label.

        The root has node ID = 0, and all other node IDs are different
        nonnegative integers. Each edge is represented by a tuple
        (node, start, end, first-char), where

            * node is the node ID of the ending node of the edge

            * start is the starting position (0-based) of the substring of text
              corresponding to the edge label

            * end is the first position (0-based) after the end of the
              substring corresponding to the edge label

            * first-char is the first character of the substring corresponding
              to the edge label

        For example, if text = "ACACAA$", an edge with label "$" from root to
        a node with ID 1 is represented by a tuple (1, 6, 7, $). This edge
        is present in the list tree[0] (corresponding to the root node),
        and it is the first edge in the list (because it has the
        smallest first character of all edges outgoing from the root).
        """

        tree_info = {}

        queue = [ root ]
        while len(queue) > 0:
            node = queue.pop(0)

            edge_info = []
            if len(node.children) > 0:
                for child_node in node.children.values():
                    queue.append(child_node)

                    edge_info.append((child_node.id,
                                      child_node._edge_start,
                                      child_node._edge_end + 1,
                                      text[child_node._edge_start]))

                # Sort the edges by their first characters.
                edge_info.sort(key=lambda x: x[3])

            if len(edge_info) > 0:
                tree_info[node.id] = edge_info

        return tree_info

def suffix_array_to_suffix_tree(sa, lcp, text):
    """
    Build suffix tree of the string text given its suffix array suffix_array
    and LCP array lcp_array. Return the tree as a mapping from a node ID
    to the list of all outgoing edges of the corresponding node. The edges in the
    list must be sorted in the ascending order by the first character of the edge label.
    Root must have node ID = 0, and all other node IDs must be different
    nonnegative integers. Each edge must be represented by a tuple (node, start, end), where
        * node is the node ID of the ending node of the edge
        * start is the starting position (0-based) of the substring of text corresponding to the edge label
        * end is the first position (0-based) after the end of the substring corresponding to the edge label

    For example, if text = "ACACAA$", an edge with label "$" from root to a node with ID 1
    must be represented by a tuple (1, 6, 7). This edge must be present in the list tree[0]
    (corresponding to the root node), and it should be the first edge in the list (because
    it has the smallest first character of all edges outgoing from the root).
    """
    # Implement this function yourself
    root = SuffixTree.construct_suffix_tree(text, sa, lcp)
    tree = SuffixTree.tree_info(text, root)

    return tree

if __name__ == '__main__':
    text = sys.stdin.readline().strip()
    sa = list(map(int, sys.stdin.readline().strip().split()))
    lcp = list(map(int, sys.stdin.readline().strip().split()))
    print(text)
    # Build the suffix tree and get a mapping from
    # suffix tree node ID to the list of outgoing Edges.
    tree = suffix_array_to_suffix_tree(sa, lcp, text)
    """
    Output the edges of the suffix tree in the required order.
    Note that we use here the contract that the root of the tree
    will have node ID = 0 and that each vector of outgoing edges
    will be sorted by the first character of the corresponding edge label.

    The following code avoids recursion to avoid stack overflow issues.
    It uses two stacks to convert recursive function to a while loop.
    This code is an equivalent of

        OutputEdges(tree, 0);

    for the following _recursive_ function OutputEdges:

    def OutputEdges(tree, node_id):
        edges = tree[node_id]
        for edge in edges:
            print("%d %d" % (edge[1], edge[2]))
            OutputEdges(tree, edge[0]);

    """
    stack = [(0, 0)]
    result_edges = []
    while len(stack) > 0:
      (node, edge_index) = stack[-1]
      stack.pop()
      if not node in tree:
        continue
      edges = tree[node]
      if edge_index + 1 < len(edges):
        stack.append((node, edge_index + 1))
      print("%d %d" % (edges[edge_index][1], edges[edge_index][2]))
      stack.append((edges[edge_index][0], 0))
