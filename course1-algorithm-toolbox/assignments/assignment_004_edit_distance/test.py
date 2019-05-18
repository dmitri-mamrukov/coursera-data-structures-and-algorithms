#!/usr/bin/python3

import unittest

from edit_distance import edit_distance

class EditDistanceTestCase(unittest.TestCase):

    def test_with_empty_and_one_char_word(self):
        word1 = ''
        word2 = 'a'
        self.assertEqual(1, edit_distance(word1, word2))

    def test_with_one_char_word_and_empty(self):
        word1 = 'a'
        word2 = ''
        self.assertEqual(1, edit_distance(word1, word2))

    def test_with_empty_and_two_char_word(self):
        word1 = ''
        word2 = 'ab'
        self.assertEqual(2, edit_distance(word1, word2))

    def test_with_two_char_word_and_empty(self):
        word1 = 'ab'
        word2 = ''
        self.assertEqual(2, edit_distance(word1, word2))

    def test_with_empty_and_three_char_word(self):
        word1 = ''
        word2 = 'abc'
        self.assertEqual(3, edit_distance(word1, word2))

    def test_with_three_char_word_and_empty(self):
        word1 = 'abc'
        word2 = ''
        self.assertEqual(3, edit_distance(word1, word2))

    def test_with_same_one_char_words(self):
        word1 = 'a'
        word2 = 'a'
        self.assertEqual(0, edit_distance(word1, word2))

    def test_with_same_two_char_words(self):
        word1 = 'ab'
        word2 = 'ab'
        self.assertEqual(0, edit_distance(word1, word2))

    def test_with_same_three_char_words(self):
        word1 = 'abc'
        word2 = 'abc'
        self.assertEqual(0, edit_distance(word1, word2))

    def test_with_words_of_different_chars(self):
        word1 = 'abc'
        word2 = 'xyz'
        self.assertEqual(3, edit_distance(word1, word2))

    def test_with_same_length_words_with_one_same_char_in_same_position(self):
        word1 = 'abc'
        word2 = 'ayz'
        self.assertEqual(2, edit_distance(word1, word2))

    def test_with_same_length_words_with_one_same_char_away_by_one(self):
        word1 = 'abc'
        word2 = 'xaz'
        self.assertEqual(3, edit_distance(word1, word2))

    def test_with_same_length_words_with_one_same_char_away_by_two(self):
        word1 = 'abc'
        word2 = 'xya'
        self.assertEqual(3, edit_distance(word1, word2))

    def test_with_exponential_and_polynomial(self):
        word1 = 'EXPONENTIAL'
        word2 = 'POLYNOMIAL'
        self.assertEqual(6, edit_distance(word1, word2))

    def test_with_snowy_and_sunny(self):
        word1 = 'SNOWY'
        word2 = 'SUNNY'
        self.assertEqual(3, edit_distance(word1, word2))

    def test_with_atgttata_and_atcgtcc(self):
        word1 = 'ATGTTATA'
        word2 = 'ATCGTCC'
        self.assertEqual(5, edit_distance(word1, word2))

    def test_with_editing_and_distance_in_uppercase(self):
        word1 = 'EDITING'
        word2 = 'DISTANCE'
        self.assertEqual(5, edit_distance(word1, word2))

    def test_with_editing_and_distance_in_lowercase(self):
        word1 = 'editing'
        word2 = 'distance'
        self.assertEqual(5, edit_distance(word1, word2))

    def test_with_democrat_and_republican(self):
        word1 = 'democrat'
        word2 = 'republican'
        self.assertEqual(8, edit_distance(word1, word2))

    def test_with_short_and_ports(self):
        word1 = 'short'
        word2 = 'ports'
        self.assertEqual(3, edit_distance(word1, word2))

if __name__ == '__main__':
    unittest.main()
