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
    def find_all_occurrences_brute_force(pattern, text):
        """
        Finds all occurrences of the pattern in the text.

        Uses the brute force algorithm.
        """

        result = []

        if len(text) < len(pattern):
            return result

        for i in range(0, len(text) - len(pattern) + 1):
            matched = True

            k = 0
            for j in range(i, i + len(pattern)):
                if pattern[k] != text[j]:
                     matched = False
                     break
                k += 1

            if matched:
                result.append(i)

        return result

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
