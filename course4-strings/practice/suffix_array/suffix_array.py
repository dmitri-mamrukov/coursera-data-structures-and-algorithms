import collections
import functools

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

class Util():

    @staticmethod
    def _suffix_compare(word, i, j):
        """
        Compares suffixes without generating entire suffixes.

        Idea:

        To compare the suffixes word[i:] and word[j:], compare the letters
        at the ith and jth indices. Return -1 if the ith letter comes before
        the jth letter, 1 if jth letter comes before the ith letter.
        If the letters match, repeat the process with the letter at the (i+1)th
        and (j+1)th indices.
        """

        length = len(word)

        while i < length and j < length:
            if word[i] == word[j]:
                i += 1
                j += 1
            elif word[i] < word[j]:
                return -1
            else:
                return 1

        return 0

    @staticmethod
    def _sort_bucket(word, bucket, order):
        """
        Performs the bucket sort. Returns the list of sorted suffixes.

        We start calling the method, which takes our string and a list of
        indices to examine. Our initial call to it will just pass in every
        index in the string – all of the suffixes as one big bucket.

        d, then, is a dictionary of initial characters to suffix indices.
        Now what we need to do is call the method recursively to go through
        each bucket and sort the strings by second position, third position,
        etc. To make the whole thing a little more efficient, rather than
        index by one additional character each time, we’ll double the number
        of characters. The first recursive call will sort on strings of
        length two, the second call will sort on four, etc.

        The order parameter indicates the number of characters we want to sort
        on.

        If a bucket contains a single element, that is appended to the result;
        otherwise, the method is called recursively and the sorted bucket is
        added to the result.
        """

        d = collections.defaultdict(list)
        for i in bucket:
            key = word[i:i + order]
            d[key].append(i)

        result = []
        for k, v in sorted(d.items()):
            if len(v) > 1:
                result += Util._sort_bucket(word, v, order * 2)
            else:
                result.append(v[0])

        return result

    @staticmethod
    def _sort_chars(word):
        """
        Performs the counting sort of the string input and returns the order
        list (which indicates the lexicographic order of the suffixes of the
        input string).

        Example:

        S = ababaa$

            Suffixes:

            $
            a$
            aa$
            baa$
            abaa$
            babaa$
            ababaa$

            Sorted suffixes:

            $
            a$
            aa$
            abaa$
            ababaa$
            baa$
            babaa$

            Taking the first char of every suffix, we see that the
            lexicographic order (within the associated suffixes) of the first
            chars are:

            order char comment
            6     $    6th char in ababaa$
            0     a    0th char in ababaa$
            2     a    2nd char in ababaa$
            4     a    4th char in ababaa$
            5     a    5th char in ababaa$
            1     b    1st char in ababaa$
            3     b    3rd char in ababaa$

            Hence, order = [ 6, 0, 2, 4, 5, 1, 3 ]

        Implementation trace:

            word = ababaa$
                   0123456

            alphabet_map = { '$': 0, 'a': 1, 'b': 2 }

            After the first computation of the count array (counting chars):

            count = [ 1, 4, 2 ]
                      0  1  2

            After the second computation of the count array (partial sums):

            count = [ 1, 5, 7 ]
                      0  1  2

            Computing the order array:

            count = [ 1, 5, 7 ]
                      0  1  2
            order = [ 0, 0, 0, 0, 0, 0, 0 ]
                      0  1  2  3  4  5  6

            ababaa$, i = 6, word[i] = $, char_index = 0, count[char_index] = 0
            count = [ 0, 5, 7 ]
                      0  1  2
            order = [ 6, 0, 0, 0, 0, 0, 0 ]
                      0  1  2  3  4  5  6

            ababaa$, i = 5, word[i] = a, char_index = 1, count[char_index] = 4
            count = [ 0, 4, 7 ]
                      0  1  2
            order = [ 6, 0, 0, 0, 5, 0, 0 ]
                      0  1  2  3  4  5  6

            ababaa$, i = 4, word[i] = a, char_index = 1, count[char_index] = 3
            count = [ 0, 3, 7 ]
                      0  1  2
            order = [ 6, 0, 0, 4, 5, 0, 0 ]
                      0  1  2  3  4  5  6

            ababaa$, i = 3, word[i] = b, char_index = 1, count[char_index] = 6
            count = [ 0, 3, 6 ]
                      0  1  2
            order = [ 6, 0, 0, 4, 5, 0, 3 ]
                      0  1  2  3  4  5  6

            ababaa$, i = 2, word[i] = a, char_index = 1, count[char_index] = 2
            count = [ 0, 2, 6 ]
                      0  1  2
            order = [ 6, 0, 2, 4, 5, 0, 3 ]
                      0  1  2  3  4  5  6

            ababaa$, i = 1, word[i] = b, char_index = 1, count[char_index] = 5
            count = [ 0, 2, 5 ]
                      0  1  2
            order = [ 6, 0, 2, 4, 5, 1, 3 ]
                      0  1  2  3  4  5  6

            ababaa$, i = 0, word[i] = a, char_index = 1, count[char_index] = 1
            count = [ 0, 1, 5 ]
                      0  1  2
            order = [ 6, 0, 2, 4, 5, 1, 3 ]
                      0  1  2  3  4  5  6
        """

        sorted_alphabet = sorted(set(word))
        alphabet_map = {}
        char_index = 0
        for ch in sorted_alphabet:
            if ch not in alphabet_map:
                alphabet_map[ch] = char_index
                char_index += 1

        order = [ 0 ] * len(word)
        count = [ 0 ] * len(alphabet_map)

        for ch in word:
            # Count the characters in the word.
            count[alphabet_map[ch]] += 1
        for i in range(1, len(alphabet_map)):
            # Compute the partial sums, which slide each element's sorted
            # position by the previous element's count of positions.
            count[i] += count[i - 1]

        # Now the count array contains the position in the sorted array of all
        # the characters of the input string right after the last such
        # character.
        #
        # For example, count[0] is equal to the number of occurrences of the
        # smallest character of the alphabet in the input string S, and if we
        # sort the characters of S, the smallest character will be in positions
        # 0 through count[0] - 1 (because count[0] contains the count of such
        # positions). The same goes for count[]] for 0 <= i < |S|.

        for i in range(len(word) - 1, -1, -1):
            # We iterate from the right to the left. We look at the character
            # and we know that the partial sums array contains the position
            # after the position where this character should be in the order
            # array. So we decrease the counter by one and we save our
            # character's position in the corresponding cell of the order array.
            char_index = alphabet_map[word[i]]
            count[char_index] -= 1
            order[count[char_index]] = i

        return order, alphabet_map

    @staticmethod
    def _compute_char_classes(word, order):
        """
        Computes equivalence classes of the partial cyclic shift.

        Theory:

            Let Ci be a partial cyclic shift of length L starting in position i.

            Ci can be equal to Cj, then they are in one equivalence class.

            This method computes class[i] number of different cyclic shifts of
            length L that are strictly smaller than Ci.

            Ci == Cj means that class[i] == class[j].

        Example:

            (See the introductory explanation in _sort_chars(word).)

            S = ababaa$

            order = [ 6, 0, 2, 4, 5, 1, 3 ]

            order char
            6     $
            0     a
            2     a
            4     a
            5     a
            1     b
            3     b

            Assign 0 to the smallest of the cyclic shifts of the current length.
            char = $ (position 6)
            class = [ _, _, _, _, _, _, 0 ]

            The next smallest cyclic shift is 'a', and it's different from the
            previous one ('$'). So we need a new equivalence class for 'a'.
            char = a (position 0)
            class = [ 1, _, _, _, _, _, 0 ]

            The next smallest cyclic shift is 'a', and it's the same as the
            previous one ('a'). So we assign 1 to it.
            char = a (position 2)
            class = [ 1, _, 1, _, _, _, 0 ]

            The next smallest cyclic shift is 'a', and it's the same as the
            previous one ('a'). So we assign 1 to it.
            char = a (position 4)
            class = [ 1, _, 1, _, 1, _, 0 ]

            The next smallest cyclic shift is 'a', and it's the same as the
            previous one ('a'). So we assign 1 to it.
            char = a (position 5)
            class = [ 1, _, 1, _, 1, 1, 0 ]

            The next smallest cyclic shift is 'b', and it's different from the
            previous one ('a'). So we need a new equivalence class for 'b'.
            char = b (position 1)
            class = [ 1, 2, 1, _, 1, 1, 0 ]

            The next smallest cyclic shift is 'b', and it's the same as the
            previous one ('b'). So we assign 1 to it.
            char = b (position 3)
            class = [ 1, 2, 1, 2, 1, 1, 0 ]

            Now we know the classes of all the single character cyclic shifts.
            The $ is in equivalence class 0. The 4 a's are in equivalence
            class 1. The 2 b's are in equivalence class 2.

        Note: The maximum value in the class array for some string S is
        the number of different characters in the initial string s (before
        adding '$').
        """

        if len(word) == 0:
            return []

        eq_class = [ 0 ] * len(word)
        eq_class[order[0]] = 0
        for i in range(1, len(word)):
            if word[order[i]] != word[order[i - 1]]:
                 eq_class[order[i]] = eq_class[order[i - 1]] + 1
            else:
                 eq_class[order[i]] = eq_class[order[i - 1]]

        return eq_class

    @staticmethod
    def _sort_double_cyclic_shifts(word, length, order, eq_class):
        """
        Sorts double cyclic shifts and returns a new order array.
        """

        # Initialize the count array to the word's length.
        #
        # This time we don't use the alphabet's size (as _sort_chars(word)
        # does) because we don't sort characters but equivalence classes of
        # cyclic shift of length L. And there are at most the word's length
        # different equivalence classes.
        count = [ 0 ] * len(word)
        # This array will store our answer. It will be the order of the sorted
        # double cyclic shift.
        new_order = [ 0 ] * len(word)

        for i in range(len(word)):
            # Count the number of occurrences of each equivalence class of
            # single cyclic shifts.
            count[eq_class[i]] += 1
        for i in range(1, len(word)):
            # Compute the partial sums, which slide each element's sorted
            # position by the previous element's count of positions.
            count[i] += count[i - 1]

        for i in range(len(word) - 1, -1, -1):
            # We iterate from the right to the left. We go through the array
            # of double cyclic shifts, which are initially sorted by their
            # second half in reverse order.
            #
            # But we don't want to actually build this array of double cyclic
            # shifts and then go through it in reverse order. We want to only
            # build this array in our head and in the code we just want to go
            # through this array in reverse order.
            #
            # We have the order array, and, if we go in direct order of this
            # array, we'll go through all the cyclic shifts of length L in
            # increasing order.
            #
            # What we need instead is, first, to go not through cyclic shifts
            # of length L but through cyclic shifts of L, which starts exactly
            # L counter-clockwise from those. That is why we decrease order[i]
            # by L at the word's length and take modulo the word's length just
            # because we go through a circle.
            start = (order[i] - length + len(word)) % len(word)
            # Take the class of this start position, which is the class of
            # the first half of the corresponding double shift by which we
            # want to sort.
            class_index = eq_class[start]
            # Decrease the partial sum corresponding to that equivalence
            # class in the counting array.
            count[class_index] -= 1
            # Put our start in the position, which the counting sort prescribes
            # to it
            new_order[count[class_index]] = start

        return new_order

    @staticmethod
    def _update_eq_classes(length, order, eq_class):
        """
        Updates the equivalence classes of the double cyclic shifts after
        sorting them. Returns an array with equivalence classes of the double
        cyclic shifts.

        The order array is on the double cyclic shifts.

        The equivalence class array and the length are on single cyclic shifts.

        To update classes we need to compute the pairs of single shifts which
        constitute cyclic shifts, which we have just sorted. We have already
        sorted the pairs. So we just need to go through them in order and
        compare each pair to the previous pair. If it's the same, then we need
        to assign it to the same class. If it's bigger, then we need to create
        a new class and assign it to this pair. To compare the pairs, we can
        compare them separately by the first element and then by the second
        element. Of course, the element of the pairs are cyclic shifts and we
        don't want to compare them directly character by character. But for
        that we already know their equivalence class is of the single cyclic
        shift, and we can just compare the equivalence classes instead of the
        cyclic shifts themselves. So we can compare any two pairs of single
        cyclic shifts in constant time.
        """

        # Basically, the order's length is the associated word's length.
        n = len(order)

        if n == 0:
            return []

        # This array will store our answer (equivalence classes of the double
        # cyclic shifts).
        new_eq_class = [ 0 ] * n
        # The smallest double cyclic shift is in the order's position 0, and
        # we assign the new equivalence class to 0.
        new_eq_class[order[0]] = 0

        for i in range(1, n):
            # We go through all the double cyclic shifts. We need to compare
            # double cyclic shift number i and double cyclic shift number i - 1.
            #
            # The starting position of double cyclic shift number i.
            curr = order[i]
            # The starting position of the previous double cyclic shift number.
            prev = order[i - 1]
            # The middle position of double cyclic shift number i,
            # where the second half starts.
            mid_curr = (curr + length) % n
            # The middle position of the previous double cyclic shift number,
            # where the second half starts.
            mid_prev = (prev + length) % n
            # We need compare them half by half.
            if (eq_class[curr] != eq_class[prev] or
                eq_class[mid_curr] != eq_class[mid_prev]):
                # At least one half is different, so the pair is different from
                # the previous one. And we need to create a new class, increase
                # the current class by 1 and assign it to the current position.
                new_eq_class[curr] = new_eq_class[prev] + 1
            else:
                # The pairs are the same, and we don't need to create a new
                # class, so we assign the same class to the current position.
                new_eq_class[curr] = new_eq_class[prev]

        return new_eq_class

    @staticmethod
    def _longest_common_prefix_of_suffixes(word, i, j, equal):
        """
        Computes the longest common prefix of suffixes, which start at
        i + offset and j + offset.

        The longest common prefix of two strings S and T is the longest such
        string u that u is a prefix of both S and T.

        We denote the length of the longest common prefix of S and T as
        LCP(S, T).
        """

        lcp = max(0, equal)
        while i + lcp < len(word) and j + lcp < len(word):
            if word[i + lcp] == word[j + lcp]:
                lcp += 1
            else:
                break

        return lcp

    @staticmethod
    def _invert_suffix_array(order):
        """
        Inverts the suffix array, using the order array.
        """

        pos = [ 0 ] * len(order)
        for i in range(0, len(order)):
            pos[order[i]] = i

        return pos

    @staticmethod
    def construct_suffix_array(word):
        """
        Constructs a suffix array from the given word.
        """

        # Sort the index array using the suffix comparison function.
        indices = range(len(word))
        suffix_array = sorted(indices,
                              key=functools.cmp_to_key(lambda i, j:
                                                       Util._suffix_compare(
                                                                           word,
                                                                           i,
                                                                           j)))

        return suffix_array

    @staticmethod
    def construct_suffix_array_manber_myers(word):
        """
        Constructs a suffix array from the given word using the algorithm by
        Manber and Myers.

        An idea was suggested by Udi Manber and Gene Myers back in the 1990’s.
        It’s a variant on bucket sort, which is a sorting algorithm that
        operates by first looking only at the first character of each string
        and putting those that share the same initial character into a bucket.
        Then it looks at each bucket for the second character in the string and
        so on. This is a handy paradigm for us, since we don’t even have
        different strings to work on; we only have indices into our one string.

        Here’s the idea: we’ll put each suffix into a bucket using its first
        character, so all the suffixes that start with ‘A’ will be in one
        bucket, all the suffixes that start with ‘B’ will be in another, and
        so on. Obviously, all the suffixes in the ‘A’ bucket will have a sort
        order before those in the ‘B’ bucket or ‘C’ bucket.
        """

        indices = [i for i in range(len(word))]

        return Util._sort_bucket(word, indices, 1)

    @staticmethod
    def construct_suffix_array_count_sort(word):
        """
        Constructs a suffix array from the given word using the count sort
        algorithm.

        Returns the order of the cyclic shifts or the suffixes of the string.

        Note: We assume that the string already has '$' in the end and that '$'
        is smaller than all the characters in the string.
        """

        # Sort the characters (single character cyclic shifts of the string).
        order, alphabet = Util._sort_chars(word)
        # Compute the equivalence classes of those characters.
        eq_class = Util._compute_char_classes(word, order)

        length = 1
        while length < len(word):
            # Sort the double cyclic shifts of the current length.
            order = Util._sort_double_cyclic_shifts(word,
                                                    length,
                                                    order,
                                                    eq_class)
            # Update their equivalence classes.
            eq_class = Util._update_eq_classes(length,
                                               order,
                                               eq_class)
            length *= 2

        # Return the order of all the suffixes of the string if it has '$'
        # in the end.
        return order

    @staticmethod
    def compute_longest_common_prefix_array(word, order):
        """
        Computes the longest common prefix array.
        """

        if len(word) == 0:
            return []

        lcp_array = [ 0 ] * (len(word) - 1)
        lcp = 0
        pos_in_order = Util._invert_suffix_array(order)
        suffix_index = order[0]
        for i in range(0, len(word)):
            order_index = pos_in_order[suffix_index]
            if order_index == len(word) - 1:
                lcp = 0
                suffix_index = (suffix_index + 1) % len(word)

                continue

            next_suffix_index = order[order_index + 1]
            lcp = Util._longest_common_prefix_of_suffixes(word,
                                                          suffix_index,
                                                          next_suffix_index,
                                                          lcp - 1)
            lcp_array[order_index] = lcp
            suffix_index = (suffix_index + 1) % len(word)

        return lcp_array

    @staticmethod
    def pattern_range(text, pattern, suffix_array):
        """
        Finds the range of the first and last occurrences of the given pattern
        in the string.

        The suffix array of a string can be used as an index to quickly locate
        every occurrence of a substring pattern P within the string S. Finding
        every occurrence of the pattern is equivalent to finding every suffix
        that begins with the substring.

        Thanks to the lexicographical ordering, these suffixes will be grouped
        together in the suffix array and can be found efficiently with two
        binary searches. The first search locates the starting position of the
        interval, and the second one determines the end position.

        Note: The end position means that the suffix group ended before it.
        That is, the last occurrence of the given pattern is at pos <= end - 1.
        """

        pattern_length = len(pattern)

        left = 0
        right = len(text)
        while left < right:
            mid = (left + right) // 2
            pos = suffix_array[mid]
            if pattern > text[pos:pos + pattern_length]:
                left = mid + 1
            else:
                right = mid

        start = left

        right = len(text)
        while left < right:
            mid = (left + right) // 2
            pos = suffix_array[mid]
            if pattern < text[pos:pos + pattern_length]:
                right = mid
            else:
                left = mid + 1

        end = right

        return (start, end)

    @staticmethod
    def pattern_matching_with_suffix_array(text, pattern, suffix_array):
        """
        Finds all occurrences of the given pattern in the string.

        Theory:

        Suppose we have a suffix array corresponding to an n-character text and
        we want to find all occurrences in the text of an m-character pattern.
        Since the suffixes are ordered, the easiest solution is to do binary
        search for the first and last occurrences of the pattern (if any) using
        O(log n) comparisons. Unfortunately, each comparison may take as much
        as O(m) time, since we may have to check all m characters of the
        pattern. So the total cost will be O(m log n) in the worst case.

        By storing additional information about the longest common prefix of
        regions of contiguous suffixes, it is possible to avoid having to
        re-examine every character in the pattern for every comparison,
        reducing the search cost to O(m + log n). With a sufficiently clever
        algorithm, this information can be computed in linear time, and can
        also be used to solve quickly such problems as finding the longest
        duplicate substrings, or most frequently occurring strings
        (GusfieldBook §7.14.4).

        Using binary search on the suffix array, most searching tasks are now
        easy:

            - Finding if a substring appears in the array uses binary search
            directly.

            - Finding all occurrences requires two binary searches, one for
            the first occurrence and one for the last. If we only want to count
            the occurrences and not return their positions, this takes
            O(m + log n) time. If we want to return their positions, it takes
            O(m + log n + k) time, where k is the number of times the pattern
            occurs.

            - Finding duplicate substrings of length m or more can be done by
            looking for adjacent entries in the array with long common prefixes,
            which takes O(mn) time in the worst case if done naively (and O(n)
            time if we have already computed longest common prefix information;
            see GusfieldBook).

        Bibliography:

        Dan Gusfield. Algorithms on Strings, Trees, and Sequences: Computer
        Science and Computational Biology. Cambridge University Press, 1997.
        """

        positions = []

        pattern_range = Util.pattern_range(text, pattern, suffix_array)

        low, high = pattern_range

        pattern_length = len(pattern)
        for i in range(low, high):
            pos = suffix_array[i]
            if pattern == text[pos:pos + pattern_length]:
                positions.append(pos)

        return positions
