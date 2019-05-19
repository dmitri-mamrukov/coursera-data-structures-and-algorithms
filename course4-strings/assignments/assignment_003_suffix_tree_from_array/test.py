#!/usr/bin/python3

import functools
import unittest

import suffix_tree_from_array

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

class SolverSolveTestCase(unittest.TestCase):

    def setUp(self):
        self.solver = suffix_tree_from_array.Solver()
        self.solver._input = self.generate_input
        self.solver._output = self.accumulate_output
        self.output_list = []
        self.index = 0

    def tearDown(self):
        pass

    def generate_input(self):
        line = self.input_list[self.index]
        self.index += 1

        return line

    def accumulate_output(self, text):
        return self.output_list.append(text)

    def verify_input(self):
        word = self.input_list[0]
        suffix_array_string = self.input_list[1]
        suffix_lcp_string = self.input_list[2]
        expected_suffix_array = Util.construct_suffix_array(word)
        expected_lcp_array = Util.compute_longest_common_prefix_array(
                                                          word,
                                                          expected_suffix_array)

        self.assertEquals(' '.join(map(str, expected_suffix_array)),
                          suffix_array_string)
        self.assertEquals(' '.join(map(str, expected_lcp_array)),
                          suffix_lcp_string)

    """
    Note that the outputs of some tests don't match those from the official
    ones. But edge strings remain valid. I think this is due to their code that
    builds a suffix tree slightly differently.

    My solution still passed all the official tests.
    """

    def test_case1(self):
        """
        The LCP array contains the longest common prefixes between
        adjacent suffixes in the suffix array of string S.

        A $
        0 1

        Suffixes:

        A$
        $

        Sorted suffixes:

        $
        A$

        index order suffix  lcp
        0     1     $       -
        1     2     A$      0
        """

        self.input_list = [
                              'A$',
                              '1 0',
                              '0',
                          ]
        expected_result = [
                              'A$',
                              '1 2',
                              '0 2',
                          ]

        self.verify_input()

        self.solver.solve()

        self.assertEquals(expected_result, self.output_list)

    def test_case2(self):
        """
        The LCP array contains the longest common prefixes between
        adjacent suffixes in the suffix array of string S.

        A A A $
        0 1 2 3

        Suffixes:

        AAA$
        AA$
        A$
        $

        Sorted suffixes:

        $
        A$
        AA$
        AAA$

        index order suffix lcp
        0     3     $      -
        1     2     A$     0
        2     1     AA$    1
        3     0     AAA$   2
        """

        self.input_list = [
                              'AAA$',
                              '3 2 1 0',
                              '0 1 2',
                          ]
        expected_result = [
                              'AAA$',
                              '3 4',
                              '2 3',
                              '3 4',
                              '2 3',
                              '3 4',
                              '2 4',
                          ]

        self.verify_input()

        self.solver.solve()

        self.assertEquals(expected_result, self.output_list)

    def test_case3(self):
        """
        The LCP array contains the longest common prefixes between
        adjacent suffixes in the suffix array of string S.

        G T A G T $
        0 1 2 3 4 5

        Suffixes:

        GTAGT$
        TAGT$
        AGT$
        GT$
        T$
        $

        Sorted suffixes:

        $
        AGT$
        GT$
        GTAGT$
        T$
        TAGT$

        index order suffix lcp
        0     5     $      -
        1     2     AGT$   0
        2     3     GT$    0
        3     0     GTAGT$ 2
        4     4     T$     0
        5     1     TAGT$  1
        """

        self.input_list = [
                              'GTAGT$',
                              '5 2 3 0 4 1',
                              '0 0 2 0 1',
                          ]
        expected_result = [
                              'GTAGT$',
                              '5 6',
                              '2 6',
                              '3 5',
                              '5 6',
                              '2 6',
                              '4 5',
                              '5 6',
                              '2 6',
                          ]

        self.verify_input()

        self.solver.solve()

        self.assertEquals(expected_result, self.output_list)

    def test_case4(self):
        """
        The LCP array contains the longest common prefixes between
        adjacent suffixes in the suffix array of string S.

        A T A A A T G $
        0 1 2 3 4 5 6 7

        Suffixes:

        ATAAATG$
        TAAATG$
        AAATG$
        AATG$
        ATG$
        TG$
        G$
        $

        Sorted suffixes:

        $
        AAATG$
        AATG$
        ATAAATG$
        ATG$
        G$
        TAAATG$
        TG$

        index order suffix    lcp
        0     7     $         -
        1     2     AAATG$    0
        2     3     AATG$     2
        3     0     ATAAATG$  1
        4     4     ATG$      2
        5     6     G$        0
        6     1     TAAATG$   0
        7     5     TG$       1
        """

        self.input_list = [
                              'ATAAATG$',
                              '7 2 3 0 4 6 1 5',
                              '0 2 1 2 0 0 1',
                          ]
        expected_result = [
                              'ATAAATG$',
                              '7 8',
                              '3 4',
                              '3 4',
                              '4 8',
                              '5 8',
                              '1 2',
                              '2 8',
                              '6 8',
                              '6 8',
                              '1 2',
                              '2 8',
                              '6 8',
                          ]

        self.verify_input()

        self.solver.solve()

        self.assertEquals(expected_result, self.output_list)

if __name__ == '__main__':
    class_names = [
                      SolverSolveTestCase,
                  ]

    suite = unittest.TestSuite()

    for c in class_names:
        suite.addTest(unittest.defaultTestLoader.loadTestsFromTestCase(c))

    unittest.TextTestRunner().run(suite)
