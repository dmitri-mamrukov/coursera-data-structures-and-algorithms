#!/usr/bin/python3

import unittest

import slow_rope

class SolverSolveTestCase(unittest.TestCase):

    def setUp(self):
        self.solver = slow_rope.Solver()
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
                              'hlelowrold',
                              '2',
                              '1 1 2',
                              '6 6 7',
                          ]
        expected_result = [
                              'helloworld',
                          ]

        self.solver.solve()

        self.assertEqual(expected_result, self.output_list)

    def test_case2(self):
        self.input_list = [
                              'abcdef',
                              '2',
                              '0 1 1',
                              '4 5 0',
                          ]
        expected_result = [
                              'efcabd',
                          ]

        self.solver.solve()

        self.assertEqual(expected_result, self.output_list)
if __name__ == '__main__':
    class_names = \
    [
        SolverSolveTestCase,
    ]

    suite = unittest.TestSuite()

    for c in class_names:
        suite.addTest(unittest.defaultTestLoader.loadTestsFromTestCase(c))

    unittest.TextTestRunner().run(suite)
