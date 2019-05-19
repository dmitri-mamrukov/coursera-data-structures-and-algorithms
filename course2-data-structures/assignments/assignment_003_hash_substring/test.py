#!/usr/bin/python3

import unittest

import hash_substring

class GetOccurrencesBaseTestCase(unittest.TestCase):

    def test_one_occurrence(self):
        pattern = 'Test'
        text = 'testTesttesT'

        self.assertEqual([ 4 ], self.method_under_test(pattern, text))

    def test_two_occurrences(self):
        pattern = 'aba'
        text = 'abacaba'

        self.assertEqual([ 0, 4 ], self.method_under_test(pattern, text))

    def test_three_occurrences(self):
        pattern = 'aaaaa'
        text = 'baaaaaaa'

        self.assertEqual([ 1, 2, 3 ], self.method_under_test(pattern, text))

class GetOccurrencesSlowTestCase(GetOccurrencesBaseTestCase):

    def setUp(self):
        self.method_under_test = hash_substring.get_occurrences_slow

    def tearDown(self):
        pass

class GetOccurrencesStillSlowTestCase(GetOccurrencesBaseTestCase):

    def setUp(self):
        self.method_under_test = hash_substring.get_occurrences_still_slow

    def tearDown(self):
        pass

class GetOccurrencesTestCase(GetOccurrencesBaseTestCase):

    def setUp(self):
        self.method_under_test = hash_substring.get_occurrences

    def tearDown(self):
        pass

if __name__ == '__main__':
    class_names = \
    [
        GetOccurrencesSlowTestCase,
        GetOccurrencesStillSlowTestCase,
        GetOccurrencesTestCase
    ]

    suite = unittest.TestSuite()

    for c in class_names:
        suite.addTest(unittest.defaultTestLoader.loadTestsFromTestCase(c))

    unittest.TextTestRunner().run(suite)
