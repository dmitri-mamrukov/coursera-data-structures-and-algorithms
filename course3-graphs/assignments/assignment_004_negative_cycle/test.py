#!/usr/bin/python3

import unittest

import negative_cycle

class SolverSolveTestCase(unittest.TestCase):

    def setUp(self):
        self.solver = negative_cycle.Solver()
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

    def test_four_nodes_case1(self):
        self.input_list = [
                              '4 4',
                              '1 2 -5',
                              '4 1 2',
                              '2 3 2',
                              '3 1 1',
                          ]
        expected_result = [
                              1
                          ]

        self.solver.solve()

        self.assertEqual(expected_result, self.output_list)

    def test_four_nodes_case2(self):
        self.input_list = [
                              '4 4',
                              '1 2 1',
                              '4 1 2',
                              '2 3 2',
                              '3 1 -5',
                          ]
        expected_result = [
                              1
                          ]

        self.solver.solve()

        self.assertEqual(expected_result, self.output_list)

    def test_four_nodes_case3(self):
        self.input_list = [
                              '4 3',
                              '1 2 -1',
                              '2 3 -2',
                              '3 4 -3',
                          ]
        expected_result = [
                              0
                          ]

        self.solver.solve()

        self.assertEqual(expected_result, self.output_list)

    def test_five_nodes_case1(self):
        self.input_list = [
                              '5 9',
                              '1 2 4',
                              '1 3 2',
                              '2 3 2',
                              '3 2 1',
                              '2 4 2',
                              '3 5 4',
                              '5 4 1',
                              '2 5 3',
                              '3 4 4',
                          ]
        expected_result = [
                              0
                          ]

        self.solver.solve()

        self.assertEqual(expected_result, self.output_list)

    def test_five_nodes_case2(self):
        self.input_list = [
                              '5 5',
                              '1 2 1',
                              '3 1 1',
                              '3 4 -1',
                              '4 5 -1',
                              '5 3 -1',
                          ]
        expected_result = [
                              1
                          ]

        self.solver.solve()

        self.assertEqual(expected_result, self.output_list)

    def test_two_components(self):
        self.input_list = [
                              '3 2',
                              '2 3 1',
                              '3 2 -2',
                          ]
        expected_result = [
                              1
                          ]

        self.solver.solve()

        self.assertEqual(expected_result, self.output_list)


if __name__ == '__main__':
    unittest.main()