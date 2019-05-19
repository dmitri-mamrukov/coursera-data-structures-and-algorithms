#!/usr/bin/python3

import io
import sys

from functools import cmp_to_key

class Util():

    @staticmethod
    def _cyclic_rotation_character(word, i, n):
        """
        Returns the nth character of the cyclic rotation (to the right)
        by i characters.

        Note: Negative indices mean those from the right end. For example, -1
        references the first element from the end, -2 the second from the end,
        -3 the third from the end, and so on.
        """

        return word[n - i % len(word)]

    @staticmethod
    def _cyclic_compare(word, i, j):
        """
        Compares cyclic rotations without generating the entire rotation.
        """

        length = len(word)
        n = 0
        while n < length:
            i_char = Util._cyclic_rotation_character(word, i, n)
            j_char = Util._cyclic_rotation_character(word, j, n)
            if i_char == j_char:
                n += 1
            elif i_char < j_char:
                return -1
            else:
                return 1

        return 0

    @staticmethod
    def _cyclic_sort(word):
        """
        Sorts the cyclic rotations based on their shift.
        """

        length = len(word)
        shifts = range(length)
        return sorted(shifts,
                      key=cmp_to_key(lambda i, j:
                                     Util._cyclic_compare(word, i, j)))


    @staticmethod
    def burrows_wheeler_transform(word):
        """
        Collects characters corresponding to the last indices of cyclic
        rotations in the sorted order and returns them as a string.
        """

        cyclic_sort = Util._cyclic_sort(word)
        last_index_chars = [Util._cyclic_rotation_character(word, i, -1)
                            for i in cyclic_sort]
        return ''.join(last_index_chars)

class Solver:
    """
    Constructs the Burrows–Wheeler Transform of a string.
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

        self._output(Util.burrows_wheeler_transform(text))

if __name__ == '__main__':
    Solver().solve()
