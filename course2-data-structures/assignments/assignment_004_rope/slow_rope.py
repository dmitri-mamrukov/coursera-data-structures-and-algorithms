#!/usr/bin/python3

import io
import sys

class SlowRope:

    def __init__(self, s):
        self._s = s

    def result(self):
        return self._s

    def process(self, i, j, k):
        t = self._s[0:i] + self._s[j + 1:]
        self._s = t[0:k] + self._s[i:j + 1] + t[k:]

class Solver:
    """
    You are given a string S and you have to process n queries. Each query is
    described by three integers i, j, k and means to cut substring S[i..j]
    (i and j are 0-based) from the string and then insert it after the k-th
    symbol of the remaining string (if the symbols are numbered from 1).
    If k = 0, S[i..j] is inserted in the beginning.
    """

    def __init__(self):
        if __name__ == '__main__':
            input_stream = io.TextIOWrapper(sys.stdin.buffer, encoding='utf-8')
            self.input_processor = input_stream

    def _input(self):
        return self.input_processor.readline().strip()

    def _output(self, text):
        print(text)

    def solve(self):
        text = self._input()
        n = int(self._input())

        rope = SlowRope(text)
        for _ in range(n):
            i, j, k = map(int, self._input().split())
            rope.process(i, j, k)

        self._output(rope.result())

if __name__ == '__main__':
    Solver().solve()
