#!/usr/bin/python3

import io
import sys

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

class Solver:
    """
    Finds all occurrences of a pattern in a string.
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

        pattern = self._input()
        text = self._input()

        result = Util.find_all_occurrences_knuth_morris_pratt(pattern, text)
        string_result = [str(x) for x in result]

        self._output(' '.join(string_result))

if __name__ == '__main__':
    Solver().solve()