#!/usr/bin/python3

import unittest

import burrows_wheeler_transform_matching

class SolverSolveTestCase(unittest.TestCase):

    def setUp(self):
        self.solver = burrows_wheeler_transform_matching.Solver()
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
                              'AGGGAA$',
                              '1',
                              'GA'
                          ]
        expected_result = [
                              '3',
                          ]

        self.solver.solve()

        self.assertEquals(expected_result, self.output_list)

    def test_case2(self):
        self.input_list = [
                              'ATT$AA',
                              '2',
                              'ATA A',
                          ]
        expected_result = [
                              '2 3',
                          ]

        self.solver.solve()

        self.assertEquals(expected_result, self.output_list)

    def test_case3(self):
        self.input_list = [
                              'AT$TCTATG',
                              '2',
                              'TCT TATG',
                          ]
        expected_result = [
                              '0 0',
                          ]

        self.solver.solve()

        self.assertEquals(expected_result, self.output_list)

if __name__ == '__main__':
    class_names = [
                      SolverSolveTestCase,
                  ]

    suite = unittest.TestSuite()

    for c in class_names:
        suite.addTest(unittest.defaultTestLoader.loadTestsFromTestCase(c))

    unittest.TextTestRunner().run(suite)
