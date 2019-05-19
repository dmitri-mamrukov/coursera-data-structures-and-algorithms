#!/usr/bin/python3

import math
import unittest

import connecting_points_kruskal
import connecting_points_prim

class BaseTestCase(unittest.TestCase):

    def generate_input(self):
        line = self.input_list[self.index]
        self.index += 1

        return line

    def accumulate_output(self, text):
        return self.output_list.append(text)

    def assert_result(self, expected_result):
        self.assertEqual(len(expected_result), len(self.output_list))
        self.assertAlmostEqual(expected_result[0],
                               self.output_list[0],
                               delta=math.pow(10, -6))

    def test_case1(self):
        self.input_list = [
                              '4',
                              '0 0',
                              '0 1',
                              '1 0',
                              '1 1',
                          ]
        expected_result = [
                              3.000000000,
                          ]

        self.solver.solve()

        self.assert_result(expected_result)

    def test_case2(self):
        self.input_list = [
                              '5',
                              '0 0',
                              '0 2',
                              '1 1',
                              '3 0',
                              '3 2',
                          ]
        expected_result = [
                              7.064495102,
                          ]

        self.solver.solve()

        self.assert_result(expected_result)

class SolverSolveWithKruskalTestCase(BaseTestCase):

    def setUp(self):
        self.solver = connecting_points_kruskal.Solver()
        self.solver._input = self.generate_input
        self.solver._output = self.accumulate_output
        self.output_list = []
        self.index = 0

    def tearDown(self):
        pass

class SolverSolveWithPrimTestCase(BaseTestCase):

    def setUp(self):
        self.solver = connecting_points_prim.Solver()
        self.solver._input = self.generate_input
        self.solver._output = self.accumulate_output
        self.output_list = []
        self.index = 0

    def tearDown(self):
        pass

if __name__ == '__main__':
    class_names = \
    [
        SolverSolveWithKruskalTestCase,
        SolverSolveWithPrimTestCase,
    ]

    suite = unittest.TestSuite()

    for c in class_names:
        suite.addTest(unittest.defaultTestLoader.loadTestsFromTestCase(c))

    unittest.TextTestRunner().run(suite)
