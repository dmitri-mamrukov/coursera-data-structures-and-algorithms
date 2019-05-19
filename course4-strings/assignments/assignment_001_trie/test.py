#!/usr/bin/python3

import unittest

import trie

class SolverSolveTestCase(unittest.TestCase):

    def setUp(self):
        self.solver = trie.Solver()
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
                              '1',
                              'ATA',
                          ]
        expected_result = [
                              '0->1:A',
                              '2->3:A',
                              '1->2:T',
                          ]

        self.solver.solve()

        self.assert_result(expected_result)

    def test_case2(self):
        self.input_list = [
                              '3',
                              'AT',
                              'AG',
                              'AC',
                          ]
        expected_result = [
                              '0->1:A',
                              '1->4:C',
                              '1->3:G',
                              '1->2:T',
                          ]

        self.solver.solve()

        self.assert_result(expected_result)

    def test_case3(self):
        self.input_list = [
                              '3',
                              'ATAGA',
                              'ATC',
                              'GAT',
                          ]
        expected_result = [
                              '0->1:A',
                              '1->2:T',
                              '2->3:A',
                              '3->4:G',
                              '4->5:A',
                              '2->6:C',
                              '0->7:G',
                              '7->8:A',
                              '8->9:T',
                          ]

        self.solver.solve()

        self.assert_result(expected_result)

if __name__ == '__main__':
    class_names = \
    [
        SolverSolveTestCase,
    ]

    suite = unittest.TestSuite()

    for c in class_names:
        suite.addTest(unittest.defaultTestLoader.loadTestsFromTestCase(c))

    unittest.TextTestRunner().run(suite)
