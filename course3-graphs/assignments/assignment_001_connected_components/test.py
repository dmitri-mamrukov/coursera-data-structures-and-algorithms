#!/usr/bin/python3

import unittest

import connected_components

class SolverSolveTestCase(unittest.TestCase):

    def setUp(self):
        self.solver = connected_components.Solver()
        self.solver._input = self.generate_input
        self.solver._output = self.accumulate_output
        self.output_list = []

    def tearDown(self):
        pass

    def generate_input(self):
        return self.input_list.pop(0)

    def accumulate_output(self, text):
        return self.output_list.append(text)

    def test_one_component(self):
        self.input_list = [
            '4 4',
            '1 2',
            '3 2',
            '4 3',
            '1 4',
        ]
        expected_result = [
            1
        ]

        self.solver.solve()

        self.assertEqual(expected_result, self.output_list)

    def test_two_components(self):
        self.input_list = [
            '4 2',
            '1 2',
            '3 2',
        ]
        expected_result = [
            2
        ]

        self.solver.solve()

        self.assertEqual(expected_result, self.output_list)

if __name__ == '__main__':
    unittest.main()
