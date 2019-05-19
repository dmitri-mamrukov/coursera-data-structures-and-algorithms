#!/usr/bin/python3

import unittest

import suffix_array

class SolverSolveTestCase(unittest.TestCase):

    def setUp(self):
        self.solver = suffix_array.Solver()
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
                              'AAA$',
                          ]
        expected_result = [
                              '3 2 1 0',
                          ]

        self.solver.solve()

        self.assertEquals(expected_result, self.output_list)

    def test_case2(self):
        self.input_list = [
                              'GAC$',
                          ]
        expected_result = [
                              '3 1 2 0',
                          ]

        self.solver.solve()

        self.assertEquals(expected_result, self.output_list)

    def test_case3(self):
        self.input_list = [
                              'GAGAGAGA$',
                          ]
        expected_result = [
                              '8 7 5 3 1 6 4 2 0',
                          ]

        self.solver.solve()

        self.assertEquals(expected_result, self.output_list)

    def test_case4(self):
        self.input_list = [
                              'AACGATAGCGGTAGA$',
                          ]
        expected_result = [
                              '15 14 0 1 12 6 4 2 8 13 3 7 9 10 11 5',
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
