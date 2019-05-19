#!/usr/bin/python3

import sys
import threading

class Solver:

    def __init__(self, n, table_sizes):
        if n <= 0:
            raise ValueError('n must be > 0.')

        if n != len(table_sizes):
            raise ValueError('n must equal to the length of the ' +
                'list of tables.')

        self._parent = list(range(0, n))
        self._rank = table_sizes
        self._max_table_size = max(table_sizes)

    @property
    def max_table_size(self):
        return self._max_table_size

    def get_parent(self, table):
        """
        Finds the parent and compresses the path.
        """
        if table != self._parent[table]:
            self._parent[table] = self.get_parent(self._parent[table])

        return self._parent[table]

    def merge(self, destination, source):
        """
        Merges two components.
        Uses the union by rank heuristic.
        Updates the max_table_size with the new maximum table size.

        Implementation:

        1. Consider table number destinationi. Traverse the path of symbolic
           links to get to the data. That is,

            while destinationi contains a symbolic link instead of real data do
                destination i <-- symlink(destinationi)

        2. Consider the table number sourcei and traverse the path of symbolic
           links from it in the same manner as for destinationi.

        3. Now, destinationi and sourcei are the numbers of two tables with
           real data. If destinationi != sourcei, copy all the rows from table
           sourcei to table destinationi, then clear the table sourcei
           and instead of real data put a symbolic link to destinationi into
           it.

        4. Print the maximum size among all n tables (recall that size is the
           number of rows in the table). If the table contains only a symbolic
           link, its size is considered to be 0.
        """
        real_destination, real_source = self.get_parent(destination), \
            self.get_parent(source)

        if real_destination == real_source:
            return
        else:
            self._rank[real_destination] += self._rank[real_source]
            self._rank[real_source] = 0
            self._parent[real_source] = real_destination
            if self._max_table_size < self._rank[real_destination]:
                self._max_table_size = self._rank[real_destination]

        return

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
