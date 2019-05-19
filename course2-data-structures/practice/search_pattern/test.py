#!/usr/bin/python3

import unittest

import search_pattern

class AreEqualTestCase(unittest.TestCase):

    def assert_equality(self, s1, s2, expected_result):
        self.assertEqual(expected_result,
            search_pattern.SearchPattern.are_equal(s1, s2))
        self.assertEqual(expected_result,
            search_pattern.SearchPattern.are_equal(s2, s1))

    def test_empty_and_empty(self):
        s1, s2 = '', ''

        self.assert_equality(s1, s2, True)

    def test_non_empty_and_empty(self):
        s1, s2 = 'a', ''

        self.assert_equality(s1, s2, False)

    def test_empty_and_non_empty(self):
        s1, s2 = '', 'a'

        self.assert_equality(s1, s2, False)

    def test_a_and_a(self):
        s1, s2 = 'a', 'a'

        self.assert_equality(s1, s2, True)

    def test_ab_and_a(self):
        s1, s2 = 'ab', 'a'

        self.assert_equality(s1, s2, False)

    def test_a_and_ab(self):
        s1, s2 = 'a', 'ab'

        self.assert_equality(s1, s2, False)

    def test_ab_and_ab(self):
        s1, s2 = 'ab', 'ab'

        self.assert_equality(s1, s2, True)

    def test_abc_and_ab(self):
        s1, s2 = 'abc', 'ab'

        self.assert_equality(s1, s2, False)

    def test_ab_and_abc(self):
        s1, s2 = 'ab', 'abc'

        self.assert_equality(s1, s2, False)

    def test_abcdefgijklmnopqrstuvwxyz_and_abcdefgijklmnopqrstuvwxyz(self):
        s1, s2 = 'abcdefgijklmnopqrstuvwxyz', 'abcdefgijklmnopqrstuvwxyz'

        self.assert_equality(s1, s2, True)

    def test_different_cases(self):
        s1, s2 = 'abcdefgijklmnopqrstuvwxyz', 'ABCDEFGIJKLMNOPQRSTUVWXYZ'

        self.assert_equality(s1, s2, False)

class PolyHashTestCase(unittest.TestCase):

    def test_empty_text(self):
        text = ''
        p = 37
        x = 31

        expected_hash = 0

        self.assertEqual(expected_hash,
            search_pattern.SearchPattern.poly_hash(text, p, x))

    def test_one_char_text(self):
        text = 'a'
        p = 37
        x = 31

        self.assertEqual(97, ord('a'))

        expected_hash = 97 % p

        self.assertEqual(expected_hash,
            search_pattern.SearchPattern.poly_hash(text, p, x))

    def test_two_char_text(self):
        text = 'ab'
        p = 37
        x = 31

        self.assertEqual(97, ord('a'))
        self.assertEqual(98, ord('b'))

        expected_hash = 98 % p
        expected_hash = (97 + expected_hash * x) % p

        self.assertEqual(expected_hash,
            search_pattern.SearchPattern.poly_hash(text, p, x))

    def test_three_char_text(self):
        text = 'abc'
        p = 37
        x = 31

        self.assertEqual(97, ord('a'))
        self.assertEqual(98, ord('b'))
        self.assertEqual(99, ord('c'))

        expected_hash = 99 % p
        expected_hash = (98 + expected_hash * x) % p
        expected_hash = (97 + expected_hash * x) % p

        self.assertEqual(expected_hash,
            search_pattern.SearchPattern.poly_hash(text, p, x))

class PrecomputeHashesTestCase(unittest.TestCase):

    def test_empty_text_and_pattern_length_as_0(self):
        text = ''
        pattern_len = 0
        p = 37
        x = 31

        expected_hashes = []

        self.assertEqual(expected_hashes,
            search_pattern.SearchPattern.precompute_hashes(
            text, pattern_len, p, x))

    def test_empty_text_and_pattern_length_as_1(self):
        text = ''
        pattern_len = 1
        p = 37
        x = 31

        expected_hashes = []

        self.assertEqual(expected_hashes,
            search_pattern.SearchPattern.precompute_hashes(
            text, pattern_len, p, x))

    def test_one_char_text_and_pattern_length_as_0(self):
        text = 'a'
        pattern_len = 0
        p = 37
        x = 31

        self.assertEqual(97, ord('a'))

        expected_hashes = []

        self.assertEqual(expected_hashes,
            search_pattern.SearchPattern.precompute_hashes(
            text, pattern_len, p, x))

    def test_two_char_text_and_pattern_length_as_0(self):
        text = 'ab'
        pattern_len = 0
        p = 37
        x = 31

        self.assertEqual(97, ord('a'))
        self.assertEqual(98, ord('b'))

        expected_hashes = []

        self.assertEqual(expected_hashes,
            search_pattern.SearchPattern.precompute_hashes(
            text, pattern_len, p, x))

    def test_three_char_text_and_pattern_length_as_0(self):
        text = 'abc'
        pattern_len = 0
        p = 37
        x = 31

        self.assertEqual(97, ord('a'))
        self.assertEqual(98, ord('b'))
        self.assertEqual(99, ord('c'))

        expected_hashes = []

        self.assertEqual(expected_hashes,
            search_pattern.SearchPattern.precompute_hashes(
            text, pattern_len, p, x))

    def test_one_char_text_and_pattern_length_as_1(self):
        text = 'a'
        pattern_len = 1
        p = 37
        x = 31

        self.assertEqual(97, ord('a'))

        h0 = search_pattern.SearchPattern.poly_hash('a', p, x)
        expected_hashes = [ h0 ]

        self.assertEqual(
            [
                search_pattern.SearchPattern.poly_hash('a', p, x)
            ],
            expected_hashes)

        self.assertEqual(expected_hashes,
            search_pattern.SearchPattern.precompute_hashes(
            text, pattern_len, p, x))

    def test_two_char_text_and_pattern_length_as_1(self):
        text = 'ab'
        pattern_len = 1
        p = 37
        x = 31

        self.assertEqual(97, ord('a'))
        self.assertEqual(98, ord('b'))

        y = 1
        y = (y * x) % p
        h1 = search_pattern.SearchPattern.poly_hash('b', p, x)
        h0 = (x * h1 + 97 - y * 98) % p
        expected_hashes = [ h0, h1 ]

        self.assertEqual(
            [
                search_pattern.SearchPattern.poly_hash('a', p, x),
                search_pattern.SearchPattern.poly_hash('b', p, x)
            ],
            expected_hashes)

        self.assertEqual(expected_hashes,
            search_pattern.SearchPattern.precompute_hashes(
            text, pattern_len, p, x))

    def test_three_char_text_and_pattern_length_as_1(self):
        text = 'abc'
        pattern_len = 1
        p = 37
        x = 31

        self.assertEqual(97, ord('a'))
        self.assertEqual(98, ord('b'))
        self.assertEqual(99, ord('c'))

        y = 1
        y = (y * x) % p
        h2 = search_pattern.SearchPattern.poly_hash('c', p, x)
        h1 = (x * h2 + 98 - y * 99) % p
        h0 = (x * h1 + 97 - y * 98) % p
        expected_hashes = [ h0, h1, h2 ]

        self.assertEqual(
            [
                search_pattern.SearchPattern.poly_hash('a', p, x),
                search_pattern.SearchPattern.poly_hash('b', p, x),
                search_pattern.SearchPattern.poly_hash('c', p, x)
            ],
            expected_hashes)

        self.assertEqual(expected_hashes,
            search_pattern.SearchPattern.precompute_hashes(
            text, pattern_len, p, x))

    def test_one_char_text_and_pattern_length_as_2(self):
        text = 'a'
        pattern_len = 2
        p = 37
        x = 31

        self.assertEqual(97, ord('a'))

        expected_hashes = []

        self.assertEqual(expected_hashes,
            search_pattern.SearchPattern.precompute_hashes(
            text, pattern_len, p, x))

    def test_two_char_text_and_pattern_length_as_2(self):
        text = 'ab'
        pattern_len = 2
        p = 37
        x = 31

        self.assertEqual(97, ord('a'))
        self.assertEqual(98, ord('b'))

        h0 = search_pattern.SearchPattern.poly_hash('ab', p, x)
        expected_hashes = [ h0 ]

        self.assertEqual(
            [
                search_pattern.SearchPattern.poly_hash('ab', p, x)
            ],
            expected_hashes)

        self.assertEqual(expected_hashes,
            search_pattern.SearchPattern.precompute_hashes(
            text, pattern_len, p, x))

    def test_three_char_text_and_pattern_length_as_2(self):
        text = 'abc'
        pattern_len = 2
        p = 37
        x = 31

        self.assertEqual(97, ord('a'))
        self.assertEqual(98, ord('b'))
        self.assertEqual(99, ord('c'))

        y = 1
        y = (y * x) % p
        y = (y * x) % p
        h1 = search_pattern.SearchPattern.poly_hash('bc', p, x)
        h0 = (x * h1 + 97 - y * 99) % p
        expected_hashes = [ h0, h1 ]

        self.assertEqual(
            [
                search_pattern.SearchPattern.poly_hash('ab', p, x),
                search_pattern.SearchPattern.poly_hash('bc', p, x)
            ],
            expected_hashes)

        self.assertEqual(expected_hashes,
            search_pattern.SearchPattern.precompute_hashes(
            text, pattern_len, p, x))

    def test_one_char_text_and_pattern_length_as_3(self):
        text = 'a'
        pattern_len = 3
        p = 37
        x = 31

        self.assertEqual(97, ord('a'))

        expected_hashes = []

        self.assertEqual(expected_hashes,
            search_pattern.SearchPattern.precompute_hashes(
            text, pattern_len, p, x))

    def test_two_char_text_and_pattern_length_as_3(self):
        text = 'ab'
        pattern_len = 3
        p = 37
        x = 31

        self.assertEqual(97, ord('a'))
        self.assertEqual(98, ord('b'))

        expected_hashes = []

        self.assertEqual(expected_hashes,
            search_pattern.SearchPattern.precompute_hashes(
            text, pattern_len, p, x))

    def test_three_char_text_and_pattern_length_as_3(self):
        text = 'abc'
        pattern_len = 3
        p = 37
        x = 31

        self.assertEqual(97, ord('a'))
        self.assertEqual(98, ord('b'))
        self.assertEqual(99, ord('c'))

        h0 = search_pattern.SearchPattern.poly_hash('abc', p, x)
        expected_hashes = [ h0 ]

        self.assertEqual(
            [
                search_pattern.SearchPattern.poly_hash('abc', p, x)
            ],
            expected_hashes)

        self.assertEqual(expected_hashes,
            search_pattern.SearchPattern.precompute_hashes(
            text, pattern_len, p, x))

class SearchPatternTestCase(unittest.TestCase):

    def test_default_text_and_default_pattern(self):
        self.assertEqual([ 0 ], self.method_under_test())

    def test_one_char_text_and_default_pattern(self):
        self.assertEqual([ 0, 1 ], self.method_under_test('a'))

    def test_two_char_text_and_default_pattern(self):
        self.assertEqual([ 0, 1, 2 ], self.method_under_test('ab'))

    def test_three_char_text_and_default_pattern(self):
        self.assertEqual([ 0, 1, 2, 3 ], self.method_under_test('abc'))

    def test_empty_text_and_empty_pattern(self):
        text = ''
        pattern = ''

        self.assertEqual([ 0 ], self.method_under_test(text, pattern))

    def test_text_as_one_char_and_empty_pattern(self):
        text = 'a'
        pattern = ''

        self.assertEqual([ 0, 1 ], self.method_under_test(text, pattern))

    def test_text_as_two_chars_and_empty_pattern(self):
        text = 'ab'
        pattern = ''

        self.assertEqual([ 0, 1, 2 ], self.method_under_test(text, pattern))

    def test_text_as_three_chars_and_empty_pattern(self):
        text = 'abc'
        pattern = ''

        self.assertEqual([ 0, 1, 2, 3 ], self.method_under_test(text, pattern))

    def test_empty_text_and_pattern_as_one_char(self):
        text = ''
        pattern = 'a'

        self.assertEqual([], self.method_under_test(text, pattern))

    def test_empty_text_and_pattern_as_two_chars(self):
        text = ''
        pattern = 'ab'

        self.assertEqual([], self.method_under_test(text, pattern))

    def test_empty_text_and_pattern_as_three_chars(self):
        text = ''
        pattern = 'abc'

        self.assertEqual([], self.method_under_test(text, pattern))

    def test_text_as_one_char_and_pattern_as_one_char_both_are_same(self):
        text = 'a'
        pattern = 'a'

        self.assertEqual([ 0 ], self.method_under_test(text, pattern))

    def test_text_as_one_char_and_pattern_as_one_char_both_are_diff(self):
        text = 'a'
        pattern = 'b'

        self.assertEqual([], self.method_under_test(text, pattern))

    def test_text_as_one_char_and_pattern_as_two_chars(self):
        text = 'a'
        pattern = 'bc'

        self.assertEqual([], self.method_under_test(text, pattern))

    def test_text_as_two_chars_and_pattern_as_first_char(self):
        text = 'ab'
        pattern = 'a'

        self.assertEqual([ 0 ], self.method_under_test(text, pattern))

    def test_text_as_two_chars_and_pattern_as_second_char(self):
        text = 'ab'
        pattern = 'b'

        self.assertEqual([ 1 ], self.method_under_test(text, pattern))

    def test_text_as_two_chars_and_pattern_as_missing_char(self):
        text = 'ab'
        pattern = 'c'

        self.assertEqual([], self.method_under_test(text, pattern))

    def test_text_as_two_chars_and_pattern_as_two_chars_both_are_same(self):
        text = 'ab'
        pattern = 'ab'

        self.assertEqual([ 0 ], self.method_under_test(text, pattern))

    def test_text_as_two_chars_and_pattern_as_two_chars_both_are_diff(self):
        text = 'cb'
        pattern = 'bc'

        self.assertEqual([], self.method_under_test(text, pattern))

    def test_text_as_two_chars_and_pattern_as_three_chars(self):
        text = 'ab'
        pattern = 'abc'

        self.assertEqual([], self.method_under_test(text, pattern))

    def test_text_and_pattern_as_three_chars(self):
        text = 'ababbababa'
        pattern = 'aba'

        self.assertEqual([ 0, 5, 7 ], self.method_under_test(text, pattern))

    def test_text_with_uppercase_char_and_pattern_as_three_chars(self):
        text = 'ababbAbaba'
        pattern = 'aba'

        self.assertEqual([ 0, 7 ], self.method_under_test(text, pattern))

    def test_text_and_pattern_as_three_chars_with_uppercase_char(self):
        text = 'ababbababa'
        pattern = 'Aba'

        self.assertEqual([], self.method_under_test(text, pattern))

    def test_text_and_pattern_differing_in_last_char(self):
        text = 'abcdefghijklmnoprqstuvwxyz'
        pattern = 'abcdefghijklmnoprqstuvwxyZ'

        self.assertEqual([], self.method_under_test(text, pattern))

    def test_text_and_pattern_both_in_upper_case(self):
        text = 'ABABABCCA'
        pattern = 'ABABC'

        self.assertEqual([ 2 ], self.method_under_test(text, pattern))

    def test_text_as_phrase_and_pattern(self):
        text = 'If you wish to understand others you must'
        pattern = 'must'

        self.assertEqual([ 37 ], self.method_under_test(text, pattern))

    def test_text_and_pattern_as_digits(self):
        text = '3141592653589793'
        pattern = '26'

        self.assertEqual([ 6 ], self.method_under_test(text, pattern))

class SearchPatternWithNaiveMatchTestCase(SearchPatternTestCase):

    def setUp(self):
        self.method_under_test = \
            search_pattern.SearchPattern.search_pattern_with_naive_match

    def tearDown(self):
        pass

class SearchPatternWithRabinKarpMatchTestCase(SearchPatternTestCase):

    def setUp(self):
        self.method_under_test = \
            search_pattern.SearchPattern.search_pattern_with_rabin_karp_match

    def tearDown(self):
        pass

class SearchPatternWithPrecomputedRabinKarpMatchTestCase(SearchPatternTestCase):

    def setUp(self):
        self.method_under_test = \
            search_pattern.SearchPattern. \
            search_pattern_with_precomputed_rabin_karp_match

    def tearDown(self):
        pass

if __name__ == '__main__':
    class_names = \
    [
        AreEqualTestCase,
        PolyHashTestCase,
        PrecomputeHashesTestCase,
        SearchPatternWithNaiveMatchTestCase,
        SearchPatternWithRabinKarpMatchTestCase,
        SearchPatternWithPrecomputedRabinKarpMatchTestCase
    ]

    suite = unittest.TestSuite()

    for c in class_names:
        suite.addTest(unittest.defaultTestLoader.loadTestsFromTestCase(c))

    unittest.TextTestRunner().run(suite)
