#!/usr/bin/python3

import io
import sys

class UkkonenSuffixTree():
    """
    Represents a suffix tree for string matching.

    Uses Ukkonen's algorithm for construction.
    """

    class Node():
        """
        Represents a node in the suffix tree.

        suffix_node
            the index of a node with a matching suffix, representing
            a suffix link; -1 indicates this node has no suffix link
        """

        def __init__(self):
            """
            Initializes.
            """

            self.suffix_node = -1

        def __repr__(self):
            """
            Returns the representation of this object.
            """

            return 'Node({})'.format(self.suffix_node)

    class Edge():
        """
        Represents an edge in the suffix tree.

        first_char_index
            the index of the start of the string part represented by this edge

        last_char_index
            the index of the end of the string part represented by this edge

        source_node_index
            the index of the source node of this edge

        destination_node_index
            the index of the destination node of this edge
        """

        def __init__(self,
                     first_char_index,
                     last_char_index,
                     source_node_index,
                     destination_node_index):
            """
            Initializes.
            """

            self.first_char_index = first_char_index
            self.last_char_index = last_char_index
            self.source_node_index = source_node_index
            self.destination_node_index = destination_node_index

        @property
        def length(self):
            """
            Returns the length.
            """

            return self.last_char_index - self.first_char_index

        def __repr__(self):
            """
            Returns the representation of this object.
            """

            return 'Edge({}, {}, {}, {})'.format(self.source_node_index,
                                                 self.destination_node_index,
                                                 self.first_char_index,
                                                 self.last_char_index)

    class Suffix():
        """
        Represents a suffix from first_char_index to last_char_index.

        source_node_index
            the index of the node where this suffix starts

        first_char_index
            the index of the start of the suffix in the string

        last_char_index
            the index of the end of the suffix in the string
        """

        def __init__(self,
                     source_node_index,
                     first_char_index,
                     last_char_index):
            """
            Initializes.
            """

            self.source_node_index = source_node_index
            self.first_char_index = first_char_index
            self.last_char_index = last_char_index

        @property
        def length(self):
            """
            Returns the length.
            """

            return self.last_char_index - self.first_char_index

        def explicit(self):
            """
            A suffix is explicit if it ends on a node. first_char_index
            is set greater than last_char_index to indicate this.
            """

            return self.first_char_index > self.last_char_index

        def implicit(self):
            """
            A suffix that is not explicit is implicit.
            """

            return self.last_char_index >= self.first_char_index

    def __init__(self, string, case_insensitive=False):
        """
        string
            the string for which to construct a suffix tree

        case_insensitive
            the flag that indicates whether string matching is case insensitive
        """

        self.string = string
        self.case_insensitive = case_insensitive
        self.n = len(string) - 1
        self.nodes = [ UkkonenSuffixTree.Node() ]
        self.edges = {}
        self.active = UkkonenSuffixTree.Suffix(0, 0, -1)

        if self.case_insensitive:
            self.string = self.string.lower()

        for i in range(len(string)):
            self._add_prefix(i)

    def __repr__(self):
        """
        Returns the representation of this object.

        Lists edges in the suffix tree.
        """

        curr_index = self.n
        s = '\tStart \tEnd \tSuffix \tFirst \tLast \tString\n'
        edges = list(self.edges.values())
        edges = sorted(edges, key=lambda x: (x.source_node_index,
                                             x.destination_node_index))
        for edge in edges:
            if edge.source_node_index == -1:
                continue

            s += '\t{} \t{} \t{} \t{} \t{} \t'.format(
                            edge.source_node_index,
                            edge.destination_node_index,
                            self.nodes[edge.destination_node_index].suffix_node,
                            edge.first_char_index,
                            edge.last_char_index)

            top = min(curr_index, edge.last_char_index)
            s += self.string[edge.first_char_index:top + 1] + '\n'

        return s

    def _add_prefix(self, last_char_index):
        """
        The core construction method.
        """

        last_parent_node = -1
        while True:
            parent_node = self.active.source_node_index
            if self.active.explicit():
                if (self.active.source_node_index,
                    self.string[last_char_index]) in self.edges:
                    # the prefix is already in the tree
                    break
            else:
                e = self.edges[self.active.source_node_index,
                               self.string[self.active.first_char_index]]
                if (self.string[e.first_char_index + self.active.length + 1] ==
                    self.string[last_char_index]):
                    # the prefix is already in the tree
                    break
                parent_node = self._split_edge(e, self.active)

            self.nodes.append(UkkonenSuffixTree.Node())
            e = UkkonenSuffixTree.Edge(last_char_index,
                                       self.n,
                                       parent_node,
                                       len(self.nodes) - 1)
            self._insert_edge(e)

            if last_parent_node > 0:
                self.nodes[last_parent_node].suffix_node = parent_node
            last_parent_node = parent_node

            if self.active.source_node_index == 0:
                self.active.first_char_index += 1
            else:
                index = self.active.source_node_index
                self.active.source_node_index = self.nodes[index].suffix_node
            self._canonize_suffix(self.active)

        if last_parent_node > 0:
            self.nodes[last_parent_node].suffix_node = parent_node

        self.active.last_char_index += 1
        self._canonize_suffix(self.active)

    def _insert_edge(self, edge):
        """
        Inserts the edge.
        """

        key = (edge.source_node_index, self.string[edge.first_char_index])
        self.edges[key] = edge

    def _remove_edge(self, edge):
        """
        Removes the edge.
        """

        key = (edge.source_node_index, self.string[edge.first_char_index])
        self.edges.pop(key)

    def _split_edge(self, edge, suffix):
        """
        Splits the edge and returns the updated edge's destination node's index.
        """

        self.nodes.append(UkkonenSuffixTree.Node())

        e = UkkonenSuffixTree.Edge(edge.first_char_index,
                                   edge.first_char_index + suffix.length,
                                   suffix.source_node_index,
                                   len(self.nodes) - 1)
        self._remove_edge(edge)
        self._insert_edge(e)

        # need to add a node for each edge
        destination_index = e.destination_node_index
        self.nodes[destination_index].suffix_node = suffix.source_node_index

        edge.first_char_index += suffix.length + 1
        edge.source_node_index = e.destination_node_index
        self._insert_edge(edge)

        return e.destination_node_index

    def _canonize_suffix(self, suffix):
        """
        Canonizes the suffix, walking along its suffix string until it is
        explicit or there are no more matched nodes.
        """

        if not suffix.explicit():
            e = self.edges[suffix.source_node_index,
                           self.string[suffix.first_char_index]]
            if e.length <= suffix.length:
                suffix.first_char_index += e.length + 1
                suffix.source_node_index = e.destination_node_index
                self._canonize_suffix(suffix)

    def find_substring(self, substring):
        """
        Returns the index of a substring in the string or -1 if it is not found.
        """

        if not substring:
            return -1

        if self.case_insensitive:
            substring = substring.lower()

        curr_node = 0
        i = 0
        while i < len(substring):
            edge = self.edges.get((curr_node, substring[i]))
            if not edge:
                return -1

            length = min(edge.length + 1, len(substring) - i)
            if (substring[i:i + length] !=
                self.string[edge.first_char_index:
                            edge.first_char_index + length]):
                return -1

            i += edge.length + 1
            curr_node = edge.destination_node_index

        return edge.first_char_index - len(substring) + length

    def has_substring(self, substring):
        return self.find_substring(substring) != -1

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

        tree = UkkonenSuffixTree(text)

        curr_index = tree.n
        values = tree.edges.values()
        sorted(values, key=lambda x: x.source_node_index)
        for edge in values:
            if edge.source_node_index == -1:
                continue

            top = min(curr_index, edge.last_char_index)
            self._output(tree.string[edge.first_char_index:top + 1])

if __name__ == '__main__':
    Solver().solve()
