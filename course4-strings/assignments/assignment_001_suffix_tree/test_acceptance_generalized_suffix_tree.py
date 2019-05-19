#!/usr/bin/python3

import os
import unittest

import generalized_suffix_tree

class AcceptanceTestCase(unittest.TestCase):

    def setUp(self):
        self.solver = generalized_suffix_tree.Solver()
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

    def assert_result(self, expected_result):
        expected_items = expected_result
        actual_items = self.output_list
        try:
            self.assertEqual(len(expected_items), len(actual_items))
            expected_count = {}
            for expected_item in expected_items:
                if not expected_item in expected_count:
                    expected_count[expected_item] = 0
                expected_count[expected_item] += 1
            count = {}
            for item in actual_items:
                if not item in count:
                    count[item] = 0
                count[item] += 1

            for item in actual_items:
                self.assertEqual(expected_count[item],
                                 count[item],
                                 'Item ' + str(item) +
                                 ' has different counts.')
        except Exception:
            self.fail('Expected: {}, actual: {} '.format(expected_items,
                                                     actual_items))

    def test(self):
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

                expected_result = [x for x in answer_text.split()]

                self.assert_result(expected_result)
            except AssertionError as e:
                print(query_file_name + ' fails: ' + str(e))
            finally:
                if query_stream is not None:
                    query_stream.close()
                if answer_stream is not None:
                    answer_stream.close()

if __name__ == '__main__':
    unittest.main()
