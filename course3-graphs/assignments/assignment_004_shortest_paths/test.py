#!/usr/bin/python3

import unittest

import shortest_paths

class SolverSolveTestCase(unittest.TestCase):

    def setUp(self):
        self.solver = shortest_paths.Solver()
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

    def test_mixed_case1(self):
        self.input_list = [
                              '6 7',
                              '1 2 10',
                              '2 3 5',
                              '1 3 100',
                              '3 5 7',
                              '5 4 10',
                              '4 3 -18',
                              '6 1 -1',
                              '1',
                          ]
        expected_result = [
                              '0',
                              '10',
                              '-',
                              '-',
                              '-',
                              '*',
                          ]

        self.solver.solve()

        self.assertEqual(expected_result, self.output_list)

    def test_mixed_case2(self):
        self.input_list = [
                              '5 4',
                              '1 2 1',
                              '4 1 2',
                              '2 3 2',
                              '3 1 -5',
                              '4',
                          ]
        expected_result = [
                              '-',
                              '-',
                              '-',
                              '0',
                              '*',
                          ]

        self.solver.solve()

        self.assertEqual(expected_result, self.output_list)

    def test_infinite_arbitrage_for_start_node_case1(self):
        """
        The start node is reachable from the one negative cycle. So, we can
        infinite-arbitrage for the starting node, and also for any node
        reachable from the starting node.
        """
        self.input_list = [
                              '4 4',
                              '1 2 -5',
                              '4 1 2',
                              '2 3 2',
                              '3 1 1',
                              '1',
                          ]
        expected_result = [
                              '-',
                              '-',
                              '-',
                              '*',
                          ]

        self.solver.solve()

        self.assertEqual(expected_result, self.output_list)

    def test_infinite_arbitrage_for_start_node_case2(self):
        """
        The start node is reachable from the one negative cycle. So, we can
        infinite-arbitrage for the starting node, and also for any node
        reachable from the starting node.
        """
        self.input_list = [
                              '5 7',
                              '1 2 10',
                              '2 3 5',
                              '1 3 100',
                              '3 5 7',
                              '5 4 10',
                              '4 3 -18',
                              '5 1 -1',
                              '1',
                          ]
        expected_result = [
                              '-',
                              '-',
                              '-',
                              '-',
                              '-',
                          ]

        self.solver.solve()

        self.assertEqual(expected_result, self.output_list)

    def test_two_components_case1(self):
        self.input_list = [
                              '3 2',
                              '2 3 -1',
                              '3 2 -1',
                              '1',
                          ]
        expected_result = [
                              '0',
                              '*',
                              '*',
                          ]

        self.solver.solve()

        self.assertEqual(expected_result, self.output_list)

    def test_two_components_case2(self):
        self.input_list = [
                              '5 4',
                              '1 2 1',
                              '4 1 2',
                              '2 3 2',
                              '3 1 -5',
                              '5',
                          ]
        expected_result = [
                              '*',
                              '*',
                              '*',
                              '*',
                              '0',
                          ]

        self.solver.solve()

        self.assertEqual(expected_result, self.output_list)

if __name__ == '__main__':
    unittest.main()
