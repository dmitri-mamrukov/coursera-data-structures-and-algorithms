#!/usr/bin/python3

import functools
import io
import sys

class SuffixArrayUtil():

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
    def construct_suffix_array(word):
        """
        Constructs a suffix array from the given word.
        """

        # Sort the index array using the suffix comparison function.
        indices = range(len(word))
        suffix_array = sorted(indices,
                              key=functools.cmp_to_key(lambda i, j:
                                                       SuffixArrayUtil. \
                                                       _suffix_compare(word,
                                                                       i,
                                                                       j)))

        return suffix_array

class BurrowWheelerUtil():

    @staticmethod
    def _cyclic_rotation_character(word, i, n):
        """
        Returns the nth character of the cyclic rotation (to the right)
        by i characters.

        Note: Negative indices mean those from the right end. For example, -1
        references the first element from the end, -2 the second from the end,
        -3 the third from the end, and so on.
        """

        return word[n - i % len(word)]

    @staticmethod
    def _cyclic_compare(word, i, j):
        """
        Compares cyclic rotations without generating the entire rotation.
        """

        length = len(word)
        n = 0
        while n < length:
            i_char = BurrowWheelerUtil._cyclic_rotation_character(word, i, n)
            j_char = BurrowWheelerUtil._cyclic_rotation_character(word, j, n)
            if i_char == j_char:
                n += 1
            else:
                if i_char < j_char:
                    return -1
                else:
                    return 1

        return 0

    @staticmethod
    def _cyclic_sort(word):
        """
        Sorts the cyclic rotations based on their shift.
        """

        length = len(word)
        shifts = range(length)
        return sorted(shifts,
                      key=functools.cmp_to_key(lambda i, j:
                                               BurrowWheelerUtil. \
                                                           _cyclic_compare(word,
                                                                           i,
                                                                           j)))

    @staticmethod
    def _multi_pattern_match(transform_word,
                             first_occurrence,
                             count,
                             pattern,
                             suffix_array):
        """
        Returns the starting index of each occurrence of the pattern in the
        given transform text using a slightly modified version of the Better
        Burrows-Wheeler Transform Matching algorithm.
        """

        top = 0
        bottom = len(transform_word) - 1
        while top <= bottom:
            if pattern != '':
                # The last char in the pattern.
                symbol = pattern[-1]
                # Remove the last char from the pattern.
                pattern = pattern[:-1]
                # Check if the positions from the top to the bottom in the
                # last column (the transform word) contain the symbol.
                if symbol in transform_word[top:bottom + 1]:
                    top = first_occurrence[symbol] + count[top][symbol]
                    bottom = (first_occurrence[symbol] +
                              count[bottom + 1][symbol] - 1)
                else:
                    return []
            else:
                return [suffix_array[i] for i in range(top, bottom + 1)]

    @staticmethod
    def burrows_wheeler_transform(word):
        """
        Collects characters corresponding to the last indices of cyclic
        rotations in the sorted order and returns them as a string.
        """

        cyclic_sort = BurrowWheelerUtil._cyclic_sort(word)
        last_index_chars = [BurrowWheelerUtil._cyclic_rotation_character(word,
                                                                         i,
                                                                         -1)
                            for i in cyclic_sort]
        return ''.join(last_index_chars)

    def get_multi_pattern_count(word, patterns):
        """
        Finds all occurrences of the given collection of patterns in the string.
        """

        transform_word = BurrowWheelerUtil.burrows_wheeler_transform(word)
        suffix_array = SuffixArrayUtil.construct_suffix_array(word)

        symbols = set(transform_word)

        # Create the count map.
        current_count = {}
        for ch in symbols:
            current_count[ch] = 0
        count = { 0: {} }
        for ch in symbols:
            count[0][ch] = current_count[ch]

        for i in range(len(transform_word)):
            current_count[transform_word[i]] += 1
            count[i + 1] = {ch: current_count[ch] for ch in symbols}

        # Get the index of the first occurrence of each character in the
        # sorted Burrows-Wheeler Transform word.
        sorted_transform_word = sorted(transform_word)
        first_occurrence = {}
        for ch in symbols:
            first_occurrence[ch] = sorted_transform_word.index(ch)

        # Perform Burrows-Wheeler Matching on each pattern, using the
        # precomputed information.
        distinct_positions = set()
        for pattern in patterns:
            result = BurrowWheelerUtil._multi_pattern_match(transform_word,
                                                            first_occurrence,
                                                            count,
                                                            pattern,
                                                            suffix_array)
            distinct_positions |= set(result)

        return distinct_positions

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

        text = self._input()
        text += Solver.SYMBOL_DOLLAR
        n = int(self._input())
        patterns = self._input().split()

        result = BurrowWheelerUtil.get_multi_pattern_count(text, patterns)

        self._output(' '.join(map(str, result)))

if __name__ == '__main__':
    Solver().solve()
