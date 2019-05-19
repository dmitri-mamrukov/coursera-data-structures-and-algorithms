import operator

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

class PositionalSuffixTree():

    class Node():

        def __init__(self, start, length):
            """
            Initializes the node.
            """

            # the label's start index on the path leading to this node
            self._start = start
            # the label's length on the path leading to this node
            self._length = length
            # outgoing edges; maps characters to nodes
            self._edges = {}

        def __repr__(self):
            """
            Returns a string representation.
            """

            return '({}, {}): {}'.format(self._start, self._length, self._edges)

    def __init__(self, text):
        """
        Makes a suffix tree, without suffix links, from the text in
        quadratic time and linear space.
        """

        text += '$'
        text_length = len(text)

        self._text = text
        self._root = self.Node(None, None)
        # a trie for the longest suffix
        self._root._edges[text[0]] = self.Node(0, text_length)

        # add the rest of the suffixes, from longest to shortest
        for i in range(1, text_length):
            # start at the root; we’ll walk down as far as we can go
            current = self._root
            j = i
            while j < text_length:
                if text[j] in current._edges:
                    child = current._edges[text[j]]

                    # walk along the edge until we exhaust its label or
                    # until we mismatch
                    k = j + 1
                    while (k - j < child._length and
                        text[k] == text[child._start + k - j]):
                        k += 1

                    if k - j == child._length:
                        # we exhausted the edge
                        current = child
                        j = k
                    else:
                        # we fell off in middle of the edge
                        existing_char, new_char = (text[child._start + k - j],
                                                   text[k])

                        # create a new node at the branch point
                        middle = self.Node(child._start, k - j)
                        middle._edges[new_char] = self.Node(k,
                                                            text_length - k)
                        # the original child becomes the middle node’s child
                        middle._edges[existing_char] = child

                        # the original child’s label is curtailed
                        child._start = child._start + k - j
                        child._length -= k - j

                        # the middle node becomes the original parent's
                        # new child
                        current._edges[text[j]] = middle
                else:
                    # fell off the tree at a node, so make a new edge
                    # hanging off it
                    current._edges[text[j]] = self.Node(j, text_length - j)

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

            # walk along the edge until we exhaust its label or
            # until we mismatch
            j = i + 1
            while (j - i < child._length and j < len(query) and
                   query[j] == self._text[child._start + j - i]):
                j += 1

            if j - i == child._length:
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
            return self._text[node._start + offset] == '$'

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
