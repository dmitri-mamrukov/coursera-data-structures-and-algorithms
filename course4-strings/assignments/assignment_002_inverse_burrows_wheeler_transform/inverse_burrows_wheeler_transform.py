#!/usr/bin/python3

import io
import sys

from functools import cmp_to_key

class Util():

    def __init__(self, word):
        """
        Initializes.
        """

        self._word = word
        self._length = len(word)

    def _cyclic_rotation_character(self, i, n):
        """
        Returns the nth character of the cyclic rotation (to the right)
        by i characters.

        Note: Negative indices mean those from the right end. For example, -1
        references the first element from the end, -2 the second from the end,
        -3 the third from the end, and so on.
        """

        return self._word[n - i % self._length]

    def _cyclic_compare(self, i, j):
        """
        Compares cyclic rotations without generating the entire rotation.
        """

        n = 0
        while n < self._length:
            i_char = self._cyclic_rotation_character(i, n)
            j_char = self._cyclic_rotation_character(j, n)
            if i_char == j_char:
                n += 1
            else:
                if i_char < j_char:
                    return -1
                else:
                    return 1

        return 0

    def _cyclic_sort(self):
        """
        Sorts the cyclic rotations based on their shift.
        """

        shifts = range(self._length)
        return sorted(shifts,
                      key=cmp_to_key(lambda i, j: self._cyclic_compare(i, j)))

    def _enumerate_word(self, word):
        """
        Enumerates the same characters in the order of their appearance in
        the given word.

        For example,

        'abcbba' returns ['a0', 'b0', 'c0', 'b1', 'b2', 'a1']
        """

        char_count = {}
        enumerated_cars = []

        for ch in word:
            if ch not in char_count:
                char_count[ch] = 0
            else:
                char_count[ch] += 1

            enumerated_cars.append(ch + str(char_count[ch]))

        return enumerated_cars

    def burrows_wheeler_transform(self):
        """
        Collects characters corresponding to the last indices of cyclic
        rotations in the sorted order and returns them as a string.
        """

        cyclic_sort = self._cyclic_sort()
        last_index_chars = [self._cyclic_rotation_character(i, -1)
                            for i in cyclic_sort]
        return ''.join(last_index_chars)

    def inverse_burrows_wheeler_transform(self):
        """
        Returns the inverse transform of the Burrows-Wheeler Transform text.
        """

        enumerated_word = self._enumerate_word(self._word)
        enumerated_sorted_word = self._enumerate_word(sorted(self._word))

        # Make a mapping between the enumerated characters at each index of the
        # enumerated Burrows-Wheeler Transform text and its sorted version.
        char_indices = range(len(self._word))
        inverse_map = {}
        for i in char_indices:
            inverse_map[enumerated_word[i]] = enumerated_sorted_word[i]

        # Make the inverse Burrows-Wheeler Transform text by a traversal
        # through the inverse map.
        inverse_word = ''
        current_char = enumerated_word[0]
        for i in char_indices:
            current_char = inverse_map[current_char]
            inverse_word += current_char[0]

        # The actual inverse word must end in the marker char, so shift the
        # sequence to the left by one.
        marker_char = inverse_word[0]
        actual_inverse_word = inverse_word[1:] + marker_char

        return actual_inverse_word

class Solver:
    """
    Reconstructs a string from its Burrows–Wheeler Transform.
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

        text = self._input()

        util = Util(text)

        self._output(util.inverse_burrows_wheeler_transform())

if __name__ == '__main__':
    Solver().solve()
