#!/usr/bin/python3

import unittest

import trie_matching

class SolverSolveTestCase(unittest.TestCase):

    def setUp(self):
        self.solver = trie_matching.Solver()
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

    def test_case1(self):
        self.input_list = [
                              'AAA',
                              '1',
                              'AA',
                          ]
        expected_result = [
                              '0 1',
                          ]

        self.solver.solve()

        self.assertEquals(expected_result, self.output_list)

    def test_case2(self):
        self.input_list = [
                              'AA',
                              '1',
                              'T',
                          ]
        expected_result = [
                              '',
                          ]

        self.solver.solve()

        self.assertEquals(expected_result, self.output_list)

    def test_case3(self):
        self.input_list = [
                              'AATCGGGTTCAATCGGGGT',
                              '2',
                              'ATCG',
                              'GGGT',
                          ]
        expected_result = [
                              '1 4 11 15',
                          ]

        self.solver.solve()

        self.assertEquals(expected_result, self.output_list)

if __name__ == '__main__':
    class_names = \
    [
        SolverSolveTestCase,
    ]

    suite = unittest.TestSuite()

    for c in class_names:
        suite.addTest(unittest.defaultTestLoader.loadTestsFromTestCase(c))

    unittest.TextTestRunner().run(suite)
