#!/usr/bin/python3

import math
import random
import unittest

import suffix_array_matching

class Util():

    @staticmethod
    def _compute_prefix_function(pattern):
        """
        Computes the prefix function on the pattern.

        Definition: The border of string S is a prefix, which is equal to a
                    suffix of S, but not equal to the whole S.

                    Examples:

                    'a' is a border of 'arba'
                    'ab' is a border of 'abcdab'
                    'abab' is a border of 'ababab'
                    'ab' is not a border of 'ab'

        Definition: The prefix function of a string P is a function s(i) that
                    for each i returns the length of the longest border of the
                    prefix P[0..i].

                    Example:

                    P: a b a b a b c a a b
                    s: 0 0 1 2 3 4 0 1 1 2
        """

        prefix_function = [ 0 ] * len(pattern)
        border = 0

        for i in range(1, len(pattern)):
            while (border > 0) and (pattern[i] != pattern[border]):
                border = prefix_function[border - 1]

            if pattern[i] == pattern[border]:
                border += 1
            else:
                border = 0

            prefix_function[i] = border

        return prefix_function

    @staticmethod
    def find_all_occurrences_knuth_morris_pratt(pattern, text):
        """
        Finds all occurrences of the pattern in the text.

        Uses the Knuth-Morris-Pratt algorithm.
        """

        if '$' in pattern:
            raise ValueError('The pattern contains $.')
        if '$' in text:
            raise ValueError('The text contains $.')

        if pattern == '':
            return list(range(0, 1 + len(text)))

        work_text = pattern + '$' + text
        prefix_function = Util._compute_prefix_function(work_text)

        result = []
        for i in range(len(pattern) + 1, len(work_text)):
            if prefix_function[i] == len(pattern):
                result.append(i - 2 * len(pattern))

        return result

class StressTestCase(unittest.TestCase):

    MAX_LENGTH_TEXT = math.pow(10, 5)
    MAX_LENGTH_PATTERN = math.pow(10, 5)
    NUM_OF_PATTERNS = math.pow(10, 1)

    def setUp(self):
        self.solver = suffix_array_matching.Solver()
        self.solver._input = self.generate_input
        self.solver._output = self.accumulate_output
        self.output_list = []
        self.index = 0

    def tearDown(self):
        pass

    def accumulate_output(self, text):
        return self.output_list.append(text)

    def generate_input(self):
        line = self.input_list[self.index]
        self.index += 1

        return line

    def assert_result(self, expected_result):
        expected_items = expected_result[0].split()
        actual_items = self.output_list[0].split()
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

    def create_text_and_patterns(self):
        alphabet = 'ACGT'

        text_length = random.randint(1, StressTestCase.MAX_LENGTH_TEXT)
        text = ''
        for i in range(text_length):
            pos = random.randint(0, len(alphabet) - 1)
            text += alphabet[pos]

        patterns = []
        num_of_patterns = random.randint(1, StressTestCase.NUM_OF_PATTERNS)
        for i in range(num_of_patterns):
            pattern_length = random.randint(0,
                                            StressTestCase.MAX_LENGTH_PATTERN)
            pattern = ''
            for i in range(pattern_length):
                pos = random.randint(0, len(alphabet) - 1)
                pattern += alphabet[pos]
            patterns.append(pattern)

        pattern_line = ' '.join(patterns)
        input_list = [ text, str(num_of_patterns), pattern_line, ]
        self.input_list = input_list
        self.output_list = []

    def generate_expected_result(self):
        text = self.input_list[0]
        patterns = self.input_list[2].split()

        unique_positions = set()
        for pattern in patterns:
            positions = Util.find_all_occurrences_knuth_morris_pratt(pattern,
                                                                     text)
            unique_positions |= set(positions)

        result = map(str, list(unique_positions))

        return [' '.join(result)]

    def test(self):
        while True:
            self.output_list.clear()
            self.index = 0

            self.create_text_and_patterns()

            expected_output = None

            try:
                self.solver.solve()

                print('solved and verifying...')

                expected_output = self.generate_expected_result()

                self.assert_result(expected_output)

                print('answer: {}\n'.format(self.output_list))
            except Exception as e:
                f = open('stress-test-failure.txt', 'w')

                f.write('input:\n')
                f.write(str(self.input_list))
                f.write('\noutput:\n')
                f.write(str(self.output_list))
                f.write('\nexpected output:\n')
                f.write(str(expected_output))

                f.close()

                raise e

if __name__ == '__main__':
    unittest.main()
