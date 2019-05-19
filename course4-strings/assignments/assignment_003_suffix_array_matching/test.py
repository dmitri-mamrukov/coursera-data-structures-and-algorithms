#!/usr/bin/python3

import unittest

import suffix_array_matching
import suffix_array_matching_burrows_wheeler1
import suffix_array_matching_burrows_wheeler2
import suffix_array_matching_with_kmp

class SolverSolveTestCase(unittest.TestCase):

    def setUp(self):
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

    def assert_result(self, expected_result):
        expected_items = expected_result[0].split()
        actual_items = self.output_list[0].split()
        try:
            self.assertEqual(len(expected_items), len(actual_items))
            expected_count = {}
            for expected_item in expected_items:
                if not expected_item in expected_count:
                    expected_count[expected_item] = 0
                expected_count[expected_item] += 1
            count = {}
            for item in actual_items:
                if not item in count:
                    count[item] = 0
                count[item] += 1

            for item in actual_items:
                self.assertEqual(expected_count[item],
                                 count[item],
                                 'Item ' + str(item) +
                                 ' has different counts.')
        except Exception:
            self.fail('Expected: {}, actual: {} '.format(expected_items,
                                                     actual_items))

    def test_case1(self):
        self.input_list = [
                              'AAA',
                              '1',
                              'A',
                          ]
        expected_result = [
                              '0 1 2',
                          ]

        self.solver.solve()

        """
        The pattern A appears at positions 0, 1, and 2 in the text.
        """

        self.assert_result(expected_result)

    def test_case2(self):
        self.input_list = [
                              'ATA',
                              '3',
                              'C G C',
                          ]
        expected_result = [
                              '',
                          ]

        self.solver.solve()

        """
        There are no occurrences of the patterns in the text.
        """

        self.assert_result(expected_result)

    def test_case3(self):
        self.input_list = [
                              'ATATATA',
                              '3',
                              'ATA C TATAT',
                          ]
        expected_result = [
                              '0 1 2 4',
                          ]

        self.solver.solve()

        """
        The pattern ATA appears at positions 0, 2, and 4; the pattern TATAT
        appears at position 1.
        """

        self.assert_result(expected_result)

    def test_case4(self):
        self.input_list = [
                              'ATATATA',
                              '2',
                              'A ATA',
                          ]
        expected_result = [
                              '0 2 4 6',
                          ]

        self.solver.solve()

        """
        The pattern A appears at positions 0, 2, 4 and 6; the pattern ATA
        appears at positions 0, 2, and 4.
        """

        self.assert_result(expected_result)

    def test_case5(self):
        self.input_list = [
                              'ATATATA',
                              '2',
                              'A AT ATA',
                          ]
        expected_result = [
                              '0 2 4 6',
                          ]

        self.solver.solve()

        """
        The pattern A appears at positions 0, 2, 4 and 6; the pattern AT
        appears at positions 0, 2, and 4; the pattern ATA appears at positions
        0, 2, and 4.
        """

        self.assert_result(expected_result)

    def test_case6(self):
        self.input_list = [
                              'GGTAAAGATG',
                              '1',
                              'AAA',
                          ]
        expected_result = [
                              '3',
                          ]

        self.solver.solve()

        """
        The pattern AAA appears at position 0.
        """

        self.assert_result(expected_result)

    def test_case7(self):
        self.input_list = [
                              'GGTAAAGATG',
                              '1',
                              'GGG',
                          ]
        expected_result = [
                              '',
                          ]

        self.solver.solve()

        """
        There are no occurrences of the pattern in the text.
        """

        self.assert_result(expected_result)

class SolverSolveWithDoubleBinarySearchTestCase(SolverSolveTestCase):

    def setUp(self):
        super(SolverSolveWithDoubleBinarySearchTestCase, self).setUp()

        self.solver = suffix_array_matching.Solver()
        self.solver._input = self.generate_input
        self.solver._output = self.accumulate_output

    def tearDown(self):
        pass

class SolverSolveWithKmpTestCase(SolverSolveTestCase):

    def setUp(self):
        super(SolverSolveWithKmpTestCase, self).setUp()

        self.solver = suffix_array_matching_with_kmp.Solver()
        self.solver._input = self.generate_input
        self.solver._output = self.accumulate_output

    def tearDown(self):
        pass

class SolverSolveWithBurrowsWheeler1TestCase(SolverSolveTestCase):

    def setUp(self):
        super(SolverSolveWithBurrowsWheeler1TestCase, self).setUp()

        self.solver = suffix_array_matching_burrows_wheeler1.Solver()
        self.solver._input = self.generate_input
        self.solver._output = self.accumulate_output

    def tearDown(self):
        pass

class SolverSolveWithBurrowsWheeler2TestCase(SolverSolveTestCase):

    def setUp(self):
        super(SolverSolveWithBurrowsWheeler2TestCase, self).setUp()

        self.solver = suffix_array_matching_burrows_wheeler2.Solver()
        self.solver._input = self.generate_input
        self.solver._output = self.accumulate_output

    def tearDown(self):
        pass

if __name__ == '__main__':
    class_names = [
                      SolverSolveWithDoubleBinarySearchTestCase,
                      SolverSolveWithKmpTestCase,
                      SolverSolveWithBurrowsWheeler1TestCase,
                      SolverSolveWithBurrowsWheeler2TestCase,
                  ]

    suite = unittest.TestSuite()

    for c in class_names:
        suite.addTest(unittest.defaultTestLoader.loadTestsFromTestCase(c))

    unittest.TextTestRunner().run(suite)
