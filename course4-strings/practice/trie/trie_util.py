#!/usr/bin/python3

from operator import itemgetter

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

        The trie looks like this:

              0
             A T
             1 2
             C
             3

        Note: The flag indicating whether a substring is a patter is necessary.
        It doesn't suffice to check whether trie[next_node] == {}.
        """

        root = 0
        new_node_id = 1

        trie = dict()
        trie[root] = dict()

        for pattern in patterns:
            current_node = root
            for i in range(len(pattern)):
                current_symbol = pattern[i]

                if current_symbol in trie[current_node]:
                    next_node, flag = trie[current_node][current_symbol]

                    if i == len(pattern) - 1 and flag == False:
                        data = (next_node, True)
                        trie[current_node][current_symbol] = data

                    current_node = next_node
                else:
                    new_node = new_node_id
                    data = (new_node, i == len(pattern) - 1)
                    trie[current_node][current_symbol] = data
                    trie[new_node] = dict()

                    current_node = new_node
                    new_node_id += 1

        return trie

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

    @staticmethod
    def build_suffix_trie(text):
        patterns = []
        for i in range(len(text)):
            patterns.append(text[i:])

        return TrieUtil.build_trie(patterns)

    @staticmethod
    def build_compressed_suffix_trie(text):
        patterns = []
        for i in range(len(text)):
            patterns.append(text[i:])

        trie = TrieUtil.build_trie(patterns)

        if text != '$':
            root = 0
            node = root
            stack = []
            stack = [ (node, len(trie[node]), x)
                     for x in trie[node].items() ] + stack

            last_parent = None
            last_symbol = None
            previous_neighbor_info = None
            symbol_chain = []
            while len(stack) > 0:
                edge_info = stack.pop(0)
                parent = edge_info[0]
                sibling_count = edge_info[1]
                edge_data = edge_info[2]
                symbol = edge_data[0]
                neighbor_info = edge_data[1]
                neighbor = neighbor_info[0]
                node = neighbor

                if last_parent is None and last_symbol is None:
                    last_parent = parent
                    last_symbol = symbol

                if sibling_count != 1:
                    if len(symbol_chain) > 1:
                        del trie[last_parent][last_symbol]
                        trie[last_parent][''.join(symbol_chain)] = \
                                                          previous_neighbor_info
                    symbol_chain.clear()
                    last_parent = parent
                    last_symbol = symbol
                else:
                    previous_neighbor_info = neighbor_info
                    if parent != root:
                        del trie[parent]
                symbol_chain.append(symbol)

                stack = [ (node, len(trie[node]), x)
                         for x in trie[node].items() ] + stack

            if len(symbol_chain) > 1:
                del trie[last_parent][last_symbol]
                trie[last_parent][''.join(symbol_chain)] = \
                                                          previous_neighbor_info

        return trie
