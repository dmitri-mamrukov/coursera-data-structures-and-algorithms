#!/usr/bin/python3

import unittest

import non_shared_substring_with_generalized_suffix_tree

class SolverSolveTestCase(unittest.TestCase):

    def setUp(self):
        self.solver = non_shared_substring_with_generalized_suffix_tree.Solver()
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

    def assert_result(self, expected_result):
        expected_items = expected_result
        actual_items = self.output_list
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
                              'A',
                              'T',
                          ]
        expected_result = [
                              'A',
                          ]

        self.solver.solve()

        self.assert_result(expected_result)

    def test_case2(self):
        self.input_list = [
                              'AAAAAAAAAAAAAAAAAAAA',
                              'TTTTTTTTTTTTTTTTTTTT',
                          ]
        expected_result = [
                              'A',
                          ]

        self.solver.solve()

        self.assert_result(expected_result)

    def test_case3(self):
        self.input_list = [
                              'CCAAGCTGCTAGAGG',
                              'CATGCTGGGCTGGCT',
                          ]
        expected_result = [
                              'CC',
                          ]

        self.solver.solve()

        self.assert_result(expected_result)

    def test_case4(self):
        self.input_list = [
                              'ATGCGATGACCTGACTGA',
                              'CTCAACGTATTGGCCAGA',
                          ]
        expected_result = [
                              'TGC',
                          ]

        self.solver.solve()

        self.assert_result(expected_result)

    def test_case5(self):
        self.input_list = [
                              'ABAB',
                              'BABA',
                          ]
        expected_result = [
                              'ABAB',
                          ]

        self.solver.solve()

        self.assert_result(expected_result)

    def test_case6(self):
        self.input_list = [
                              'ABXAB',
                              'BABAB',
                          ]
        expected_result = [
                              'X',
                          ]

        self.solver.solve()

        self.assert_result(expected_result)

    def test_case7(self):
        self.input_list = [
                              'ABXYAB',
                              'BAXBAB',
                          ]
        expected_result = [
                              'Y',
                          ]

        self.solver.solve()

        self.assert_result(expected_result)

    def test_case8(self):
        self.input_list = [
                              'ABXYAB',
                              'BAYXBAB',
                          ]
        expected_result = [
                              'BX',
                          ]

        self.solver.solve()

        self.assert_result(expected_result)

if __name__ == '__main__':
    class_names = [
                      SolverSolveTestCase,
                  ]

    suite = unittest.TestSuite()

    for c in class_names:
        suite.addTest(unittest.defaultTestLoader.loadTestsFromTestCase(c))

    unittest.TextTestRunner().run(suite)
