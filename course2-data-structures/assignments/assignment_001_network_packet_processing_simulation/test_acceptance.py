#!/usr/bin/python3

from os import listdir
from os.path import isfile, join
import os
import sys

import unittest

from process_packages import Buffer, process_requests, read_requests, \
    Request, Response

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

                size, count = map(int, query_stream.readline().strip().split())
                requests = read_requests(count, query_stream)

                print('Doing Test: ' + str(i))
                buffer = Buffer(size)
                responses = process_requests(requests, buffer)
                result_text = ''
                for i, response in enumerate(responses):
                    result_text += str((response.start_time
                        if not response.dropped else -1))
                    if i != len(responses) - 1:
                        result_text += os.linesep

                self.assertEqual(answer_text, result_text)
            except AssertionError as e:
                print(query_file_name + ' fails: ' + str(e))
            finally:
                if query_stream is not None:
                    query_stream.close()
                if answer_stream is not None:
                    answer_stream.close()

if __name__ == '__main__':
    unittest.main()
