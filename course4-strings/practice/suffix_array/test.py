#!/usr/bin/python3

import unittest

import suffix_array

class UtilHelpersTestCase(unittest.TestCase):

    def setUp(self):
        pass

    def tearDown(self):
        pass

    def assert_alphabet(self, expected_alphabet, alphabet):
        self.assertEqual(len(expected_alphabet), len(alphabet))
        for k, v in alphabet.items():
            self.assertEqual(v, expected_alphabet[k])

    def test_suffix_compare_with_0_0(self):
        word = 'word'

        self.assertEqual(0,
                         suffix_array.Util._suffix_compare(word, 0, 0))

    def test_suffix_compare_with_0_1(self):
        word = 'word'

        self.assertEqual(1,
                         suffix_array.Util._suffix_compare(word, 0, 1))

    def test_suffix_compare_with_0_2(self):
        word = 'word'

        self.assertEqual(1,
                         suffix_array.Util._suffix_compare(word, 0, 2))

    def test_suffix_compare_with_0_3(self):
        word = 'word'

        self.assertEqual(1,
                         suffix_array.Util._suffix_compare(word, 0, 3))

    def test_suffix_compare_with_1_0(self):
        word = 'word'

        self.assertEqual(-1,
                         suffix_array.Util._suffix_compare(word, 1, 0))

    def test_suffix_compare_with_1_1(self):
        word = 'word'

        self.assertEqual(0,
                         suffix_array.Util._suffix_compare(word, 1, 1))

    def test_suffix_compare_with_1_2(self):
        word = 'word'

        self.assertEqual(-1,
                         suffix_array.Util._suffix_compare(word, 1, 2))

    def test_suffix_compare_with_1_3(self):
        word = 'word'

        self.assertEqual(1,
                         suffix_array.Util._suffix_compare(word, 1, 3))

    def test_suffix_compare_with_2_0(self):
        word = 'word'

        self.assertEqual(-1,
                         suffix_array.Util._suffix_compare(word, 2, 0))

    def test_suffix_compare_with_2_1(self):
        word = 'word'

        self.assertEqual(1,
                         suffix_array.Util._suffix_compare(word, 2, 1))

    def test_suffix_compare_with_2_2(self):
        word = 'word'

        self.assertEqual(0,
                         suffix_array.Util._suffix_compare(word, 2, 2))

    def test_suffix_compare_with_2_3(self):
        word = 'word'

        self.assertEqual(1,
                         suffix_array.Util._suffix_compare(word, 2, 3))

    def test_suffix_compare_with_3_0(self):
        word = 'word'

        self.assertEqual(-1,
                         suffix_array.Util._suffix_compare(word, 3, 0))

    def test_suffix_compare_with_3_1(self):
        word = 'word'

        self.assertEqual(-1,
                         suffix_array.Util._suffix_compare(word, 3, 1))

    def test_suffix_compare_with_3_2(self):
        word = 'word'

        self.assertEqual(-1,
                         suffix_array.Util._suffix_compare(word, 3, 2))

    def test_suffix_compare_with_3_3(self):
        word = 'word'

        self.assertEqual(0,
                         suffix_array.Util._suffix_compare(word, 3, 3))

    def test_sort_chars_with_empty(self):
        word = ''
        expected_alphabet = {}

        order, alphabet = suffix_array.Util._sort_chars(word)

        self.assertEqual([], order)
        self.assert_alphabet(expected_alphabet, alphabet)

    def test_sort_chars_with_z(self):
        word = '$'
        expected_alphabet = { '$': 0, }

        order, alphabet = suffix_array.Util._sort_chars(word)

        self.assertEqual([ 0, ], order)
        self.assert_alphabet(expected_alphabet, alphabet)

    def test_sort_chars_with_abz(self):
        word = 'ab$'
        expected_alphabet = { '$': 0, 'a': 1, 'b': 2, }

        order, alphabet = suffix_array.Util._sort_chars(word)

        self.assertEqual([ 2, 0, 1, ], order)
        self.assert_alphabet(expected_alphabet, alphabet)

    def test_sort_chars_with_abcz(self):
        word = 'abc$'
        expected_alphabet = { '$': 0, 'a': 1, 'b': 2, 'c': 3, }

        order, alphabet = suffix_array.Util._sort_chars(word)

        self.assertEqual([ 3, 0, 1, 2, ], order)
        self.assert_alphabet(expected_alphabet, alphabet)

    def test_sort_chars_with_ababaaz(self):
        word = 'ababaa$'
        expected_alphabet = { '$': 0, 'a': 1, 'b': 2, }

        order, alphabet = suffix_array.Util._sort_chars(word)

        self.assertEqual([ 6, 0, 2, 4, 5, 1, 3, ], order)
        self.assert_alphabet(expected_alphabet, alphabet)

    def test_sort_chars_with_aacgatagcggtagaz(self):
        word = 'AACGATAGCGGTAGA$'
        expected_alphabet = { '$': 0, 'A': 1, 'C': 2, 'G': 3, 'T': 4, }

        order, alphabet = suffix_array.Util._sort_chars(word)

        self.assertEqual([ 15, 0, 1, 4, 6, 12, 14, 2, 8, 3, 7, 9, 10,
                          13, 5, 11, ], order)
        self.assert_alphabet(expected_alphabet, alphabet)

    def test_compute_char_classes_with_empty(self):
        word = ''

        order, alphabet = suffix_array.Util._sort_chars(word)

        self.assertEqual([],
                         suffix_array.Util._compute_char_classes(word, order))

    def test_compute_char_classes_with_z(self):
        word = '$'

        order, alphabet = suffix_array.Util._sort_chars(word)

        self.assertEqual([ 0, ],
                         suffix_array.Util._compute_char_classes(word, order))

    def test_compute_char_classes_with_a(self):
        word = 'a$'

        order, alphabet = suffix_array.Util._sort_chars(word)

        self.assertEqual([ 1, 0, ],
                         suffix_array.Util._compute_char_classes(word, order))

    def test_compute_char_classes_with_ab(self):
        word = 'ab$'

        order, alphabet = suffix_array.Util._sort_chars(word)

        self.assertEqual([ 1, 2, 0, ],
                         suffix_array.Util._compute_char_classes(word, order))

    def test_compute_char_classes_with_abcz(self):
        word = 'abc$'

        order, alphabet = suffix_array.Util._sort_chars(word)

        self.assertEqual([ 1, 2, 3, 0, ],
                         suffix_array.Util._compute_char_classes(word, order))

    def test_compute_char_classes_with_ababaaz(self):
        word = 'ababaa$'

        order, alphabet = suffix_array.Util._sort_chars(word)

        self.assertEqual([ 1, 2, 1, 2, 1, 1, 0, ],
                         suffix_array.Util._compute_char_classes(word, order))

    def test_compute_char_classes_with_aacgatagcggtagaz(self):
        word = 'AACGATAGCGGTAGA$'

        order, alphabet = suffix_array.Util._sort_chars(word)

        self.assertEqual([ 1, 1, 2, 3, 1, 4, 1, 3, 2, 3, 3, 4, 1, 3, 1, 0, ],
                         suffix_array.Util._compute_char_classes(word, order))

    def test_sort_double_cyclic_shifts_with_empty_and_length_of_one(self):
        word = ''
        order, alphabet = suffix_array.Util._sort_chars(word)
        eq_class = suffix_array.Util._compute_char_classes(word, order)
        length = 1

        new_order = suffix_array.Util._sort_double_cyclic_shifts(word,
                                                                 length,
                                                                 order,
                                                                 eq_class)

        self.assertEqual([], order)
        self.assertEqual([], eq_class)
        self.assertEqual([], new_order)

    def test_sort_double_cyclic_shifts_with_z_and_length_of_one(self):
        word = '$'
        order, alphabet = suffix_array.Util._sort_chars(word)
        eq_class = suffix_array.Util._compute_char_classes(word, order)
        length = 1

        new_order = suffix_array.Util._sort_double_cyclic_shifts(word,
                                                                 length,
                                                                 order,
                                                                 eq_class)

        self.assertEqual([ 0, ], order)
        self.assertEqual([ 0, ], eq_class)
        self.assertEqual([ 0, ], new_order)

    def test_sort_double_cyclic_shifts_with_az_and_length_of_one(self):
        word = 'a$'
        order, alphabet = suffix_array.Util._sort_chars(word)
        eq_class = suffix_array.Util._compute_char_classes(word, order)
        length = 1

        new_order = suffix_array.Util._sort_double_cyclic_shifts(word,
                                                                 length,
                                                                 order,
                                                                 eq_class)

        self.assertEqual([ 1, 0, ], order)
        self.assertEqual([ 1, 0, ], eq_class)
        self.assertEqual([ 1, 0, ], new_order)

    def test_sort_double_cyclic_shifts_with_abz_and_length_of_one(self):
        word = 'ab$'
        order, alphabet = suffix_array.Util._sort_chars(word)
        eq_class = suffix_array.Util._compute_char_classes(word, order)
        length = 1

        new_order = suffix_array.Util._sort_double_cyclic_shifts(word,
                                                                 length,
                                                                 order,
                                                                 eq_class)

        self.assertEqual([ 2, 0, 1, ], order)
        self.assertEqual([ 1, 2, 0, ], eq_class)
        self.assertEqual([ 2, 0, 1, ], new_order)

    def test_sort_double_cyclic_shifts_with_abcz_and_length_of_one(self):
        word = 'abc$'
        order, alphabet = suffix_array.Util._sort_chars(word)
        eq_class = suffix_array.Util._compute_char_classes(word, order)
        length = 1

        new_order = suffix_array.Util._sort_double_cyclic_shifts(word,
                                                                 length,
                                                                 order,
                                                                 eq_class)

        self.assertEqual([ 3, 0, 1, 2, ], order)
        self.assertEqual([ 1, 2, 3, 0, ], eq_class)
        self.assertEqual([ 3, 0, 1, 2, ], new_order)

    def test_sort_double_cyclic_shifts_with_ababaaz_and_length_of_one(self):
        word = 'ababaa$'
        order, alphabet = suffix_array.Util._sort_chars(word)
        eq_class = suffix_array.Util._compute_char_classes(word, order)
        length = 1

        new_order = suffix_array.Util._sort_double_cyclic_shifts(word,
                                                                 length,
                                                                 order,
                                                                 eq_class)

        self.assertEqual([ 6, 0, 2, 4, 5, 1, 3, ], order)
        self.assertEqual([ 1, 2, 1, 2, 1, 1, 0, ], eq_class)
        self.assertEqual([ 6, 5, 4, 0, 2, 1, 3, ], new_order)

    def test_sort_double_cyclic_shifts_with_aacgatagcggtagaz_and_one(self):
        word = 'AACGATAGCGGTAGA$'
        order, alphabet = suffix_array.Util._sort_chars(word)
        eq_class = suffix_array.Util._compute_char_classes(word, order)
        length = 1

        new_order = suffix_array.Util._sort_double_cyclic_shifts(word,
                                                                 length,
                                                                 order,
                                                                 eq_class)

        self.assertEqual([ 15, 0, 1, 4, 6, 12, 14, 2, 8, 3, 7, 9, 10,
                          13, 5, 11, ], order)
        self.assertEqual([ 1, 1, 2, 3, 1, 4, 1, 3, 2, 3, 3, 4, 1, 3, 1, 0, ],
                         eq_class)
        self.assertEqual([ 15, 14, 0, 1, 6, 12, 4, 2, 8, 3, 13, 7, 9, 10,
                          5, 11, ],
                         new_order)

    def test_sort_double_cyclic_shifts_with_aacgatagcggtagaz_and_two(self):
        word = 'AACGATAGCGGTAGA$'
        order, alphabet = suffix_array.Util._sort_chars(word)
        eq_class = suffix_array.Util._compute_char_classes(word, order)
        length = 2

        new_order = suffix_array.Util._sort_double_cyclic_shifts(word,
                                                                 length,
                                                                 order,
                                                                 eq_class)

        self.assertEqual([ 15, 0, 1, 4, 6, 12, 14, 2, 8, 3, 7, 9, 10,
                          13, 5, 11, ], order)
        self.assertEqual([ 1, 1, 2, 3, 1, 4, 1, 3, 2, 3, 3, 4, 1, 3, 1, 0, ],
                         eq_class)
        self.assertEqual([ 15, 14, 4, 12, 0, 6, 1, 2, 8, 13, 10, 7, 3, 9,
                          5, 11, ],
                         new_order)

    def test_update_eq_classes_with_empty_and_length_of_one(self):
        word = ''
        order, alphabet = suffix_array.Util._sort_chars(word)
        eq_class = suffix_array.Util._compute_char_classes(word, order)
        length = 1
        new_order = suffix_array.Util._sort_double_cyclic_shifts(word,
                                                                 length,
                                                                 order,
                                                                 eq_class)

        new_eq_class = suffix_array.Util._update_eq_classes(length,
                                                            new_order,
                                                            eq_class)

        self.assertEqual([], order)
        self.assertEqual([], eq_class)
        self.assertEqual([], new_order)
        self.assertEqual([], new_eq_class)

    def test_update_eq_classes_with_z_and_length_of_one(self):
        word = '$'
        order, alphabet = suffix_array.Util._sort_chars(word)
        eq_class = suffix_array.Util._compute_char_classes(word, order)
        length = 1
        new_order = suffix_array.Util._sort_double_cyclic_shifts(word,
                                                                 length,
                                                                 order,
                                                                 eq_class)

        new_eq_class = suffix_array.Util._update_eq_classes(length,
                                                            new_order,
                                                            eq_class)
        self.assertEqual([ 0, ], order)
        self.assertEqual([ 0, ], eq_class)
        self.assertEqual([ 0, ], new_order)
        self.assertEqual([ 0, ], new_eq_class)

    def test_update_eq_classes_with_az_and_length_of_one(self):
        word = 'a$'
        order, alphabet = suffix_array.Util._sort_chars(word)
        eq_class = suffix_array.Util._compute_char_classes(word, order)
        length = 1
        new_order = suffix_array.Util._sort_double_cyclic_shifts(word,
                                                                 length,
                                                                 order,
                                                                 eq_class)

        new_eq_class = suffix_array.Util._update_eq_classes(length,
                                                            new_order,
                                                            eq_class)

        self.assertEqual([ 1, 0, ], order)
        self.assertEqual([ 1, 0, ], eq_class)
        self.assertEqual([ 1, 0, ], new_order)
        self.assertEqual([ 1, 0, ], new_eq_class)

    def test_update_eq_classes_with_abz_and_length_of_one(self):
        word = 'ab$'
        order, alphabet = suffix_array.Util._sort_chars(word)
        eq_class = suffix_array.Util._compute_char_classes(word, order)
        length = 1
        new_order = suffix_array.Util._sort_double_cyclic_shifts(word,
                                                                 length,
                                                                 order,
                                                                 eq_class)

        new_eq_class = suffix_array.Util._update_eq_classes(length,
                                                            new_order,
                                                            eq_class)

        self.assertEqual([ 2, 0, 1, ], order)
        self.assertEqual([ 1, 2, 0, ], eq_class)
        self.assertEqual([ 2, 0, 1, ], new_order)
        self.assertEqual([ 1, 2, 0, ], new_eq_class)

    def test_update_eq_classes_with_abcz_and_length_of_one(self):
        word = 'abc$'
        order, alphabet = suffix_array.Util._sort_chars(word)
        eq_class = suffix_array.Util._compute_char_classes(word, order)
        length = 1
        new_order = suffix_array.Util._sort_double_cyclic_shifts(word,
                                                                 length,
                                                                 order,
                                                                 eq_class)

        new_eq_class = suffix_array.Util._update_eq_classes(length,
                                                            new_order,
                                                            eq_class)

        self.assertEqual([ 3, 0, 1, 2, ], order)
        self.assertEqual([ 1, 2, 3, 0, ], eq_class)
        self.assertEqual([ 3, 0, 1, 2, ], new_order)
        self.assertEqual([ 1, 2, 3, 0, ], new_eq_class)

    def test_update_eq_classes_with_ababaaz_and_length_of_one(self):
        word = 'ababaa$'
        order, alphabet = suffix_array.Util._sort_chars(word)
        eq_class = suffix_array.Util._compute_char_classes(word, order)
        length = 1
        new_order = suffix_array.Util._sort_double_cyclic_shifts(word,
                                                                 length,
                                                                 order,
                                                                 eq_class)

        new_eq_class = suffix_array.Util._update_eq_classes(length,
                                                            new_order,
                                                            eq_class)

        self.assertEqual([ 6, 0, 2, 4, 5, 1, 3, ], order)
        self.assertEqual([ 1, 2, 1, 2, 1, 1, 0, ], eq_class)
        self.assertEqual([ 6, 5, 4, 0, 2, 1, 3, ], new_order)
        self.assertEqual([ 3, 4, 3, 4, 2, 1, 0, ], new_eq_class)

    def test_update_eq_classes_with_aacgatagcggtagaz(self):
        """
        S = AACGATAGCGGTAGA$

        Cyclic shifts:

        AACGATAGCGGTAGA$
        $AACGATAGCGGTAGA
        A$AACGATAGCGGTAG
        GA$AACGATAGCGGTA
        AGA$AACGATAGCGGT
        TAGA$AACGATAGCGG
        GTAGA$AACGATAGCG
        GGTAGA$AACGATAGC
        CGGTAGA$AACGATAG
        GCGGTAGA$AACGATA
        AGCGGTAGA$AACGAT
        TAGCGGTAGA$AACGA
        ATAGCGGTAGA$AACG
        GATAGCGGTAGA$AAC
        CGATAGCGGTAGA$AA
        ACGATAGCGGTAGA$A

        Sorted cyclic shifts:

        $AACGATAGCGGTAGA
        A$AACGATAGCGGTAG
        AACGATAGCGGTAGA$
        ACGATAGCGGTAGA$A
        AGA$AACGATAGCGGT
        AGCGGTAGA$AACGAT
        ATAGCGGTAGA$AACG
        CGATAGCGGTAGA$AA
        CGGTAGA$AACGATAG
        GA$AACGATAGCGGTA
        GATAGCGGTAGA$AAC
        GCGGTAGA$AACGATA
        GGTAGA$AACGATAGC
        GTAGA$AACGATAGCG
        TAGA$AACGATAGCGG
        TAGCGGTAGA$AACGA
        """

        word = 'AACGATAGCGGTAGA$'
        order, alphabet = suffix_array.Util._sort_chars(word)
        eq_class = suffix_array.Util._compute_char_classes(word, order)
        length = 1
        new_order = suffix_array.Util._sort_double_cyclic_shifts(word,
                                                                 length,
                                                                 order,
                                                                 eq_class)

        new_eq_class = suffix_array.Util._update_eq_classes(length,
                                                            new_order,
                                                            eq_class)

        self.assertEqual([ 15, 0, 1, 4, 6, 12, 14, 2, 8, 3, 7, 9, 10,
                          13, 5, 11, ], order)
        self.assertEqual([ 1, 1, 2, 3, 1, 4, 1, 3, 2, 3, 3, 4, 1, 3, 1, 0, ],
                         eq_class)
        self.assertEqual([ 15, 14, 0, 1, 6, 12, 4, 2, 8, 3, 13, 7, 9, 10,
                          5, 11, ],
                         new_order)
        self.assertEqual([ 2, 3, 6, 7, 5, 11, 4, 8, 6, 9, 10, 11, 4, 7, 1, 0, ],
                         new_eq_class)

class UtilSuffixArrayConstructionTestCase(unittest.TestCase):

    def setUp(self):
        pass

    def tearDown(self):
        pass

    def test_with_word(self):
        word = 'word'

        """
        Suffixes:

        word
        ord
        rd
        d

        Sorted suffixes:

        3 d
        1 ord
        2 rd
        0 word
        """

        self.assertEqual([ 3, 1, 2, 0, ],
                         self.construct_suffix_array_method(word))

    def test_with_gacz(self):
        word = 'GAC$'

        """
        Suffixes:

        GAC$
        AC$
        C$
        $

        Sorted suffixes:

        3 $
        1 AC$
        2 C$
        0 GAC$
        """

        self.assertEqual([ 3, 1, 2, 0, ],
                         self.construct_suffix_array_method(word))

    def test_with_gagagagaz(self):
        word = 'GAGAGAGA$'

        """
        Suffixes:

        GAGAGAGA$
        AGAGAGA$
        GAGAGA$
        AGAGA$
        GAGA$
        AGA$
        GA$
        A$
        $

        Sorted suffixes:

        8 $
        7 A$
        5 AGA$
        3 AGAGA$
        1 AGAGAGA$
        6 GA$
        4 GAGA$
        2 GAGAGA$
        0 GAGAGAGA$
        """

        self.assertEqual([ 8, 7, 5, 3, 1, 6, 4, 2, 0, ],
                         self.construct_suffix_array_method(word))

    def test_with_aacgatagcggtagaz(self):
        word = 'AACGATAGCGGTAGA$'

        """
        Suffixes:

        AACGATAGCGGTAGA$
        ACGATAGCGGTAGA$
        CGATAGCGGTAGA$
        GATAGCGGTAGA$
        ATAGCGGTAGA$
        TAGCGGTAGA$
        AGCGGTAGA$
        GCGGTAGA$
        CGGTAGA$
        GGTAGA$
        GTAGA$
        TAGA$
        AGA$
        GA$
        A$
        $

        Sorted suffixes:

        15 $
        14 A$
        0  AACGATAGCGGTAGA$
        1  ACGATAGCGGTAGA$
        12 AGA$
        6  AGCGGTAGA$
        4  ATAGCGGTAGA$
        2  CGATAGCGGTAGA$
        8  CGGTAGA$
        13 GA$
        3  GATAGCGGTAGA$
        7  GCGGTAGA$
        9  GGTAGA$
        10 GTAGA$
        11 TAGA$
        5  TAGCGGTAGA$
        """

        self.assertEqual([ 15, 14, 0, 1, 12, 6, 4, 2, 8, 13, 3, 7, 9, 10,
                          11, 5, ],
                         self.construct_suffix_array_method(word))

    def test_with_panamabananasz(self):
        word = 'panamabananas$'

        """
        Suffixes:

        panamabananas$
        anamabananas$
        namabananas$
        amabananas$
        mabananas$
        abananas$
        bananas$
        ananas$
        nanas$
        anas$
        nas$
        as$
        s$
        $

        Sorted suffixes:

        13 $
        5  abananas$
        3  amabananas$
        1  anamabananas$
        7  ananas$
        9  anas$
        11 as$
        6  bananas$
        4  mabananas$
        2  namabananas$
        8  nanas$
        10 nas$
        0  panamabananas$
        12 s$
        """

        self.assertEqual([ 13, 5, 3, 1, 7, 9, 11, 6, 4, 2, 8, 10, 0, 12, ],
                         self.construct_suffix_array_method(word))

    def test_with_aacgatagcggtagaz(self):
        word = 'AACGATAGCGGTAGA$'

        """
        Suffixes:

        AACGATAGCGGTAGA$
        ACGATAGCGGTAGA$
        CGATAGCGGTAGA$
        GATAGCGGTAGA$
        ATAGCGGTAGA$
        TAGCGGTAGA$
        AGCGGTAGA$
        GCGGTAGA$
        CGGTAGA$
        GGTAGA$
        GTAGA$
        TAGA$
        AGA$
        GA$
        A$
        $

        Sorted suffixes:

        15 $
        14 A$
        0  AACGATAGCGGTAGA$
        1  ACGATAGCGGTAGA$
        12 AGA$
        6  AGCGGTAGA$
        4  ATAGCGGTAGA$
        2  CGATAGCGGTAGA$
        8  CGGTAGA$
        13 GA$
        3  GATAGCGGTAGA$
        7  GCGGTAGA$
        9  GGTAGA$
        10 GTAGA$
        11 TAGA$
        5  TAGCGGTAGA$
        """

        self.assertEqual([ 15, 14, 0, 1, 12, 6, 4, 2, 8, 13, 3, 7, 9, 10,
                          11, 5, ],
                         self.construct_suffix_array_method(word))

class UtilConstructSuffixArrayTestCase(UtilSuffixArrayConstructionTestCase):
    def setUp(self):
        self.construct_suffix_array_method = \
                                        suffix_array.Util.construct_suffix_array

    def tearDown(self):
        pass

class UtilConstructSuffixArrayManberMyersTestCase(
                                           UtilSuffixArrayConstructionTestCase):
    def setUp(self):
        self.construct_suffix_array_method = \
                           suffix_array.Util.construct_suffix_array_manber_myers

    def tearDown(self):
        pass

class UtilConstructSuffixArrayCountSortTestCase(
                                           UtilSuffixArrayConstructionTestCase):
    def setUp(self):
        self.construct_suffix_array_method = \
                           suffix_array.Util.construct_suffix_array_count_sort

    def tearDown(self):
        pass

class UtilPatternMatchingWithSuffixArrayTestCase(unittest.TestCase):

    def setUp(self):
        pass

    def tearDown(self):
        pass

    def assert_pattern_result(self,
                              text,
                              pattern,
                              expected_suffix_array,
                              expected_pattern_range,
                              expected_pattern_positions):
        self.suffix_array = suffix_array.Util. \
                                         construct_suffix_array_count_sort(text)

        pattern_range = suffix_array.Util.pattern_range(text,
                                                        pattern,
                                                        self.suffix_array)

        self.assertEqual(expected_pattern_range, pattern_range)

        pattern_positions = suffix_array.Util. \
                           pattern_matching_with_suffix_array(text,
                                                              pattern,
                                                              self.suffix_array)

        self.assertEqual(expected_pattern_positions, pattern_positions)

    def test_with_panamabananasz(self):
        """
        p  a  n  a  m  a  b  a  n  a  n  a  s  $
        0  1  2  3  4  5  6  7  8  9  10 11 12 13

        Suffixes:

        panamabananas$
        anamabananas$
        namabananas$
        amabananas$
        mabananas$
        abananas$
        bananas$
        ananas$
        nanas$
        anas$
        nas$
        as$
        s$
        $

        Sorted suffixes:

        index order suffix
        0     13    $
        1     5     abananas$
        2     3     amabananas$
        3     1     anamabananas$
        4     7     ananas$
        5     9     anas$
        6     11    as$
        7     6     bananas$
        8     4     mabananas$
        9     2     namabananas$
        10    8     nanas$
        11    10    nas$
        12    0     panamabananas$
        13    12    s$
        """

        text = 'panamabananas$'
        expected_suffix_array = [ 13, 5, 3, 1, 7, 9, 11, 6, 4, 2, 8, 10,
                                 0, 12, ]

        pattern = 'a'
        expected_pattern_range = (1, 7)
        expected_pattern_positions = [ 5, 3, 1, 7, 9, 11, ]

        self.assert_pattern_result(text,
                                   pattern,
                                   expected_suffix_array,
                                   expected_pattern_range,
                                   expected_pattern_positions)

        pattern = 'pa'
        expected_pattern_range = (12, 13)
        expected_pattern_positions = [ 0, ]

        self.assert_pattern_result(text,
                                   pattern,
                                   expected_suffix_array,
                                   expected_pattern_range,
                                   expected_pattern_positions)

        pattern = 'na'
        expected_pattern_range = (9, 12)
        expected_pattern_positions = [ 2, 8, 10, ]

        self.assert_pattern_result(text,
                                   pattern,
                                   expected_suffix_array,
                                   expected_pattern_range,
                                   expected_pattern_positions)

        pattern = 'ana'
        expected_pattern_range = (3, 6)
        expected_pattern_positions = [ 1, 7, 9, ]

        self.assert_pattern_result(text,
                                   pattern,
                                   expected_suffix_array,
                                   expected_pattern_range,
                                   expected_pattern_positions)

        pattern = '$'
        expected_pattern_range = (0, 1)
        expected_pattern_positions = [ 13, ]

        self.assert_pattern_result(text,
                                   pattern,
                                   expected_suffix_array,
                                   expected_pattern_range,
                                   expected_pattern_positions)

        pattern = 's$'
        expected_pattern_range = (13, 14)
        expected_pattern_positions = [ 12, ]

        self.assert_pattern_result(text,
                                   pattern,
                                   expected_suffix_array,
                                   expected_pattern_range,
                                   expected_pattern_positions)

        pattern = 'x'
        expected_pattern_range = (14, 14)
        expected_pattern_positions = []

        self.assert_pattern_result(text,
                                   pattern,
                                   expected_suffix_array,
                                   expected_pattern_range,
                                   expected_pattern_positions)

        pattern = 'bach'
        expected_pattern_range = (7, 7)
        expected_pattern_positions = []

        self.assert_pattern_result(text,
                                   pattern,
                                   expected_suffix_array,
                                   expected_pattern_range,
                                   expected_pattern_positions)
        pattern = text
        expected_pattern_range = (12, 13)
        expected_pattern_positions = [ 0, ]

        self.assert_pattern_result(text,
                                   pattern,
                                   expected_suffix_array,
                                   expected_pattern_range,
                                   expected_pattern_positions)

        pattern = 'extra' + text
        expected_pattern_range = (8, 8)
        expected_pattern_positions = []

        self.assert_pattern_result(text,
                                   pattern,
                                   expected_suffix_array,
                                   expected_pattern_range,
                                   expected_pattern_positions)

        pattern = text + 'extra'
        expected_pattern_range = (13, 13)
        expected_pattern_positions = []

        self.assert_pattern_result(text,
                                   pattern,
                                   expected_suffix_array,
                                   expected_pattern_range,
                                   expected_pattern_positions)

class UtilComputeLongestCommonPrefixTestCase(unittest.TestCase):

    def setUp(self):
        pass

    def tearDown(self):
        pass

    def test_with_empty(self):
        """
        The LCP array contains the longest common prefixes between
        adjacent suffixes in the suffix array of string S.

        Empty strings have empty suffix and LCP arrays.
        """

        word = ''

        order = suffix_array.Util.construct_suffix_array_count_sort(word)

        self.assertEqual([], order)

        lcp = suffix_array.Util.compute_longest_common_prefix_array(word,
                                                                    order)

        self.assertEqual([], lcp)

    def test_with_z(self):
        """
        The LCP array contains the longest common prefixes between
        adjacent suffixes in the suffix array of string S.

        $
        0

        Suffixes:

        $

        Sorted suffixes:

        $

        index order suffix lcp
        0     1     $      -
        """

        word = '$'

        order = suffix_array.Util.construct_suffix_array_count_sort(word)

        self.assertEqual([ 0, ], order)

        lcp = suffix_array.Util.compute_longest_common_prefix_array(word,
                                                                    order)

        self.assertEqual([], lcp)

    def test_with_az(self):
        """
        The LCP array contains the longest common prefixes between
        adjacent suffixes in the suffix array of string S.

        a $
        0 1

        Suffixes:

        a$
        $

        Sorted suffixes:

        $
        a$

        index order suffix lcp
        0     1     $      -
        1     0     a$     0
        """

        word = 'a$'

        order = suffix_array.Util.construct_suffix_array_count_sort(word)

        self.assertEqual([ 1, 0, ], order)

        lcp = suffix_array.Util.compute_longest_common_prefix_array(word,
                                                                    order)

        self.assertEqual([ 0, ], lcp)

    def test_with_abz(self):
        """
        The LCP array contains the longest common prefixes between
        adjacent suffixes in the suffix array of string S.

        a b $
        0 1 2

        Suffixes:

        ab$
        b$
        $

        Sorted suffixes:

        $
        ab$
        b$

        index order suffix lcp
        0     2     $      -
        1     0     ab$    0
        2     1     b$     0
        """

        word = 'ab$'

        order = suffix_array.Util.construct_suffix_array_count_sort(word)

        self.assertEqual([ 2, 0, 1, ], order)

        lcp = suffix_array.Util.compute_longest_common_prefix_array(word,
                                                                    order)

        self.assertEqual([ 0, 0, ], lcp)

    def test_with_aaz(self):
        """
        The LCP array contains the longest common prefixes between
        adjacent suffixes in the suffix array of string S.

        a a $
        0 1 2

        Suffixes:

        aa$
        a$
        $

        Sorted suffixes:

        $
        a$
        aa$

        index order suffix lcp
        0     2     $      -
        1     1     a$     0
        2     0     aa$    1
        """

        word = 'aa$'

        order = suffix_array.Util.construct_suffix_array_count_sort(word)

        self.assertEqual([ 2, 1, 0, ], order)

        lcp = suffix_array.Util.compute_longest_common_prefix_array(word,
                                                                    order)

        self.assertEqual([ 0, 1, ], lcp)

    def test_with_abaz(self):
        """
        The LCP array contains the longest common prefixes between
        adjacent suffixes in the suffix array of string S.

        a b a $
        0 1 2 3

        Suffixes:

        aba$
        ba$
        a$
        $

        Sorted suffixes:

        $
        a$
        aba$
        ba$

        index order suffix lcp
        0     3     $      -
        1     2     a$     0
        2     0     aba$   1
        3     1     ba$    0
        """

        word = 'aba$'

        order = suffix_array.Util.construct_suffix_array_count_sort(word)

        self.assertEqual([ 3, 2, 0, 1, ], order)

        lcp = suffix_array.Util.compute_longest_common_prefix_array(word,
                                                                    order)

        self.assertEqual([ 0, 1, 0, ], lcp)

    def test_with_ababaaz(self):
        """
        The LCP array contains the longest common prefixes between
        adjacent suffixes in the suffix array of string S.

        a b a b a a $
        0 1 2 3 4 5 6

        Suffixes:

        ababaa$
        babaa$
        abaa$
        baa$
        aa$
        a$
        $

        Sorted suffixes:

        $
        a$
        aa$
        abaa$
        ababaa$
        baa$
        babaa$

        index order suffix   lcp
        0     6     $        -
        1     5     a$       0
        2     4     aa$      1
        3     2     abaa$    1
        4     0     ababaa$  3
        5     3     baa$     0
        6     1     babaa$   2
        """

        word = 'ababaa$'

        order = suffix_array.Util.construct_suffix_array_count_sort(word)

        self.assertEqual([ 6, 5, 4, 2, 0, 3, 1, ], order)

        lcp = suffix_array.Util.compute_longest_common_prefix_array(word,
                                                                    order)

        self.assertEqual([ 0, 1, 1, 3, 0, 2, ], lcp)

    def test_with_bananaz(self):
        """
        The LCP array contains the longest common prefixes between
        adjacent suffixes in the suffix array of string S.

        b a n a n a $
        0 1 2 3 4 5 6

        Suffixes:

        banana$
        anana$
        nana$
        ana$
        na$
        a$
        $

        Sorted suffixes:

        $
        a$
        ana$
        anana$
        banana$
        na$
        nana$

        index order suffix  lcp
        0     6     $       -
        1     5     a$      0
        2     3     ana$    1
        3     1     anana$  3
        4     0     banana$ 0
        5     4     na$     0
        6     2     nana$   2
        """

        word = 'banana$'

        order = suffix_array.Util.construct_suffix_array_count_sort(word)

        self.assertEqual([ 6, 5, 3, 1, 0, 4, 2, ], order)

        lcp = suffix_array.Util.compute_longest_common_prefix_array(word,
                                                                    order)

        self.assertEqual([ 0, 1, 3, 0, 0, 2, ], lcp)

class SuffixTreeNodeTestCase(unittest.TestCase):

    def setUp(self):
        pass

    def tearDown(self):
        pass

    def test_constructor(self):
        parent = 1

        node = suffix_array.SuffixTree.Node(parent)

        self.assertEqual(parent, node.parent)
        self.assertEqual([], node.children)

    def test_update_parent(self):
        parent = 1

        node = suffix_array.SuffixTree.Node(parent)

        self.assertEqual(parent, node.parent)
        self.assertEqual([], node.children)

        new_parent = 2

        node.update_parent(new_parent)

        self.assertEqual(new_parent, node.parent)
        self.assertEqual([], node.children)

    def test_add_child_once(self):
        parent = -1
        parent_node = suffix_array.SuffixTree.Node(parent)
        child = 1

        parent_node.add_child(child)

        self.assertEqual(parent, parent_node.parent)
        self.assertEqual([ child, ], parent_node.children)

    def test_add_child_several_times(self):
        parent = -1
        parent_node = suffix_array.SuffixTree.Node(parent)
        child1 = 1
        child2 = 2
        child3 = 3

        parent_node.add_child(child1)
        parent_node.add_child(child2)
        parent_node.add_child(child3)

        self.assertEqual(parent, parent_node.parent)
        self.assertEqual([ child1, child2, child3, ], parent_node.children)

    def test_remove_child_as_missing(self):
        parent = -1
        parent_node = suffix_array.SuffixTree.Node(parent)
        child = 1

        with self.assertRaisesRegex(ValueError,
                                    "list\.remove\(x\)\: x not in list"):
            parent_node.remove_child(child)

    def test_remove_child_once(self):
        parent = -1
        parent_node = suffix_array.SuffixTree.Node(parent)
        child = 1

        parent_node.add_child(child)

        self.assertEqual(parent, parent_node.parent)
        self.assertEqual([ child, ], parent_node.children)

        parent_node.remove_child(child)

        self.assertEqual(parent, parent_node.parent)
        self.assertEqual([], parent_node.children)

    def test_repr(self):
        parent = -1
        parent_node = suffix_array.SuffixTree.Node(parent)
        child1 = 1
        child2 = 2
        child3 = 3

        parent_node.add_child(child1)
        parent_node.add_child(child2)
        parent_node.add_child(child3)

        self.assertEqual('parent=-1, children=[1, 2, 3]',
                         repr(parent_node))

class SuffixTreeEdgeTestCase(unittest.TestCase):

    def setUp(self):
        pass

    def tearDown(self):
        pass

    def test_constructor(self):
        start = 1
        end = 2

        edge = suffix_array.SuffixTree.Edge(start, end)

        self.assertEqual(start, edge.start)
        self.assertEqual(end, edge.end)

    def test_repr(self):
        start = 1
        end = 2

        edge = suffix_array.SuffixTree.Edge(start, end)

        self.assertEqual('(start=1, end=2)',
                         repr(edge))

class SuffixTreeTestCase(unittest.TestCase):

    def setUp(self):
        pass

    def tearDown(self):
        pass

    def assert_number_of_nodes_and_edges(self, tree, number_of_nodes):
        self.assertEqual(number_of_nodes, len(tree._nodes))
        self.assertEqual(len(tree._nodes) - 1, len(tree._edges))

    def assert_items(self, expected_items, actual_items):
        try:
            self.assertEqual(len(expected_items), len(actual_items))
            expected_count = {}
            for expected_item in expected_items:
                if not expected_item in expected_count:
                    expected_count[expected_item] = 0
                expected_count[expected_item] += 1
            count = {}
            for item in actual_items:
                if not item in count:
                    count[item] = 0
                count[item] += 1

            for item in actual_items:
                self.assertEqual(expected_count[item],
                                 count[item],
                                 'Item ' + str(item) +
                                 ' has different counts.')
        except Exception:
            self.fail('Expected: {}, actual: {} '.format(expected_items,
                                                     actual_items))

    def test_constructor_with_az(self):
        """
        A  $
        0  1

        Suffixes:

        A$
        $

        Sorted suffixes:

        $
        A$

        index order suffix
        0     1     $
        1     0     A$
        """

        self.word = 'A$'

        self.suffix_array = suffix_array.Util. \
                                    construct_suffix_array_count_sort(self.word)

        self.assertEqual([ 1, 0, ],
                         self.suffix_array)

        self.lcp_array = suffix_array.Util. \
                          compute_longest_common_prefix_array(self.word,
                                                              self.suffix_array)

        self.assertEqual([ 0, ],
                         self.lcp_array)

        tree = suffix_array.SuffixTree(self.word,
                                       self.suffix_array,
                                       self.lcp_array)

        self.assertEqual(self.word, tree._word)
        self.assertEqual(self.suffix_array, tree._suffix_array)
        self.assertEqual(self.lcp_array, tree._lcp_array)

        self.assert_number_of_nodes_and_edges(tree, 3)

        expected_nodes = []
        expected_edges = []

        self.assertEqual(-1, tree._nodes[0].parent)
        self.assertEqual([ 1, 2, ], tree._nodes[0].children)
        expected_nodes.append(0)

        self.assertEqual(0, tree._nodes[1].parent)
        self.assertEqual([], tree._nodes[1].children)
        expected_nodes.append(1)

        self.assertEqual(0, tree._nodes[2].parent)
        self.assertEqual([], tree._nodes[2].children)
        expected_nodes.append(2)

        self.assert_items(expected_nodes, list(range(len(tree._nodes))))

        edge = tree._edges[(0, 1)]
        self.assertEqual(1, edge._start)
        self.assertEqual(2, edge._end)
        self.assertEqual('$', self.word[edge._start:edge._end])
        expected_edges.append(edge)

        edge = tree._edges[(0, 2)]
        self.assertEqual(0, edge._start)
        self.assertEqual(2, edge._end)
        self.assertEqual('A$', self.word[edge._start:edge._end])
        expected_edges.append(edge)

        self.assert_items(expected_edges, tree._edges.values())

        expected_edge_strings = [ '$', 'A$', ]

        self.assert_items(expected_edge_strings, tree.edge_strings())

    def test_constructor_with_aaaz(self):
        """
        A  A  A  $
        0  1  2  3

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

        index order suffix
        0     3     $
        1     2     A$
        2     1     AA$
        3     0     AAA$
        """

        self.word = 'AAA$'

        self.suffix_array = suffix_array.Util. \
                                    construct_suffix_array_count_sort(self.word)

        self.assertEqual([ 3, 2, 1, 0, ],
                         self.suffix_array)

        self.lcp_array = suffix_array.Util. \
                          compute_longest_common_prefix_array(self.word,
                                                              self.suffix_array)

        self.assertEqual([ 0, 1, 2, ],
                         self.lcp_array)

        tree = suffix_array.SuffixTree(self.word,
                                       self.suffix_array,
                                       self.lcp_array)

        self.assertEqual(self.word, tree._word)
        self.assertEqual(self.suffix_array, tree._suffix_array)
        self.assertEqual(self.lcp_array, tree._lcp_array)

        self.assert_number_of_nodes_and_edges(tree, 7)

        expected_nodes = []
        expected_edges = []

        self.assertEqual(-1, tree._nodes[0].parent)
        self.assertEqual([ 1, 3, ], tree._nodes[0].children)
        expected_nodes.append(0)

        self.assertEqual(0, tree._nodes[1].parent)
        self.assertEqual([], tree._nodes[1].children)
        expected_nodes.append(1)

        self.assertEqual(0, tree._nodes[3].parent)
        self.assertEqual([ 2, 5, ], tree._nodes[3].children)
        expected_nodes.append(3)

        self.assertEqual(3, tree._nodes[2].parent)
        self.assertEqual([], tree._nodes[2].children)
        expected_nodes.append(2)

        self.assertEqual(3, tree._nodes[5].parent)
        self.assertEqual([ 4, 6, ], tree._nodes[5].children)
        expected_nodes.append(5)

        self.assertEqual(5, tree._nodes[4].parent)
        self.assertEqual([], tree._nodes[4].children)
        expected_nodes.append(4)

        self.assertEqual(5, tree._nodes[6].parent)
        self.assertEqual([], tree._nodes[6].children)
        expected_nodes.append(6)

        self.assert_items(expected_nodes, list(range(len(tree._nodes))))

        edge = tree._edges[(0, 1)]
        self.assertEqual(3, edge._start)
        self.assertEqual(4, edge._end)
        self.assertEqual('$', self.word[edge._start:edge._end])
        expected_edges.append(edge)

        edge = tree._edges[(0, 3)]
        self.assertEqual(2, edge._start)
        self.assertEqual(3, edge._end)
        self.assertEqual('A', self.word[edge._start:edge._end])
        expected_edges.append(edge)

        edge = tree._edges[(3, 2)]
        self.assertEqual(3, edge._start)
        self.assertEqual(4, edge._end)
        self.assertEqual('$', self.word[edge._start:edge._end])
        expected_edges.append(edge)

        edge = tree._edges[(3, 5)]
        self.assertEqual(2, edge._start)
        self.assertEqual(3, edge._end)
        self.assertEqual('A', self.word[edge._start:edge._end])
        expected_edges.append(edge)

        edge = tree._edges[(5, 4)]
        self.assertEqual(3, edge._start)
        self.assertEqual(4, edge._end)
        self.assertEqual('$', self.word[edge._start:edge._end])
        expected_edges.append(edge)

        edge = tree._edges[(5, 6)]
        self.assertEqual(2, edge._start)
        self.assertEqual(4, edge._end)
        self.assertEqual('A$', self.word[edge._start:edge._end])
        expected_edges.append(edge)

        self.assert_items(expected_edges, tree._edges.values())

        expected_edge_strings = [ '$', '$', '$', 'A', 'A', 'A$', ]

        self.assert_items(expected_edge_strings, tree.edge_strings())

    def test_constructor_with_gtagtz(self):
        """
        G  T  A  G  T  $
        0  1  2  3  4  5

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

        index order suffix
        0     5     $
        1     2     AGT$
        2     3     GT$
        3     0     GTAGT$
        4     4     T$
        5     1     TAGT$
        """

        self.word = 'GTAGT$'

        self.suffix_array = suffix_array.Util. \
                                    construct_suffix_array_count_sort(self.word)

        self.assertEqual([ 5, 2, 3, 0, 4, 1, ],
                         self.suffix_array)

        self.lcp_array = suffix_array.Util. \
                          compute_longest_common_prefix_array(self.word,
                                                              self.suffix_array)

        self.assertEqual([ 0, 0, 2, 0, 1, ],
                         self.lcp_array)

        tree = suffix_array.SuffixTree(self.word,
                                       self.suffix_array,
                                       self.lcp_array)

        self.assertEqual(self.word, tree._word)
        self.assertEqual(self.suffix_array, tree._suffix_array)
        self.assertEqual(self.lcp_array, tree._lcp_array)

        self.assert_number_of_nodes_and_edges(tree, 9)

        expected_nodes = []
        expected_edges = []

        self.assertEqual(-1, tree._nodes[0].parent)
        self.assertEqual([ 1, 2, 4, 7, ], tree._nodes[0].children)
        expected_nodes.append(0)

        self.assertEqual(0, tree._nodes[1].parent)
        self.assertEqual([], tree._nodes[1].children)
        expected_nodes.append(1)

        self.assertEqual(0, tree._nodes[2].parent)
        self.assertEqual([], tree._nodes[2].children)
        expected_nodes.append(2)

        self.assertEqual(0, tree._nodes[4].parent)
        self.assertEqual([ 3, 5, ], tree._nodes[4].children)
        expected_nodes.append(4)

        self.assertEqual(0, tree._nodes[7].parent)
        self.assertEqual([ 6, 8, ], tree._nodes[7].children)
        expected_nodes.append(7)

        self.assertEqual(4, tree._nodes[3].parent)
        self.assertEqual([], tree._nodes[3].children)
        expected_nodes.append(3)

        self.assertEqual(4, tree._nodes[5].parent)
        self.assertEqual([], tree._nodes[5].children)
        expected_nodes.append(5)

        self.assertEqual(7, tree._nodes[6].parent)
        self.assertEqual([], tree._nodes[6].children)
        expected_nodes.append(6)

        self.assertEqual(7, tree._nodes[8].parent)
        self.assertEqual([], tree._nodes[8].children)
        expected_nodes.append(8)

        self.assert_items(expected_nodes, list(range(len(tree._nodes))))

        edge = tree._edges[(0, 1)]
        self.assertEqual(5, edge._start)
        self.assertEqual(6, edge._end)
        self.assertEqual('$', self.word[edge._start:edge._end])
        expected_edges.append(edge)

        edge = tree._edges[(0, 2)]
        self.assertEqual(2, edge._start)
        self.assertEqual(6, edge._end)
        self.assertEqual('AGT$', self.word[edge._start:edge._end])
        expected_edges.append(edge)

        edge = tree._edges[(0, 4)]
        self.assertEqual(3, edge._start)
        self.assertEqual(5, edge._end)
        self.assertEqual('GT', self.word[edge._start:edge._end])
        expected_edges.append(edge)

        edge = tree._edges[(0, 7)]
        self.assertEqual(4, edge._start)
        self.assertEqual(5, edge._end)
        self.assertEqual('T', self.word[edge._start:edge._end])
        expected_edges.append(edge)

        edge = tree._edges[(4, 3)]
        self.assertEqual(5, edge._start)
        self.assertEqual(6, edge._end)
        self.assertEqual('$', self.word[edge._start:edge._end])
        expected_edges.append(edge)

        edge = tree._edges[(4, 5)]
        self.assertEqual(2, edge._start)
        self.assertEqual(6, edge._end)
        self.assertEqual('AGT$', self.word[edge._start:edge._end])
        expected_edges.append(edge)

        edge = tree._edges[(7, 6)]
        self.assertEqual(5, edge._start)
        self.assertEqual(6, edge._end)
        self.assertEqual('$', self.word[edge._start:edge._end])
        expected_edges.append(edge)

        edge = tree._edges[(7, 8)]
        self.assertEqual(2, edge._start)
        self.assertEqual(6, edge._end)
        self.assertEqual('AGT$', self.word[edge._start:edge._end])
        expected_edges.append(edge)

        self.assert_items(expected_edges, tree._edges.values())

        expected_edge_strings = [ '$', '$', '$', 'AGT$', 'AGT$', 'AGT$',
                                 'GT', 'T', ]

        self.assert_items(expected_edge_strings, tree.edge_strings())

    def test_constructor_with_panamabananasz(self):
        """
        p  a  n  a  m  a  b  a  n  a  n  a  s  $
        0  1  2  3  4  5  6  7  8  9  10 11 12 13

        Suffixes:

        panamabananas$
        anamabananas$
        namabananas$
        amabananas$
        mabananas$
        abananas$
        bananas$
        ananas$
        nanas$
        anas$
        nas$
        as$
        s$
        $

        Sorted suffixes:

        index order suffix
        0     13    $
        1     5     abananas$
        2     3     amabananas$
        3     1     anamabananas$
        4     7     ananas$
        5     9     anas$
        6     11    as$
        7     6     bananas$
        8     4     mabananas$
        9     2     namabananas$
        10    8     nanas$
        11    10    nas$
        12    0     panamabananas$
        13    12    s$
        """

        self.word = 'panamabananas$'

        self.suffix_array = suffix_array.Util. \
                                    construct_suffix_array_count_sort(self.word)

        self.assertEqual([ 13, 5, 3, 1, 7, 9, 11, 6, 4, 2, 8, 10, 0, 12, ],
                         self.suffix_array)

        self.lcp_array = suffix_array.Util. \
                          compute_longest_common_prefix_array(self.word,
                                                              self.suffix_array)

        self.assertEqual([ 0, 1, 1, 3, 3, 1, 0, 0, 0, 2, 2, 0, 0, ],
                         self.lcp_array)

        tree = suffix_array.SuffixTree(self.word,
                                       self.suffix_array,
                                       self.lcp_array)

        self.assertEqual(self.word, tree._word)
        self.assertEqual(self.suffix_array, tree._suffix_array)
        self.assertEqual(self.lcp_array, tree._lcp_array)

        self.assert_number_of_nodes_and_edges(tree, 18)

        expected_nodes = []
        expected_edges = []

        self.assertEqual(-1, tree._nodes[0].parent)
        self.assertEqual([ 1, 3, 10, 11, 13, 16, 17, ],
                         tree._nodes[0].children)
        expected_nodes.append(0)

        self.assertEqual(0, tree._nodes[1].parent)
        self.assertEqual([], tree._nodes[1].children)
        expected_nodes.append(1)

        self.assertEqual(0, tree._nodes[3].parent)
        self.assertEqual([ 2, 4, 6, 9, ], tree._nodes[3].children)
        expected_nodes.append(3)

        self.assertEqual(0, tree._nodes[10].parent)
        self.assertEqual([], tree._nodes[10].children)
        expected_nodes.append(10)

        self.assertEqual(0, tree._nodes[11].parent)
        self.assertEqual([], tree._nodes[11].children)
        expected_nodes.append(11)

        self.assertEqual(0, tree._nodes[13].parent)
        self.assertEqual([ 12, 14, 15, ], tree._nodes[13].children)
        expected_nodes.append(13)

        self.assertEqual(0, tree._nodes[16].parent)
        self.assertEqual([], tree._nodes[16].children)
        expected_nodes.append(16)

        self.assertEqual(0, tree._nodes[17].parent)
        self.assertEqual([], tree._nodes[17].children)
        expected_nodes.append(17)

        self.assertEqual(3, tree._nodes[2].parent)
        self.assertEqual([], tree._nodes[2].children)
        expected_nodes.append(2)

        self.assertEqual(3, tree._nodes[4].parent)
        self.assertEqual([], tree._nodes[4].children)
        expected_nodes.append(4)

        self.assertEqual(3, tree._nodes[6].parent)
        self.assertEqual([ 5, 7, 8, ], tree._nodes[6].children)
        expected_nodes.append(6)

        self.assertEqual(3, tree._nodes[9].parent)
        self.assertEqual([], tree._nodes[9].children)
        expected_nodes.append(9)

        self.assertEqual(13, tree._nodes[12].parent)
        self.assertEqual([], tree._nodes[12].children)
        expected_nodes.append(12)

        self.assertEqual(13, tree._nodes[14].parent)
        self.assertEqual([], tree._nodes[14].children)
        expected_nodes.append(14)

        self.assertEqual(13, tree._nodes[15].parent)
        self.assertEqual([], tree._nodes[15].children)
        expected_nodes.append(15)

        self.assertEqual(6, tree._nodes[5].parent)
        self.assertEqual([], tree._nodes[5].children)
        expected_nodes.append(5)

        self.assertEqual(6, tree._nodes[7].parent)
        self.assertEqual([], tree._nodes[7].children)
        expected_nodes.append(7)

        self.assertEqual(6, tree._nodes[8].parent)
        self.assertEqual([], tree._nodes[8].children)
        expected_nodes.append(8)

        self.assert_items(expected_nodes, list(range(len(tree._nodes))))

        edge = tree._edges[(0, 1)]
        self.assertEqual(13, edge._start)
        self.assertEqual(14, edge._end)
        self.assertEqual('$', self.word[edge._start:edge._end])
        expected_edges.append(edge)

        edge = tree._edges[(0, 3)]
        self.assertEqual(5, edge._start)
        self.assertEqual(6, edge._end)
        self.assertEqual('a', self.word[edge._start:edge._end])
        expected_edges.append(edge)

        edge = tree._edges[(0, 10)]
        self.assertEqual(6, edge._start)
        self.assertEqual(14, edge._end)
        self.assertEqual('bananas$', self.word[edge._start:edge._end])
        expected_edges.append(edge)

        edge = tree._edges[(0, 11)]
        self.assertEqual(4, edge._start)
        self.assertEqual(14, edge._end)
        self.assertEqual('mabananas$', self.word[edge._start:edge._end])
        expected_edges.append(edge)

        edge = tree._edges[(0, 13)]
        self.assertEqual(2, edge._start)
        self.assertEqual(4, edge._end)
        self.assertEqual('na', self.word[edge._start:edge._end])
        expected_edges.append(edge)

        edge = tree._edges[(0, 16)]
        self.assertEqual(0, edge._start)
        self.assertEqual(14, edge._end)
        self.assertEqual('panamabananas$', self.word[edge._start:edge._end])
        expected_edges.append(edge)

        edge = tree._edges[(0, 17)]
        self.assertEqual(12, edge._start)
        self.assertEqual(14, edge._end)
        self.assertEqual('s$', self.word[edge._start:edge._end])
        expected_edges.append(edge)

        edge = tree._edges[(3, 2)]
        self.assertEqual(6, edge._start)
        self.assertEqual(14, edge._end)
        self.assertEqual('bananas$', self.word[edge._start:edge._end])
        expected_edges.append(edge)

        edge = tree._edges[(3, 4)]
        self.assertEqual(4, edge._start)
        self.assertEqual(14, edge._end)
        self.assertEqual('mabananas$', self.word[edge._start:edge._end])
        expected_edges.append(edge)

        edge = tree._edges[(3, 6)]
        self.assertEqual(2, edge._start)
        self.assertEqual(4, edge._end)
        self.assertEqual('na', self.word[edge._start:edge._end])
        expected_edges.append(edge)

        edge = tree._edges[(3, 9)]
        self.assertEqual(12, edge._start)
        self.assertEqual(14, edge._end)
        self.assertEqual('s$', self.word[edge._start:edge._end])
        expected_edges.append(edge)

        edge = tree._edges[(13, 12)]
        self.assertEqual(4, edge._start)
        self.assertEqual(14, edge._end)
        self.assertEqual('mabananas$', self.word[edge._start:edge._end])
        expected_edges.append(edge)

        edge = tree._edges[(13, 14)]
        self.assertEqual(10, edge._start)
        self.assertEqual(14, edge._end)
        self.assertEqual('nas$', self.word[edge._start:edge._end])
        expected_edges.append(edge)

        edge = tree._edges[(13, 15)]
        self.assertEqual(12, edge._start)
        self.assertEqual(14, edge._end)
        self.assertEqual('s$', self.word[edge._start:edge._end])
        expected_edges.append(edge)

        edge = tree._edges[(6, 5)]
        self.assertEqual(4, edge._start)
        self.assertEqual(14, edge._end)
        self.assertEqual('mabananas$', self.word[edge._start:edge._end])
        expected_edges.append(edge)

        edge = tree._edges[(6, 7)]
        self.assertEqual(10, edge._start)
        self.assertEqual(14, edge._end)
        self.assertEqual('nas$', self.word[edge._start:edge._end])
        expected_edges.append(edge)

        edge = tree._edges[(6, 8)]
        self.assertEqual(12, edge._start)
        self.assertEqual(14, edge._end)
        self.assertEqual('s$', self.word[edge._start:edge._end])
        expected_edges.append(edge)

        self.assert_items(expected_edges, tree._edges.values())

        expected_edge_strings = [ '$', 'a', 'bananas$', 'bananas$',
                                 'mabananas$', 'mabananas$', 'mabananas$',
                                 'mabananas$', 'na', 'na', 'nas$', 'nas$',
                                 's$', 's$', 's$', 's$', 'panamabananas$', ]

        self.assert_items(expected_edge_strings, tree.edge_strings())

    def test_node_and_edge_words_with_aaaz(self):
        self.word = 'AAA$'

        self.suffix_array = suffix_array.Util. \
                                    construct_suffix_array_count_sort(self.word)

        self.assertEqual([ 3, 2, 1, 0, ],
                         self.suffix_array)

        self.lcp_array = suffix_array.Util. \
                          compute_longest_common_prefix_array(self.word,
                                                              self.suffix_array)

        self.assertEqual([ 0, 1, 2, ],
                         self.lcp_array)

        tree = suffix_array.SuffixTree(self.word,
                                       self.suffix_array,
                                       self.lcp_array)

        self.assert_number_of_nodes_and_edges(tree, 7)

        self.assertEqual(-1, tree._nodes[0].parent)
        self.assertEqual([ 1, 3, ], tree._nodes[0].children)
        self.assertEqual('', tree.node_word(0))

        self.assertEqual(0, tree._nodes[1].parent)
        self.assertEqual([], tree._nodes[1].children)
        self.assertEqual('$', tree.node_word(1))

        self.assertEqual(0, tree._nodes[3].parent)
        self.assertEqual([ 2, 5, ], tree._nodes[3].children)
        self.assertEqual('A', tree.node_word(3))

        self.assertEqual(3, tree._nodes[2].parent)
        self.assertEqual([], tree._nodes[2].children)
        self.assertEqual('A$', tree.node_word(2))

        self.assertEqual(3, tree._nodes[5].parent)
        self.assertEqual([ 4, 6, ], tree._nodes[5].children)
        self.assertEqual('AA', tree.node_word(5))

        self.assertEqual(5, tree._nodes[4].parent)
        self.assertEqual([], tree._nodes[4].children)
        self.assertEqual('AA$', tree.node_word(4))

        self.assertEqual(5, tree._nodes[6].parent)
        self.assertEqual([], tree._nodes[6].children)
        self.assertEqual('AAA$', tree.node_word(6))

        edge = tree._edges[(0, 1)]
        self.assertEqual(3, edge._start)
        self.assertEqual(4, edge._end)
        self.assertEqual('$', self.word[edge._start:edge._end])
        self.assertEqual('$', tree.edge_word(edge))

        edge = tree._edges[(0, 3)]
        self.assertEqual(2, edge._start)
        self.assertEqual(3, edge._end)
        self.assertEqual('A', self.word[edge._start:edge._end])
        self.assertEqual('A', tree.edge_word(edge))

        edge = tree._edges[(3, 2)]
        self.assertEqual(3, edge._start)
        self.assertEqual(4, edge._end)
        self.assertEqual('$', self.word[edge._start:edge._end])
        self.assertEqual('$', tree.edge_word(edge))

        edge = tree._edges[(3, 5)]
        self.assertEqual(2, edge._start)
        self.assertEqual(3, edge._end)
        self.assertEqual('A', self.word[edge._start:edge._end])
        self.assertEqual('A', tree.edge_word(edge))

        edge = tree._edges[(5, 4)]
        self.assertEqual(3, edge._start)
        self.assertEqual(4, edge._end)
        self.assertEqual('$', self.word[edge._start:edge._end])
        self.assertEqual('$', tree.edge_word(edge))

        edge = tree._edges[(5, 6)]
        self.assertEqual(2, edge._start)
        self.assertEqual(4, edge._end)
        self.assertEqual('A$', self.word[edge._start:edge._end])
        self.assertEqual('A$', tree.edge_word(edge))

    def test_node_depth_with_aaaz(self):
        self.word = 'AAA$'

        self.suffix_array = suffix_array.Util. \
                                    construct_suffix_array_count_sort(self.word)

        self.assertEqual([ 3, 2, 1, 0, ],
                         self.suffix_array)

        self.lcp_array = suffix_array.Util. \
                          compute_longest_common_prefix_array(self.word,
                                                              self.suffix_array)

        self.assertEqual([ 0, 1, 2, ],
                         self.lcp_array)

        tree = suffix_array.SuffixTree(self.word,
                                       self.suffix_array,
                                       self.lcp_array)

        self.assert_number_of_nodes_and_edges(tree, 7)

        self.assertEqual(-1, tree._nodes[0].parent)
        self.assertEqual([ 1, 3, ], tree._nodes[0].children)
        self.assertEqual('', tree.node_word(0))
        self.assertEqual(0, tree.node_depth(0))

        self.assertEqual(0, tree._nodes[1].parent)
        self.assertEqual([], tree._nodes[1].children)
        self.assertEqual('$', tree.node_word(1))
        self.assertEqual(0, tree.node_depth(1))

        self.assertEqual(0, tree._nodes[3].parent)
        self.assertEqual([ 2, 5, ], tree._nodes[3].children)
        self.assertEqual('A', tree.node_word(3))
        self.assertEqual(1, tree.node_depth(3))

        self.assertEqual(3, tree._nodes[2].parent)
        self.assertEqual([], tree._nodes[2].children)
        self.assertEqual('A$', tree.node_word(2))
        self.assertEqual(1, tree.node_depth(2))

        self.assertEqual(3, tree._nodes[5].parent)
        self.assertEqual([ 4, 6, ], tree._nodes[5].children)
        self.assertEqual('AA', tree.node_word(5))
        self.assertEqual(2, tree.node_depth(5))

        self.assertEqual(5, tree._nodes[4].parent)
        self.assertEqual([], tree._nodes[4].children)
        self.assertEqual('AA$', tree.node_word(4))
        self.assertEqual(2, tree.node_depth(4))

        self.assertEqual(5, tree._nodes[6].parent)
        self.assertEqual([], tree._nodes[6].children)
        self.assertEqual('AAA$', tree.node_word(6))
        self.assertEqual(3, tree.node_depth(6))

if __name__ == '__main__':
    class_names = [
                      UtilHelpersTestCase,
                      UtilConstructSuffixArrayTestCase,
                      UtilConstructSuffixArrayManberMyersTestCase,
                      UtilConstructSuffixArrayCountSortTestCase,
                      UtilPatternMatchingWithSuffixArrayTestCase,
                      UtilComputeLongestCommonPrefixTestCase,
                    SuffixTreeNodeTestCase,
                    SuffixTreeEdgeTestCase,
                      SuffixTreeTestCase,
                  ]

    suite = unittest.TestSuite()

    for c in class_names:
        suite.addTest(unittest.defaultTestLoader.loadTestsFromTestCase(c))

    unittest.TextTestRunner().run(suite)
