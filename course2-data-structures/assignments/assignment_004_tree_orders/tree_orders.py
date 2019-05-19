#!/usr/bin/python3

import io
import sys
import threading

class Solver:

    def __init__(self):
        if __name__ == '__main__':
            input_stream = io.TextIOWrapper(sys.stdin.buffer, encoding='utf-8')
            self.input_processor = input_stream

    def _input(self):
        return self.input_processor.readline().strip()

    def _output(self, text):
        print(text)

    def in_order_traverse(self, i, nodes):
        if i == -1:
            return

        self.in_order_traverse(self.left[i], nodes)

        nodes.append(self.key[i])

        self.in_order_traverse(self.right[i], nodes)

    def pre_order_traverse(self, i, nodes):
        if i == -1:
            return

        nodes.append(self.key[i])

        self.pre_order_traverse(self.left[i], nodes)

        self.pre_order_traverse(self.right[i], nodes)

    def post_order_traverse(self, i, nodes):
        if i == -1:
            return

        self.post_order_traverse(self.left[i], nodes)

        self.post_order_traverse(self.right[i], nodes)

        nodes.append(self.key[i])

    def in_order(self):
        self.result = []

        self.in_order_traverse(0, self.result)

        return self.result

    def pre_order(self):
        self.result = []

        self.pre_order_traverse(0, self.result)

        return self.result

    def post_order(self):
        self.result = []

        self.post_order_traverse(0, self.result)

        return self.result

    def solve(self):
        self.n = int(self._input())
        self.key = [0 for i in range(self.n)]
        self.left = [0 for i in range(self.n)]
        self.right = [0 for i in range(self.n)]

        for i in range(self.n):
            [a, b, c] = map(int, self._input().split())
            self.key[i] = a
            self.left[i] = b
            self.right[i] = c

        self._output(' '.join(str(x) for x in self.in_order()))
        self._output(' '.join(str(x) for x in self.pre_order()))
        self._output(' '.join(str(x) for x in self.post_order()))

def main():
    Solver().solve()

if __name__ == '__main__':
    sys.setrecursionlimit(10**6) # the max depth of recursion
    threading.stack_size(2**25)  # a new thread will get a stack of such size
    threading.Thread(target=main).start()
