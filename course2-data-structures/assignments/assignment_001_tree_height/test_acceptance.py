#!/usr/bin/python3

from os import listdir
from os.path import isfile, join
import sys
import threading

import unittest

from tree_height import process

class AcceptanceTestCase(unittest.TestCase):

    def test(self):
        test_dir = 'tests'
        files = [ f for f in listdir(test_dir) if isfile(join(test_dir, f)) ]
        for i in range(1, len(files) // 2 + 1):
            query_file_name = 'tests/' + str(i).zfill(2)
            answer_file_name = query_file_name + '.a'

            query_stream = None
            answer_stream = None

            try:
                query_stream = open(query_file_name, 'r')
                answer_stream = open(answer_file_name, 'r')
                answer_text = answer_stream.read().strip()

                n = int(query_stream.readline())
                parents = list(map(int, query_stream.readline().split()))

                print('Doing Test: ' + str(i))
                result = process(n, parents)

                self.assertEqual(answer_text, str(result))
            except AssertionError as e:
                print(query_file_name + ' fails: ' + str(e))
            finally:
                if query_stream is not None:
                    query_stream.close()
                if answer_stream is not None:
                    answer_stream.close()

def main():
    unittest.main()

if __name__ == '__main__':
    """Instructor Michael Levin: Not only those three lines are critical for
    everything to work correctly, but also creating and starting a Thread
    object and calling your solution function inside it, because you set the
    stack size for threading, not for the whole program.
    """
    sys.setrecursionlimit(10**7) # max depth of recursion
    threading.stack_size(2**25)  # a new thread will get a stack of such a size
    threading.Thread(target = main).start()
