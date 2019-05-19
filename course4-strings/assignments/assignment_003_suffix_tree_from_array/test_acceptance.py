#!/usr/bin/python3

import os
import unittest

import suffix_tree_from_array

"""
Note that the outputs of some tests don't match those from the official
ones. But edge strings remain valid. I think this is due to their code that
builds a suffix tree slightly differently.

My solution still passed all the official tests.
"""

class AcceptanceTestCase(unittest.TestCase):

    def setUp(self):
        self.solver = suffix_tree_from_array.Solver()
        self.solver._input = self.generate_input
        self.solver._output = self.accumulate_output
        self.output_list = []
        self.index = 0

    def accumulate_output(self, text):
        return self.output_list.append(text)

    def generate_input(self):
        line = self.input_list[self.index]
        self.index += 1

        return line

    def test(self):
        failed = False

        test_dir = 'acceptance_tests'
        files = [f for f in os.listdir(test_dir)
                 if os.path.isfile(os.path.join(test_dir, f))]
        for i in range(1, len(files) // 2 + 1):
            self.output_list.clear()
            self.index = 0

            query_file_name = test_dir + '/' + str(i).zfill(2)
            answer_file_name = query_file_name + '.a'

            query_stream = None
            answer_stream = None

            try:
                query_stream = open(query_file_name, 'r')
                answer_stream = open(answer_file_name, 'r')

                query_text = query_stream.read().strip()
                self.input_list = query_text.split(os.linesep)
                answer_text = answer_stream.read().strip()

                self.solver.solve()

                self.assertEqual(answer_text,
                                 os.linesep.join(self.output_list))
            except AssertionError as e:
                failed = True
                print(query_file_name + ' fails: ' + str(e))
            finally:
                if query_stream is not None:
                    query_stream.close()
                if answer_stream is not None:
                    answer_stream.close()

        if failed:
            self.fail('Acceptance tests failed.')

if __name__ == '__main__':
    unittest.main()
