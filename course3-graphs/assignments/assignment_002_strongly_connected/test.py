#!/usr/bin/python3

import unittest

import strongly_connected

class SolverSolveTestCase(unittest.TestCase):

    def setUp(self):
        self.solver = strongly_connected.Solver()
        self.solver._input = self.generate_input
        self.solver._output = self.accumulate_output
        self.output_list = []

    def tearDown(self):
        pass

    def generate_input(self):
        return self.input_list.pop(0)

    def accumulate_output(self, text):
        return self.output_list.append(text)

    def test_four_nodes(self):
        self.input_list = [
            '4 4',
            '1 2',
            '4 1',
            '2 3',
            '3 1',
        ]
        expected_result = [
            2
        ]

        self.solver.solve()

        self.assertEqual(expected_result, self.output_list)

    def test_five_nodes(self):
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
            5
        ]

        self.solver.solve()

        self.assertEqual(expected_result, self.output_list)

    def test_three_nodes(self):
        self.input_list = [
            '3 4',
            '1 2',
            '2 1',
            '2 3',
            '3 2',
        ]
        expected_result = [
            1
        ]

        self.solver.solve()

        self.assertEqual(expected_result, self.output_list)

    def test_nine_nodes_case1(self):
        self.input_list = [
            '9 11',
            '1 2',
            '2 5',
            '2 6',
            '3 2',
            '4 1',
            '5 1',
            '5 3',
            '5 8',
            '7 8',
            '8 6',
            '8 7',
        ]
        expected_result = [
            5
        ]

        self.solver.solve()

        self.assertEqual(expected_result, self.output_list)

    def test_nine_nodes_case2(self):
        self.input_list = [
            '9 13',
            '1 5',
            '2 1',
            '2 3',
            '2 7',
            '3 9',
            '4 1',
            '4 7',
            '5 8',
            '6 2',
            '6 3',
            '6 9',
            '7 8',
            '8 6',
        ]
        expected_result = [
            4
        ]

        self.solver.solve()

        self.assertEqual(expected_result, self.output_list)

if __name__ == '__main__':
    unittest.main()
