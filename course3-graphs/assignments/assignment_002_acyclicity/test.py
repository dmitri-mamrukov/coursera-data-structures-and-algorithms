#!/usr/bin/python3

import unittest

import acyclicity

class SolverSolveTestCase(unittest.TestCase):

    def setUp(self):
        self.solver = acyclicity.Solver()
        self.solver._input = self.generate_input
        self.solver._output = self.accumulate_output
        self.output_list = []

    def tearDown(self):
        pass

    def generate_input(self):
        return self.input_list.pop(0)

    def accumulate_output(self, text):
        return self.output_list.append(text)

    def test_one_cycle(self):
        self.input_list = [
            '4 4',
            '1 2',
            '4 1',
            '2 3',
            '3 1',
        ]
        expected_result = [
            1
        ]

        self.solver.solve()

        self.assertEqual(expected_result, self.output_list)

    def test_no_cycle(self):
        self.input_list = [
            '5 7',
            '1 2',
            '2 3',
            '1 3',
            '3 4',
            '1 4',
            '2 5',
            '3 5',
        ]
        expected_result = [
            0
        ]

        self.solver.solve()

        self.assertEqual(expected_result, self.output_list)

if __name__ == '__main__':
    unittest.main()
