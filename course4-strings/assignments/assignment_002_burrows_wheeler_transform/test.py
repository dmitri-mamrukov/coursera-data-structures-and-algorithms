#!/usr/bin/python3

import unittest

import burrows_wheeler_transform

class SolverSolveTestCase(unittest.TestCase):

    def setUp(self):
        self.solver = burrows_wheeler_transform.Solver()
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
                              'AA$',
                          ]
        expected_result = [
                              'AA$',
                          ]

        self.solver.solve()

        self.assertEquals(expected_result, self.output_list)

    def test_case2(self):
        self.input_list = [
                              'ACACACAC$',
                          ]
        expected_result = [
                              'CCCC$AAAA',
                          ]

        self.solver.solve()

        self.assertEquals(expected_result, self.output_list)

    def test_case3(self):
        self.input_list = [
                              'AGACATA$',
                          ]
        expected_result = [
                              'ATG$CAAA',
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
