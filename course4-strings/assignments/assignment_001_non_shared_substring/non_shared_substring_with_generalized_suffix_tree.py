#!/usr/bin/python3

import io
import sys
import threading

class GeneralizedSuffixTree(object):
    """
    Represents a generalized suffix tree for string matching.

    Uses a list of words.
    """

    WORD_DELIMITER_CHAR = '$'

    class Node():
        """
        Represents a node in the generalized suffix tree.
        """

        def __init__(self, parent, words=set()):
            """
            Initializes.
            """

            self._parent = parent
            self._children = []
            self._words = words

        @property
        def parent(self):
            """
            Returns the parent node ID.
            """

            return self._parent

        @property
        def children(self):
            """
            Returns the IDs of the child nodes.
            """

            return self._children

        @property
        def words(self):
            """
            Returns the set of the indices of the words that pass through
            this node.
            """

            return self._words

        def __repr__(self):
            """
            Returns the string representation.
            """

            return 'parent={}, children={}, words={}'.format(self._parent,
                                                             self._children,
                                                             self._words)

    class Edge():
        """
        Represents an edge in the generalized suffix tree.
        """

        def __init__(self, word_index, start_index, stop_index):
            """
            Initializes.
            """

            self._word_index = word_index
            self._start_index = start_index
            self._stop_index = stop_index

        def __repr__(self):
            """
            Returns the string representation.
            """

            return 'word={}, start_index={}, stop_index={}'.format(
                                                             self._word_index,
                                                             self._start_index,
                                                             self._stop_index)

    def __init__(self, words):
        """
        Initializes.
        """

        self._words = []
        root = GeneralizedSuffixTree.Node(-1)
        self._nodes = [ root ]
        self._edges = {}

        for word in words:
            self._add_word(word, len(words) > 1)

    def _add_word(self, word, multiple=True):
        """
        Adds the word to the tree.

        Algorithm:

            - Append $<count> to the word (so that all the words are delimited
              by $0, ..., and $(N - 1).

            - Add each suffix of the word to the tree.

                - Find the insertion point and corresponding suffix.

                - Create a new node and add it as a child to its parent node.

                - Create an edge from the insertion point to the new node.
        """

        word += GeneralizedSuffixTree.WORD_DELIMITER_CHAR
        if multiple:
            word += str(len(self._words))
        self._words.append(word)

        end_index = word.index(GeneralizedSuffixTree.WORD_DELIMITER_CHAR)
        for i in range(end_index + 1):
            suffix = word[i:]
            insertion_suffix, insertion_parent_id = self._insert_node(suffix)

            new_word_index = len(self._words) - 1
            node = GeneralizedSuffixTree.Node(insertion_parent_id,
                                              { new_word_index })
            self._nodes.append(node)
            new_child_id = len(self._nodes) - 1
            self._nodes[insertion_parent_id]._children.append(new_child_id)

            end_index = len(word)
            start_index = end_index - len(insertion_suffix)
            edge = GeneralizedSuffixTree.Edge(new_word_index,
                                              start_index,
                                              end_index)
            self._edges[insertion_parent_id, new_child_id] = edge

    def _insert_node(self, suffix, current_node=0):
        """
        Traverses the tree to determine the insertion point of the given suffix.

        Algorithm:

            - Update the current node's word indices to include the last word's
              index.

            - If the first character of the given suffix is the delimiter,
              then return (suffix, current node).

            - Consider each child edge leading from the current node.

                - If the entire edge is a prefix of the suffix, make a
                  recursive call to move to the child node and traverse
                  further down the tree.

                - Otherwise, if the edge partially overlaps in the prefix of
                  the current suffix, split the edge and insert a new node
                  at the split point (which is at the end of the overlap).
                  Return (offset suffix, new node ID).
        """

        new_word_index = len(self._words) - 1
        self._nodes[current_node]._words.add(new_word_index)

        if suffix[0] == GeneralizedSuffixTree.WORD_DELIMITER_CHAR:
            return suffix, current_node

        for child_id in self._nodes[current_node]._children:
            edge = self._edges[current_node, child_id]
            edge_word = self.edge_substring(edge)

            if suffix[:len(edge_word)] == edge_word:
                suffix = suffix[len(edge_word):]
                return self._insert_node(suffix, child_id)
            elif suffix[0] == edge_word[0]:
                offset = 0
                while (suffix[offset] == edge_word[offset] !=
                                     GeneralizedSuffixTree.WORD_DELIMITER_CHAR):
                    offset += 1

                new_node_id = self._split_edge(current_node, child_id, offset)

                return suffix[offset:], new_node_id

        return suffix, current_node

    def _split_edge(self, parent_id, child_id, split_pos):
        """
        Splits the edge between the given parent and child nodes at the given
        split position.

        Inserts a new node at the split position and returns the index of the
        new node.

        Algorithm:

            - Create a new node, copying the child node's word indices and
              adding the last word's index. The node's parent is the old edge's
              parent node. The node's children is the old edge's child node.

            - The old edge's parent node's children are updated to include the
              new node and exclude the old edge's child node.

            - The old edge's child node's parent is updated as the new node.

            - The tree's edges are updated to remove the old edge and to add
              2 new edges from the parent node to the new node and from the new
              node to the child node.
        """

        new_node_id = len(self._nodes)
        new_word_index = len(self._words) - 1
        word_indices = self._nodes[child_id]._words | { new_word_index }
        new_node = GeneralizedSuffixTree.Node(parent_id,
                                              words=word_indices)
        self._nodes.append(new_node)
        self._nodes[new_node_id]._children.append(child_id)

        self._nodes[parent_id]._children.append(new_node_id)
        self._nodes[parent_id]._children.remove(child_id)

        self._nodes[child_id]._parent = new_node_id

        old_edge = self._edges[parent_id, child_id]
        parent_to_new_node_edge = GeneralizedSuffixTree.Edge(
                                              old_edge._word_index,
                                              old_edge._start_index,
                                              old_edge._start_index + split_pos)
        self._edges[parent_id, new_node_id] = parent_to_new_node_edge
        new_node_to_child_edge = GeneralizedSuffixTree.Edge(
                                              old_edge._word_index,
                                              old_edge._start_index + split_pos,
                                              old_edge._stop_index)
        self._edges[new_node_id, child_id] = new_node_to_child_edge
        del self._edges[parent_id, child_id]

        return new_node_id

    def edge_substring(self, edge):
        """
        Returns the substring that corresponds to the given edge.
        """

        word = self._words[edge._word_index]

        return word[edge._start_index:edge._stop_index]

    def node_substring(self, node_id):
        """
        Returns the substring that corresponds to a traversal from
        the root to the given node.

        Algorithm:

            - Traverse the tree from the given node to the root.
              Accumulate characters over the visited edges.
        """

        word = ''
        while self._nodes[node_id]._parent != -1:
            edge = self._edges[self._nodes[node_id]._parent, node_id]
            word = self.edge_substring(edge) + word

            node_id = self._nodes[node_id]._parent

        return word

    def node_depth(self, node_id):
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

        if node_id == 0:
            return 0

        edge = self._edges[self._nodes[node_id]._parent, node_id]
        edge_word = self.edge_substring(edge)
        depth = None
        if GeneralizedSuffixTree.WORD_DELIMITER_CHAR not in edge_word:
            depth = len(edge_word)
        else:
            marker_index = edge_word.index(
                                      GeneralizedSuffixTree.WORD_DELIMITER_CHAR)
            depth = len(edge_word[:marker_index])
        node_id = self._nodes[node_id]._parent

        while self._nodes[node_id]._parent != -1:
            edge = self._edges[self._nodes[node_id]._parent, node_id]
            edge_word = self.edge_substring(edge)
            depth += len(edge_word)

            node_id = self._nodes[node_id]._parent

        return depth

    @property
    def nodes(self):
        """
        Returns the nodes.
        """

        return self._nodes

    @property
    def edges(self):
        """
        Returns the edges.
        """

        return self._edges

class Solver:
    """
    Finds the shortest substring of one string that does not appear
    in another string.
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

    def find_shortest_nonshared_substring(self, text1, text2):
        tree = GeneralizedSuffixTree([ text1, text2 ])

        # Find all nodes that are reached only by traversing the first word.
        # This means that the substring up to that node is only in the first
        # word.
        word_index = 0
        all_node_ids = range(len(tree.nodes))
        node_ids = filter(lambda x: tree.nodes[x].words == { word_index },
                          all_node_ids)

        # Exclude all nodes that correspond to the delimiter that is unique
        # to the first word.
        node_ids = filter(lambda x: tree.edge_substring(
                                  tree.edges[tree.nodes[x].parent, x]) != '$0',
                          node_ids)

        # In order to get the shortest substring, use only the first character
        # of the last edge, hence the substring has its length of the parent's
        # depth plus one.
        shortest_node_id = min(node_ids,
                               key=lambda x:
                               tree.node_depth(tree.nodes[x].parent) + 1)

        # The shortest nonshared substring is the substring that leads up to
        # the first character of the edge that is connected to the optimal node.
        shortest_node_parent_id = tree.nodes[shortest_node_id].parent
        parent_substring = tree.node_substring(shortest_node_parent_id)
        edge = tree.edges[shortest_node_parent_id, shortest_node_id]
        first_char = tree.edge_substring(edge)[0]
        answer = parent_substring + first_char

        return answer

    def solve(self):
        """
        Solves the problem.

        Idea:

        This may be solved with the generalized suffix tree.

        After constructing the generalized suffix tree, you need to perform
        breadth-first search and find the first node not belonging to both
        strings. The path from the root to this node gives the shortest
        uncommon substring.
        """

        text1 = self._input()
        text2 = self._input()

        self._output(self.find_shortest_nonshared_substring(text1, text2))

def main():
    Solver().solve()

if __name__ == '__main__':
    """Instructor Michael Levin: Not only those three lines are critical for
    everything to work correctly, but also creating and starting a Thread
    object and calling your solution function inside it, because you set the
    stack size for threading, not for the whole program.
    """
    sys.setrecursionlimit(10**7) # max depth of recursion
    threading.stack_size(2**25)  # a new thread will get a stack of such a size
    threading.Thread(target = main).start()
