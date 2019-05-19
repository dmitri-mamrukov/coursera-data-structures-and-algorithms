#!/usr/bin/python3

import unittest

import burrows_wheeler_transform

class BurrowsWheelerTransformTestCase(unittest.TestCase):

    def setUp(self):
        pass

    def tearDown(self):
        pass

    def cyclic_compare_chars(self, word, i, j):
        if word[-i] < word[-j]:
            return -1
        if word[-i] == word[-j]:
            return 0
        if word[-i] > word[-j]:
            return 1

    def assert_inverse_burrows_wheeler_transform(self,
                                                 original_word,
                                                 expected_transform_word):
        transform_word = burrows_wheeler_transform.Util. \
                                        burrows_wheeler_transform(original_word)

        self.assertEqual(expected_transform_word, transform_word)

        inverse_transform_word = burrows_wheeler_transform.Util. \
                               inverse_burrows_wheeler_transform(transform_word)

        self.assertEqual(original_word, inverse_transform_word)

    def test_cyclic_rotation_character_by_i_as_0(self):
        word = 'word'

        self.assertEqual('w',
                         burrows_wheeler_transform.Util. \
                                         _cyclic_rotation_character(word, 0, 0))
        self.assertEqual('o',
                         burrows_wheeler_transform.Util. \
                                         _cyclic_rotation_character(word, 0, 1))
        self.assertEqual('r',
                         burrows_wheeler_transform.Util. \
                                         _cyclic_rotation_character(word, 0, 2))
        self.assertEqual('d',
                         burrows_wheeler_transform.Util. \
                                         _cyclic_rotation_character(word, 0, 3))

    def test_cyclic_rotation_character_by_i_as_1(self):
        word = 'word'

        self.assertEqual('w',
                         burrows_wheeler_transform.Util. \
                                         _cyclic_rotation_character(word, 1, 1))
        self.assertEqual('o',
                         burrows_wheeler_transform.Util. \
                                         _cyclic_rotation_character(word, 1, 2))
        self.assertEqual('r',
                         burrows_wheeler_transform.Util. \
                                         _cyclic_rotation_character(word, 1, 3))
        self.assertEqual('d',
                         burrows_wheeler_transform.Util. \
                                         _cyclic_rotation_character(word, 1, 4))

    def test_cyclic_rotation_character_by_i_as_2(self):
        word = 'word'

        self.assertEqual('w',
                         burrows_wheeler_transform.Util. \
                                         _cyclic_rotation_character(word, 2, 2))
        self.assertEqual('o',
                         burrows_wheeler_transform.Util. \
                                         _cyclic_rotation_character(word, 2, 3))
        self.assertEqual('r',
                         burrows_wheeler_transform.Util. \
                                         _cyclic_rotation_character(word, 2, 4))
        self.assertEqual('d',
                        burrows_wheeler_transform.Util. \
                                         _cyclic_rotation_character(word, 2, 5))

    def test_cyclic_rotation_character_by_i_as_3(self):
        word = 'word'

        self.assertEqual('w',
                         burrows_wheeler_transform.Util. \
                                         _cyclic_rotation_character(word, 3, 3))
        self.assertEqual('o',
                         burrows_wheeler_transform.Util. \
                                         _cyclic_rotation_character(word, 3, 4))
        self.assertEqual('r',
                         burrows_wheeler_transform.Util. \
                                         _cyclic_rotation_character(word, 3, 5))
        self.assertEqual('d',
                         burrows_wheeler_transform.Util. \
                                         _cyclic_rotation_character(word, 3, 6))

    def test_cyclic_compare_with_i_and_j_as_0_and_0(self):
        word = 'word'

        i = 0
        j = 0
        self.assertEqual(0,
                         burrows_wheeler_transform.Util. \
                                                    _cyclic_compare(word, i, j))
        self.assertEqual(self.cyclic_compare_chars(word, i, j),
                         burrows_wheeler_transform.Util. \
                                                    _cyclic_compare(word, i, j))

    def test_cyclic_compare_with_i_and_j_as_0_and_1(self):
        word = 'word'

        i = 0
        j = 1
        self.assertEqual(1,
                         burrows_wheeler_transform.Util. \
                                                    _cyclic_compare(word, i, j))
        self.assertEqual(self.cyclic_compare_chars(word, i, j),
                         burrows_wheeler_transform.Util. \
                                                    _cyclic_compare(word, i, j))

    def test_cyclic_compare_with_i_and_j_as_0_and_2(self):
        word = 'word'

        i = 0
        j = 2
        self.assertEqual(1,
                         burrows_wheeler_transform.Util. \
                                                    _cyclic_compare(word, i, j))
        self.assertEqual(self.cyclic_compare_chars(word, i, j),
                         burrows_wheeler_transform.Util. \
                                                    _cyclic_compare(word, i, j))

    def test_cyclic_compare_with_i_and_j_as_0_and_3(self):
        word = 'word'

        i = 0
        j = 3
        self.assertEqual(1,
                         burrows_wheeler_transform.Util. \
                                                    _cyclic_compare(word, i, j))
        self.assertEqual(self.cyclic_compare_chars(word, i, j),
                         burrows_wheeler_transform.Util. \
                                                    _cyclic_compare(word, i, j))

    def test_cyclic_compare_with_i_and_j_as_1_and_0(self):
        word = 'word'

        i = 1
        j = 0
        self.assertEqual(-1,
                         burrows_wheeler_transform.Util. \
                                                    _cyclic_compare(word, i, j))
        self.assertEqual(self.cyclic_compare_chars(word, i, j),
                         burrows_wheeler_transform.Util. \
                                                    _cyclic_compare(word, i, j))

    def test_cyclic_compare_with_i_and_j_as_1_and_1(self):
        word = 'word'

        i = 1
        j = 1
        self.assertEqual(0,
                         burrows_wheeler_transform.Util. \
                                                    _cyclic_compare(word, i, j))
        self.assertEqual(self.cyclic_compare_chars(word, i, j),
                         burrows_wheeler_transform.Util. \
                                                    _cyclic_compare(word, i, j))

    def test_cyclic_compare_with_i_and_j_as_1_and_2(self):
        word = 'word'

        i = 1
        j = 2
        self.assertEqual(-1,
                         burrows_wheeler_transform.Util. \
                                                    _cyclic_compare(word, i, j))
        self.assertEqual(self.cyclic_compare_chars(word, i, j),
                         burrows_wheeler_transform.Util. \
                                                    _cyclic_compare(word, i, j))

    def test_cyclic_compare_with_i_and_j_as_1_and_3(self):
        word = 'word'

        i = 1
        j = 3
        self.assertEqual(-1,
                         burrows_wheeler_transform.Util. \
                                                    _cyclic_compare(word, i, j))
        self.assertEqual(self.cyclic_compare_chars(word, i, j),
                         burrows_wheeler_transform.Util. \
                                                    _cyclic_compare(word, i, j))

    def test_cyclic_compare_with_i_and_j_as_2_and_0(self):
        word = 'word'

        i = 2
        j = 0
        self.assertEqual(-1,
                         burrows_wheeler_transform.Util. \
                                                    _cyclic_compare(word, i, j))
        self.assertEqual(self.cyclic_compare_chars(word, i, j),
                         burrows_wheeler_transform.Util. \
                                                    _cyclic_compare(word, i, j))

    def test_cyclic_compare_with_i_and_j_as_2_and_1(self):
        word = 'word'

        i = 2
        j = 1
        self.assertEqual(1,
                         burrows_wheeler_transform.Util. \
                                                    _cyclic_compare(word, i, j))
        self.assertEqual(self.cyclic_compare_chars(word, i, j),
                         burrows_wheeler_transform.Util. \
                                                    _cyclic_compare(word, i, j))

    def test_cyclic_compare_with_i_and_j_as_2_and_2(self):
        word = 'word'

        i = 2
        j = 2
        self.assertEqual(0,
                         burrows_wheeler_transform.Util. \
                                                    _cyclic_compare(word, i, j))
        self.assertEqual(self.cyclic_compare_chars(word, i, j),
                         burrows_wheeler_transform.Util. \
                                                    _cyclic_compare(word, i, j))

    def test_cyclic_compare_with_i_and_j_as_2_and_3(self):
        word = 'word'

        i = 2
        j = 3
        self.assertEqual(1,
                         burrows_wheeler_transform.Util. \
                                                    _cyclic_compare(word, i, j))
        self.assertEqual(self.cyclic_compare_chars(word, i, j),
                         burrows_wheeler_transform.Util. \
                                                    _cyclic_compare(word, i, j))

    def test_cyclic_compare_with_i_and_j_as_3_and_0(self):
        word = 'word'

        i = 3
        j = 0
        self.assertEqual(-1,
                         burrows_wheeler_transform.Util. \
                                                    _cyclic_compare(word, i, j))
        self.assertEqual(self.cyclic_compare_chars(word, i, j),
                         burrows_wheeler_transform.Util. \
                                                    _cyclic_compare(word, i, j))

    def test_cyclic_compare_with_i_and_j_as_3_and_1(self):
        word = 'word'

        i = 3
        j = 1
        self.assertEqual(1,
                         burrows_wheeler_transform.Util. \
                                                    _cyclic_compare(word, i, j))
        self.assertEqual(self.cyclic_compare_chars(word, i, j),
                         burrows_wheeler_transform.Util. \
                                                    _cyclic_compare(word, i, j))

    def test_cyclic_compare_with_i_and_j_as_3_and_2(self):
        word = 'word'

        i = 3
        j = 2
        self.assertEqual(-1,
                         burrows_wheeler_transform.Util. \
                                                    _cyclic_compare(word, i, j))
        self.assertEqual(self.cyclic_compare_chars(word, i, j),
                         burrows_wheeler_transform.Util. \
                                                    _cyclic_compare(word, i, j))

    def test_cyclic_compare_with_i_and_j_as_3_and_3(self):
        word = 'word'

        i = 3
        j = 3
        self.assertEqual(0,
                         burrows_wheeler_transform.Util. \
                                                    _cyclic_compare(word, i, j))
        self.assertEqual(self.cyclic_compare_chars(word, i, j),
                         burrows_wheeler_transform.Util. \
                                                    _cyclic_compare(word, i, j))

    def test_cyclic_sort_of_word(self):
        word = 'word'

        """
        Cyclic rotations (to the right):

        word
        dwor
        rdwo
        ordw

        Sorting the cyclic rotations:

        dwor -> shift by 1
        ordw -> shift by 3
        rdwo -> shift by 2
        word -> shift by 0
        """

        self.assertEqual([ 1, 3, 2, 0 ],
                         burrows_wheeler_transform.Util._cyclic_sort(word))

    def test_cyclic_sort_of_aa(self):
        word = 'AA$'

        """
        Cyclic rotations (to the right):

        AA$
        $AA
        A$A

        Sorting the cyclic rotations:

        $AA -> shift by 1
        A$A -> shift by 2
        AA$ -> shift by 0
        """

        self.assertEqual([ 1, 2, 0 ],
                         burrows_wheeler_transform.Util._cyclic_sort(word))

    def test_cyclic_sort_of_acacacac(self):
        word = 'ACACACAC$'

        """
        Cyclic rotations (to the right):

        ACACACAC$
        $ACACACAC
        C$ACACACA
        AC$ACACAC
        CAC$ACACA
        ACAC$ACAC
        CACAC$ACA
        ACACAC$AC
        CACACAC$A

        Sorting the cyclic rotations:

        $ACACACAC -> shift by 1
        AC$ACACAC -> shift by 3
        ACAC$ACAC -> shift by 5
        ACACAC$AC -> shift by 7
        ACACACAC$ -> shift by 0
        C$ACACACA -> shift by 2
        CAC$ACACA -> shift by 4
        CACAC$ACA -> shift by 6
        CACACAC$A -> shift by 8
        """

        self.assertEqual([ 1, 3, 5, 7, 0, 2, 4, 6, 8 ],
                         burrows_wheeler_transform.Util._cyclic_sort(word))

    def test_cyclic_sort_of_agacata(self):
        word = 'AGACATA$'

        """
        Cyclic rotations (to the right):

        AGACATA$
        $AGACATA
        A$AGACAT
        TA$AGACA
        ATA$AGAC
        CATA$AGA
        ACATA$AG
        GACATA$A

        Sorting the cyclic rotations:

        $AGACATA -> shift by 1
        A$AGACAT -> shift by 2
        ACATA$AG -> shift by 6
        AGACATA$ -> shift by 0
        ATA$AGAC -> shift by 4
        CATA$AGA -> shift by 5
        GACATA$A -> shift by 7
        TA$AGACA -> shift by 3
        """

        self.assertEqual([ 1, 2, 6, 0, 4, 5, 7, 3 ],
                         burrows_wheeler_transform.Util._cyclic_sort(word))

    def test_burrows_wheeler_transform_of_aaz(self):
        word = 'AA$'

        self.assertEqual('AA$',
                         burrows_wheeler_transform.Util. \
                                                burrows_wheeler_transform(word))

    def test_burrows_wheeler_transform_of_acacacacz(self):
        word = 'ACACACAC$'

        self.assertEqual('CCCC$AAAA',
                         burrows_wheeler_transform.Util. \
                                                burrows_wheeler_transform(word))

    def test_burrows_wheeler_transform_of_agacataz(self):
        word = 'AGACATA$'

        self.assertEqual('ATG$CAAA',
                         burrows_wheeler_transform.Util. \
                                                burrows_wheeler_transform(word))

    def test_enumerate_word_as_az(self):
        self.assertEqual([ 'a0', ],
                         burrows_wheeler_transform.Util._enumerate_word('a'))

    def test_enumerate_word_as_abz(self):
        self.assertEqual([ 'a0', 'b0', ],
                         burrows_wheeler_transform.Util._enumerate_word('ab'))

    def test_enumerate_word_as_abcz(self):
        self.assertEqual([ 'a0', 'b0', 'c0', ],
                         burrows_wheeler_transform.Util._enumerate_word('abc'))

    def test_enumerate_word_as_abcbbaz(self):
        self.assertEqual([ 'a0', 'b0', 'c0', 'b1', 'b2', 'a1', ],
                         burrows_wheeler_transform.Util._enumerate_word(
                                                                      'abcbba'))

    def test_inverse_burrows_wheeler_transform_of_aaz(self):
        original_word = 'AA$'
        expected_transform_word = 'AA$'

        self.assert_inverse_burrows_wheeler_transform(original_word,
                                                      expected_transform_word)

    def test_inverse_burrows_wheeler_transform_of_acacacacz(self):
        original_word = 'ACACACAC$'
        expected_transform_word = 'CCCC$AAAA'

        self.assert_inverse_burrows_wheeler_transform(original_word,
                                                      expected_transform_word)

    def test_inverse_burrows_wheeler_transform_of_agacataz(self):
        original_word = 'AGACATA$'
        expected_transform_word = 'ATG$CAAA'

        self.assert_inverse_burrows_wheeler_transform(original_word,
                                                      expected_transform_word)

    def test_get_pattern_count_of_agggaaz(self):
        transform_word = 'AGGGAA$'
        patterns = [ 'GA', ]
        expected_original_word = 'GAGAGA$'

        self.assert_inverse_burrows_wheeler_transform(expected_original_word,
                                                      transform_word)

        self.assertEquals([ 3, ],
                          burrows_wheeler_transform.Util.get_pattern_count(
                                                      transform_word, patterns))

    def test_get_pattern_count_of_attzaa(self):
        transform_word = 'ATT$AA'
        patterns = [ 'ATA', 'A', ]
        expected_original_word = 'ATATA$'

        self.assert_inverse_burrows_wheeler_transform(expected_original_word,
                                                      transform_word)

        self.assertEquals([ 2, 3, ],
                          burrows_wheeler_transform.Util.get_pattern_count(
                                                      transform_word, patterns))

    def test_get_pattern_count_of_atztctatg(self):
        transform_word = 'AT$TCTATG'
        patterns = [ 'TCT', 'TATG', ]
        expected_original_word = 'ATCGTTTA$'

        self.assert_inverse_burrows_wheeler_transform(expected_original_word,
                                                      transform_word)

        self.assertEquals([ 0, 0, ],
                          burrows_wheeler_transform.Util.get_pattern_count(
                                                      transform_word, patterns))

    def test_get_pattern_count_better_of_agggaaz(self):
        transform_word = 'AGGGAA$'
        patterns = [ 'GA', ]
        expected_original_word = 'GAGAGA$'

        self.assert_inverse_burrows_wheeler_transform(expected_original_word,
                                                      transform_word)

        self.assertEquals([ 3, ],
                          burrows_wheeler_transform.Util. \
                             get_pattern_count_better(transform_word, patterns))

    def test_get_pattern_count_better_of_attzaa(self):
        transform_word = 'ATT$AA'
        patterns = [ 'ATA', 'A', ]
        expected_original_word = 'ATATA$'

        self.assert_inverse_burrows_wheeler_transform(expected_original_word,
                                                      transform_word)

        self.assertEquals([ 2, 3, ],
                          burrows_wheeler_transform.Util. \
                             get_pattern_count_better(transform_word, patterns))

    def test_get_pattern_count_better_of_atztctatg(self):
        transform_word = 'AT$TCTATG'
        patterns = [ 'TCT', 'TATG', ]
        expected_original_word = 'ATCGTTTA$'

        self.assert_inverse_burrows_wheeler_transform(expected_original_word,
                                                      transform_word)

        self.assertEquals([ 0, 0, ],
                          burrows_wheeler_transform.Util. \
                             get_pattern_count_better(transform_word, patterns))

if __name__ == '__main__':
    class_names = [
                      BurrowsWheelerTransformTestCase,
                  ]

    suite = unittest.TestSuite()

    for c in class_names:
        suite.addTest(unittest.defaultTestLoader.loadTestsFromTestCase(c))

    unittest.TextTestRunner().run(suite)
