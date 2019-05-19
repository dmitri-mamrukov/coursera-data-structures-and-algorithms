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
                    current_node = tree[current_node][current_symbol]
                else:
                    new_node = new_node_id
                    tree[current_node][current_symbol] = new_node
                    tree[new_node] = dict()

                    current_node = new_node
                    new_node_id += 1

        return tree

class Solver:
    """
    Constructs a trie from a collection of patterns,

    Input: An integer n and a collection of strings Patterns = { p1,..., pn }.
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

        patterns = []
        for i in range(n):
            patterns.append(self._input())

        tree = TrieUtil.build_trie(patterns)

        for node in tree:
            for symbol, neighbor in tree[node].items():
                self._output('{}->{}:{}'.format(node, neighbor, symbol))

if __name__ == '__main__':
    Solver().solve()
