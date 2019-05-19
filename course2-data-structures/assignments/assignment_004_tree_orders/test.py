#!/usr/bin/python3

import unittest

import tree_orders

class TreeOrdersTestCase(unittest.TestCase):

    def setUp(self):
        self.solver = tree_orders.Solver()
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

    def test_one_node_tree(self):
        self.input_list = [
                              '1',
                              '123 -1 -1',
                          ]
        expected_result = [
                              '123',
                              '123',
                              '123',
                          ]

        self.solver.solve()

        self.assertEqual(expected_result, self.output_list)

    def test_two_node_tree_as_root_and_left(self):
        self.input_list = [
                              '2',
                              '11 1 -1',
                              '22 -1 -1',
                          ]
        expected_result = [
                              '22 11',
                              '11 22',
                              '22 11',
                          ]

        self.solver.solve()

        self.assertEqual(expected_result, self.output_list)

    def test_two_node_tree_as_root_and_right(self):
        self.input_list = [
                              '2',
                              '11 -1 1',
                              '22 -1 -1',
                          ]
        expected_result = [
                              '11 22',
                              '11 22',
                              '22 11',
                          ]

        self.solver.solve()

        self.assertEqual(expected_result, self.output_list)

    def test_three_node_tree(self):
        self.input_list = [
                              '3',
                              '11 1 2',
                              '22 -1 -1',
                              '33 -1 -1',
                          ]
        expected_result = [
                              '22 11 33',
                              '11 22 33',
                              '22 33 11',
                          ]

        self.solver.solve()

        self.assertEqual(expected_result, self.output_list)

    def test_five_node_tree(self):
        self.input_list = [
                              '5',
                              '4 1 2',
                              '2 3 4',
                              '5 -1 -1',
                              '1 -1 -1',
                              '3 -1 -1',
                          ]
        expected_result = [
                              '1 2 3 4 5',
                              '4 2 1 3 5',
                              '1 3 2 5 4',
                          ]

        self.solver.solve()

        self.assertEqual(expected_result, self.output_list)

    def test_ten_node_tree(self):
        self.input_list = [
                              '10',
                              '0 7 2',
                              '10 -1 -1',
                              '20 -1 6',
                              '30 8 9',
                              '40 3 -1',
                              '50 -1 -1',
                              '60 1 -1',
                              '70 5 4',
                              '80 -1 -1',
                              '90 -1 -1',
                          ]
        expected_result = [
                              '50 70 80 30 90 40 0 20 10 60',
                              '0 70 50 40 30 80 90 20 60 10',
                              '50 80 90 30 40 70 10 60 20 0',
                          ]

        self.solver.solve()

        self.assertEqual(expected_result, self.output_list)

    def test_thirty_one_node_tree_as_complete_tree(self):
        self.input_list = [
                              '31',
                              '0 7 2',
                              '10 27 28',
                              '20 10 6',
                              '30 8 9',
                              '40 3 13',
                              '50 11 12',
                              '60 1 16',
                              '70 5 4',
                              '80 -1 -1',
                              '90 -1 -1',
                              '100 14 15',
                              '110 17 18',
                              '120 19 20',
                              '130 21 22',
                              '140 23 24',
                              '150 25 26',
                              '160 29 30',
                              '170 -1 -1',
                              '180 -1 -1',
                              '190 -1 -1',
                              '200 -1 -1',
                              '210 -1 -1',
                              '220 -1 -1',
                              '230 -1 -1',
                              '240 -1 -1',
                              '250 -1 -1',
                              '260 -1 -1',
                              '270 -1 -1',
                              '280 -1 -1',
                              '290 -1 -1',
                              '300 -1 -1',
                          ]
        expected_result = [
                              '170 110 180 50 190 120 200 70 80 30 90 40 210 ' +
                              '130 220 0 230 140 240 100 250 150 260 20 270 ' +
                              '10 280 60 290 160 300',
                              '0 70 50 110 170 180 120 190 200 40 30 80 90 ' +
                              '130 210 220 20 100 140 230 240 150 250 260 60 ' +
                              '10 270 280 160 290 300',
                              '170 180 110 190 200 120 50 80 90 30 210 220 ' +
                              '130 40 70 230 240 140 250 260 150 100 270 280 ' +
                              '10 290 300 160 60 20 0',
                          ]

        self.solver.solve()

        self.assertEqual(expected_result, self.output_list)

if __name__ == '__main__':
    unittest.main()
