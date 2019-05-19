#!/usr/bin/python3

import io
import sys

class SuffixTree():

    class Node():

        def __init__(self, label):
            """
            Initializes the node.
            """

            # the label on the path leading to this node
            self._label = label
            # outgoing edges; maps characters to nodes
            self._edges = {}

        def __repr__(self):
            """
            Returns a string representation.
            """

            return '{}: {}'.format(self._label, self._edges)

    def __init__(self, text):
        """
        Makes a suffix tree, without suffix links, from the text in
        quadratic time and linear space.
        """

        text += '$'
        self._root = self.Node(None)
        # a trie for the longest suffix
        self._root._edges[text[0]] = self.Node(text)

        # add the rest of the suffixes, from longest to shortest
        for i in range(1, len(text)):
            # start at the root; we’ll walk down as far as we can go
            current = self._root
            j = i
            while j < len(text):
                if text[j] in current._edges:
                    child = current._edges[text[j]]
                    label = child._label

                    # walk along the edge until we exhaust its label or
                    # until we mismatch
                    k = j + 1
                    while k - j < len(label) and text[k] == label[k - j]:
                        k += 1

                    if k - j == len(label):
                        # we exhausted the edge
                        current = child
                        j = k
                    else:
                        # we fell off in middle of the edge
                        existing_char, new_char = label[k - j], text[k]

                        # create a new node at the branch point
                        middle = self.Node(label[:k - j])
                        middle._edges[new_char] = self.Node(text[k:])
                        # the original child becomes the middle node’s child
                        middle._edges[existing_char] = child

                        # the original child’s label is curtailed
                        child._label = label[k - j:]

                        # the middle node becomes the original parent's
                        # new child
                        current._edges[text[j]] = middle
                else:
                    # fell off the tree at a node, so make a new edge
                    # hanging off it
                    current._edges[text[j]] = self.Node(text[j:])

    def __repr__(self):
        """
        Returns a string representation.
        """

        return str(self._root)

    def follow_path(self, query):
        """
        Follows the path given by s.

        If we fall off the tree, returns None.

        If we finish mid-edge, returns (node, offset) where 'node' is a child
        node and 'offset' is the node's label's offset.

        If we finish on a node, returns (node, None).
        """

        current = self._root
        i = 0
        while i < len(query):
            ch = query[i]
            if ch not in current._edges:
                # fell off at a node
                return (None, None)

            child = current._edges[ch]
            label = child._label

            # walk along the edge until we exhaust its label or
            # until we mismatch
            j = i + 1
            while (j - i < len(label) and j < len(query) and
                   query[j] == label[j - i]):
                j += 1

            if j - i == len(label):
                # exhausted the edge
                current = child
                i = j
            elif j == len(query):
                # exhausted the query string in middle of the edge
                return (child, j - i)
            else:
                # fell off in the middle of the edge
                return (None, None)

        # exhausted the query string at an internal node
        return (current, None)

    def has_substring(self, query):
        """
        Returns true iff the query appears as a substring.
        """

        node, offset = self.follow_path(query)

        return node is not None

    def has_suffix(self, query):
        """
        Returns true iff the query is a suffix.
        """

        node, offset = self.follow_path(query)
        if node is None:
            # fell off the tree
            return False
        if offset is None:
            # finished on top of a node
            return '$' in node._edges
        else:
            # finished at 'offset' within an edge leading to 'node'
            return node._label[offset] == '$'

class Solver:
    """
    Constructs a suffix tree of a string.
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
        text = self._input()
        # remove the '$' ending as our data structure prepends it to the text
        text = text[:len(text) - 1]

        tree = SuffixTree(text)

        queue = []
        queue.append(tree._root)
        while len(queue) > 0:
            node = queue.pop(0)
            if node._label is not None:
                self._output(node._label)
            for neighbor in node._edges.values():
                queue.append(neighbor)

if __name__ == '__main__':
    Solver().solve()
