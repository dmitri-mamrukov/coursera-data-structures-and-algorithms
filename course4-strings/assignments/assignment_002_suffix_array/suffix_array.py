#!/usr/bin/python3

import collections
import functools
import io
import sys

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

class Solver:
    """
    Constructs a suffix array of a string.
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

    def solve(self):
        """
        Solves the problem.
        """

        text = self._input()

        suffix_array = Util.construct_suffix_array_manber_myers(text)
        string_suffix_array = [str(x) for x in suffix_array]

        self._output(' '.join(string_suffix_array))

if __name__ == '__main__':
    Solver().solve()
