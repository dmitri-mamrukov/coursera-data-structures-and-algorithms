#!/usr/bin/python3

import io
import sys

class TrieUtil:

    @staticmethod
    def build_trie(patterns):
        """
        Returns a trie built from patterns in the form of a dictionary of
        dictionaries, e.g. {0:{'A':1,'T':2},1:{'C':3}} where

            - the key of the external dictionary is the node ID (integer), and

            - the internal dictionary contains all the trie edges outgoing
              from the corresponding node, and the keys are the letters on
              those edges, and the values are the node IDs to which these
              edges lead.

        The tree looks like this:

              0
             A T
             1 2
             C
             3
        """

        root = 0
        new_node_id = 1

        tree = dict()
        tree[root] = dict()

        for pattern in patterns:
            current_node = root
            for i in range(len(pattern)):
                current_symbol = pattern[i]

                if current_symbol in tree[current_node]:
                    next_node, flag = tree[current_node][current_symbol]

                    if i == len(pattern) - 1 and flag == False:
                        data = (next_node, True)
                        tree[current_node][current_symbol] = data

                    current_node = next_node
                else:
                    new_node = new_node_id
                    data = (new_node, i == len(pattern) - 1)
                    tree[current_node][current_symbol] = data
                    tree[new_node] = dict()

                    current_node = new_node
                    new_node_id += 1

        return tree

    @staticmethod
    def prefix_trie_matching(text, trie):
        """
        Finds whether any strings in Patterns match a prefix of Text.
        Returns a matching pattern; otherwise, an empty string.

        Given a string Text and Trie(Patterns), we can quickly check whether
        any string from Patterns matches a prefix of Text. To do so, we start
        reading symbols from the beginning of Text and see what string these
        symbols “spell” as we proceed along the path downward from the root of
        the trie. For each new symbol in Text, if we encounter this symbol
        along an edge leading down from the present node, then we continue
        along this edge; otherwise, we stop and conclude that no string in
        Patterns matches a prefix of Text. If we make it all the way to a leaf,
        then the pattern spelled out by this path matches a prefix of Text.
        """

        if len(text) == 0:
            return ''

        index = 0
        symbol = text[index]
        node = 0
        symbols = []
        while True:
            edges = trie[node]
            if len(edges) == 0:
                if len(symbols) <= len(text):
                    return ''.join(symbols)
                else:
                    return ''
            elif symbol in edges:
                symbols.append(symbol)
                node, is_pattern = edges[symbol]

                if is_pattern and len(symbols) <= len(text):
                    return ''.join(symbols)

                index += 1
                if index < len(text):
                    symbol = text[index]
            else:
                return ''

    @staticmethod
    def trie_matching(text, trie):
        """
        Returns a list of positions, where matching patterns occur in the text.

        To find whether any strings in Patterns match a substring of Text
        starting at position k, we chop off the first k − 1 symbols from
        Text and run prefix_trie_matching on the shortened string. As a
        result, to solve the Multiple Pattern Matching Problem, we simply
        iterate PrefixTrieMatching |Text| times, chopping the first symbol
        off of Text before each new iteration.

        Note that in practice there is no need to actually chop the first
        k − 1 symbols of Text. Instead, we just read Text from the k-th symbol.
        """

        positions = []

        index = 0
        while index < len(text):
            if TrieUtil.prefix_trie_matching(text[index:], trie) != '':
                positions.append(index)
            index += 1

        return positions

class Solver:
    """
    Implements the TrieMatching algorithm.

    Input: A string Text, an integer n and a collection of strings
           Patterns = { p1,..., pn }.
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
        n = int(self._input())

        patterns = []
        for i in range(n):
            patterns.append(self._input())

        tree = TrieUtil.build_trie(patterns)
        positions = TrieUtil.trie_matching(text, tree)

        self._output(' '.join([str(x) for x in positions]))

if __name__ == '__main__':
    Solver().solve()
