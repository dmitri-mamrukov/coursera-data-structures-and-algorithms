#!/usr/bin/python3

import io
import sys

class SuffixArrayUtil():

    @staticmethod
    def _sort_chars(word, alphabet_map):
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

        return order

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
    def construct_suffix_array(word, alphabet_map):
        """
        Constructs a suffix array from the given word using the count sort
        algorithm.

        Returns the order of the cyclic shifts or the suffixes of the string.

        Note: We assume that the string already has '$' in the end and that '$'
        is smaller than all the characters in the string.
        """

        # Sort the characters (single character cyclic shifts of the string).
        order = SuffixArrayUtil._sort_chars(word, alphabet_map)
        # Compute the equivalence classes of those characters.
        eq_class = SuffixArrayUtil._compute_char_classes(word, order)

        length = 1
        while length < len(word):
            # Sort the double cyclic shifts of the current length.
            order = SuffixArrayUtil._sort_double_cyclic_shifts(word,
                                                               length,
                                                               order,
                                                               eq_class)
            # Update their equivalence classes.
            eq_class = SuffixArrayUtil._update_eq_classes(length,
                                                          order,
                                                          eq_class)
            length *= 2

        # Return the order of all the suffixes of the string if it has '$'
        # in the end.
        return order

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

        pattern_range = SuffixArrayUtil.pattern_range(text,
                                                      pattern,
                                                      suffix_array)

        low, high = pattern_range

        pattern_length = len(pattern)
        for i in range(low, high):
            pos = suffix_array[i]
            if pattern == text[pos:pos + pattern_length]:
                positions.append(pos)

        return positions

class Solver:
    """
    Performs pattern matching with the suffix array a string.

    Output Format: All starting positions (in any order) in Text where a
    pattern appears as a substring (using 0-based indexing as usual).
    If several patterns occur at the same position of the Text, still output
    this position only once.
    """

    SYMBOL_DOLLAR = '$'

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

    def solve(self):
        """
        Solves the problem.
        """

        alphabet_map = { '$': 0, 'A': 1, 'C': 2, 'G': 3, 'T': 4, }

        text = self._input()
        text += Solver.SYMBOL_DOLLAR
        n = int(self._input())
        patterns = self._input().split()

        suffix_array = SuffixArrayUtil.construct_suffix_array(text,
                                                              alphabet_map)

        positions = set()
        for pattern in patterns:
            result = SuffixArrayUtil.pattern_matching_with_suffix_array(
                                                                   text,
                                                                   pattern,
                                                                   suffix_array)
            positions |= set(result)

        self._output(' '.join(map(str, positions)))

if __name__ == '__main__':
    Solver().solve()