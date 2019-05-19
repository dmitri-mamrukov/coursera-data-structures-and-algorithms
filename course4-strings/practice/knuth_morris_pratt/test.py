#!/usr/bin/python3

import unittest

import knuth_morris_pratt

class UtilHelpersTestCase(unittest.TestCase):

    def setUp(self):
        pass

    def tearDown(self):
        pass

    def assert_compute_prefix_function(self, pattern, expected_result):
        result = knuth_morris_pratt.Util._compute_prefix_function(pattern)

        self.assertEqual(len(expected_result), len(result))
        self.assertEqual(expected_result, result)

    def test_compute_prefix_function_of_empty_string(self):
        pattern = ''

        self.assert_compute_prefix_function(pattern,
                                            [])

    def test_compute_prefix_function_of_a(self):
        pattern = 'a'

        self.assert_compute_prefix_function(pattern,
                                            [ 0, ])

    def test_compute_prefix_function_of_ab(self):
        pattern = 'ab'

        self.assert_compute_prefix_function(pattern,
                                            [ 0, 0, ])

    def test_compute_prefix_function_of_abc(self):
        pattern = 'abc'

        self.assert_compute_prefix_function(pattern,
                                            [ 0, 0, 0, ])

    def test_compute_prefix_function_of_aa(self):
        pattern = 'aa'

        self.assert_compute_prefix_function(pattern,
                                            [ 0, 1, ])

    def test_compute_prefix_function_of_axa(self):
        pattern = 'axa'

        self.assert_compute_prefix_function(pattern,
                                            [ 0, 0, 1, ])

    def test_compute_prefix_function_of_abababcaab(self):
        pattern = 'abababcaab'

        self.assert_compute_prefix_function(pattern,
                                            [ 0, 0, 1, 2, 3, 4, 0, 1, 1, 2, ])

    def test_compute_prefix_function_of_abababca(self):
        pattern = 'abababca'

        self.assert_compute_prefix_function(pattern,
                                            [ 0, 0, 1, 2, 3, 4, 0, 1, ])

    def test_compute_prefix_function_of_abrazabracadabra(self):
        pattern = 'abra$abracadabra'

        self.assert_compute_prefix_function(pattern,
                                            [ 0, 0, 0, 1, 0, 1, 2, 3, 4, 0, 1,
                                             0, 1, 2, 3, 4, ])

class FindAllOccurrencesTestCase(unittest.TestCase):

    def setUp(self):
        pass

    def tearDown(self):
        pass

    def test_with_empty_and_abracadabra(self):
        pattern = ''
        text = 'abracadabra'

        self.assertEqual([ 0, 1, 2, 3, 4, 5, 6, 7, 8, 9, 10, 11, ],
                         self.find_all_occurrences_method(pattern, text))

    def test_with_abra_and_empty(self):
        pattern = 'abra'
        text = ''

        self.assertEqual([],
                         self.find_all_occurrences_method(pattern, text))

    def test_with_abra_and_abracadabra(self):
        pattern = 'abra'
        text = 'abracadabra'

        self.assertEqual([ 0, 7, ],
                         self.find_all_occurrences_method(pattern, text))

    def test_with_ata_and_cgatatatccatag(self):
        pattern = 'ATA'
        text = 'CGATATATCCATAG'

        self.assertEqual([ 2, 4, 10, ],
                         self.find_all_occurrences_method(pattern, text))

class FindAllOccurrencesKnuthMorrisPrattTestCase(FindAllOccurrencesTestCase):
    def setUp(self):
        self.find_all_occurrences_method = \
                 knuth_morris_pratt.Util.find_all_occurrences_knuth_morris_pratt

    def tearDown(self):
        pass

    def test_with_special_symbol_in_pattern(self):
        pattern = 'pat$tern'
        text = 'text'

        with self.assertRaisesRegex(ValueError,
                                    'The pattern contains \$.'):
            self.find_all_occurrences_method(pattern, text)

    def test_with_special_symbol_in_text(self):
        pattern = 'pattern'
        text = 'te$xt'

        with self.assertRaisesRegex(ValueError,
                                    'The text contains \$.'):
            self.find_all_occurrences_method(pattern, text)

class FindAllOccurrencesBruteForceTestCase(FindAllOccurrencesTestCase):
    def setUp(self):
        self.find_all_occurrences_method = \
                 knuth_morris_pratt.Util.find_all_occurrences_brute_force

    def tearDown(self):
        pass

if __name__ == '__main__':
    class_names = [
                      UtilHelpersTestCase,
                      FindAllOccurrencesKnuthMorrisPrattTestCase,
                      FindAllOccurrencesBruteForceTestCase,
                  ]

    suite = unittest.TestSuite()

    for c in class_names:
        suite.addTest(unittest.defaultTestLoader.loadTestsFromTestCase(c))

    unittest.TextTestRunner().run(suite)
