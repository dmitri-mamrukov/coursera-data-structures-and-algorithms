#!/usr/bin/python3

import math
import unittest

import trie_util

class TrieUtilBuildTrieTestCase(unittest.TestCase):

    def setUp(self):
        pass

    def tearDown(self):
        pass

    def assert_trie(self, expected_trie, trie):
        self.assertEqual(len(expected_trie), len(trie))
        for node in trie:
            self.assertEqual(len(expected_trie[node]), len(trie[node]))
            for symbol, neighbor in trie[node].items():
                self.assertEqual(expected_trie[node][symbol], neighbor)

    def test_empty_patterns(self):
        patterns = []

        trie = trie_util.TrieUtil.build_trie(patterns)

        expected_trie = { 0: {}, }

        self.assert_trie(expected_trie, trie)

    def test_one_char_pattern(self):
        patterns = [ 'a', ]

        trie = trie_util.TrieUtil.build_trie(patterns)

        expected_trie = { 0: { 'a': (1, True), },
                         1: {}, }

        self.assert_trie(expected_trie, trie)

    def test_two_char_pattern(self):
        patterns = [ 'ab', ]

        trie = trie_util.TrieUtil.build_trie(patterns)

        expected_trie = { 0: { 'a': (1, False), },
                         1: { 'b': (2, True), },
                         2: {}, }

        self.assert_trie(expected_trie, trie)

    def test_three_char_pattern(self):
        patterns = [ 'abc', ]

        trie = trie_util.TrieUtil.build_trie(patterns)

        expected_trie = { 0: { 'a': (1, False), },
                         1: { 'b': (2, False), },
                         2: { 'c': (3, True), },
                         3: {}, }

        self.assert_trie(expected_trie, trie)

    def test_two_patterns(self):
        patterns = [ 'a', 'bc', ]

        trie = trie_util.TrieUtil.build_trie(patterns)

        expected_trie = { 0: { 'a': (1, True), 'b': (2, False), },
                         1: {},
                         2: { 'c': (3, True), },
                         3: {}, }

        self.assert_trie(expected_trie, trie)

    def test_three_patterns(self):
        patterns = [ 'a', 'bc', 'def', ]

        trie = trie_util.TrieUtil.build_trie(patterns)

        expected_trie = { 0: { 'a': (1, True), 'b': (2, False),
                              'd': (4, False), },
                         1: {},
                         2: { 'c': (3, True), },
                         3: {},
                         4: { 'e': (5, False), },
                         5: { 'f': (6, True), },
                         6: {}, }

        self.assert_trie(expected_trie, trie)

    def test_one_branch(self):
        patterns = [ 'ATA', ]

        trie = trie_util.TrieUtil.build_trie(patterns)

        expected_trie = { 0: { 'A': (1, False), },
                         1: { 'T': (2, False), },
                         2: { 'A': (3, True), },
                         3: {}, }

        self.assert_trie(expected_trie, trie)

    def test_two_branches(self):
        patterns = [ 'ATAGA', 'ATC', 'GAT', ]

        trie = trie_util.TrieUtil.build_trie(patterns)

        expected_trie = { 0: { 'A': (1, False), 'G': (7, False), },
                         1: { 'T': (2, False), },
                         2: { 'A': (3, False), 'C': (6, True), },
                         3: { 'G': (4, False), },
                         4: { 'A': (5, True), },
                         5: {},
                         6: {},
                         7: { 'A': (8, False), },
                         8: { 'T': (9, True), },
                         9: {}, }

        self.assert_trie(expected_trie, trie)

    def test_three_branches(self):
        patterns = [ 'AT', 'AG', 'AC', ]

        trie = trie_util.TrieUtil.build_trie(patterns)

        expected_trie = { 0: { 'A': (1, False), },
                         1: { 'T': (2, True), 'G': (3, True),
                             'C': (4, True), },
                         2: {},
                         3: {},
                         4: {}, }

        self.assert_trie(expected_trie, trie)

    def test_common_prefixes_a_ab_abc(self):
        patterns = [ 'A', 'AB', 'ABC', ]

        trie = trie_util.TrieUtil.build_trie(patterns)

        expected_trie = { 0: { 'A': (1, True), },
                         1: { 'B': (2, True), },
                         2: { 'C': (3, True), },
                         3: {}, }

        self.assert_trie(expected_trie, trie)

    def test_common_prefixes_a_abc_ab(self):
        patterns = [ 'A', 'ABC', 'AB', ]

        trie = trie_util.TrieUtil.build_trie(patterns)

        expected_trie = { 0: { 'A': (1, True), },
                         1: { 'B': (2, True), },
                         2: { 'C': (3, True), },
                         3: {}, }

        self.assert_trie(expected_trie, trie)

    def test_common_prefixes_ab_a_abc(self):
        patterns = [ 'AB', 'A', 'ABC', ]

        trie = trie_util.TrieUtil.build_trie(patterns)

        expected_trie = { 0: { 'A': (1, True), },
                         1: { 'B': (2, True), },
                         2: { 'C': (3, True), },
                         3: {}, }

        self.assert_trie(expected_trie, trie)

    def test_common_prefixes_ab_abc_a(self):
        patterns = [ 'AB', 'ABC', 'A', ]

        trie = trie_util.TrieUtil.build_trie(patterns)

        expected_trie = { 0: { 'A': (1, True), },
                         1: { 'B': (2, True), },
                         2: { 'C': (3, True), },
                         3: {}, }

        self.assert_trie(expected_trie, trie)

    def test_common_prefixes_abc_a_ab(self):
        patterns = [ 'ABC', 'A', 'AB', ]

        trie = trie_util.TrieUtil.build_trie(patterns)

        expected_trie = { 0: { 'A': (1, True), },
                         1: { 'B': (2, True), },
                         2: { 'C': (3, True), },
                         3: {}, }

        self.assert_trie(expected_trie, trie)

    def test_common_prefixes_abc_ab_a(self):
        patterns = [ 'ABC', 'AB', 'A', ]

        trie = trie_util.TrieUtil.build_trie(patterns)

        expected_trie = { 0: { 'A': (1, True), },
                         1: { 'B': (2, True), },
                         2: { 'C': (3, True), },
                         3: {}, }

        self.assert_trie(expected_trie, trie)

    def test_common_prefixes_abc_ab_a_xy(self):
        patterns = [ 'ABC', 'AB', 'A', 'XY', ]

        trie = trie_util.TrieUtil.build_trie(patterns)

        expected_trie = { 0: { 'A': (1, True), 'X': (4, False), },
                         1: { 'B': (2, True), },
                         2: { 'C': (3, True), },
                         3: {},
                         4: { 'Y': (5, True), },
                         5: {}, }

        self.assert_trie(expected_trie, trie)

class TrieUtilPrefixTrieMatchingTestCase(unittest.TestCase):

    def setUp(self):
        pass

    def tearDown(self):
        pass

    def test_empty_and_empty(self):
        patterns = []
        text = ''

        trie = trie_util.TrieUtil.build_trie(patterns)
        result = trie_util.TrieUtil.prefix_trie_matching(text, trie)

        self.assertEquals('', result)

    def test_empty_and_a(self):
        patterns = []
        text = 'a'

        trie = trie_util.TrieUtil.build_trie(patterns)
        result = trie_util.TrieUtil.prefix_trie_matching(text, trie)

        self.assertEquals('', result)

    def test_empty_and_ab(self):
        patterns = []
        text = 'ab'

        trie = trie_util.TrieUtil.build_trie(patterns)
        result = trie_util.TrieUtil.prefix_trie_matching(text, trie)

        self.assertEquals('', result)

    def test_empty_and_abc(self):
        patterns = []
        text = 'abc'

        trie = trie_util.TrieUtil.build_trie(patterns)
        result = trie_util.TrieUtil.prefix_trie_matching(text, trie)

        self.assertEquals('', result)

    def test_a_and_empty(self):
        patterns = [ 'a', ]
        text = ''

        trie = trie_util.TrieUtil.build_trie(patterns)
        result = trie_util.TrieUtil.prefix_trie_matching(text, trie)

        self.assertEquals('', result)

    def test_a_and_a(self):
        patterns = [ 'a', ]
        text = 'a'

        trie = trie_util.TrieUtil.build_trie(patterns)
        result = trie_util.TrieUtil.prefix_trie_matching(text, trie)

        self.assertEquals('a', result)

    def test_a_and_ab(self):
        patterns = [ 'a', ]
        text = 'ab'

        trie = trie_util.TrieUtil.build_trie(patterns)
        result = trie_util.TrieUtil.prefix_trie_matching(text, trie)

        self.assertEquals('a', result)

    def test_a_and_abc(self):
        patterns = [ 'a', ]
        text = 'abc'

        trie = trie_util.TrieUtil.build_trie(patterns)
        result = trie_util.TrieUtil.prefix_trie_matching(text, trie)

        self.assertEquals('a', result)

    def test_a_and_x(self):
        patterns = [ 'a', ]
        text = 'x'

        trie = trie_util.TrieUtil.build_trie(patterns)
        result = trie_util.TrieUtil.prefix_trie_matching(text, trie)

        self.assertEquals('', result)

    def test_a_and_xy(self):
        patterns = [ 'a', ]
        text = 'xy'

        trie = trie_util.TrieUtil.build_trie(patterns)
        result = trie_util.TrieUtil.prefix_trie_matching(text, trie)

        self.assertEquals('', result)

    def test_a_and_xyz(self):
        patterns = [ 'a', ]
        text = 'xyz'

        trie = trie_util.TrieUtil.build_trie(patterns)
        result = trie_util.TrieUtil.prefix_trie_matching(text, trie)

        self.assertEquals('', result)

    def test_ab_and_empty(self):
        patterns = [ 'ab', ]
        text = ''

        trie = trie_util.TrieUtil.build_trie(patterns)
        result = trie_util.TrieUtil.prefix_trie_matching(text, trie)

        self.assertEquals('', result)

    def test_ab_and_a(self):
        patterns = [ 'ab', ]
        text = 'a'

        trie = trie_util.TrieUtil.build_trie(patterns)
        result = trie_util.TrieUtil.prefix_trie_matching(text, trie)

        self.assertEquals('', result)

    def test_ab_and_ab(self):
        patterns = [ 'ab', ]
        text = 'ab'

        trie = trie_util.TrieUtil.build_trie(patterns)
        result = trie_util.TrieUtil.prefix_trie_matching(text, trie)

        self.assertEquals('ab', result)

    def test_ab_and_abc(self):
        patterns = [ 'ab', ]
        text = 'abc'

        trie = trie_util.TrieUtil.build_trie(patterns)
        result = trie_util.TrieUtil.prefix_trie_matching(text, trie)

        self.assertEquals('ab', result)

    def test_ab_and_x(self):
        patterns = [ 'ab', ]
        text = 'x'

        trie = trie_util.TrieUtil.build_trie(patterns)
        result = trie_util.TrieUtil.prefix_trie_matching(text, trie)

        self.assertEquals('', result)

    def test_ab_and_xy(self):
        patterns = [ 'ab', ]
        text = 'xy'

        trie = trie_util.TrieUtil.build_trie(patterns)
        result = trie_util.TrieUtil.prefix_trie_matching(text, trie)

        self.assertEquals('', result)

    def test_ab_and_xyz(self):
        patterns = [ 'ab', ]
        text = 'xyz'

        trie = trie_util.TrieUtil.build_trie(patterns)
        result = trie_util.TrieUtil.prefix_trie_matching(text, trie)

        self.assertEquals('', result)

    def test_abc_and_empty(self):
        patterns = [ 'abc', ]
        text = ''

        trie = trie_util.TrieUtil.build_trie(patterns)
        result = trie_util.TrieUtil.prefix_trie_matching(text, trie)

        self.assertEquals('', result)

    def test_abc_and_a(self):
        patterns = [ 'abc', ]
        text = 'a'

        trie = trie_util.TrieUtil.build_trie(patterns)
        result = trie_util.TrieUtil.prefix_trie_matching(text, trie)

        self.assertEquals('', result)

    def test_abc_and_ab(self):
        patterns = [ 'abc', ]
        text = 'ab'

        trie = trie_util.TrieUtil.build_trie(patterns)
        result = trie_util.TrieUtil.prefix_trie_matching(text, trie)

        self.assertEquals('', result)

    def test_abc_and_abc(self):
        patterns = [ 'abc', ]
        text = 'abc'

        trie = trie_util.TrieUtil.build_trie(patterns)
        result = trie_util.TrieUtil.prefix_trie_matching(text, trie)

        self.assertEquals('abc', result)

    def test_abc_and_x(self):
        patterns = [ 'abc', ]
        text = 'x'

        trie = trie_util.TrieUtil.build_trie(patterns)
        result = trie_util.TrieUtil.prefix_trie_matching(text, trie)

        self.assertEquals('', result)

    def test_abc_and_xy(self):
        patterns = [ 'abc', ]
        text = 'xy'

        trie = trie_util.TrieUtil.build_trie(patterns)
        result = trie_util.TrieUtil.prefix_trie_matching(text, trie)

        self.assertEquals('', result)

    def test_abc_and_xyz(self):
        patterns = [ 'abc', ]
        text = 'xyz'

        trie = trie_util.TrieUtil.build_trie(patterns)
        result = trie_util.TrieUtil.prefix_trie_matching(text, trie)

        self.assertEquals('', result)

    def test_a_x_and_empty(self):
        patterns = [ 'a', 'x', ]
        text = ''

        trie = trie_util.TrieUtil.build_trie(patterns)
        result = trie_util.TrieUtil.prefix_trie_matching(text, trie)

        self.assertEquals('', result)

    def test_a_x_and_a(self):
        patterns = [ 'a', 'x', ]
        text = 'a'

        trie = trie_util.TrieUtil.build_trie(patterns)
        result = trie_util.TrieUtil.prefix_trie_matching(text, trie)

        self.assertEquals('a', result)

    def test_a_x_and_ab(self):
        patterns = [ 'a', 'x', ]
        text = 'ab'

        trie = trie_util.TrieUtil.build_trie(patterns)
        result = trie_util.TrieUtil.prefix_trie_matching(text, trie)

        self.assertEquals('a', result)

    def test_a_x_and_abc(self):
        patterns = [ 'a', 'x', ]
        text = 'abc'

        trie = trie_util.TrieUtil.build_trie(patterns)
        result = trie_util.TrieUtil.prefix_trie_matching(text, trie)

        self.assertEquals('a', result)

    def test_a_x_and_x(self):
        patterns = [ 'a', 'x', ]
        text = 'x'

        trie = trie_util.TrieUtil.build_trie(patterns)
        result = trie_util.TrieUtil.prefix_trie_matching(text, trie)

        self.assertEquals('x', result)

    def test_a_x_and_xy(self):
        patterns = [ 'a', 'x', ]
        text = 'xy'

        trie = trie_util.TrieUtil.build_trie(patterns)
        result = trie_util.TrieUtil.prefix_trie_matching(text, trie)

        self.assertEquals('x', result)

    def test_a_x_and_xyz(self):
        patterns = [ 'a', 'x', ]
        text = 'xyz'

        trie = trie_util.TrieUtil.build_trie(patterns)
        result = trie_util.TrieUtil.prefix_trie_matching(text, trie)

        self.assertEquals('x', result)

    def test_ab_xy_and_empty(self):
        patterns = [ 'ab', 'xy', ]
        text = ''

        trie = trie_util.TrieUtil.build_trie(patterns)
        result = trie_util.TrieUtil.prefix_trie_matching(text, trie)

        self.assertEquals('', result)

    def test_ab_xy_and_a(self):
        patterns = [ 'ab', 'xy', ]
        text = 'a'

        trie = trie_util.TrieUtil.build_trie(patterns)
        result = trie_util.TrieUtil.prefix_trie_matching(text, trie)

        self.assertEquals('', result)

    def test_ab_xy_and_ab(self):
        patterns = [ 'ab', 'xy', ]
        text = 'ab'

        trie = trie_util.TrieUtil.build_trie(patterns)
        result = trie_util.TrieUtil.prefix_trie_matching(text, trie)

        self.assertEquals('ab', result)

    def test_ab_xy_and_abc(self):
        patterns = [ 'ab', 'xy', ]
        text = 'abc'

        trie = trie_util.TrieUtil.build_trie(patterns)
        result = trie_util.TrieUtil.prefix_trie_matching(text, trie)

        self.assertEquals('ab', result)

    def test_ab_xy_and_x(self):
        patterns = [ 'ab', 'xy', ]
        text = 'x'

        trie = trie_util.TrieUtil.build_trie(patterns)
        result = trie_util.TrieUtil.prefix_trie_matching(text, trie)

        self.assertEquals('', result)

    def test_ab_xy_and_xy(self):
        patterns = [ 'ab', 'xy', ]
        text = 'xy'

        trie = trie_util.TrieUtil.build_trie(patterns)
        result = trie_util.TrieUtil.prefix_trie_matching(text, trie)

        self.assertEquals('xy', result)

    def test_ab_xy_and_xyz(self):
        patterns = [ 'ab', 'xy', ]
        text = 'xyz'

        trie = trie_util.TrieUtil.build_trie(patterns)
        result = trie_util.TrieUtil.prefix_trie_matching(text, trie)

        self.assertEquals('xy', result)

    def test_abc_xyz_and_empty(self):
        patterns = [ 'abc', 'xyz', ]
        text = ''

        trie = trie_util.TrieUtil.build_trie(patterns)
        result = trie_util.TrieUtil.prefix_trie_matching(text, trie)

        self.assertEquals('', result)

    def test_abc_xyz_and_a(self):
        patterns = [ 'abc', 'xyz', ]
        text = 'a'

        trie = trie_util.TrieUtil.build_trie(patterns)
        result = trie_util.TrieUtil.prefix_trie_matching(text, trie)

        self.assertEquals('', result)

    def test_abc_xyz_and_ab(self):
        patterns = [ 'abc', 'xyz', ]
        text = 'ab'

        trie = trie_util.TrieUtil.build_trie(patterns)
        result = trie_util.TrieUtil.prefix_trie_matching(text, trie)

        self.assertEquals('', result)

    def test_abc_xyz_and_abc(self):
        patterns = [ 'abc', 'xyz', ]
        text = 'abc'

        trie = trie_util.TrieUtil.build_trie(patterns)
        result = trie_util.TrieUtil.prefix_trie_matching(text, trie)

        self.assertEquals('abc', result)

    def test_abc_xyz_and_x(self):
        patterns = [ 'abc', 'xyz', ]
        text = 'x'

        trie = trie_util.TrieUtil.build_trie(patterns)
        result = trie_util.TrieUtil.prefix_trie_matching(text, trie)

        self.assertEquals('', result)

    def test_abc_xyz_and_xy(self):
        patterns = [ 'abc', 'xyz', ]
        text = 'xy'

        trie = trie_util.TrieUtil.build_trie(patterns)
        result = trie_util.TrieUtil.prefix_trie_matching(text, trie)

        self.assertEquals('', result)

    def test_abc_xyz_and_xyz(self):
        patterns = [ 'abc', 'xyz', ]
        text = 'xyz'

        trie = trie_util.TrieUtil.build_trie(patterns)
        result = trie_util.TrieUtil.prefix_trie_matching(text, trie)

        self.assertEquals('xyz', result)

    def test_aa_and_a(self):
        patterns = [ 'aa', ]
        text = 'a'

        trie = trie_util.TrieUtil.build_trie(patterns)
        result = trie_util.TrieUtil.prefix_trie_matching(text, trie)

        self.assertEquals('', result)

    def test_aa_and_aa(self):
        patterns = [ 'aa', ]
        text = 'aa'

        trie = trie_util.TrieUtil.build_trie(patterns)
        result = trie_util.TrieUtil.prefix_trie_matching(text, trie)

        self.assertEquals('aa', result)

    def test_at_a_ag_and_acata(self):
        patterns = [ 'AT', 'A', 'AG', ]
        text = 'ACATA'

        trie = trie_util.TrieUtil.build_trie(patterns)
        result = trie_util.TrieUtil.prefix_trie_matching(text, trie)

        self.assertEquals('A', result)

class TrieUtilTrieMatchingTestCase(unittest.TestCase):

    def setUp(self):
        pass

    def tearDown(self):
        pass

    def test_empty_and_empty(self):
        patterns = []
        text = ''

        trie = trie_util.TrieUtil.build_trie(patterns)
        result = trie_util.TrieUtil.trie_matching(text, trie)

        self.assertEquals([], result)

    def test_empty_and_a(self):
        patterns = []
        text = 'a'

        trie = trie_util.TrieUtil.build_trie(patterns)
        result = trie_util.TrieUtil.trie_matching(text, trie)

        self.assertEquals([], result)

    def test_empty_and_ab(self):
        patterns = []
        text = 'ab'

        trie = trie_util.TrieUtil.build_trie(patterns)
        result = trie_util.TrieUtil.trie_matching(text, trie)

        self.assertEquals([], result)

    def test_empty_and_abc(self):
        patterns = []
        text = 'abc'

        trie = trie_util.TrieUtil.build_trie(patterns)
        result = trie_util.TrieUtil.trie_matching(text, trie)

        self.assertEquals([], result)

    def test_a_and_empty(self):
        patterns = [ 'a', ]
        text = ''

        trie = trie_util.TrieUtil.build_trie(patterns)
        result = trie_util.TrieUtil.trie_matching(text, trie)

        self.assertEquals([], result)

    def test_a_and_a(self):
        patterns = [ 'a', ]
        text = 'a'

        trie = trie_util.TrieUtil.build_trie(patterns)
        result = trie_util.TrieUtil.trie_matching(text, trie)

        self.assertEquals([ 0 ], result)

    def test_a_and_ab(self):
        patterns = [ 'a', ]
        text = 'ab'

        trie = trie_util.TrieUtil.build_trie(patterns)
        result = trie_util.TrieUtil.trie_matching(text, trie)

        self.assertEquals([ 0 ], result)

    def test_a_and_abc(self):
        patterns = [ 'a', ]
        text = 'abc'

        trie = trie_util.TrieUtil.build_trie(patterns)
        result = trie_util.TrieUtil.trie_matching(text, trie)

        self.assertEquals([ 0 ], result)

    def test_a_and_x(self):
        patterns = [ 'a', ]
        text = 'x'

        trie = trie_util.TrieUtil.build_trie(patterns)
        result = trie_util.TrieUtil.trie_matching(text, trie)

        self.assertEquals([], result)

    def test_a_and_xy(self):
        patterns = [ 'a', ]
        text = 'xy'

        trie = trie_util.TrieUtil.build_trie(patterns)
        result = trie_util.TrieUtil.trie_matching(text, trie)

        self.assertEquals([], result)

    def test_a_and_xyz(self):
        patterns = [ 'a', ]
        text = 'xyz'

        trie = trie_util.TrieUtil.build_trie(patterns)
        result = trie_util.TrieUtil.trie_matching(text, trie)

        self.assertEquals([], result)

    def test_ab_and_empty(self):
        patterns = [ 'ab', ]
        text = ''

        trie = trie_util.TrieUtil.build_trie(patterns)
        result = trie_util.TrieUtil.trie_matching(text, trie)

        self.assertEquals([], result)

    def test_ab_and_a(self):
        patterns = [ 'ab', ]
        text = 'a'

        trie = trie_util.TrieUtil.build_trie(patterns)
        result = trie_util.TrieUtil.trie_matching(text, trie)

        self.assertEquals([], result)

    def test_ab_and_ab(self):
        patterns = [ 'ab', ]
        text = 'ab'

        trie = trie_util.TrieUtil.build_trie(patterns)
        result = trie_util.TrieUtil.trie_matching(text, trie)

        self.assertEquals([ 0 ], result)

    def test_ab_and_abc(self):
        patterns = [ 'ab', ]
        text = 'abc'

        trie = trie_util.TrieUtil.build_trie(patterns)
        result = trie_util.TrieUtil.trie_matching(text, trie)

        self.assertEquals([ 0 ], result)

    def test_ab_and_x(self):
        patterns = [ 'ab', ]
        text = 'x'

        trie = trie_util.TrieUtil.build_trie(patterns)
        result = trie_util.TrieUtil.trie_matching(text, trie)

        self.assertEquals([], result)

    def test_ab_and_xy(self):
        patterns = [ 'ab', ]
        text = 'xy'

        trie = trie_util.TrieUtil.build_trie(patterns)
        result = trie_util.TrieUtil.trie_matching(text, trie)

        self.assertEquals([], result)

    def test_ab_and_xyz(self):
        patterns = [ 'ab', ]
        text = 'xyz'

        trie = trie_util.TrieUtil.build_trie(patterns)
        result = trie_util.TrieUtil.trie_matching(text, trie)

        self.assertEquals([], result)

    def test_abc_and_empty(self):
        patterns = [ 'abc', ]
        text = ''

        trie = trie_util.TrieUtil.build_trie(patterns)
        result = trie_util.TrieUtil.trie_matching(text, trie)

        self.assertEquals([], result)

    def test_abc_and_a(self):
        patterns = [ 'abc', ]
        text = 'a'

        trie = trie_util.TrieUtil.build_trie(patterns)
        result = trie_util.TrieUtil.trie_matching(text, trie)

        self.assertEquals([], result)

    def test_abc_and_ab(self):
        patterns = [ 'abc', ]
        text = 'ab'

        trie = trie_util.TrieUtil.build_trie(patterns)
        result = trie_util.TrieUtil.trie_matching(text, trie)

        self.assertEquals([], result)

    def test_abc_and_abc(self):
        patterns = [ 'abc', ]
        text = 'abc'

        trie = trie_util.TrieUtil.build_trie(patterns)
        result = trie_util.TrieUtil.trie_matching(text, trie)

        self.assertEquals([ 0 ], result)

    def test_abc_and_x(self):
        patterns = [ 'abc', ]
        text = 'x'

        trie = trie_util.TrieUtil.build_trie(patterns)
        result = trie_util.TrieUtil.trie_matching(text, trie)

        self.assertEquals([], result)

    def test_abc_and_xy(self):
        patterns = [ 'abc', ]
        text = 'xy'

        trie = trie_util.TrieUtil.build_trie(patterns)
        result = trie_util.TrieUtil.trie_matching(text, trie)

        self.assertEquals([], result)

    def test_abc_and_xyz(self):
        patterns = [ 'abc', ]
        text = 'xyz'

        trie = trie_util.TrieUtil.build_trie(patterns)
        result = trie_util.TrieUtil.trie_matching(text, trie)

        self.assertEquals([], result)

    def test_a_x_and_empty(self):
        patterns = [ 'a', 'x', ]
        text = ''

        trie = trie_util.TrieUtil.build_trie(patterns)
        result = trie_util.TrieUtil.trie_matching(text, trie)

        self.assertEquals([], result)

    def test_a_x_and_a(self):
        patterns = [ 'a', 'x', ]
        text = 'a'

        trie = trie_util.TrieUtil.build_trie(patterns)
        result = trie_util.TrieUtil.trie_matching(text, trie)

        self.assertEquals([ 0 ], result)

    def test_a_x_and_ab(self):
        patterns = [ 'a', 'x', ]
        text = 'ab'

        trie = trie_util.TrieUtil.build_trie(patterns)
        result = trie_util.TrieUtil.trie_matching(text, trie)

        self.assertEquals([ 0 ], result)

    def test_a_x_and_abc(self):
        patterns = [ 'a', 'x', ]
        text = 'abc'

        trie = trie_util.TrieUtil.build_trie(patterns)
        result = trie_util.TrieUtil.trie_matching(text, trie)

        self.assertEquals([ 0 ], result)

    def test_a_x_and_x(self):
        patterns = [ 'a', 'x', ]
        text = 'x'

        trie = trie_util.TrieUtil.build_trie(patterns)
        result = trie_util.TrieUtil.trie_matching(text, trie)

        self.assertEquals([ 0 ], result)

    def test_a_x_and_xy(self):
        patterns = [ 'a', 'x', ]
        text = 'xy'

        trie = trie_util.TrieUtil.build_trie(patterns)
        result = trie_util.TrieUtil.trie_matching(text, trie)

        self.assertEquals([ 0 ], result)

    def test_a_x_and_xyz(self):
        patterns = [ 'a', 'x', ]
        text = 'xyz'

        trie = trie_util.TrieUtil.build_trie(patterns)
        result = trie_util.TrieUtil.trie_matching(text, trie)

        self.assertEquals([ 0 ], result)

    def test_ab_xy_and_empty(self):
        patterns = [ 'ab', 'xy', ]
        text = ''

        trie = trie_util.TrieUtil.build_trie(patterns)
        result = trie_util.TrieUtil.trie_matching(text, trie)

        self.assertEquals([], result)

    def test_ab_xy_and_a(self):
        patterns = [ 'ab', 'xy', ]
        text = 'a'

        trie = trie_util.TrieUtil.build_trie(patterns)
        result = trie_util.TrieUtil.trie_matching(text, trie)

        self.assertEquals([], result)

    def test_ab_xy_and_ab(self):
        patterns = [ 'ab', 'xy', ]
        text = 'ab'

        trie = trie_util.TrieUtil.build_trie(patterns)
        result = trie_util.TrieUtil.trie_matching(text, trie)

        self.assertEquals([ 0 ], result)

    def test_ab_xy_and_abc(self):
        patterns = [ 'ab', 'xy', ]
        text = 'abc'

        trie = trie_util.TrieUtil.build_trie(patterns)
        result = trie_util.TrieUtil.trie_matching(text, trie)

        self.assertEquals([ 0 ], result)

    def test_ab_xy_and_x(self):
        patterns = [ 'ab', 'xy', ]
        text = 'x'

        trie = trie_util.TrieUtil.build_trie(patterns)
        result = trie_util.TrieUtil.trie_matching(text, trie)

        self.assertEquals([], result)

    def test_ab_xy_and_xy(self):
        patterns = [ 'ab', 'xy', ]
        text = 'xy'

        trie = trie_util.TrieUtil.build_trie(patterns)
        result = trie_util.TrieUtil.trie_matching(text, trie)

        self.assertEquals([ 0 ], result)

    def test_ab_xy_and_xyz(self):
        patterns = [ 'ab', 'xy', ]
        text = 'xyz'

        trie = trie_util.TrieUtil.build_trie(patterns)
        result = trie_util.TrieUtil.trie_matching(text, trie)

        self.assertEquals([ 0 ], result)

    def test_abc_xyz_and_empty(self):
        patterns = [ 'abc', 'xyz', ]
        text = ''

        trie = trie_util.TrieUtil.build_trie(patterns)
        result = trie_util.TrieUtil.trie_matching(text, trie)

        self.assertEquals([], result)

    def test_abc_xyz_and_a(self):
        patterns = [ 'abc', 'xyz', ]
        text = 'a'

        trie = trie_util.TrieUtil.build_trie(patterns)
        result = trie_util.TrieUtil.trie_matching(text, trie)

        self.assertEquals([], result)

    def test_abc_xyz_and_ab(self):
        patterns = [ 'abc', 'xyz', ]
        text = 'ab'

        trie = trie_util.TrieUtil.build_trie(patterns)
        result = trie_util.TrieUtil.trie_matching(text, trie)

        self.assertEquals([], result)

    def test_abc_xyz_and_abc(self):
        patterns = [ 'abc', 'xyz', ]
        text = 'abc'

        trie = trie_util.TrieUtil.build_trie(patterns)
        result = trie_util.TrieUtil.trie_matching(text, trie)

        self.assertEquals([ 0 ], result)

    def test_abc_xyz_and_x(self):
        patterns = [ 'abc', 'xyz', ]
        text = 'x'

        trie = trie_util.TrieUtil.build_trie(patterns)
        result = trie_util.TrieUtil.trie_matching(text, trie)

        self.assertEquals([], result)

    def test_abc_xyz_and_xy(self):
        patterns = [ 'abc', 'xyz', ]
        text = 'xy'

        trie = trie_util.TrieUtil.build_trie(patterns)
        result = trie_util.TrieUtil.trie_matching(text, trie)

        self.assertEquals([], result)

    def test_abc_xyz_and_xyz(self):
        patterns = [ 'abc', 'xyz', ]
        text = 'xyz'

        trie = trie_util.TrieUtil.build_trie(patterns)
        result = trie_util.TrieUtil.trie_matching(text, trie)

        self.assertEquals([ 0 ], result)

    def test_aa_and_a(self):
        patterns = [ 'aa', ]
        text = 'a'

        trie = trie_util.TrieUtil.build_trie(patterns)
        result = trie_util.TrieUtil.trie_matching(text, trie)

        self.assertEquals([], result)

    def test_aa_and_a(self):
        patterns = [ 'aa', ]
        text = 'aa'

        trie = trie_util.TrieUtil.build_trie(patterns)
        result = trie_util.TrieUtil.trie_matching(text, trie)

        self.assertEquals([ 0 ], result)

    def test_aa_and_aaa(self):
        patterns = [ 'aa', ]
        text = 'aaa'

        trie = trie_util.TrieUtil.build_trie(patterns)
        result = trie_util.TrieUtil.trie_matching(text, trie)

        self.assertEquals([ 0, 1 ], result)

    def test_aa_and_aaaa(self):
        patterns = [ 'aa', ]
        text = 'aaaa'

        trie = trie_util.TrieUtil.build_trie(patterns)
        result = trie_util.TrieUtil.trie_matching(text, trie)

        self.assertEquals([ 0, 1, 2 ], result)

    def test_an_and_bananas(self):
        patterns = [ 'an', ]
        text = 'bananas'

        trie = trie_util.TrieUtil.build_trie(patterns)
        result = trie_util.TrieUtil.trie_matching(text, trie)

        self.assertEquals([ 1, 3 ], result)

    def test_na_and_bananas(self):
        patterns = [ 'na', ]
        text = 'bananas'

        trie = trie_util.TrieUtil.build_trie(patterns)
        result = trie_util.TrieUtil.trie_matching(text, trie)

        self.assertEquals([ 2, 4 ], result)

    def test_patterns_and_panamabananas(self):
        patterns = [ 'banana', 'pan', 'and', 'nab', 'antenna', 'bandana',
                    'ananas', 'nana' ]
        text = 'panamabananas'

        trie = trie_util.TrieUtil.build_trie(patterns)
        result = trie_util.TrieUtil.trie_matching(text, trie)

        self.assertEquals([ 0, 6, 7, 8 ], result)

    def test_at_a_ag_and_acata(self):
        patterns = [ 'AT', 'A', 'AG', ]
        text = 'ACATA'

        trie = trie_util.TrieUtil.build_trie(patterns)
        result = trie_util.TrieUtil.trie_matching(text, trie)

        self.assertEquals([ 0, 2, 4 ], result)

class TrieUtilBuildSuffixTrieTestCase(unittest.TestCase):

    def setUp(self):
        pass

    def tearDown(self):
        pass

    def assert_trie(self, expected_trie, trie):
        self.assertEqual(len(expected_trie), len(trie))
        for node in trie:
            self.assertEqual(len(expected_trie[node]), len(trie[node]))
            for symbol, neighbor in trie[node].items():
                self.assertEqual(expected_trie[node][symbol], neighbor)

    def test_empty_text(self):
        text = '$'

        trie = trie_util.TrieUtil.build_suffix_trie(text)

        expected_trie = { 0: { '$': (1, True), },
                         1: {} }

        self.assert_trie(expected_trie, trie)

    def test_a(self):
        text = 'a$'

        trie = trie_util.TrieUtil.build_suffix_trie(text)

        expected_trie = { 0: { 'a': (1, False), '$': (3, True), },
                         1: { '$': (2, True), },
                         2: {},
                         3: {}, }

        self.assert_trie(expected_trie, trie)

    def test_ab(self):
        text = 'ab$'

        trie = trie_util.TrieUtil.build_suffix_trie(text)

        expected_trie = { 0: { 'a': (1, False), 'b': (4, False),
                              '$': (6, True), },
                         1: { 'b': (2, False), },
                         2: { '$': (3, True), },
                         3: {},
                         4: { '$': (5, True), },
                         5: {},
                         6: {}, }

        self.assert_trie(expected_trie, trie)

    def test_abac(self):
        text = 'abac$'

        trie = trie_util.TrieUtil.build_suffix_trie(text)

        expected_trie = { 0: { 'a': (1, False), 'b': (6, False),
                              'c': (12, False), '$': (14, True), },
                         1: { 'b': (2, False), 'c': (10, False), },
                         2: { 'a': (3, False), },
                         3: { 'c': (4, False), },
                         4: { '$': (5, True), },
                         5: {},
                         6: { 'a': (7, False), },
                         7: { 'c': (8, False), },
                         8: { '$': (9, True), },
                         9: {},
                         10: { '$': (11, True), },
                         11: {},
                         12: { '$': (13, True), },
                         13: {},
                         14: {}, }

        self.assert_trie(expected_trie, trie)

    def test_abab(self):
        text = 'abab$'

        trie = trie_util.TrieUtil.build_suffix_trie(text)

        expected_trie = { 0: { 'a': (1, False), 'b': (6, False),
                              '$': (12, True), },
                         1: { 'b': (2, False), },
                         2: { 'a': (3, False), '$': (10, True), },
                         3: { 'b': (4, False), },
                         4: { '$': (5, True), },
                         5: {},
                         6: { 'a': (7, False), '$': (11, True), },
                         7: { 'b': (8, False), },
                         8: { '$': (9, True), },
                         9: {},
                         10: {},
                         11: {},
                         12: {}, }

        self.assert_trie(expected_trie, trie)

    def test_aca(self):
        text = 'aca$'

        trie = trie_util.TrieUtil.build_suffix_trie(text)

        expected_trie = { 0: { 'a': (1, False), 'c': (5, False),
                              '$': (9, True), },
                         1: { 'c': (2, False), '$': (8, True), },
                         2: { 'a': (3, False), },
                         3: { '$': (4, True), },
                         4: {},
                         5: { 'a': (6, False), },
                         6: { '$': (7, True), },
                         7: {},
                         8: {},
                         9: {}, }

        self.assert_trie(expected_trie, trie)

    def test_ataaatg(self):
        text = 'ataaatg$'

        trie = trie_util.TrieUtil.build_suffix_trie(text)

        expected_trie = { 0: { 'a': (1, False), 't': (9, False),
                              'g': (28, False), '$': (30, True), },
                         1: { 't': (2, False), 'a': (16, False), },
                         2: { 'a': (3, False), 'g': (24, False), },
                         3: { 'a': (4, False), },
                         4: { 'a': (5, False), },
                         5: { 't': (6, False), },
                         6: { 'g': (7, False), },
                         7: { '$': (8, True), },
                         8: {},
                         9: { 'a': (10, False), 'g': (26, False), },
                         10: { 'a': (11, False), },
                         11: { 'a': (12, False), },
                         12: { 't': (13, False), },
                         13: { 'g': (14, False), },
                         14: { '$': (15, True), },
                         15: {},
                         16: { 'a': (17, False), 't': (21, False), },
                         17: { 't': (18, False), },
                         18: { 'g': (19, False), },
                         19: { '$': (20, True), },
                         20: {},
                         21: { 'g': (22, False), },
                         22: { '$': (23, True), },
                         23: {},
                         24: { '$': (25, True), },
                         25: {},
                         26: { '$': (27, True), },
                         27: {},
                         28: { '$': (29, True), },
                         29: {},
                         30: {}, }

        self.assert_trie(expected_trie, trie)

    def test_panamabananas(self):
        text = 'panamabananas$'

        trie = trie_util.TrieUtil.build_suffix_trie(text)

        expected_trie = { 0: { 'p': (1, False), 'a': (15, False),
                              'n': (28, False), 'm': (50, False),
                              'b': (68, False), 's': (90, False),
                              '$': (92, True), },
                         1: { 'a': (2, False), },
                         2: { 'n': (3, False), },
                         3: { 'a': (4, False), },
                         4: { 'm': (5, False), },
                         5: { 'a': (6, False), },
                         6: { 'b': (7, False), },
                         7: { 'a': (8, False), },
                         8: { 'n': (9, False), },
                         9: { 'a': (10, False), },
                         10: { 'n': (11, False), },
                         11: { 'a': (12, False), },
                         12: { 's': (13, False), },
                         13: { '$': (14, True), },
                         14: {},
                         15: { 'n': (16, False), 'm': (40, False),
                              'b': (60, False), 's': (88, False), },
                         16: { 'a': (17, False), },
                         17: { 'n': (76, False), 's': (84, False),
                              'm': (18, False), },
                         18: { 'a': (19, False), },
                         19: { 'b': (20, False), },
                         20: { 'a': (21, False), },
                         21: { 'n': (22, False), },
                         22: { 'a': (23, False), },
                         23: { 'n': (24, False), },
                         24: { 'a': (25, False), },
                         25: { 's': (26, False), },
                         26: { '$': (27, True), },
                         27: {},
                         28: { 'a': (29, False), },
                         29: { 'm': (30, False), 'n': (80, False),
                              's': (86, False), },
                         30: { 'a': (31, False), },
                         31: { 'b': (32, False), },
                         32: { 'a': (33, False), },
                         33: { 'n': (34, False), },
                         34: { 'a': (35, False), },
                         35: { 'n': (36, False), },
                         36: { 'a': (37, False), },
                         37: { 's': (38, False), },
                         38: { '$': (39, True), },
                         39: {},
                         40: { 'a': (41, False), },
                         41: { 'b': (42, False), },
                         42: { 'a': (43, False), },
                         43: { 'n': (44, False), },
                         44: { 'a': (45, False), },
                         45: { 'n': (46, False), },
                         46: { 'a': (47, False), },
                         47: { 's': (48, False), },
                         48: { '$': (49, True), },
                         49: {},
                         50: { 'a': (51, False), },
                         51: { 'b': (52, False), },
                         52: { 'a': (53, False), },
                         53: { 'n': (54, False), },
                         54: { 'a': (55, False), },
                         55: { 'n': (56, False), },
                         56: { 'a': (57, False), },
                         57: { 's': (58, False), },
                         58: { '$': (59, True), },
                         59: {},
                         60: { 'a': (61, False), },
                         61: { 'n': (62, False), },
                         62: { 'a': (63, False), },
                         63: { 'n': (64, False), },
                         64: { 'a': (65, False), },
                         65: { 's': (66, False), },
                         66: { '$': (67, True), },
                         67: {},
                         68: { 'a': (69, False), },
                         69: { 'n': (70, False), },
                         70: { 'a': (71, False), },
                         71: { 'n': (72, False), },
                         72: { 'a': (73, False), },
                         73: { 's': (74, False), },
                         74: { '$': (75, True), },
                         75: {},
                         76: { 'a': (77, False), },
                         77: { 's': (78, False), },
                         78: { '$': (79, True), },
                         79: {},
                         80: { 'a': (81, False), },
                         81: { 's': (82, False), },
                         82: { '$': (83, True), },
                         83: {},
                         84: { '$': (85, True), },
                         85: {},
                         86: { '$': (87, True), },
                         87: {},
                         88: { '$': (89, True), },
                         89: {},
                         90: { '$': (91, True), },
                         91: {},
                         92: {}, }

        self.assert_trie(expected_trie, trie)

class TrieUtilBuildCompressedSuffixTrieTestCase(unittest.TestCase):

    def setUp(self):
        pass

    def tearDown(self):
        pass

    def assert_trie(self, expected_trie, trie):
        self.assertEqual(len(expected_trie), len(trie))
        for node in trie:
            self.assertEqual(len(expected_trie[node]), len(trie[node]))
            for symbol, neighbor in trie[node].items():
                self.assertEqual(expected_trie[node][symbol], neighbor)

    def test_empty_text(self):
        text = '$'

        trie = trie_util.TrieUtil.build_compressed_suffix_trie(text)

        expected_trie = { 0: { '$': (1, True), },
                         1: {}, }

        self.assert_trie(expected_trie, trie)

    def test_a(self):
        text = 'a$'

        trie = trie_util.TrieUtil.build_compressed_suffix_trie(text)

        expected_trie = { 0: { 'a$': (2, True), '$': (3, True), },
                         2: {},
                         3: {}, }

        self.assert_trie(expected_trie, trie)

    def test_ab(self):
        text = 'ab$'

        trie = trie_util.TrieUtil.build_compressed_suffix_trie(text)

        expected_trie = { 0: { 'ab$': (3, True), 'b$': (5, True),
                              '$': (6, True), },
                         3: {},
                         5: {},
                         6: {}, }

        self.assert_trie(expected_trie, trie)

    def test_aca(self):
        text = 'aca$'

        trie = trie_util.TrieUtil.build_compressed_suffix_trie(text)

        expected_trie = { 0: { 'a': (1, False), 'ca$': (7, True),
                              '$': (9, True), },
                         1: { 'ca$': (4, True), '$': (8, True), },
                         4: {},
                         7: {},
                         8: {},
                         9: {}, }

        self.assert_trie(expected_trie, trie)

    def test_abac(self):
        text = 'abac$'

        trie = trie_util.TrieUtil.build_compressed_suffix_trie(text)

        expected_trie = { 0: { 'a': (1, False), 'bac$': (9, True),
                              'c$': (13, True), '$': (14, True), },
                         1: { 'bac$': (5, True), 'c$': (11, True), },
                         5: {},
                         9: {},
                         11: {},
                         13: {},
                         14: {}, }

        self.assert_trie(expected_trie, trie)

    def test_abab(self):
        text = 'abab$'

        trie = trie_util.TrieUtil.build_compressed_suffix_trie(text)

        expected_trie = { 0: { 'ab': (2, False), 'b': (6, False),
                              '$': (12, True), },
                         2: { 'ab$': (5, True), '$': (10, True), },
                         5: {},
                         6: { 'ab$': (9, True), '$': (11, True), },
                         9: {},
                         10: {},
                         11: {},
                         12: {}, }

        self.assert_trie(expected_trie, trie)

    def test_ataaatg(self):
        text = 'ataaatg$'

        trie = trie_util.TrieUtil.build_compressed_suffix_trie(text)

        expected_trie = { 0: { 'a': (1, False), 't': (9, False),
                              'g$': (29, True), '$': (30, True), },
                         1: { 't': (2, False), 'a': (16, False), },
                         2: { 'aaatg$': (8, True), 'g$': (25, True), },
                         8: {},
                         9: { 'aaatg$': (15, True), 'g$': (27, True), },
                         15: {},
                         16: { 'atg$': (20, True), 'tg$': (23, True), },
                         20: {},
                         23: {},
                         25: {},
                         27: {},
                         29: {},
                         30: {}, }

        self.assert_trie(expected_trie, trie)

    def test_panamabananas(self):
        text = 'panamabananas$'

        trie = trie_util.TrieUtil.build_compressed_suffix_trie(text)

        expected_trie = { 0: { 'panamabananas$': (14, True), 'a': (15, False),
                              'na': (29, False), 'mabananas$': (59, True),
                              'bananas$': (75, True), 's$': (91, True),
                              '$': (92, True), },
                         14: {},
                         15: { 'na': (17, False), 'mabananas$': (49, True),
                              'bananas$': (67, True), 's$': (89, True), },
                         17: { 'mabananas$': (27, True), 'nas$': (79, True),
                              's$': (85, True), },
                         27: {},
                         29: { 'mabananas$': (39, True), 'nas$': (83, True),
                              's$': (87, True), },
                         39: {},
                         49: {},
                         59: {},
                         67: {},
                         75: {},
                         79: {},
                         83: {},
                         85: {},
                         87: {},
                         89: {},
                         91: {},
                         92: {}, }

        self.assert_trie(expected_trie, trie)

if __name__ == '__main__':
    class_names = \
    [
        TrieUtilBuildTrieTestCase,
        TrieUtilPrefixTrieMatchingTestCase,
        TrieUtilTrieMatchingTestCase,
        TrieUtilBuildSuffixTrieTestCase,
        TrieUtilBuildCompressedSuffixTrieTestCase,
    ]

    suite = unittest.TestSuite()

    for c in class_names:
        suite.addTest(unittest.defaultTestLoader.loadTestsFromTestCase(c))

    unittest.TextTestRunner().run(suite)
