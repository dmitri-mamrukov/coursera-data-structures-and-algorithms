#!/usr/bin/python3

from os import listdir
from os.path import isfile, join

import unittest

from check_brackets import process

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
                query_text = query_stream.read()
                answer_text = answer_stream.read().strip()

                result = process(query_text)

                self.assertEqual(answer_text, str(result))
            except AssertionError as e:
                print(query_file_name + ' fails: ' + str(e))
            finally:
                if query_stream is not None:
                    query_stream.close()
                if answer_stream is not None:
                    answer_stream.close()

if __name__ == '__main__':
    unittest.main()
