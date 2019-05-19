#!/usr/bin/python3

import sys
import threading

class Node:

    def __init__ (self, label, size, parent=None):
        self._label = label
        self._size = size
        self._parent = self if parent == None else parent

    def __str__(self):
        return str(self._label)

    def __repr__(self):
        return ('[label=' + str(self._label) + ', size=' +
            str(self._size) + ', parent=' + str(self._parent) + ']')

class Solver:

    def __init__(self, n, table_sizes):
        if n <= 0:
            raise ValueError('n must be > 0.')

        if n != len(table_sizes):
            raise ValueError('n must equal to the length of the ' +
                'list of tables.')

        self._nodes = [ Node(i, size) for i, size in enumerate(table_sizes) ]

        self._max_table_size = max(table_sizes)

    def merge(self, destination, source):
        real_destination, real_source = (self.get_parent(
            self._nodes[destination]), self.get_parent(self._nodes[source]))

        if real_destination == real_source:
            return

        real_source._parent = real_destination
        real_destination._size += real_source._size
        real_source._size = 0
        if self.max_table_size < real_destination._size:
            self._max_table_size = real_destination._size

    def get_parent(self, x):
        if x._parent == x:
           return x
        else:
           x._parent = self.get_parent(x._parent)

           return x._parent

    @property
    def max_table_size(self):
        return self._max_table_size

def main():
    n, m = map(int, sys.stdin.readline().split())
    table_sizes = list(map(int, sys.stdin.readline().split()))

    solver = Solver(n, table_sizes)

    for i in range(m):
        destination, source = map(int, sys.stdin.readline().split())

        solver.merge(destination - 1, source - 1)

        print(solver.max_table_size)

if __name__ == '__main__':
    """Instructor Michael Levin: Not only those three lines are critical for
    everything to work correctly, but also creating and starting a Thread
    object and calling your solution function inside it, because you set the
    stack size for threading, not for the whole program.
    """
    sys.setrecursionlimit(10**7) # max depth of recursion
    threading.stack_size(2**25)  # a new thread will get a stack of such a size
    threading.Thread(target = main).start()
