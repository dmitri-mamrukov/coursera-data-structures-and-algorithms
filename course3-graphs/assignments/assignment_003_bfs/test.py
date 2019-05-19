#!/usr/bin/python3

import unittest

import bfs

class SolverSolveTestCase(unittest.TestCase):

    def setUp(self):
        self.solver = bfs.Solver()
        self.solver._input = self.generate_input
        self.solver._output = self.accumulate_output
        self.output_list = []

    def tearDown(self):
        pass

    def generate_input(self):
        return self.input_list.pop(0)

    def accumulate_output(self, text):
        return self.output_list.append(text)

    def test_case1(self):
        self.input_list = [
            '4 4',
            '1 2',
            '4 1',
            '2 3',
            '3 1',
            '2 4',
        ]
        expected_result = [
            2
        ]

        self.solver.solve()

        self.assertEqual(expected_result, self.output_list)

    def test_case2(self):
        self.input_list = [
            '5 4',
            '5 2',
            '1 3',
            '3 4',
            '1 4',
            '3 5',
        ]
        expected_result = [
            -1
        ]

        self.solver.solve()

        self.assertEqual(expected_result, self.output_list)

if __name__ == '__main__':
    unittest.main()
