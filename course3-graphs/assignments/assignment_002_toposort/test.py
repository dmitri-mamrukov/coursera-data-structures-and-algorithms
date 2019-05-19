#!/usr/bin/python3

import unittest

import toposort

class SolverSolveTestCase(unittest.TestCase):

    def setUp(self):
        self.solver = toposort.Solver()
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
            '4 3',
            '1 2',
            '4 1',
            '3 1',
        ]
        expected_result = [
            '4 3 1 2'
        ]

        self.solver.solve()

        self.assertEqual(expected_result, self.output_list)

    def test_case2(self):
        self.input_list = [
            '5 7',
            '2 1',
            '3 2',
            '3 1',
            '4 3',
            '4 1',
            '5 2',
            '5 3',
        ]
        expected_result = [
            '5 4 3 2 1'
        ]

        self.solver.solve()

        self.assertEqual(expected_result, self.output_list)

if __name__ == '__main__':
    unittest.main()
