#!/usr/bin/python3

import math
import unittest

import clustering

class SolverSolveTestCase(unittest.TestCase):

    def setUp(self):
        self.solver = clustering.Solver()
        self.solver._input = self.generate_input
        self.solver._output = self.accumulate_output
        self.output_list = []
        self.index = 0

    def tearDown(self):
        pass

    def generate_input(self):
        line = self.input_list[self.index]
        self.index += 1

        return line

    def accumulate_output(self, text):
        return self.output_list.append(text)

    def assert_result(self, expected_result):
        self.assertEqual(len(expected_result), len(self.output_list))
        self.assertAlmostEqual(expected_result[0],
                               self.output_list[0],
                               delta=math.pow(10, -6))

    def test_case1(self):
        self.input_list = [
                              '12',
                              '7 6',
                              '4 3',
                              '5 1',
                              '1 7',
                              '2 7',
                              '5 7',
                              '3 3',
                              '7 8',
                              '2 8',
                              '4 4',
                              '6 7',
                              '2 6',
                              '3',
                          ]
        expected_result = [
                              2.828427124746,
                          ]

        self.solver.solve()

        self.assert_result(expected_result)

    def test_case2(self):
        self.input_list = [
                              '8',
                              '3 1',
                              '1 2',
                              '4 6',
                              '9 8',
                              '9 9',
                              '8 9',
                              '3 11',
                              '4 12',
                              '4',
                          ]
        expected_result = [
                              5.000000000,
                          ]

        self.solver.solve()

        self.assert_result(expected_result)

if __name__ == '__main__':
    unittest.main()
